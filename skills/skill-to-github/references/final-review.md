# Mandatory final release review

Use this acceptance review before publication and again on the published result. It joins the existing reader-experience, asset, copy and privacy checks; it does not replace them or add another user-approval round.

## Before publication

- Read the final skill as an operator. Confirm that its promised output, scope and stop conditions are coherent, its required references/resources ship, and any scripts received meaningful checks. Inspect whether it requires a final review of its actual output with workflow-specific criteria, fixes and rechecks. If absent, add an appropriate review within the authorized skill update; do not treat a generic “QA passed” sentence as sufficient.
- Complete the [reader-experience review](documentation.md#reader-experience-review) on the rendered English and Arabic pages, including separate About wording and comparison to any supplied reference. Can a newcomer explain what this does, install it, send the first prompt and recognize a useful result? File presence, matching headings and a palette match do not answer that question.
- Review the actual included images at reading size and final platform copy against the repository facts, language/brand direction, exact URL and keyword. English/Arabic facts must agree. Reuse suitable approved assets for a narrow instruction update; regenerate only assets whose claims or presentation are affected, or when requested. A text-only patch is not a new social campaign.
- Complete [privacy review](privacy-review.md) on the exact staged diff/package, history/identity and any archives. Verify the install paths, links and archive structure a reader will actually use. Keep review evidence and personal profiles outside the public package.

## After publication

- Read back the actual GitHub commit, file inventory, metadata and changed bytes, comparing them to the reviewed package. Check public rendering and downloads affected by the change; for release archives, download and inspect the uploaded archive, not only its local source. Preserve old release tags/assets; publish a new version when updating distributed packages.
- Confirm that the final response points to the correct live repository/version and describes the work accurately. Separate merged/pushed work, a pending PR, downloadable packages and any missing outputs. Do not call the release complete based solely on a local scan, green tests or a push response.

Fix findings before the next distribution step and recheck the affected pages, artifacts or downloads after correction. Retain concise private evidence of the version reviewed, actual checks, reference comparison, fixes and limitations. A required output or consequential failed check remains pending rather than silently passing. Do not expand review into social posting, new paid services or unrelated repository changes.
