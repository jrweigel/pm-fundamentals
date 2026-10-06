---
name: pm-closeout
description: Close a project with canonical closeout.md and retrospective.md artifacts.
---
# Closeout

Before closing, verify tasks are Complete or explicitly descoped, open RAID items are resolved
or transferred, the sponsor agrees, and an operations owner exists. Assess outcomes against the
charter's baseline, measurement methods, and agreed health/success criteria; label estimates and
missing evidence rather than inventing results. Ask the named outcome owners to validate measured
results; do not treat deliverable completion as proof that an outcome occurred. Write `closeout.md`
and `retrospective.md`.

Append material learnings to `learnings.md` as they emerge. Convert selected retrospective
improvements into owned experiments with a falsifiable hypothesis, due date, evidence source, and
success criteria; track follow-through rather than stopping at the retro. Set
`project.yaml.phase: Complete` and `statusColor: Complete` only after explicit closure approval.
For a material AI-workflow change, create a dated record from `templates/ai-learning-record.md`
under `learnings/`, linking its evidence, outcome IDs, and resulting decision IDs; do not create
one for routine AI use. Export DOCX on demand.
