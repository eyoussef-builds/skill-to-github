# Friendly bilingual release documentation

Make the README feel like a helpful person walking the reader through a useful tool. Simple language means concrete actions and recognizable examples; it does not require talking down to adults or explaining file formats before showing the result.

## Main reading path

1. A readable banner, a language switch and short navigation. Add accurate badges only for real facts; never invent a release/version or imply every listed agent was tested.
2. A familiar problem and one clear benefit. Explain the user's action and the resulting experience in a few numbered steps, supported by an original workflow illustration. Introduce technical terms only when needed.
3. A compact “what can it do?” table. Explain actual outputs, relevant users and prerequisites.
4. Installation with two practical routes: a copy-and-paste prompt for an agent able to install files, and a manual download/copy method. Show the exact folder to copy, how to unzip on Mac/Windows, how to check discovery, and the first prompt to send. Do not link to non-existent release assets; GitHub's source ZIP is an alternative.
5. A first-use walkthrough with one action per step, expected results and the points where the user decides. Mark illustrative examples as invented. Do not promise access, quality, cost, speed, activation or account ownership that the actual skill cannot establish.
6. A brief privacy section and a link to the detailed data-handling guide. Explain what local helpers do and what the host's model/connected services process. Avoid implying that local code means all model processing is local.
7. Expandable FAQs for likely questions. Put implementation, helper commands and detailed file maps in a developer section or linked guide. Include updating, preserving local changes and uninstalling.
8. A clear license and approved public signature, support link and bilingual sharing captions/infographic downloads.

The desired presentation combines plain benefits, original visuals, clear setup checkpoints and progressive technical detail. Apply the same approved palette from `brand-style.md` to README banners and workflow diagrams. Preserve genuine supplied product screenshots. Study a user-supplied public reference when provided; transfer its explanatory approach, not its unrelated screenshots, claims, product requirements or license.

## English and Arabic

Write both main guides and both detailed installation guides. Use idiomatic Arabic rather than transliterating every English term. Set RTL reading order where supported, keep commands/identifiers/URLs legible LTR, and retain Western digits `0–9`. Give corresponding sections the same facts and meaningful examples. Verify actual Markdown rendering, navigation, collapsible sections and image links after publication.

## Installation across agents

For broad distribution, cover the agents relevant to the skill. The user's established distribution format includes guides for 15 agents: Codex, Claude Code, OpenClaw, Hermes Agent, Cursor, Grok Bot, OpenCode, GitHub Copilot, Gemini CLI, Windsurf/Cascade/Devin Desktop, Cline, Roo Code, Aider, Amp and Goose. Adapt names/paths to current official documentation and real applicability rather than treating this list as a compatibility guarantee.

For each entry, provide native install/copy steps where supported, personal/project scope, invocation and a discovery check. Otherwise label an explicit instruction-reading adaptation. Include macOS/Linux and PowerShell or manual Windows instructions as appropriate. Preserve existing customized folders instead of silently overwriting them. Explain remote/cloud access separately from local installation.

Link to the official documentation actually checked and state that documentation verification is distinct from end-to-end execution in that harness. Prefer honest partial support to an invented universal installer. A history collector for one product does not gain access to other agents' native histories because its instructions can be loaded there.

## GitHub presentation

Use a concise benefit-led About description, including short Arabic wording where it fits. Ensure homepage, license and any topics describe the actual skill. Keep installation documentation in the repository with the full `skills/<name>/` package. Link the share images and captions without embedding private examples. Use a release ZIP only when deliberately built from the reviewed files; inspect archive contents and member names before uploading.
