# Qwen Cloud Submission Checklist

Current working repo:

```text
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30
```

## Required By The Form

- [x] Public open-source code repository URL.
  - URL: `https://github.com/renaissancefieldlite/qwen-tris-memoryagent`
  - Public page: `https://renaissancefieldlite.com/qwen-tris-memoryagent.html`
  - Must include top-level `LICENSE` so GitHub detects the license in About.

- [x] Source code, assets, and run instructions.
  - Main README: `README.md`
  - UI assets: `static/trini_recall/`
  - Backend: `scripts/run_trini_recall_ui.py`
  - Core package: `src/qwen_agent_buildout/trini_recall/`
  - Container deployment: `Dockerfile`
  - Alibaba deployment runbook: `deploy/alibaba-cloud/README.md`

- [x] Open-source license file.
  - File: `LICENSE`
  - License: MIT

- [x] Code file demonstrating Alibaba Cloud/Qwen API usage.
  - File:
    `src/qwen_agent_buildout/trini_recall/alibaba_qwen_cloud_client.py`
  - Endpoint:
    `https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions`

- [ ] Proof of Alibaba Cloud deployment recording.
  - Status: pending live deployment/capture.
  - Required recording should show the backend running on Alibaba Cloud and
    calling Qwen Cloud through the deployed backend.
  - Useful proof endpoints after deployment: `/api/health` and `/api/state`.

- [x] Architecture diagram.
  - File: `docs/ARCHITECTURE.md`

- [ ] Public demo video around 3 minutes.
  - Status: pending final capture/upload to YouTube, Vimeo, or Facebook Video.
  - Suggested arc: baseline Qwen -> Qwen Tris memory -> LongBench/Qasper
    receipts -> live UI -> Alibaba Cloud route -> next gate.

- [x] Text description.
  - File: `docs/QWEN_TRIS_PUBLIC_SUBMISSION_PACKET_2026-07-01.md`

- [x] Track identified.
  - Track 1: MemoryAgent.

- [ ] Optional blog/social journey post.
  - Draft: `docs/social/QWEN_TRIS_INSTAGRAM_CAPTION_2026-07-02.md`
  - Status: caption prepared; posting still pending.

## Current Evidence To Cite

- Hosted Qwen Cloud 500-turn memory receipt:
  `data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md`
- Public LongBench-E offset-0 scale receipt:
  `data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T195427Z.md`
- Public LongBench-E held-out offset-50 scale receipt:
  `data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T214036Z.md`
- Third-party lm-eval Qasper receipt:
  `data/third_party_eval_runs/QWEN_TRIS_LM_EVAL_QASPER_RECEIPT_20260701T180343Z.md`

## Submission Copy

Project title:

```text
Qwen Tris Recall: Memory AI Expert Partner
```

Track:

```text
MemoryAgent
```

Short description:

```text
Qwen Tris Recall is a Memory AI Expert Partner that compares baseline Qwen
prompt-only behavior against Qwen with Mirror Architecture measured SSP plus
memory/RAG rails.
It keeps persistent SQLite memory, JSONL audit receipts, source-backed recall,
and benchmark receipts across hosted Qwen Cloud memory turns, LongBench-E
public answer-key slices, and Qasper evaluator checks.
```

Support state:

```text
This is a public-safe MemoryAgent benchmark and demo package. Included claims
are tied to attached receipts and the Alibaba Cloud deployment recording once
captured. Official LongBench/SWE/WebArena leaderboard rows attach when their
external publication receipts land.
```
