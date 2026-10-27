"""Update explicitly approved existing Drive PDFs; never create files or folders.

Default: offline dry run. --check-remote adds read-only Drive validation.
--apply enables backup then conditional media replacement. --restore reads a
verified backup, but still backs up the current version before replacing it.
"""
import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from urllib.parse import quote

API = 'https://www.googleapis.com/drive/v3/files/'
UPLOAD = 'https://www.googleapis.com/upload/drive/v3/files/'
PDF = 'application/pdf'
FOLDER = 'application/vnd.google-apps.folder'


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def identifier(value):
    if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9_-]+', value) or value.startswith('REPLACE_'):
        raise ValueError('Missing or invalid verified Drive ID')
    return value


def plan(manifest, targets):
    documents = manifest['documents']
    keys = [d['key'] for d in documents]
    if len(keys) != len(set(keys)):
        raise ValueError('Duplicate document key')
    selected = []
    used = set()
    for document in documents:
        if document.get('approved') is not True:
            continue
        key = document['key']
        if not re.fullmatch(r'[a-z0-9-]+', key):
            raise ValueError('Unsafe document key')
        root = identifier(targets.get('root_folder_id'))
        subject = document['subject']
        parts = subject.split('/')
        if len(parts) != 2 or parts[0] not in {'01-universitetsfag', '02-fysikbibliotek'} or not re.fullmatch(r'[a-z0-9-]+', parts[1]):
            raise ValueError('Target must identify a main area and its subject')
        area = identifier(targets.get('areas', {}).get(parts[0]))
        folder = identifier(targets.get('subjects', {}).get(subject))
        file_id = identifier(targets.get('files', {}).get(key))
        if len({root, area, folder, file_id}) != 4 or file_id in used:
            raise ValueError('Duplicate or conflicting Drive targets')
        used.add(file_id)
        selected.append((document, root, area, folder, file_id))
    return selected


def request(session, method, url, **kwargs):
    response = session.request(method, url, timeout=120, **kwargs)
    if not 200 <= response.status_code < 300:
        # Do not include server payloads or request headers in logs.
        raise RuntimeError(f'Drive {method} failed: HTTP {response.status_code}')
    return response


def metadata(session, file_id):
    return request(session, 'GET', API + quote(file_id), params={
        'fields': 'id,name,mimeType,parents,trashed,version,capabilities(canEdit)',
        'supportsAllDrives': 'true',
    })


def check_remote(session, root, area, folder, file_id):
    for folder_id, parent in [(root, None), (area, root), (folder, area)]:
        info = metadata(session, folder_id).json()
        if info.get('trashed') or info.get('mimeType') != FOLDER:
            raise ValueError('Target folder missing, trashed or wrong type')
        if parent and parent not in info.get('parents', []):
            raise ValueError('Subject folder is outside the configured archive root')
    response = metadata(session, file_id)
    info = response.json()
    if (info.get('trashed') or info.get('mimeType') != PDF
            or folder not in info.get('parents', [])
            or not info.get('capabilities', {}).get('canEdit')):
        raise ValueError('Existing target is not an editable PDF in the expected folder')
    if not response.headers.get('ETag') or not info.get('version'):
        raise ValueError('Missing ETag/version; conditional replacement cannot be guaranteed')
    return response


def replace(session, file_id, folder, content, backup_dir, key):
    before = metadata(session, file_id)
    info = before.json()
    if (info.get('mimeType') != PDF or info.get('trashed')
            or folder not in info.get('parents', [])
            or not info.get('capabilities', {}).get('canEdit')):
        raise ValueError('Target changed after validation')
    etag = before.headers.get('ETag')
    if not etag or not info.get('version'):
        raise ValueError('Missing ETag/version; conditional replacement cannot be guaranteed')
    old = request(session, 'GET', API + quote(file_id), params={
        'alt': 'media', 'supportsAllDrives': 'true',
    }).content
    if not old.startswith(b'%PDF-'):
        raise ValueError('Existing media is not a PDF; refusing replacement')
    current = metadata(session, file_id)
    if current.headers.get('ETag') != etag or current.json().get('version') != info['version']:
        raise ValueError('Drive file changed while backing up')
    directory = Path(backup_dir)
    directory.mkdir(parents=True, exist_ok=True)
    # Exclusive creation prevents accidentally overwriting an earlier backup.
    with (directory / f'{key}.pdf').open('xb') as output:
        output.write(old)
    record = {'key': key, 'file_id': file_id, 'version': info['version'], 'sha256': sha256(old)}
    with (directory / f'{key}.json').open('x') as output:
        json.dump(record, output, indent=2)
    # Only update the media. No create, rename, parent move, or delete request.
    request(session, 'PATCH', UPLOAD + quote(file_id), params={
        'uploadType': 'media', 'supportsAllDrives': 'true',
    }, headers={'Content-Type': PDF, 'If-Match': etag}, data=content)
    downloaded = request(session, 'GET', API + quote(file_id), params={
        'alt': 'media', 'supportsAllDrives': 'true',
    }).content
    if sha256(downloaded) != sha256(content):
        raise ValueError('Post-upload checksum mismatch; backup retained for manual recovery')
    return record


def restore_content(directory, key, file_id):
    directory = Path(directory)
    record = json.loads((directory / f'{key}.json').read_text())
    data = (directory / f'{key}.pdf').read_bytes()
    if (record.get('key') != key or record.get('file_id') != file_id
            or sha256(data) != record.get('sha256') or not data.startswith(b'%PDF-')):
        raise ValueError('Backup identity or checksum mismatch')
    return data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', default='config/pdf-publication.json')
    parser.add_argument('--targets', help='Target JSON; defaults to DRIVE_TARGETS_JSON')
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--check-remote', action='store_true')
    parser.add_argument('--restore', help='Directory containing prior backup artifacts')
    parser.add_argument('--backup-dir', default='build/drive-backup')
    args = parser.parse_args()
    manifest = json.loads(Path(args.manifest).read_text())
    targets = json.loads(Path(args.targets).read_text() if args.targets else os.environ.get('DRIVE_TARGETS_JSON', '{}'))
    selected = plan(manifest, targets)
    if not selected:
        print('No approved documents; no Drive requests performed.')
        return
    # All PDFs/backup records must pass before any network mutation.
    payloads = []
    for document, root, area, folder, file_id in selected:
        if args.restore:
            data = restore_content(args.restore, document['key'], file_id)
        else:
            from validate_publication import validate
            validate(document)
            data = Path(document['pdf']).read_bytes()
        payloads.append((document, root, area, folder, file_id, data))
    if not (args.apply or args.check_remote):
        print(f'Dry run: {len(payloads)} approved existing PDF targets. No network requests.')
        return
    # Use short-lived ADC credentials from GitHub OIDC, never a key in Git.
    import google.auth
    from google.auth.transport.requests import AuthorizedSession
    credentials, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/drive'])
    session = AuthorizedSession(credentials)
    for document, root, area, folder, file_id, data in payloads:
        check_remote(session, root, area, folder, file_id)
    if args.apply:
        for document, root, area, folder, file_id, data in payloads:
            replace(session, file_id, folder, data, args.backup_dir, document['key'])
            print(f"Updated existing PDF: {document['key']}")
    else:
        print('Read-only remote checks passed; no files changed.')


if __name__ == '__main__':
    main()
