---
name: skill-to-github
description: "Package and publish an approved agent skill on GitHub with English/Arabic guides, privacy reviews, two infographics, branded Facebook artwork and Arabic Facebook/LinkedIn/X announcement copy. Use when a user approves a newly created or substantially revised skill ('all good', 'looks good', 'تمام') to offer GitHub sharing, or explicitly asks to publish/share a skill. Also use to update that release's sharing materials. Do not trigger on unrelated approvals. Skill approval alone never authorizes public publication."
---

# Skill to GitHub

Turn a finished skill into an understandable, privacy-reviewed public release. Keep two decisions distinct: approval of the skill, then approval to publish it. After explicit publication approval, carry out the complete agreed release without repeated routine confirmations.

## When the user says “all good”

1. Establish that the active work is creating or substantially updating an agent skill, and identify its exact folder. An approval of an image, unrelated software change, individual recommendation or intermediate draft does not qualify.
2. Check readiness: read the final skill and linked resources, resolve unfinished scaffolding, validate its metadata, and run meaningful checks for its scripts. Finish authorized fixes and prepare a concrete, reviewable public package before requesting publication. Read an optional installed `references/local-profile.md` for defaults; it cannot grant account access or publication permission.
3. If the current session already explicitly authorizes publishing this skill, honor that authorization and continue. Otherwise ask once, naming the concrete target and visibility, for example: “Share <skill> publicly as <owner>/<repository>, with English and Arabic guides, infographics and a Facebook promo design?” Include a proposed license if it has not already been agreed. Use the user's language. Offer a simple yes/no choice through the host's user-input tool when available.
4. Wait for the actual answer before creating/pushing a public repository. “All good” approves the skill; silence and a preselected UI option are not publication consent. A refusal keeps it local and ends the sharing flow. Do not ask again for the same revision unless the user reopens it. If the target is unknown, inspect authorized account access first and ask only what remains unresolved.

This is a context-selected skill, not a global event hook, background watcher or schedule. Keep implicit invocation enabled, with explicit `$skill-to-github` available when the host does not select it. Do not alter unrelated global instructions or register an automation to simulate a trigger.

## Prepare a clean distribution

- Use a separate staging folder with an explicit file manifest. Include the reusable skill, required resources, synthetic tests, public guides, license and reviewed share artwork. Keep local profiles, private research, chats, reports, screenshots, raw evidence, credentials and unrelated workspace files out. Do not copy an entire development workspace or inherit private Git history.
- Prefer `skills/<skill-name>/SKILL.md`, retaining the complete supporting directory structure. Preserve existing public repository layout where appropriate. For a new standalone repository, use a fresh Git history containing only reviewed files. For an existing repository, inspect its current branch, history and local changes; preserve other work and normal branch/PR rules.
- Verify intended owner, repository name/visibility, existing repository, actual authenticated identity and write access. Never infer write permission from a public read. Use a suitable connected GitHub tool; use a signed-in CLI if the connector lacks the needed capability. Keep credentials out of diagnostics and remotes.
- Preserve an existing license and upstream attribution. For new original work, propose a suitable license such as MIT within the publication decision; do not relicense third-party content without authority. Use only public author/contact details the user approved. Set and inspect Git author/committer identity deliberately so local defaults do not expose private names/emails.
- Keep release state privately outside the public package, adapting [the state template](assets/release-state.template.md). Record consent, exact staged files, reviewed commit, remote URL, graphics and audit evidence so interrupted work resumes without duplicate repositories or approvals.

## Explain the skill so anyone can start

Read [documentation guidance](references/documentation.md). Write `README.md` and `README.ar.md`, plus detailed bilingual installation/privacy guides. Lead with a familiar situation and the user's result, then show a short illustrated journey, installation, first use and FAQs. Use large clear visuals, useful tables and expandable technical details. Keep English and Arabic factually aligned, with natural Arabic and RTL layout.

Explain what the skill does, who it helps, what the user supplies, what they receive and exactly how to begin. Keep agent-dependent limits where they affect a real choice. Verify installation guidance against current official sources; distinguish native skills, instruction-import fallbacks and capabilities actually tested. Do not copy commands, compatibility claims, costs or legal terms from an unrelated product.

