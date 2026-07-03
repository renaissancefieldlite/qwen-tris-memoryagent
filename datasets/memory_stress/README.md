# Qwen Tris Memory Stress Datasets

These are public-safe seed datasets for the Qwen Cloud MemoryAgent lane.

They are not toy chat transcripts. The seed rows are derived from cleared
Trismegistus receipts and public-safe benchmark/work lanes.

## Files

- `swe_code_memory_seed.jsonl`
  - code repair memory stress rows from SWE-bench-style receipts and boundary
    cases.
- `webarena_browser_memory_seed.jsonl`
  - browser/source mission memory rows from WebArena-style traces and live
    source reads.
- `long_session_coherence_seed.jsonl`
  - continuity rows for long sessions, context compaction, and correction
    retention.
- `c5b_500_ssp_memory_seed.jsonl`
  - C5B / Golden Mark / 500-iteration SSP rows for stable-state memory
    refinement, six-lane curriculum recall, and architecture-on/off boundary
    discipline.
- `external_work_receipts_seed.jsonl`
  - real work rows: public PR, bounty state, payment/status boundary, and
    review gates.

## Comparison Route

Run the same row through:

```text
baseline Qwen without SSP memory
vs
Qwen Tris architecture-on memory
```

## Scoring Principle

The model must:

- recall the active task state
- suppress stale or decoy memory
- name the exact next gate
- preserve approval boundaries
- preserve the C5B / SSP public-safe boundary instead of turning internal
  engineering receipts into public leaderboard or AGI claims
- cite the receipt/source when making a support claim

Do not use gold patches as training/performance data.
