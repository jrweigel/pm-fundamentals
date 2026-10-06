---
name: pm-plan
description: Create and maintain plan.yaml for tasks and milestones.
---
# Project plan

Maintain `plan.yaml`; never make XLSX the source. Each task includes stable ID, deliverable,
one `deliverableOwner` who produces the work, an `outcomeId` linking it to the result it advances,
start/end dates, State, percent complete, notes, acceptance criteria, evidence source, confirmation
status, the dependency/decision it unblocks, linked decision ID, and last-updated date. The
linked outcome's `outcomeOwner` in `project.yaml` verifies whether the result occurred; do not
duplicate that ownership on each task. The same person may hold both roles.

Every task must link to an outcome. For enabling work, define or link to the supported outcome
rather than leaving the task orphaned. Valid State values are `Not started`, `In progress`,
`At risk`, `Blocked/delayed`, `Complete`, and `Milestone`.

Do not turn tentative language into a commitment: leave confirmation `Unconfirmed` until the
owner/decision maker confirms. Preserve existing rows, calculate overdue items and upcoming
milestones, and link claims or decisions to `evidence.yaml` / `decisions.yaml` when available.
Set `keyDates.planApproved` only after approval; move to Execute when the baseline is approved and
work has started. Export XLSX only when needed.
