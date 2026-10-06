# PM Fundamentals Toolkit

Markdown/YAML-first project-management tools informed by industry practices and the author's
experience applying them. The lifecycle is organized as **Define -> Plan -> Execute -> Close**,
with Managing/Controlling and Change Management across the lifecycle.

The repository is designed for software engineers, project managers, and AI agents. Markdown and
YAML are the source of truth; DOCX, XLSX, and PPTX are disposable exports generated on demand.
Artifacts are diffable, reviewable, searchable, and deployable from GitHub.
This project is licensed under the [MIT License](LICENSE).

## Quick start

Python 3.10+ is required for Office exports. Install the exporter dependencies with
`python -m pip install -r requirements.txt`.

Every project starts in its own OneDrive folder:
`<user's OneDrive root>\Documents\Projects\<project-slug>\`. Resolve the signed-in OneDrive root
for the current user; do not assume a particular account name or tenant path.
Use relative links within the folder so it can later move into or become a git repository without
changing the PM model.

1. Create `Documents\Projects\<project-slug>\` in the user's OneDrive. Resolve the OneDrive root
   from the current account/environment; ask the user if it is ambiguous.
2. Copy `templates/project.yaml` (define outcomes and their outcome owners), `plan.yaml`,
   `raid.yaml`, and `decisions.yaml`, plus relevant Markdown templates. Add `evidence.yaml` when
   material claims or metrics need a durable source trail. Copy `project-README.md` as `README.md`
   and `project.gitignore` as `.gitignore`.
3. Use the skills in `skills/` with Copilot CLI, Scout, or another agent runtime.
   Use `skills/wg-session-ops/SKILL.md` after recurring project sessions to turn
   transcripts and notes into confirmed issue updates, status artifacts, and draft
   team recaps.
   Plan items identify a `deliverableOwner` and link to one `outcomeId`; the outcome's
   `outcomeOwner` is accountable for verifying results. Use the AI learning record only for
   material AI-workflow changes, not routine AI usage.
4. Generate Office deliverables only when a stakeholder needs them:

```powershell
python exporters/pmfx/to_docx.py --input "<OneDriveRoot>\Documents\Projects\my-project\charter.md" --output Charter.docx
python exporters/pmfx/to_xlsx.py --project "<OneDriveRoot>\Documents\Projects\my-project" --output Project-Tracker.xlsx
python exporters/pmfx/to_pptx.py --input "<OneDriveRoot>\Documents\Projects\my-project\kickoff.md" --output Kickoff-Deck.pptx
```

## Repository contract

- Never author directly in binary Office files.
- Preserve the enum values in the YAML templates.
- Keep one project per folder under `Documents\Projects\<project-slug>\`.
- Use relative links within the project; if the folder becomes a git repo later, commit its
  canonical artifacts with it.
- Create and review project-specific RYG criteria with the decision owner before issuing a color;
  use `Unassessed` until criteria are agreed.
- Apply the AI workflow intake only when the proposed work changes or introduces an AI-enabled
  user workflow.
- Distinguish observed facts, estimates, assumptions, and recommendations; link material claims to
  dated sources and measurement methods.
- Treat generated Office files as build outputs.
- Do not send generated artifacts without previewing recipients and content.

The exporters create clean, unprotected files. The artifact fields were adapted from standalone
program-management templates supplied by a third-party vendor; the original vendor files are not
included. This toolkit is an independent project and is not an official product or standard of
Microsoft or the template vendor.

## Promote a project folder to Git

Project folders remain on OneDrive. When version control is useful, review
[`docs/promote-to-git.md`](docs/promote-to-git.md); it initializes Git in place and does not
move the project or automatically publish it to a remote.
