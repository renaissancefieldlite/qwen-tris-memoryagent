# Track 4 Packet - Autopilot Agent

## Submission Thesis

Qwen Autopilot handles an end-to-end real business workflow from ambiguous
request intake through source-backed response/quote generation, risk review,
and human approval.

## Recommended First Workflow

Inbound customer or partner request to:

1. classify request
2. gather needed details
3. retrieve source policy/pricing/service constraints
4. draft quote or response
5. perform risk/release check
6. request human approval
7. prepare final send packet

## Existing Overlap

- Quadro intake/evidence/decision gates.
- Golden Field Lite memory for preferences and account context.
- Cash-ops/no-call audit style workflows if explicitly cleared.

## Build Plan

1. Define the workflow packet and approval checkpoints.
2. Build dry-run tool interfaces first: no real send, payment, or external
   account mutation.
3. Add Qwen Cloud reasoning for ambiguity handling and draft generation.
4. Add human-in-the-loop gates at quote approval and final send.
5. Log every tool call and decision.

## Real Evidence Gate

Use a real sanitized business request. No synthetic customer demo unless it is
clearly marked as a UI-only smoke test.

Metrics:

- ambiguity resolved
- missing information asked
- policy/source citations
- human checkpoint count
- external side effects blocked or approved
- end-to-end completion time

## Do Not Copy

- private email
- credentials
- financial account data
- live send actions without explicit approval

