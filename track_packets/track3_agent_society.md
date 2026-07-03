# Track 3 Packet - Agent Society

## Submission Thesis

Qwen Agent Society is a production multi-agent decision room where specialist
agents decompose a real task, negotiate evidence and risk, resolve conflicts,
and produce a human-signoff packet with measurable improvement over a
single-agent baseline.

## Existing Overlap

- Quadro is the primary source skeleton.
- Quadro already has intake, evidence, policy/risk, decision packet, memory,
  JSONL audit, and signoff gates.

## Build Plan

1. Clone Quadro public-safe modules into Qwen-specific names.
2. Replace or wrap model calls with Qwen Cloud adapters.
3. Add explicit disagreement protocol: conflict type, agent positions,
   evidence cited, resolution, and unresolved risk.
4. Add single-agent baseline runner on the same real task packet.
5. Produce architecture docs and demo evidence.

## Real Evidence Gate

Use a real sanitized task packet and real Qwen calls. Record both single-agent
and multi-agent outputs.

Metrics:

- task decomposition completeness
- source citations retained
- disagreements detected/resolved
- runtime/call count
- human gate result
- improvement over single-agent baseline

## Do Not Copy

- Band credentials
- `.env`
- live Band config
- audit SQLite DBs
- private source packets

