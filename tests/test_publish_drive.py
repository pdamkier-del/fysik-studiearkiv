"""Publication safety checks using fake HTTP only; never access Google Drive."""
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import publish_drive as drive


class Response:
    def __init__(self, info=None, data=b'', status=200, etag='"v1"'):
        self.info, self.content, self.status_code = info, data, status
        self.headers = {'ETag': etag} if etag else {}
    def json(self):
        return self.info


class Session:
    def __init__(self, responses):
        self.responses, self.calls = list(responses), []
    def request(self, method, url, **kwargs):
        self.calls.append((method, url, kwargs))
        return self.responses.pop(0)


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.doc = dict(key='matematik', subject='02-fysikbibliotek/statistik', approved=True)
        self.targets = dict(root_folder_id='root', areas={'02-fysikbibliotek': 'area'}, subjects={'02-fysikbibliotek/statistik': 'folder'}, files={'matematik': 'file'})
        self.info = dict(id='file', mimeType=drive.PDF, parents=['folder'], version='1', capabilities={'canEdit': True})
    def test_unapproved_documents_need_no_targets(self):
        self.doc['approved'] = False
        self.assertEqual(drive.plan({'documents': [self.doc]}, {}), [])
    def test_missing_id_and_duplicate_mapping_fail(self):
        with self.assertRaises(ValueError):
            drive.plan({'documents': [self.doc]}, {})
        other = dict(self.doc, key='other')
        self.targets['files']['other'] = 'file'
        with self.assertRaises(ValueError):
            drive.plan({'documents': [self.doc, other]}, self.targets)
    def test_failed_build_prevents_transport_creation(self):
        import json
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = dict(documents=[dict(self.doc, pdf=str(root/'absent.pdf'), log=str(root/'failed.log'), minimum_pages=1)])
            (root/'manifest.json').write_text(json.dumps(manifest))
            (root/'targets.json').write_text(json.dumps(self.targets))
            argv = ['publish_drive.py', '--manifest', str(root/'manifest.json'), '--targets', str(root/'targets.json'), '--apply']
            with patch.object(sys, 'argv', argv), patch.object(drive, 'request') as transport:
                with self.assertRaises(ValueError):
                    drive.main()
                transport.assert_not_called()
    def test_wrong_subject_folder_aborts(self):
        session = Session([Response(dict(mimeType=drive.FOLDER)), Response(dict(mimeType=drive.FOLDER, parents=['root'])), Response(dict(mimeType=drive.FOLDER, parents=['elsewhere']))])
        with self.assertRaises(ValueError):
            drive.check_remote(session, 'root', 'area', 'folder', 'file')
        self.assertTrue(all(call[0] == 'GET' for call in session.calls))
    def test_read_only_preflight_checks_full_hierarchy(self):
        session = Session([Response(dict(mimeType=drive.FOLDER)), Response(dict(mimeType=drive.FOLDER, parents=['root'])), Response(dict(mimeType=drive.FOLDER, parents=['area'])), Response(self.info)])
        drive.check_remote(session, 'root', 'area', 'folder', 'file')
        self.assertEqual([c[0] for c in session.calls], ['GET', 'GET', 'GET', 'GET'])
    def test_mathematics_pdf_lives_directly_in_main_area(self):
        doc = dict(self.doc, subject='00-matematik')
        targets = dict(root_folder_id='root', areas={'00-matematik': 'math-area'}, files={'matematik': 'file'})
        selected = drive.plan({'documents': [doc]}, targets)
        self.assertEqual(selected[0][2:4], ('math-area', 'math-area'))
        info = dict(self.info, parents=['math-area'])
        session = Session([Response(dict(mimeType=drive.FOLDER)), Response(dict(mimeType=drive.FOLDER, parents=['root'])), Response(info)])
        drive.check_remote(session, 'root', 'math-area', 'math-area', 'file')
        self.assertEqual([c[0] for c in session.calls], ['GET', 'GET', 'GET'])
    def test_nested_mathematics_target_is_rejected(self):
        with self.assertRaises(ValueError):
            drive.plan({'documents': [dict(self.doc, subject='00-matematik/extra')]}, self.targets)
    def test_wrong_main_area_aborts_before_file_access(self):
        session = Session([Response(dict(mimeType=drive.FOLDER)), Response(dict(mimeType=drive.FOLDER, parents=['elsewhere']))])
        with self.assertRaises(ValueError):
            drive.check_remote(session, 'root', 'area', 'folder', 'file')
        self.assertEqual(len(session.calls), 2)
        self.assertTrue(all(call[0] == 'GET' for call in session.calls))
    def test_old_flat_targets_require_explicit_migration(self):
        del self.targets['areas']
        with self.assertRaises(ValueError):
            drive.plan({'documents': [self.doc]}, self.targets)
    def test_wrong_mime_or_permission_blocks_write(self):
        for change in [dict(mimeType='image/svg+xml'), dict(capabilities={'canEdit': False}), dict(trashed=True), dict(parents=['elsewhere'])]:
            session = Session([Response(dict(self.info, **change))])
            with tempfile.TemporaryDirectory() as directory:
                with self.assertRaises(ValueError):
                    drive.replace(session, 'file', 'folder', b'%PDF-new', directory, 'matematik')
            self.assertTrue(all(c[0] == 'GET' for c in session.calls))
    def test_backup_precedes_conditional_update_and_checksum(self):
        old, new = b'%PDF-old', b'%PDF-new'
        session = Session([Response(self.info), Response(data=old), Response(self.info), Response(), Response(data=new)])
        with tempfile.TemporaryDirectory() as directory:
            drive.replace(session, 'file', 'folder', new, directory, 'matematik')
            self.assertEqual(Path(directory, 'matematik.pdf').read_bytes(), old)
            self.assertEqual(drive.restore_content(directory, 'matematik', 'file'), old)
            with self.assertRaises(ValueError):
                drive.restore_content(directory, 'matematik', 'other-file')
            Path(directory, 'matematik.pdf').write_bytes(b'%PDF-tampered')
            with self.assertRaises(ValueError):
                drive.restore_content(directory, 'matematik', 'file')
        self.assertEqual([c[0] for c in session.calls], ['GET', 'GET', 'GET', 'PATCH', 'GET'])
        self.assertEqual(session.calls[3][2]['headers']['If-Match'], '"v1"')
        self.assertNotIn('addParents', session.calls[3][2]['params'])
    def test_concurrent_change_aborts_before_write(self):
        changed = dict(self.info, version='2')
        session = Session([Response(self.info), Response(data=b'%PDF-old'), Response(changed, etag='"v2"')])
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                drive.replace(session, 'file', 'folder', b'%PDF-new', directory, 'matematik')
        self.assertTrue(all(c[0] == 'GET' for c in session.calls))
    def test_no_etag_no_update(self):
        session = Session([Response(self.info, etag=None)])
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                drive.replace(session, 'file', 'folder', b'%PDF-new', directory, 'matematik')
    def test_failed_upload_keeps_backup(self):
        session = Session([Response(self.info), Response(data=b'%PDF-old'), Response(self.info), Response(status=412)])
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(RuntimeError):
                drive.replace(session, 'file', 'folder', b'%PDF-new', directory, 'matematik')
            self.assertEqual(Path(directory, 'matematik.pdf').read_bytes(), b'%PDF-old')
    def test_post_upload_mismatch_is_failure(self):
        session = Session([Response(self.info), Response(data=b'%PDF-old'), Response(self.info), Response(), Response(data=b'%PDF-other')])
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                drive.replace(session, 'file', 'folder', b'%PDF-new', directory, 'matematik')


if __name__ == '__main__':
    unittest.main()
