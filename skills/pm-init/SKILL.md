---
name: pm-init
description: Initialize a PM Fundamentals project folder from the repository templates.
---
# Initialize a project

Create `<project-slug>/` under the OneDrive project root —
`<user's OneDrive root>\Documents\Projects\<project-slug>\` — never inside the
Scout workspace or the `pm-fundamentals` tooling repo. Copy `templates/project.yaml`,
`plan.yaml`, `raid.yaml`, `decisions.yaml`, and the Markdown templates needed for the project.
Create `evidence.yaml` when material claims or metrics need a durable source trail. Populate only
facts supplied by the user or retrieved from authorized context.
Define each intended outcome in `project.yaml.outcomes` with a stable `outcomeId`, measure,
baseline/target, and one accountable `outcomeOwner`. Copy `templates/learnings.md` as
`learnings.md`. For AI-related work, create `learnings/` and copy
`templates/ai-learning-record.md` there as a starting record only when a meaningful workflow
change has evidence to capture.
Set `phase: Define`, `statusColor: Unassessed`, and dates in ISO format until the decision owner
agrees on project-specific Green/Yellow/Red criteria.

## Intake

Always establish, scaled to project size. A small effort can use one outcome signal, a short
hypothesis, and a simple decision gate; keep unused detail explicitly out rather than imposing
ceremony:

- problem, target users, intended outcome, scope and non-goals
- decision owner and review/approval boundaries
- falsifiable hypothesis, baseline, leading indicator, measurement source/method
- first decision gate and its criteria
- access, integration, governance-review, and shared-resource dependencies before promising dates
- existing work-tracking system of record and any required status/ownership mappings; never assume
  GitHub, Azure DevOps, or another provider
- status/reporting expectations and project-specific RYG thresholds for the outcome, schedule,
  quality, adoption, or other relevant signals

For AI-enabled workflow proposals only, add the conditional AI intake in `project.yaml` and
`charter.md`: where users already work; validation of real-record permissions and routing;
representative messy cases; comparison against a baseline and alternatives on the same quality
criteria; quality review and human override; production-readiness criteria distinct from prototype
feasibility; and explicit stop, pivot, or expand criteria. Start with one bounded capability and
expand only when observed user friction or evidence justifies it. Do not make these checks a
requirement for non-AI work.

Do not overwrite an existing project without confirmation. Use relative links between project
files and avoid embedding the absolute OneDrive root so the folder can later move into or become
a git repository unchanged. Copy `templates/project-README.md` and `templates/project.gitignore`
into the project folder as `README.md` and `.gitignore`; include `learnings.md` in the project
from the outset. Do not initialize Git automatically; offer the documented promotion
steps only when useful or requested. Do not create a duplicate routing brief in the Scout
workspace. Seed a concise checklist in the user's task system only when that integration is
available. Route charter work to `skills/pm-charter/SKILL.md`.
