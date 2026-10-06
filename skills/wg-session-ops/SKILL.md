---
name: wg-session-ops
description: Turn a project or working-group session into evidence-backed work tracking, canonical status artifacts, and a reviewable team recap.
---

# Working-group session operations

Use this skill after a recurring project, working-group, or steering meeting when the
session produces decisions, owners, status changes, or new asks. The workflow is:

`Ingest -> Extract -> Triage -> Confirm -> Publish -> Sync -> Recap`

## Inputs

Read the project's `project.yaml`, `plan.yaml`, `raid.yaml`, `decisions.yaml`, and canonical
workstream status document before acting; read `evidence.yaml` and `learnings.md` when present.
Collect the meeting transcript, meeting chat, linked documents, and any existing issue/PR
references from authorized sources. The transcript or user-provided notes are the evidence
baseline; do not infer decisions from silence.

Project configuration may optionally define:

```yaml
workTracking:
  provider: "" # Set to the project's actual system; never assume one.
  projectReference: ""
  statusField: ""
  statusValues: [] # Exact values from the configured system.
  statusMapping: {} # Optional mapping from PM concepts to system-specific values.
  ownershipBoundaries: []
  canonicalStatusFile: ""
  teamChannel: ""
```

Do not assume GitHub, Azure DevOps, a project hierarchy, status vocabulary, or channel. If the
project has no configured integration, prepare a local Markdown/YAML proposal and ask which
system of record to use before attempting external writes.

## Extract

Produce a proposal containing:

- decisions and supporting evidence locations
- workstream, epic, and task mapping
- owners and ownership changes
- new issues or description changes
- status transitions and reasons
- milestone/date changes
- unresolved questions, dependencies, and risks
- distinguish confirmed decisions from proposals and open questions; include rationale,
  alternatives, dissent/concerns, decision owner, evidence reference, and next review point
- for each proposed action, capture one owner, deliverable, due date, confirmation status, and
  the outcomeId it advances, and the dependency or decision it unblocks; distinguish the
  deliverable owner from the outcome owner who verifies results. Tentative language remains
  unconfirmed.
- classify material claims as observed, estimate, assumption, or recommendation; preserve source,
  date, denominator, method, freshness, confidence, and contradictory evidence when available
- draft team recap and participation asks

Keep facts, explicit decisions, and inferred recommendations separate. Preserve issue
history; do not close or reassign work solely because it was not mentioned.

## Triage rules

- Respect every configured ownership boundary. Escalate protected work to its owner.
- Match status to evidence using the project's configured status mapping. Treat common labels such
  as backlog, ready, in progress, in review, and done as examples only; do not force them onto a
  system with different semantics. Completion requires the project's acceptance criteria.
- Prefer updating an existing issue over creating a duplicate.
- Use stable issue IDs and link parent epics, plans, PRs, and canonical artifacts.
- Record a concise, evidence-backed reason for each status transition using the configured
  system's appropriate history/comment mechanism.
- Treat milestone changes, ownership changes, issue closure, and outbound communication
  as consequential actions requiring confirmation.

## Confirmation gate

Before any write, show a compact change table with item, old value, new value, reason,
and evidence. Show exact external comments and the exact team recap, including recipients or
channel. Do not publish external work-tracker changes, edit canonical files, or send messages until
the user explicitly confirms.

## Publish and sync

After confirmation:

1. Apply only the configured system's approved field updates (for example, description, owner,
   milestone, or status).
2. Record approved rationale in the configured system when it supports change history/comments.
3. Update `workstream-status.md` from the same extracted facts.
4. Append confirmed decisions to `decisions.yaml`; record material evidence in `evidence.yaml`
   when the project uses that ledger. Do not rewrite confirmed decision history; supersede by
   appending a new record.
5. Update `project.yaml`, `plan.yaml`, or `raid.yaml` when the change affects lifecycle,
   dates, tasks, risks, issues, or changes. Add a learning to `learnings.md` when the meeting
   yields a reusable observation or follow-through experiment. For a material AI workflow change,
   create a linked record from `templates/ai-learning-record.md` under `learnings/`; record before,
   change, observed result and guardrails, and what will change next, linked to evidence/outcome/
   decision IDs. Do not create a record for routine AI use.
6. Commit related Markdown/YAML changes together when the project uses Git.
7. Verify the resulting issue/project state and document links.

Never send the recap automatically unless the user separately confirms the exact
outbound message. Draft-only is the default.

## Recap structure

Use `templates/wg-recap.md` as the structure:

1. thank-you and source/recording link
2. current phase or sprint
3. workstream-by-workstream decisions and asks
4. issue and artifact links
5. explicit ways to volunteer or provide feedback
6. owner for corrections and next checkpoint

Do not include private calendar, email, transcript, or document details that are not
appropriate for the intended audience.
