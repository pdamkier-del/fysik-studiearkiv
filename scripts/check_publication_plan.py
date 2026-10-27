"""Exercise all declared publication targets offline with synthetic Drive IDs.

No credentials or production mappings are loaded. Approval is simulated only in
an ephemeral copy of the manifest; the real manifest remains unchanged.
"""
import json
from pathlib import Path
import subprocess
import sys
import tempfile

root = Path(__file__).resolve().parents[1]
manifest_path = root / 'config/pdf-publication.json'
original = manifest_path.read_bytes()
manifest = json.loads(original)
targets = {'root_folder_id': 'fake-root', 'areas': {}, 'subjects': {}, 'files': {}}
for document in manifest['documents']:
    parts = document['subject'].split('/')
    area, subject = parts[0], parts[-1]
    targets['areas'][area] = 'fake-area-' + area
    if len(parts) == 2:
        targets['subjects'][document['subject']] = 'fake-subject-' + area + '-' + subject
    targets['files'][document['key']] = 'fake-file-' + document['key']
    document['approved'] = True
with tempfile.TemporaryDirectory() as directory:
    temporary = Path(directory)
    (temporary / 'manifest.json').write_text(json.dumps(manifest))
    (temporary / 'targets.json').write_text(json.dumps(targets))
    subprocess.run([
        sys.executable, str(root / 'scripts/publish_drive.py'),
        '--manifest', str(temporary / 'manifest.json'),
        '--targets', str(temporary / 'targets.json'),
    ], cwd=root, check=True)
if manifest_path.read_bytes() != original:
    raise RuntimeError('Offline plan check modified the production manifest')
print('Offline synthetic plan passed; production approvals and Drive files untouched.')
