---
name: pm-change-mgmt
description: Maintain change-mgmt.md for impact, ADKAR, communications, training, and sustainment.
---
# Change management

If impact is unassessed, score the seven 1-5 prompts in the template and calculate the total:
`28-35 HIGH`, `14-27 MEDIUM`, `7-13 LOW`. Medium/High normally requires a formal workstream.
Maintain audiences, impact strategy, ADKAR Activities, Communications Plan, Training Plan,
Training Schedule, Training Session Plan, and Sustainment Plan. Update `project.yaml` with
`changeManagementActive`, `changeLevel`, and `lastUpdated`. Keep adoption measures linked to
the project's agreed baseline and measurement method; do not treat workflow/tool counts alone as
proof of behavior change. Link adoption goals to outcome IDs in `project.yaml`, identify an
outcome owner who verifies behavior/result measures, and distinguish those from deliverable owners
who produce training or communications. Use `templates/training.md` and
export a training deck with `to_pptx.py` only after training content is ready.