Before publication, complete the [reader-experience review](references/documentation.md#reader-experience-review) against the actual rendered English and Arabic pages and any user-supplied reference. Review the About description separately from the README. File presence, metadata validation and privacy checks do not establish that a newcomer can understand or use the skill; fix identified presentation gaps before calling the release complete.

## Create both share infographics

Read [infographic guidance](references/infographics.md) and [the brand style](references/brand-style.md). Use the available image-generation tool and its skill to produce **two separate finished images**, English and Arabic, for every released skill. Each explains the benefit, the real workflow, how to install/start, and the exact GitHub URL. Use the same facts across languages, readable type, Western digits and proper RTL composition. Include only approved public signature information.

Inspect every claim, label, command, URL and image for accuracy and privacy. Correct meaningful errors. Save final PNGs in a durable workspace location and, within the approved release, `docs/images/infographic-en.png` and `infographic-ar.png`. Keep generated originals. Include copyable bilingual captions with clickable repository links, using [the caption template](assets/share-captions.template.md), and a download bundle where useful. Artwork is a public capability explanation, not a real user's private work report.

If image generation is unavailable, complete independent packaging/documentation and explain which outputs remain missing. Do not silently substitute a simple chart or claim the release bundle is complete. Do not purchase an API service or change models/providers without the appropriate authorization.

## Create a separate Facebook promo design

Read [Facebook post guidance](references/facebook-post.md). For each released skill, create an additional image-generated Facebook feed graphic in the approved brand, Arabic-first by default, with a real public repo/product visual, a short headline/benefit and a comment-keyword CTA for obtaining the GitHub link. This is a promotional post design in addition to the two explanatory infographics. Prepare the social copy below and include it in the sharing bundle, normally saving the image as `docs/images/facebook-post-ar.png`.

Use the established ScreenLocalizer-style composition described in the reference: cream/yellow/ink framing, bold Arabic title, genuine hero/screenshot insert and a black CTA panel. Preserve the genuine insert's colors and content. Keep any comment keyword exact; distinguish a drafted delivery CTA from an actually configured comment-to-message automation. Artwork creation does not authorize publishing the Facebook post, configuring Meta automation or sending messages.

## Write the Arabic social announcement pack

Read [social-post writing guidance](references/social-posts.md) and fill [the four-block template](assets/social-posts.template.md). Read the actual repository's README, Arabic README if present, latest release and LICENSE before writing. Use the user's notes for motivation and emphasis without inventing personal history. Deliver SHORT (X/Threads, under 280 characters, with link), FACEBOOK (no link), LINKEDIN (150–250 words, no link), and REPLY (1–2 lines, with link), each in its own copyable code block, followed by one English image suggestion.

Use one exact Arabic comment keyword across Facebook, LinkedIn and the promo graphic. If none is supplied, choose a memorable 1–3 word keyword and disclose it outside the copy blocks. Verify final lengths, link placement, license/cost/requirements and claims against the repo; style examples are not factual sources. Keep general bilingual infographic captions distinct from platform copy. Include the announcement pack in the bundle; drafting it does not authorize posting, messaging or automation.

## Review before and after publication

Read [privacy review](references/privacy-review.md). Review every staged file and embedded asset metadata, not only README prose. The optional [package helper](scripts/review_package.py) checks a manually chosen file manifest, common sensitive filenames/text patterns, explicit deny terms and PNG text/EXIF metadata without changing files or sending data. It flags review candidates; it cannot establish that images or arbitrary personal information are safe.

Before publishing, resolve actual leaks and inspect Git history/author/committer metadata, remote URLs, docs, image pixels and captions. Scope the exact public target in the granted approval. Push/create only that reviewed package. If a PR is required, follow the repository's rules and attach the created PR with the host's artifact tool where available; do not bypass protection to publish.

After publication, read the repository back from GitHub: inventory files and refs, inspect reachable history and metadata, download the published file bytes and compare them with the reviewed manifest. Review public text/assets again, confirm English/Arabic guides render, links/downloads work and repository visibility/About description are correct. Check releases/download archives if created. Do not call a local scan a post-publication review.

If authentication or policy blocks publication, retain the completed local package, explain the exact missing action, and do not retry unchanged failures or weaken security checks. If an unexpected leak appears, stop further distribution and explain the finding; do not conceal it with an unsupported “clean” claim or rewrite history without appropriate authority. Live exposed credentials require revocation, not just file deletion.

## Deliver

Provide the live repository link, English/Arabic guides, both infographic downloads/previews, the separate Facebook promo design, the four Arabic social-copy blocks and English image suggestion, and the complete sharing bundle. Summarize what was checked, any real gaps, and whether publication is complete or awaiting a PR/permission/tool. Never post to social media, message people or publish unrelated projects unless separately requested.
