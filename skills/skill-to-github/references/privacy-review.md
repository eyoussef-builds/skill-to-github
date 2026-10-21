# Public-package and remote review

The goal is to publish reusable methods without publishing the creator's actual computer, customers, accounts or work. A scanner helps find candidates; an agent must still inspect the content and every image. Never promise that a pattern scan proves universal absence of personal information.

## Clean export and manifest

Choose an explicit list of public files. Copy only those files into a separate staging folder, with fresh history for a new standalone repository. Exclude personal/local profiles, raw research conversations, chat exports, reports, real example outputs, screenshots of private work, scratch evidence, credential/config files, unrelated source trees, caches, system files and backup archives. Keep private source-to-public mappings and deny terms outside the repository.

Review every admitted file manually. Fictional examples and synthetic fixture IDs must be labeled and traceable as synthetic. Preserve useful runtime conventions such as `~/.agents/skills/`; remove actual machine usernames, mounted-volume names and private absolute paths. Public contact details must be explicitly approved; finding a name/email in another repository does not by itself approve reusing it.

The package helper takes a JSON array of explicit relative file paths:

```sh
python3 scripts/review_package.py /path/to/staging \
  --manifest /path/to/private-public-file-list.json \
  --allow-email public-contact@example.com
```

Add `--deny-term` arguments for known private identifiers only in the private review environment. It prints finding categories and relative locations, not matched values. Inspect all findings; verified synthetic/public matches can be documented as reviewed, but never blanket-allow every finding to get a green result. The helper reads files and hashes them without modifying the source or uploading anything.

The manifest also captures SHA-256 hashes for later comparison. A file list is not authorization: the list itself must be deliberately reviewed. PNG metadata findings require inspection; pixel-level text and images always need visual review. Unsupported binary formats need manual inspection rather than a clean claim.

## Text and assets

Look for secret values and connection strings, internal URLs/IPs, private contact/identity, account/project/chat IDs, copied prompts/history, private names and source paths. Check code, comments, fixtures, filenames, docs, captions, SVG text, manifests and archives. In images, check all visible text and metadata. Do not use private production assets as convenient sample screenshots.

Keep clear data-handling claims: a local helper without network code is different from a host model or image service processing its inputs. Public privacy documentation must explain this accurately.

## Git and publication

Before the first push, inspect exactly staged files, full reachable Git history, refs, author and committer names/emails, commit messages, remote URLs, license and release archives. Configure repository-local approved identity rather than relying on a private global identity. Disable accidental signing/identity additions when they would reveal unapproved information, while following repository requirements. Do not upload the parent workspace or its history.

For an existing repository, review the changes against current upstream and preserve unrelated work. Do not force-push, delete history, remove attribution or change visibility/licensing without the required authority. A fresh export avoids carrying a private development history into a new public repository.

After pushing, inspect GitHub's actual public state: visibility, About text, file inventory, refs, commits/metadata, every published file and relevant release assets. Download the server-side blobs and compare their bytes/hashes with the reviewed manifest; re-scan/inspect the downloaded content. Check actual rendered English/Arabic guides and assets. Review older reachable versions as well, including deleted files. Use scoped requests to GitHub rather than dumping unrelated account data.

If a real secret is exposed, tell the user promptly and arrange provider revocation/rotation through an authorized route. Removing the latest file does not invalidate the secret or erase copies. Stop further distribution of affected artifacts, preserve the prepared clean work, and handle any disruptive history changes with appropriate authority. Report what was actually reviewed and any remaining limitations.
