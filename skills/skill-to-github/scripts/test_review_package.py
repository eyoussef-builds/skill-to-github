"""Synthetic privacy-review fixtures; never read a real home/history directory."""

import hashlib
import json
from pathlib import Path
import struct
import tempfile
import unittest
import zlib

import review_package as rp


def chunk(kind, payload=b''):
    return struct.pack('>I', len(payload)) + kind + payload + struct.pack('>I', zlib.crc32(kind+payload))


class PackageReviewTests(unittest.TestCase):
    def test_explicit_manifest_and_readonly_hashes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = b'# A public instruction\n'
            (root/'SKILL.md').write_bytes(data)
            result = rp.review(root, ['SKILL.md'])
            self.assertEqual(result['findings'], [])
            self.assertEqual(result['sha256']['SKILL.md'], hashlib.sha256(data).hexdigest())
            self.assertEqual((root/'SKILL.md').read_bytes(), data)
            self.assertEqual(set(p.name for p in root.iterdir()), {'SKILL.md'})

    def test_unexpected_and_missing_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'private-notes.md').write_text('not in manifest')
            categories = {f['category'] for f in rp.review(root, ['SKILL.md'])['findings']}
            self.assertEqual(categories, {'unexpected_file', 'missing_file'})

    def test_sensitive_values_are_flagged_but_not_printed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            token = 'ghp_' + 'A'*30
            deny = 'PrivateCustomerFixture'
            (root/'SKILL.md').write_text(token+'\n'+deny+'\n'+str(Path('/Users')/'synthetic-user'/'project'))
            result = rp.review(root, ['SKILL.md'], deny_terms=[deny])
            categories = {f['category'] for f in result['findings']}
            self.assertEqual(categories, {'credential_token', 'explicit_private_term', 'machine_path'})
            output = json.dumps(result)
            self.assertNotIn(token, output)
            self.assertNotIn(deny, output)
            self.assertNotIn('synthetic-user', output)

    def test_public_email_allowlist(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root/'README.md').write_text('public-contact@example.com')
            self.assertEqual(rp.review(root, ['README.md'])['findings'][0]['category'], 'unapproved_email')
            self.assertEqual(rp.review(root, ['README.md'], allow_emails=['public-contact@example.com'])['findings'], [])

    def test_png_metadata_and_pixels_need_review(self):
        data = rp.PNG + chunk(b'IHDR', b'0'*13) + chunk(b'tEXt', b'Author\0SYNTHETIC_PRIVATE') + chunk(b'IEND')
        result = rp.png_findings(data, 'illustration.png')
        self.assertEqual({x['category'] for x in result}, {'image_pixels_require_visual_review', 'embedded_text_or_exif_requires_review'})
        self.assertNotIn('SYNTHETIC_PRIVATE', json.dumps(result))

    def test_malformed_png_is_not_clean(self):
        result = rp.png_findings(rp.PNG + struct.pack('>I', 100) + b'tEXt', 'bad.png')
        self.assertIn('malformed_png', {x['category'] for x in result})

    def test_symlink_does_not_read_external_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)/'package'
            root.mkdir()
            external = Path(tmp)/'outside.txt'
            external.write_text('outside content')
            (root/'SKILL.md').symlink_to(external)
            result = rp.review(root, ['SKILL.md'])
            self.assertIn('symlink_not_read', {x['category'] for x in result['findings']})
            self.assertEqual(result['files_reviewed'], 0)

    def test_manifest_cannot_escape_root(self):
        with tempfile.TemporaryDirectory() as tmp:
            for value in ['../outside.txt', '/absolute/file', 'C:\\Users\\fixture\\file', '.git/config']:
                with self.assertRaises(ValueError):
                    rp.review(Path(tmp), [value])


if __name__ == '__main__':
    unittest.main()
