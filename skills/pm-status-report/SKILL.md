---
name: pm-status-report
description: Generate a Markdown status report from project state, plan, and RAID data.
---
# Status report

Create a dated `status-report.md` from `templates/status-report.md`. Lead with outcome, what
changed, evidence, blockers, and the specific decision/help needed; include milestones,
accomplishments, next-period activities, and sponsor-visible risks/issues as supporting detail.
Report progress against each intended outcome and its baseline/target, name the outcome owner who
verifies the result, and distinguish delivered outputs from observed outcomes.

Use the project-agreed criteria in `project.yaml.healthCriteria` to assign Green/Yellow/Red. Do
not apply universal thresholds or invent criteria. If criteria are absent, status remains
`Unassessed`; propose criteria for the decision owner to agree before treating a color as
meaningful. Explain which indicators drove the color and cite evidence sources, dates, denominators,
and measurement methods when relevant. Distinguish observed facts, estimates, assumptions, and
recommendations; note material contradictory or stale evidence. Any override requires a rationale
and confirmation by the decision owner. Update `project.yaml` after confirmation. `Complete` is reserved for formally closed projects.
Export DOCX only on request and preview recipients before distribution.
