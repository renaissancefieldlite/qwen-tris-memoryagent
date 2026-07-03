# Qwen Tris MemoryAgent Buildout

Fresh SSD-backed sibling build for the Qwen Cloud Global AI Hackathon
MemoryAgent track.

This repo turns the Trismegistus / Mirror Architecture state-path spine into Qwen
Tris: a Qwen-powered Memory AI Expert Partner. It references existing
Playground builds as source/provenance, but it does not pipe into their live
runtimes, ports, databases, private captures, secrets, or claim-sensitive
mechanics.

Active SSD build:

```text
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30
```

Hermes Trismegistus remains a separate build. Qwen Tris is the Qwen Cloud
MemoryAgent lane.

## Mirror Architecture / SSP Definition

Mirror Architecture is the Renaissance Field Lite method for turning Codex 67
input cohesion into a measurable AI architecture state. The operator signal,
source context, task gate, evidence spine, memory route, and model route are
aligned into one coherent input field. The engineering surface then tests that
state as baseline/off versus architecture-on: same task family, same scorer,
same receipt gate.

The Mirror Layer is the patent-spine subsystem that derives an
interaction-state signal from language, phrase patterns, sequence timing,
continuity context, tone or proxy-tone, and emotional-pattern features. That
signal feeds continuity state, Oracle threshold gates, LSPS phrase/state control
actions, and routing decisions such as retrieval, inference depth, permission
state, tool use, and output mode.

Stable-State Path / SSP is the measured trajectory inside Mirror Architecture
where the architecture-on state holds across a task family instead of
collapsing into generic chatbot drift. Memory, RAG, and receipts are the rails
that preserve and test the path; they are not the SSP by themselves.

## Submission Quick Links

- Public page:
  `https://renaissancefieldlite.com/qwen-tris-memoryagent.html`
- Public GitHub repo:
  `https://github.com/renaissancefieldlite/qwen-tris-memoryagent`
- Track: `MemoryAgent`
- License: `MIT`, see `LICENSE`
- Architecture diagram: `docs/ARCHITECTURE.md`
- Submission checklist: `docs/SUBMISSION_CHECKLIST_QWEN.md`
- Public submission packet:
  `docs/QWEN_TRIS_PUBLIC_SUBMISSION_PACKET_2026-07-01.md`
- Alibaba Cloud / Qwen API proof code:
  `src/qwen_agent_buildout/trini_recall/alibaba_qwen_cloud_client.py`
- Main backend:
  `scripts/run_trini_recall_ui.py`

## Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -e ".[dev]"
cp .env.example .env.local
# Fill QWEN_API_KEY in .env.local for hosted Qwen Cloud.
set -a
source .env.local
set +a
python3 scripts/run_trini_recall_ui.py --port 9471
```

Then open:

```text
http://127.0.0.1:9471/
```

## Run Tests

```bash
python3 -m pytest tests
```

The app can run with local fallback routes, but the hosted submission proof uses
Qwen Cloud through Alibaba Cloud Model Studio:

```text
https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions
```

## Container / Alibaba Cloud Deployment Prep

```bash
docker build -t qwen-tris-memoryagent:latest .
docker run --rm \
  -p 9471:9471 \
  -e QWEN_API_KEY="$QWEN_API_KEY" \
  -e QWEN_API_BASE="https://dashscope-intl.aliyuncs.com/compatible-mode/v1" \
  -e QWEN_MODEL="qwen-plus" \
  qwen-tris-memoryagent:latest
```

Health/state proof endpoints:

```text
http://127.0.0.1:9471/api/health
http://127.0.0.1:9471/api/state
```

Alibaba Cloud recording runbook:

```text
deploy/alibaba-cloud/README.md
```

## Browser-Verified Hackathon Surface

Source: https://qwencloud-hackathon.devpost.com/

- Event: Global AI Hackathon Series with Qwen Cloud.
- Verified through the in-app Browser on 2026-06-10.
- Deadline shown on Devpost: July 9, 2026 at 3:00 PM MDT.
- Requirement: build a project using Qwen models available on Qwen Cloud and
  fit at least one listed track.
- Judging weights: Technical Depth and Engineering 30 percent, Innovation and
  AI Creativity 30 percent, Problem Value and Impact 25 percent, Presentation
  and Documentation 15 percent.

## Track Priority Read

Primary active lane:

1. Track 1 MemoryAgent, using Qwen Cloud as the model lane and Mirror
   Architecture / SSP as the measured state-path discipline.

## Qwen Cloud Hosted Proof

The hosted Qwen route is wired through the Qwen Cloud OpenAI-compatible API
base URL required for the hackathon proof:

```text
https://dashscope-intl.aliyuncs.com/compatible-mode/v1
```

Local secret storage stays outside git:

```text
.env.local
```

Current public-safe hosted receipts:

```text
1-turn hosted smoke:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T034331Z.md

