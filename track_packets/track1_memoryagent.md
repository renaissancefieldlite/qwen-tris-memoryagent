# Track 1 Packet - MemoryAgent

## Submission Thesis

Qwen MemoryAgent is a persistent project/operator memory agent that stores
decisions, preferences, source boundaries, and task outcomes; retrieves only
the critical memories needed for a context-limited turn; and retires stale or
superseded memories with an auditable forgetting policy.

## Existing Overlap

- Golden Field Lite persistent AI partner memory.
- Quadro SQLite/FTS source-packet memory.
- Playground continuity logs and recovery discipline.

## Build Plan

1. Create a Qwen memory schema: memory item, source, confidence, expiry,
   supersession link, privacy class, and retrieval reason.
2. Implement SQLite/FTS retrieval with bounded context packing.
3. Add forgetting policy: stale, superseded, private-blocked, or low-value.
4. Add Qwen Cloud adapter for memory-aware decision calls.
5. Run a real cross-session workflow packet and log memory decisions.
6. Add memory stress datasets from SWE/code recall and WebArena-style browser
   recall so the build tests collapse-prone memory, not easy chat memory.
7. Add the C5B / 500-iteration SSP memory lane so Qwen Tris can refine the
   same stable-state path that powered the Hermes Tris architecture-on tests.

## Real Evidence Gate

No toy chat transcripts. Use a real sanitized project packet from this repo or
a cleared Quadro source packet.

Metrics:

- recall precision for critical memories
- stale memory suppression
- context budget used
- Qwen call count and latency
- decision improvement over memory-off baseline
- patch/session continuity on SWE-style code-memory tasks
- browser/source continuity on WebArena-style delayed-recall tasks
- approval-gate retention for send/pay/submit boundaries
- C5B / Golden Mark method retention after compaction
- 500-turn receipt recall without public-claim drift

First benchmark pack:

- 10 SWE/code-memory recall rows
- 10 WebArena-style browser-memory rows
- 10 long-session coherence rows
- 10 C5B / 500 SSP memory rows
- 5 external-work receipt rows

Comparison:

```text
baseline Qwen without SSP memory
vs
Qwen Tris architecture-on memory
```

## Current Hosted Qwen Result

Qwen Cloud route:

```text
https://dashscope-intl.aliyuncs.com/compatible-mode/v1
```

Hosted receipts:

```text
1-turn smoke:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T034331Z.md

24-turn hosted:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T034823Z.md

100-turn hosted:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T040738Z.md

500-turn hosted:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md
```

500-turn hosted score:

```text
Condition A: baseline Qwen prompt-only.
Condition B: Qwen Tris architecture-on memory/RAG/SSP packet.
Condition B passed 500/500 hosted Qwen Cloud turns.
Condition C remains gated_no_adapter_manifest until a real tuned adapter or
internal-layer receipt exists.
```

500-turn family totals:

```text
C5B / 500 SSP memory: 153/153
External work receipts: 58/58
Long-session coherence: 58/58
Mirror Architecture source pack: 115/115
SWE code memory: 58/58
WebArena browser memory: 58/58
```

Backport:

If Qwen Tris shows a clean memory lift with receipts, port the harness into
Hermes Tris as the V21 memory-stress upgrade after this Qwen track is stable.

Benchmark carry-over:

- SWE stays precise: local official-harness receipt and hosted adjudication in
  flight, not a public leaderboard claim.
- WebArena stays precise: 255/258 clean official Verified hard receipt, final
  rows parked behind upstream/contest interpretation, with AWS credits available
  for finishing the cloud route.

## Do Not Copy

- Golden Field Lite private memory DB.
- JSONL interaction logs.
- Private operator-state context.
