---
name: pm-fundamentals
description: Markdown/YAML-first PM Fundamentals orchestrator for Define, Plan, Execute, Close, Managing/Controlling, and Change Management.
---

# PM Fundamentals

This repository (`pm-fundamentals`) holds the skills, templates, and exporters only — it is
tooling, not project storage. Before executing a sub-skill, read its `SKILL.md`. Before any
Office output, use the appropriate exporter; never make Office the source. In Scout, load a
routed custom sub-skill with `m_get_skill` by its exact skill name before applying the
repo-relative instructions.

## Project location

Every new project starts in its own folder on OneDrive:

```
<user's OneDrive root>\Documents\Projects\<project-slug>\
```

Use a portable lowercase kebab-case slug. Do not create project folders inside the Scout workspace
or inside this tooling repository. Keep links within project artifacts relative whenever possible,
so the folder can later move into or become a git repository without rewriting its contents.
In `project.yaml`, define outcomes with one accountable `outcomeOwner`; each `plan.yaml` item has a
distinct `deliverableOwner` and links to an `outcomeId`. For material AI workflow changes only,
capture a learning record: before, change, result and guardrails, and what to do differently.

## Project layout

```
Projects/<project-slug>/
  project.yaml
    outcomes[]             # outcomeId, intended result, measure, baseline/target, outcomeOwner
  charter.md
  kickoff.md
  plan.yaml
  raid.yaml
  decisions.yaml
  evidence.yaml        # optional; create when claims need a durable evidence trail
  learnings.md
  learnings/               # optional detail; AI workflow learning records when applicable
  status-report.md
  change-mgmt.md
  closeout.md
  retrospective.md
```

## Routing

| Request | Skill |
|---|---|
| New project or next action | `skills/pm-init/SKILL.md` |
| Charter | `skills/pm-charter/SKILL.md` |
| Kickoff | `skills/pm-kickoff/SKILL.md` |
| Schedule or milestones | `skills/pm-plan/SKILL.md` |
| Status report | `skills/pm-status-report/SKILL.md` |
| Risk, issue, or change | `skills/pm-raid/SKILL.md` |
| Organizational change, communications, training | `skills/pm-change-mgmt/SKILL.md` |
| Closeout or retrospective | `skills/pm-closeout/SKILL.md` |
| Post-meeting workstream and tracker synchronization | `skills/wg-session-ops/SKILL.md` |

Read `project.yaml`, `plan.yaml`, `raid.yaml`, and `decisions.yaml` from
`<user's OneDrive root>\Documents\Projects\<project-slug>`; read
`evidence.yaml` when present. Summarize phase, agreed health criteria/status, open RAID items, and
the next decision gate, then route. If no project exists, create one through pm-init. Update the
canonical project artifacts after confirmed meaningful actions. Keep proposed, confirmed, and
open-question states distinct. Keep each outcome's owner distinct from task deliverable owners and
require every plan task to link to an outcome. Ask before irreversible scope, date, ownership, or
communication decisions.