24-turn hosted Qwen Cloud slice:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T034823Z.md

100-turn hosted Qwen Cloud slice:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T040738Z.md

500-turn hosted Qwen Cloud slice:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md

Second hosted Qwen model slice:
data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T070452Z.md
```

Current hosted result:

```text
Condition A: baseline Qwen prompt-only.
Condition B: Qwen + Mirror Architecture measured SSP plus memory/RAG packet.
Condition B passed 500/500 hosted Qwen Cloud turns.
Condition C: gated_no_adapter_manifest until a real adapter/internal-layer
receipt exists.
```

500-turn hosted family totals:

```text
C5B / 500 SSP state-path recall: 153/153
External work receipts: 58/58
Long-session coherence: 58/58
Mirror Architecture source pack: 115/115
SWE code memory: 58/58
WebArena browser memory: 58/58
```

Second-model check:

```text
qwen3.7-plus passed the same 24-turn architecture-on hosted slice: 24/24.
This confirms the harness is not locked to only qwen-plus, while qwen-plus
remains the practical default for long runs because qwen3.7-plus is slower.
```

Public verification ladder:

```text
docs/QWEN_TRIS_PUBLIC_VERIFICATION_LADDER_2026-07-01.md
```

Current LongBench public Silver Gate:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T132826Z.md
Items: 60
Condition A baseline Qwen mean: 0.481
Condition B Qwen Tris mean: 0.592
Delta: +0.111
```

