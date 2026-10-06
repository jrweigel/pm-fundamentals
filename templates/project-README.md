# {{ projectName }}

Project files are maintained in Markdown/YAML. Office documents are generated outputs; edit the
canonical source files instead.

## Start here

- `project.yaml` — intake, health criteria, phase, and key dates
- `project.yaml.outcomes` — intended outcomes, measures, and accountable outcome owners
- `project.yaml.workTracking` — optional actual system-of-record configuration; no provider is assumed
- `charter.md` — problem, outcome, scope, measures, and authorization
- `plan.yaml` — deliverable owners, outcome links, and acceptance criteria
- `raid.yaml` — risks, issues, and changes
- `decisions.yaml` — append-only decisions and open questions
- `evidence.yaml` — optional evidence ledger
- `learnings.md` — continuous learning and follow-through experiments
- `learnings/` — optional detailed learning records, including AI-workflow learning when relevant

Every plan task names a `deliverableOwner` and links to an outcome ID in `project.yaml`. Each
outcome has one `outcomeOwner` accountable for verifying whether the intended result occurred.
These may be the same person, but represent different responsibilities.

Use relative links so this folder remains portable. The folder starts in OneDrive and can be
initialized as a Git repository later when appropriate.
