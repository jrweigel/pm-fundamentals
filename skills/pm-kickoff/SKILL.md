---
name: pm-kickoff
description: Draft kickoff.md and optionally export a PPTX kickoff deck.
---
# Kickoff

Read `charter.md`, `project.yaml`, and relevant entries from `decisions.yaml`; write `kickoff.md`
from its template. Cover agenda, introductions, the problem/outcome and hypothesis, agreed success
measures and RYG criteria, project overview, outcome owners and how results will be verified,
deliverable owners and what they will produce, change management overview when active,
project information/guidelines, first decision gate, next steps, and Q&A.
Keep Markdown canonical. Generate the
audience deck only with `python exporters/pmfx/to_pptx.py --input kickoff.md --output Kickoff-Deck.pptx`.
Preview attendees and content before scheduling or sending anything.
