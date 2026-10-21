#!/usr/bin/env python3
"""Read-only review of an explicitly allowlisted public skill package.

Findings are review candidates, not proof of a leak. A clean pattern scan is not
an anonymization guarantee; image pixels and Git history need separate review.
No network calls, uploads, source writes or automatic publication.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import struct

PATTERNS = {
    'private_key': r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    'credential_token': r'\b(?:ghp_|gho_|github_pat_)[A-Za-z0-9_]{20,}|\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}|\bAKIA[0-9A-Z]{16}\b|\bAIza[A-Za-z0-9_-]{30,}|\bxox[baprs]-[A-Za-z0-9-]{20,}',
    'provider_secret': r'\b(?:sk_live_|sk_test_|whsec_)[A-Za-z0-9]{16,}',
    'machine_path': r'/Users/[^\s/]+/|/Volumes/[^\n]+|/home/[^\s/]+/|[A-Z]:\\Users\\[^\\\s]+\\',
    'credential_url': r'(?i)\b(?:https?|postgres(?:ql)?|mysql|mongodb(?:\+srv)?)://[^\s/@:]+:[^\s/@]+@',
}
EMAIL = re.compile(r'[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
SENSITIVE_SUFFIXES = {'.pem', '.key', '.p12', '.pfx', '.sqlite', '.sqlite3', '.db', '.jsonl', '.zst'}
SENSITIVE_NAMES = {'.env', '.ds_store', 'local-profile.md', 'credentials.json', 'token.json', 'tokens.json'}
PNG = b'\x89PNG\r\n\x1a\n'


def finding(path, category, line=None):
    value = {'path': path, 'category': category}
    if line is not None:
        value['line'] = line
    return value


def text_findings(text, rel, allow_emails, deny_terms):
    results = []
    for number, line in enumerate(text.splitlines(), 1):
        for category, pattern in PATTERNS.items():
            if re.search(pattern, line):
                results.append(finding(rel, category, number))
        if set(EMAIL.findall(line)) - set(allow_emails):
            results.append(finding(rel, 'unapproved_email', number))
        if any(term and term.casefold() in line.casefold() for term in deny_terms):
            results.append(finding(rel, 'explicit_private_term', number))
    return results


def png_findings(data, rel):
    """Flag text/EXIF for human inspection without printing the embedded values."""
    results = [finding(rel, 'image_pixels_require_visual_review')]
    offset = len(PNG)
    ended = False
    while offset + 12 <= len(data):
        length = struct.unpack('>I', data[offset:offset+4])[0]
        kind = data[offset+4:offset+8]
        if offset + length + 12 > len(data):
            return results + [finding(rel, 'malformed_png')]
        if kind in {b'tEXt', b'zTXt', b'iTXt', b'eXIf'}:
            results.append(finding(rel, 'embedded_text_or_exif_requires_review'))
        offset += length + 12
        if kind == b'IEND':
            ended = True
            if offset != len(data):
                results.append(finding(rel, 'trailing_binary_data_requires_review'))
            break
    if not ended:
        results.append(finding(rel, 'malformed_png'))
    return results


def review(root, manifest, allow_emails=(), deny_terms=()):
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError('Staging root must be an existing directory')
    if not isinstance(manifest, list) or not all(isinstance(x, str) for x in manifest):
        raise ValueError('Manifest must be a JSON array of relative file paths')
    if len(set(manifest)) != len(manifest):
        raise ValueError('Manifest contains duplicate paths')
    expected = set()
    for value in manifest:
        path = PurePosixPath(value)
        if not value or path.is_absolute() or '..' in path.parts or '\\' in value or ':' in value or '.git' in path.parts:
            raise ValueError('Manifest contains an unsafe or nonportable path')
        expected.add(path.as_posix())
    findings, hashes, actual = [], {}, set()
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root).as_posix()
        if '.git' in path.relative_to(root).parts:
            continue  # Inspect reachable Git history separately; never publish .git itself.
        if path.is_symlink():
            findings.append(finding(rel, 'symlink_not_read'))
            continue
        if path.is_file():
            actual.add(rel)
    findings += [finding(p, 'unexpected_file') for p in sorted(actual-expected)]
    findings += [finding(p, 'missing_file') for p in sorted(expected-actual)]
    for rel in sorted(expected & actual):
        path = root / rel
        if path.name.casefold() in SENSITIVE_NAMES or path.name.startswith('.env.') or path.suffix.casefold() in SENSITIVE_SUFFIXES or '__pycache__' in path.parts or path.suffix in {'.pyc', '.pyo'}:
            findings.append(finding(rel, 'sensitive_filename'))
        data = path.read_bytes()
        hashes[rel] = hashlib.sha256(data).hexdigest()
        if data.startswith(PNG):
            findings += png_findings(data, rel)
            continue
        try:
            text = data.decode('utf-8')
        except UnicodeDecodeError:
            findings.append(finding(rel, 'binary_requires_manual_review'))
            continue
        if '\x00' in text:
            findings.append(finding(rel, 'binary_requires_manual_review'))
        else:
            findings += text_findings(text, rel, allow_emails, deny_terms)
    return {'files_reviewed': len(hashes), 'sha256': hashes, 'findings': findings,
            'status': 'review_required' if findings else 'no_pattern_findings',
            'limitation': 'Patterns are review aids. Inspect images, meaning, identifiers, archives and complete Git history independently; this is not a privacy guarantee.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', help='Explicit public staging folder')
    parser.add_argument('--manifest', required=True, help='JSON array of reviewed relative file paths')
    parser.add_argument('--allow-email', action='append', default=[], help='Explicitly approved public email')
    parser.add_argument('--deny-term', action='append', default=[], help='Private identifier to flag without displaying its value')
    args = parser.parse_args()
    result = review(args.root, json.loads(Path(args.manifest).read_text()), args.allow_email, args.deny_term)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result['findings'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
