---
name: pm-charter
description: Draft and maintain charter.md as the canonical project charter.
---
# Charter

Read `project.yaml` and write `charter.md` from `templates/charter.md`. Preserve the standard
charter sections and include the intake: problem, target users, outcome, scope/non-goals, decision
owner, review boundaries, falsifiable hypothesis, baseline, leading indicator, measurement
source/method, first decision gate, dependencies, and an outcomes register in `project.yaml`.
Each outcome has a stable ID, intended result, measure, baseline/target, and one outcome owner
accountable for verifying the result. Plan tasks name their deliverable owner and link to an
outcome ID; those roles may be held by the same person but are distinct responsibilities. For
AI-enabled proposals only, complete
the conditional AI workflow intake; do not force it on unrelated work. Define a bounded initial
capability and production-readiness criteria; a successful prototype demonstrates feasibility,
not production readiness. Expand only when evidence or observed user friction warrants it.

Agree project-specific RYG criteria with the decision owner before the first status report.
Record thresholds, signal source, measurement method, agreement date, and review trigger in
`project.yaml.healthCriteria`. The RYG labels remain Green/Yellow/Red, but do not infer thresholds
from a universal rule. If criteria are not yet agreed, keep status `Unassessed`. Resolve people
rather than guessing identities. Leave unknown values as `TBD` and surface evidence gaps. Only
set `keyDates.charterApproved` after explicit approval. Export DOCX only when requested.
