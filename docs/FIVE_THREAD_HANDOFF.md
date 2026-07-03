# Five Thread Handoff

Use this file to fork five Codex threads. Each thread owns one track and writes
only inside this repo unless explicitly approved.

## Thread 1 - MemoryAgent

Track:

```text
Track 1: MemoryAgent
```

Goal:

Build a Qwen-powered memory agent that persists user/project preferences,
retrieves critical memories under context limits, and forgets stale state with
an auditable policy.

Source overlap:

- Golden Field Lite persistent memory.
- Quadro SQLite/FTS memory.
- Playground memory discipline and locked-source continuity logs.

Owned files:

- `track_packets/track1_memoryagent.md`
- future `src/qwen_agent_buildout/memory_agent/*`
- future `tests/test_memory_agent*.py`

First gate:

Read the source inventory, then copy or reimplement only public-safe memory
guts into a Qwen-specific module. No private memory DBs or JSONL logs.

Proof gate:

Real cross-session task packet with before/after recall, stale-memory pruning,
and Qwen Cloud call logs.

## Thread 2 - AI Showrunner

Track:

```text
Track 2: AI Showrunner
```

Goal:

Build a public-safe showrunner agent that turns an approved project packet into
a short demo/drama pipeline: script, storyboard, shot list, generation plan,
asset ledger, and edit decision list.

Source overlap:

- Quadro evidence packets and demo-script discipline.
- Golden Field Lite narrative continuity.
- Public-safe RFL pitch/deck style constraints where explicitly cleared.

Owned files:

- `track_packets/track2_ai_showrunner.md`
- future `src/qwen_agent_buildout/showrunner/*`
- future `tests/test_showrunner*.py`

First gate:

Create the showrunner packet schema and keep it public-safe. Do not use private
operator-state context or raw artifacts as video content.

Proof gate:

One approved public-safe source packet converted into script, storyboard, and
generation/edit ledger. If Wan/HappyHorse is used, log the exact Qwen route and
artifact IDs.

## Thread 3 - Agent Society

Track:

```text
Track 3: Agent Society
```

Goal:

Port Quadro into a Qwen Cloud agent society: intake, evidence, policy/risk,
decision packet, and human approval agents with disagreement handling and a
single-agent baseline comparison.

Source overlap:

- Quadro is the main source skeleton.
- Golden Field Lite can inform memory/state continuity.

Owned files:

- `track_packets/track3_agent_society.md`
- future `src/qwen_agent_buildout/agent_society/*`
- future `tests/test_agent_society*.py`

First gate:

Copy the Quadro public-safe agent skeleton into this repo under renamed Qwen
modules. Remove Band-specific and private config assumptions unless they are
kept behind adapters.

Proof gate:

Run the same real task packet through single-agent and multi-agent modes, then
report efficiency, conflicts resolved, sources cited, and human gate status.

## Thread 4 - Autopilot Agent

Track:

```text
Track 4: Autopilot Agent
```

Goal:

Build a production-ready autopilot for a real business workflow. Recommended
first workflow: inbound customer/request packet to scoped quote, source-backed
response, risk check, and human approval.

Source overlap:

- Quadro intake/evidence/decision packet.
- Funding/cash-ops discipline for no-call audit/quote style workflows.
- Golden Field Lite persistence for account preferences and follow-up memory.

Owned files:

- `track_packets/track4_autopilot_agent.md`
- future `src/qwen_agent_buildout/autopilot/*`
- future `tests/test_autopilot*.py`

First gate:

Define the real workflow packet and human checkpoints. Do not connect email,
payment, or external send actions until the dry-run packet passes.

Proof gate:

End-to-end dry run on a real sanitized request packet, with tool invocations,
ambiguous-input handling, approval checkpoint, and no external send unless
explicitly approved.

## Thread 5 - EdgeAgent

Track:

```text
Track 5: EdgeAgent
```

Goal:

Build a Qwen-powered edge/cloud orchestration demo that uses edge sensor or
device-state inputs, sends only privacy-safe summaries to Qwen Cloud, and acts
locally with offline/weak-network fallback.

Source overlap:

- B.A.S.I.S. Phase 12C capture and trace discipline.
- Orin/YRA direct-control boundary.
- B.A.S.I.S. Mac/MLX versus Orin trace manifest separation.

Owned files:

- `track_packets/track5_edgeagent.md`
- future `src/qwen_agent_buildout/edge_agent/*`
- future `tests/test_edge_agent*.py`

First gate:

Use only sanitized manifests/status summaries, not raw captures. Do not change
Mac network services, routes, adapters, DNS, or Orin Ethernet settings.

Proof gate:

Edge/cloud run showing local perception summary, Qwen reasoning call, local
action recommendation, privacy filter, latency/bandwidth note, and offline
fallback behavior.

## Shared Coordinator Gate

Main repo steward owns:

- `QWEN_BUILDOUT_LOG.md`
- `docs/BROWSER_VERIFICATION_2026-06-10.md`
- `docs/LOCKED_LANGUAGE_AND_BOUNDARIES.md`
- `source_inventory/PLAYGROUND_SOURCE_MAP.md`
- final README/submission assembly

