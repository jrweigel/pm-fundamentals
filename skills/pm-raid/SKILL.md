---
name: pm-raid
description: Maintain canonical RAID data in raid.yaml.
---
# RAID

Maintain `raid.yaml` with `risks`, `issues`, and `changes` arrays. Include `evidenceSource` for
material claims and a `decisionId` when an entry was created or changed due to a recorded
decision. Risks use Probability/Severity
`High|Medium|Low`, numeric Score = P x S (3/2/1), and require mitigation/contingency when score
is 6 or higher. Issues use State `New|Open/Unassigned|Open/Assigned|Closed|On Hold|Cancelled`
and Priority `High|Medium|Low`. Changes use Status `Proposed|Approved|Rejected|Deferred`.
Never delete history; transition status instead. Use stable sequential IDs and update
`project.yaml.lastUpdated`. Offer a linked Issue when a risk occurs. Export XLSX on demand.
