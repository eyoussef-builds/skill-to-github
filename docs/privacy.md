# Privacy and data handling

[العربية](privacy.ar.md) · [Main guide](../README.md)

## What this repository contains

Reusable release instructions, supporting references, blank templates, a read-only review helper, synthetic tests, documentation and public artwork. Approved author contacts are limited to `eyoussef-builds`, `hello@eyoussef.me` and `eyoussef.me`.

Personal profiles, original chats, actual work reports, private projects, release-state notes, device paths, account identifiers and credentials are excluded. Generic installation conventions such as `~/.agents/skills/` are instructions for your own account, not the creator's device details. The tests intentionally construct synthetic token/path/email examples; they do not contain working credentials or real user records.

## When you use it

Your assistant reads the skill you want to publish and its relevant resources. It may see private development context while preparing a clean public export. A Markdown skill does not grant account access or create a separate security boundary. The host's tool permissions and model/service settings apply.

Only deliberately reviewed and approved public files should be sent to GitHub. Keep manifests, source mappings, personal defaults and filled release-state notes outside that public package. Your local `references/local-profile.md` is optional and excluded by this repository's Git rules; preserve it when updating. Ignore rules cannot remove files already committed or protect force-added files.

Image generation receives the production prompt and any supplied references. Use public or expressly approved visual inputs, never private chats, internal dashboards or customer information. Social copy is checked against public repository facts and intentionally supplied announcement notes. Drafting copy does not post it, send replies or configure a comment automation.

Your model and connected services process whatever inputs they receive under their own policies. A local helper with no upload code does not mean your entire AI workflow runs offline.

## What the optional helper does

`review_package.py` reads a manually chosen staging folder and an explicit JSON file list. It flags unexpected/missing files, suspicious filenames, common credential/path patterns, unapproved emails, supplied private deny terms and PNG text/EXIF metadata. It reports categories and relative locations, not matched secret values, and calculates SHA-256 hashes. It does not change files, send network requests or publish anything.

The helper cannot judge all personal information, image pixels, arbitrary binary content, Git history, legal permission or whether a release is safe. The agent must inspect meaning and visuals, review actual staged files/full reachable history, and read the published files back from GitHub. Passing synthetic tests or getting no pattern findings is not a universal privacy guarantee.

## Before publishing your own skill

1. Read every proposed file and inspect every image. Use blank templates or invented examples instead of actual private work.
2. Exclude credentials, raw transcripts, personal profiles, `.env` files, internal URLs, private people/client data and local machine details.
3. Inspect author/committer identity, remotes and full reachable history. A clean export with fresh history is appropriate for a new standalone reusable package; preserve attribution and existing repository rules.
4. Review the exact public GitHub state after publication, including file bytes, reachable history, metadata, images and release archives.
5. Share bug reports with synthetic examples. Keep real review manifests and evidence private.

## Report a privacy issue

Email [hello@eyoussef.me](mailto:hello@eyoussef.me) with the affected public file and a minimal description. Do not paste a secret into a public issue. An exposed live credential needs provider revocation/rotation; deleting the current file does not invalidate it or remove earlier copies.