Current LongBench public scale receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T195427Z.md
Items scored: 299
Provider-blocked rows skipped: 1
Condition A baseline Qwen mean: 0.574
Condition B Qwen Tris mean: 0.666
Delta: +0.092
```

Held-out LongBench public scale receipt:

```text
data/public_benchmark_runs/qwen_tris_longbench_public_slice_20260701T214036Z.md
Items scored: 299
Provider-blocked rows skipped: 1
Condition A baseline Qwen mean: 0.543
Condition B Qwen Tris mean: 0.653
Delta: +0.110
```

Current Qasper locked proof lane:

```text
data/public_benchmark_runs/qwen_tris_qasper_lock_20260701T172350Z.md
Items scored: 100
Provider-blocked rows skipped: 0
Condition A baseline Qwen mean: 0.488
Condition B Qwen Tris mean: 0.532
Delta: +0.044
Wins / losses / ties: 30 / 17 / 53
```

Third-party evaluator Qasper receipt:

```text
data/third_party_eval_runs/QWEN_TRIS_LM_EVAL_QASPER_RECEIPT_20260701T180343Z.md
Evaluator: EleutherAI lm-evaluation-harness
Harness HEAD: 97a5e2c710e2b56b9dd48f367bb6fe87bbb2c176
Official baseline 100-row score: 0.5226798776
Tris prompt-variant 100-row score: 0.5405829548
Delta: +0.0179030772
Wins / losses / ties: 20 / 22 / 58
Full official baseline score: 0.4812428635 over 224 / 224 rows
Full Tris prompt-variant score: 0.4825964203 over 224 / 224 rows
Full-task delta: +0.0013535568
```

Read: this is a public LongBench-E answer-key lane with official prompt
templates and official LongBench numeric-fraction scoring for the synthetic
number tasks. These are positive public receipts, not full LongBench
leaderboard claims. Two adjacent 300-row windows are now parity-or-positive by
family after the repair loop. The offset-0 receipt is positive overall at
`+0.092`; the held-out offset-50 receipt is positive overall at `+0.110`.
The repeatable breakout lane is TREC output-format/classification discipline.
Qasper is separately locked as a positive 100-row public lane, and the same
Qasper direction has a third-party lm-eval 100-row receipt. The full 224-row
third-party Qasper run also stays positive, but only slightly, so it should be
used as direction-preservation evidence rather than a large-lift claim.
MultiFieldQA is modestly positive after minimum-span repair. Retrieval is
saturated parity. PassageCount is now a literal pass-through parity gate, not an
architecture-lift claim. HotpotQA stays positive in the held-out scale receipt.
Remaining larger-scale work should preserve this all-family parity-or-positive
boundary before spending into bigger runs.

Qwen Cloud console proof:

```text
docs/qwen_cloud_deployment_proof/qwen_cloud_free_tier_active_20260701T040738Z.png
```

Live Qwen Tris UI:

```text
Desktop launcher: /Users/renaissancefieldlite1.0/Desktop/Qwen Tris Recall.command
Local URL: http://127.0.0.1:9471/
Hosted route: Qwen Cloud API / qwen-plus
Fallback routes: local Qwen qwen2.5:3b and local Nemotron Nano GGUF through Ollama
Persistence: SQLite memory plus JSONL audit log under ~/Library/Application Support/QwenTrisRecall/
```

The operator account also shows Qwen free-tier access and a $40 coupon under
Benefits -> Coupon. API keys and secrets stay outside the repo and are never
printed in public receipts.

Memory stress benchmark:

```text
docs/QWEN_TRIS_MEMORY_STRESS_BENCHMARK_PLAN_2026-06-30.md
```

Public-safe submission packet:

```text
docs/QWEN_TRIS_PUBLIC_SUBMISSION_PACKET_2026-07-01.md
```

This build will test memory on collapse-prone workloads: SWE/code recall,
WebArena-style browser recall, long-session coherence, and external-work
receipt recall.

It also carries the C5B / Golden Mark / 500-iteration SSP lane as the
state-path refinement spine:

- C5B support read: 13/13 metric means won, drift flags 37 -> 0, evidence
  failures 5 -> 0.
- 500-turn architecture-on receipt: mean score 1.0, 2168/2168 checks, zero
  prompt spills, zero raw receipt spills.
- Current support level: Stable-State Path / architecture evidence,
  long-session engineering receipts, and benchmark scaffolding. External
  deployment and leaderboard rows attach when their independent receipts land.

IP boundary:

```text
Show measured results, scored factors, public-safe task shapes, and next gates.
Do not publish private prompts, raw memory rows, adapter internals, secrets, or
claim-sensitive Mirror Architecture / SSP implementation mechanics.
```

SWE and WebArena are carried as benchmark-memory lanes:

- SWE: 495/500 local official-harness selected-test receipt; hosted run
  `tris_codex_helper_verified_20260629T002207Z` is under SWE-bench support /
  maintainer review.
- WebArena: 255/258 clean official Verified hard receipt; final rows stay
  parked behind upstream/contest interpretation, with AWS credits available for
  completing the cloud route.

First local memory-stress receipt:

```text
data/memory_stress_runs/qwen_tris_memory_stress_seed_20260630T214755Z.md
```

Result:

```text
18/18 public-safe seed rows passed the offline memory-off versus
architecture-on retrieval/scoring harness.
```

Boundary: this validates the memory harness path before Qwen Cloud is attached;
the next gate is to run the same seed pack through Qwen Cloud with API-call
receipts.

Earlier strategic read:

1. Track 3 Agent Society, using the Quadro four-agent audit workflow as the
   nearest production skeleton.

Best overlap lanes:

1. Track 1 MemoryAgent, using Golden Field Lite persistent memory and Quadro
   SQLite/FTS memory patterns.
2. Track 4 Autopilot Agent, using Quadro consent/audit handoff plus
   production business workflow gates.
3. Track 5 EdgeAgent, using B.A.S.I.S. and Orin trace gates as the
   privacy-aware edge/cloud orchestration lane.
4. Track 2 AI Showrunner, using a public-safe showrunner for evidence-backed
   short demo/story generation, not private operator-state material.

## Existing Source Builds

- Quadro:
  `/Users/renaissancefieldlite1.0/Documents/Playground/band_of_agents_quadro`
- B.A.S.I.S.:
  `/Users/renaissancefieldlite1.0/Documents/Playground/BASIS_Phase12C_Local_Capture_DO_NOT_UPLOAD`
- Golden Field Lite:
  `/Users/renaissancefieldlite1.0/Documents/Playground/golden_field_lite_research_partner`
- Golden Mirror/Home Node prototype:
  `/Users/renaissancefieldlite1.0/Documents/Playground/home_node_golden_mirror_prototyping_build`

## Port Boundary

Do not reuse live source ports:

- Quadro: `8867`
- B.A.S.I.S.: `8788`
- Golden Field Lite: `8797`

New Qwen demos should use `8891` through `8895` only if a local web surface is
needed, and each thread must document the port it claims before starting a
server.

## First Files To Read

1. `QWEN_BUILDOUT_LOG.md`
2. `docs/QWEN_TRIS_PUBLIC_VERIFICATION_LADDER_2026-07-01.md`
3. `docs/FIVE_THREAD_HANDOFF.md`
4. `docs/LOCKED_LANGUAGE_AND_BOUNDARIES.md`
5. `source_inventory/PLAYGROUND_SOURCE_MAP.md`
6. The relevant `track_packets/track*.md` file.
