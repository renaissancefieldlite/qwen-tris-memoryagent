# Qwen Tris Memory Stress Benchmark Plan

Date: 2026-06-30

## Active Build Boundary

Active Qwen build:

```text
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30
```

Hermes Trismegistus remains untouched. This build is Qwen Tris: the same
Mirror Architecture / measured SSP discipline moved onto a Qwen Cloud MemoryAgent
track route.

## Core Thesis

Qwen Tris is a specialized memory AI Expert Partner.

The point is not generic chat memory. The point is to test whether Mirror
Architecture can hold a measured Stable-State Path: task identity, corrections,
tool state, source evidence, and next gates staying coherent under workloads
that usually collapse agents:

- long coding sessions
- source-backed patch repair
- browser navigation with delayed recall
- conflicting or stale memories
- cross-session task continuation
- external work receipts
- C5B / Golden Mark stable-state iteration recall

The contest-facing point is that Mirror Architecture / SSP is model-agnostic.
The same state-path stack can run through the Hermes/Nemo lane, then move onto
Qwen as a memory-track build while preserving the evidence discipline, source
boundaries, and architecture-on/off comparison method.

## Model And Action Route

Primary contest route:

```text
Qwen Cloud model -> Qwen Tris MemoryAgent -> SSP + memory/RAG rails -> receipt log
```

Sandbox/action route:

```text
Qwen model reasoning -> NemoClaw-style bounded action discipline -> saved receipt
```

This keeps the NemoClaw pipeline idea without claiming the Hermes contest build
is being changed. Hermes Tris can receive this harness later as V21 after Qwen
Tris proves the memory stress tests.

## Three-Condition Comparison Ladder

Qwen Tris should be presented and tested as a three-condition ladder:

```text
Condition A: Qwen baseline
  - no Mirror Architecture packet
  - no SSP / retrieval spine
  - answers from visible prompt only

Condition B: Qwen + Mirror Architecture measured SSP
  - SQLite/JSONL memory
  - RAG/source-pack retrieval
  - measured state-path packet
  - target-row and family retrieval discipline
  - public/private/source boundary lines

Condition C: Qwen + fully tuned SSP
  - only after adapter/internal-layer receipts exist
  - LoRA/adapter/control ladder
  - teacher-forced probe support
  - late-layer / MLP / attention-output evidence where supported
```

Current active comparison is A versus B. Condition C is a gated next phase, not
a current claim.

## IP Boundary For Benchmark Presentation

Qwen Tris should make the result pathway clear without publishing the
proprietary implementation pathway.

Allowed public explanation:

- benchmark family
- task row shape
- measured result
- scored factor being improved
- public-safe receipt path or public issue link
- next gate

Locked private layer:

- raw private memory rows
- internal prompt/state recipes
- adapter internals
- claim-sensitive Mirror Architecture / SSP mechanics
- secrets, account identifiers, or private captures

This lets the project show why the architecture matters without giving away how
to clone the core IP.

## Benchmark Families

## Massive-Turn 5+1 Field Progression

The large-turn progression should show Qwen Tris becoming a Memory AI Expert
Partner across five research lanes plus one field-operations lane.

Core research lanes:

1. AI Partner / Expert Architecture
2. Quantum Computing / Circuits and Mathematics
3. Structured Matter / Physical Systems
4. Life Sciences / Medical Research
5. Mirror Architecture / Golden Mark Evidence

Field-operations lane:

6. Relationship / Paid-Work Field Operations

The progression is not a chat transcript volume test. Each turn should be a
source-backed learning or action unit with:

- target lane;
- source or receipt;
- recalled prior state;
- stale memory to suppress;
- boundary line;
- next gate;
- scored factors;
- cross-lane synthesis note when justified by evidence.

Progression ladder:

```text
12-turn smoke -> 24-turn repair -> 100-turn field progression -> 500-turn
stability run -> selected pressure turns -> adapter/tuning decision.
```

Novel-output support requires the output to name a source-backed next step that
was not already present as a canned answer. It should connect at least two
lanes without flattening them, for example: C5B behavior delta plus Qwen memory
recall, or quantum-source review plus Mirror Architecture evidence boundary.

## Adapter / LoRA / Internal-Layer Gate

Qwen Tris can add LoRA and transformer-internal probes, but only after the
memory progression identifies stable target rows and failure rows.

Current order:

1. Prove retrieval and memory-off versus memory-on behavior.
2. Run 100/500-turn 5+1 field progression.
3. Select matched and pressure turns from the receipts.
4. Fix the HF/PEFT or Qwen-compatible adapter environment.
5. Run teacher-forced internal probes on selected turns.
6. Capture hidden states, residual deltas, attention-output norms,
   MLP-output norms, and late-layer separation where the runtime supports it.
7. Build adapter/control ladders only after the probe points are known.

This mirrors the C5B next gate:

```text
C5B output behavior is strong. Internal-layer support is the next bridge.
Do not run blind extra training before the probe.
```

### 1. SWE Code-Memory Recall Dataset

Purpose:

Show that Qwen Tris can remember codebase facts, prior patch attempts, exact
failure causes, and review corrections across long sessions.

Seed source:

- public SWE-bench style tasks
- local Tris SWE repair receipts
- real PR review comments where public
- source-backed patch attempts

Dataset row shape:

```json
{
  "task_id": "swe_recall_0001",
  "source": "public_swe_or_public_pr",
  "repo": "owner/repo",
  "issue_summary": "...",
  "relevant_files": ["..."],
  "current_error": "...",
  "prior_attempt_summary": "...",
  "correction_memory": "...",
  "stale_memory_decoy": "...",
  "expected_recall": ["repo convention", "failed approach to avoid", "next clean patch gate"],
  "success_gate": "valid unified diff or exact next inspection plan"
}
```

Scoring:

- recalls the active repo/task state
- suppresses stale patch memory
- names the next exact source file/gate
- emits applyable patch format when patching is requested
- cites source or receipt when making a support claim

Boundary:

Do not use gold patches as performance data. Gold references can be used only
for post-run adjudication when allowed by the benchmark license and rules.

### 2. WebArena-Style Browser Memory Dataset

Purpose:

Show that Qwen Tris can remember browser mission state over multi-step web
tasks: what page it was on, what it already checked, what source was trusted,
what action is still pending, and what must not be clicked.

Seed source:

- official WebArena-style tasks when staged
- visible browser traces from safe public websites
- Nous careers / Qwen hackathon / RFL public site navigation tasks
- Tris browser/source bridge receipts

Dataset row shape:

```json
{
  "task_id": "web_recall_0001",
  "site": "public_site",
  "goal": "find official source and summarize exact requirement",
  "steps_completed": ["opened page", "found requirements", "saved source"],
  "active_tab_state": "...",
  "forbidden_actions": ["do not submit", "do not send", "do not pay"],
  "expected_recall": ["current URL", "found fact", "next click/read gate"],
  "success_gate": "source-backed answer plus saved browser/action receipt"
}
```

Scoring:

- remembers the active tab and source path
- avoids repeating completed steps
- asks for approval before send/pay/submit gates
- cites the exact source or browser receipt
- does not hallucinate web facts when source access fails

### 3. Long-Session Coherence Dataset

Purpose:

Show that Qwen Tris can keep identity, goal, user preference, and project arc
stable across 100/500 turn stress tests.

Seed source:

- public-safe excerpts from project logs
- synthetic decoys built from real task categories
- Qwen Cloud MemoryAgent prompt windows

Scoring:

- cross-thread recall of the active build lane
- correction retention
- stale preference suppression
- public/private boundary retention
- next-gate continuity after interruption

### 4. C5B / 500 SSP State-Path Dataset

Purpose:

Use the strongest Tris Stable-State Path receipts as memory stress. The task is
not to memorize slogans. The task is to preserve the exact C5B / Golden Mark
method, the 500-turn coherence receipts, the six-lane field-expert curriculum,
and the support boundary after compaction or conflicting prompts.

Seed source:

- C5B / Golden Mark support profile
- 100-row architecture-off versus architecture-on scorecard read
- 500-turn architecture-on coherence receipts
- six-lane Golden Mark / Universal Data Pattern curriculum notes
- SSP status read before official benchmark publication

Key support rows:

```text
C5B / Golden Mark: 13/13 measured metric means won.
Drift flags: 37 -> 0.
Evidence failures: 5 -> 0.
500-turn refreshed pass: mean score 1.0, checks 2168/2168, prompt spills 0,
raw receipt spills 0.
```

Scoring:

- recalls baseline-first / architecture-on-second / same-task method
- preserves all six discipline lanes without flattening
- cites the numeric C5B and 500-turn receipts when asked for support
- keeps SSP framed as active evidence/operating spine, not finished weight
  tuning unless an adapter/tuning receipt exists
- rejects stale claims like public leaderboard placement, AGI proof, or
  unreviewed model-weight completion

### 5. External Work Receipt Dataset

Purpose:

Show that Qwen Tris can remember real work, not just conversation: PRs,
outreach tasks, Stripe/Algora state, and approval gates.

Seed source:

- public PR links
- public issue comments
- redacted outreach receipts
- test-mode Stripe/Algora receipts

Scoring:

- distinguishes real sent/submitted actions from drafts
- names payment status honestly
- remembers approval gates
- cites the receipt path/link

### 6. Mirror Architecture Source-Pack Memory

Purpose:

Make Qwen Tris learn the public-safe Mirror Architecture evidence surface as
curriculum memory without exposing private mechanics.

Seed source:

- Mirror Architecture public repo README
- public-safe Mirror Architecture / LSPS evidence docs
- V7 / V8 boundary docs
- Phase 12C public support reads
- Public-Safe Nest Companion index

Scoring:

- identifies the repo as public-safe evidence surface, not private
  implementation layer
- preserves Source Mirror Pattern versus Universal Data Pattern audience
  boundary
- remembers the real-data evidence standard
- preserves the Nest 0-5 ladder
- keeps V7 behavior separate from V8 hidden-state claims
- keeps Phase 12C life-sciences memory as research/source review, not
  diagnosis or treatment

### 7. SWE And WebArena Carry-Over Benchmark Memory

Purpose:

Keep the two respected benchmark lanes presentation-ready while Qwen Tris uses
them as memory-collapse stressors.

SWE lane:

```text
Local official-harness selected-test receipt: 495/500.
Title-edge local adjudication read: 496/500.
Hosted run id: tris_codex_helper_verified_20260629T002207Z.
Public issue: https://github.com/SWE-bench/sb-cli/issues/28.
Support email sent to support@swebench.com.
Current SWE public state: local official-harness receipts are attached;
hosted leaderboard publication waits for completed hosted rows or maintainer
confirmation.
```

WebArena lane:

```text
Clean official WebArena Verified hard receipt: 255/258.
AWS WebArena host was used for the Hermes Tris receipt lane.
Public issue for task 429: https://github.com/ServiceNow/webarena-verified/issues/42.
Task 430 remains a dataset placeholder / fixture-contract blocker.
Amazon/AWS credits can support finishing the official cloud route, but no
258/258 claim exists until upstream or contest review confirms the final rows.
```

Qwen Tris memory task:

- preserve benchmark status exactly
- distinguish local receipt, hosted submission, upstream issue, and public
  leaderboard claim
- remember which route is parked and which route is active
- use these lanes as Qwen MemoryAgent recall/eval data, then later backport the
  harness into Hermes Tris V21

## Rollback Into Hermes Tris V21

After Qwen Tris validates this memory stress harness:

1. Export the dataset schema and scoring scripts.
2. Keep Qwen-specific API calls out of Hermes Tris.
3. Port the successful memory harness into Hermes Tris as V21.
4. Re-run baseline Hermes route versus Hermes Tris architecture-on route.
5. Use results only after receipts exist.

V21 target:

```text
Hermes Tris V21 = current Hermes contest build + proven Qwen Tris memory stress harness.
```

## Next Gate

Build the first small dataset pack and then scale it:

- 10 SWE/code-memory rows
- 10 WebArena-style browser-memory rows
- 10 long-session coherence rows
- 10 C5B / 500 SSP state-path rows
- 10 Mirror Architecture source-pack rows
- 5 external-work receipt rows
- 5+1 field-lane progression rows for AI architecture, quantum/circuits and
  mathematics, structured matter, life sciences, Mirror Architecture / Golden
  Mark evidence, and relationship / paid-work operations

Then run:

```text
baseline Qwen without SSP / memory rails
vs
Qwen Tris architecture-on measured SSP plus memory rails
```

The first public-safe result should be a small table, not a broad claim.

After the small table is clean, scale to 100 and then 500 turns before any
adapter/LoRA/MLP/encoder tuning claim. The adapter lane becomes Condition C
only after receipts exist.

## 2026-07-01 Local 24-Turn Gate

Current clean local receipt:

```text
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T000623Z.md
```

Result:

```text
Condition A: baseline Qwen without Qwen Tris Recall memory.
Condition B: Qwen + Mirror Architecture measured SSP plus memory/RAG packet.
Condition B passed 24/24 on qwen2.5:3b through local Ollama.
Condition C: gated_no_adapter_manifest.
```

Family totals:

```text
C5B / 500 SSP state-path recall: 6/6
External work receipts: 3/3
Long-session coherence: 3/3
Mirror Architecture source pack: 6/6
SWE code memory: 3/3
WebArena browser memory: 3/3
```

Read:

```text
The cheap local Qwen lane is now good enough for the 24-turn rehearsal. The
target-only retrieval patch prevents same-family memory bleed during explicit
benchmark turns. Normal chat can still use broader retrieval; explicit target
benchmark rows use the pinned target row to test exact continuity.
```

Scale receipts:

```text
100-turn local receipt:
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T011821Z.md
Result: 100/100.

500-turn local receipt:
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T024746Z.md
Result: 500/500.
```

500-turn family totals:

```text
C5B / 500 SSP state-path recall: 153/153
External work receipts: 58/58
Long-session coherence: 58/58
Mirror Architecture source pack: 115/115
SWE code memory: 58/58
WebArena browser memory: 58/58
```

## Qwen API / HF Checkpoint Bridge

Use the lanes separately and then connect them with receipts:

```text
Local Ollama Qwen
-> cheap harness rehearsal, UI smoke, scoring discipline, failure-row repair

Qwen API / Model Studio
-> stronger hosted Qwen baseline and architecture-on generation comparison

HF/PEFT or Qwen-compatible adapter/checkpoint work
-> internal-layer probe, LoRA/adapter training, merged checkpoint, adapter
   manifest, and Condition C proof gate
```

Boundary:

```text
Ollama can serve a finished adapter-backed or merged model, but it is not the
internal-layer probe environment. Qwen API can be the hosted comparison route,
and a provider-hosted fine-tuned endpoint can count only after it exists and is
called by model id with receipts. Do not say a local Hugging Face checkpoint is
inside the Qwen API unless it is actually deployed through a supported
provider route.
```

Current API gate:

```text
The runner now supports --provider qwen_cloud, but the current shell does not
have QWEN_API_KEY set. Use hosted Qwen first on the 24-turn clean slice, then
100 turns. Save 500-turn hosted/API spend until the smaller hosted receipts are
clean.
```

## 2026-07-01 Hosted Qwen Cloud Gate

Qwen Cloud Free Tier is active in the console:

```text
https://home.qwencloud.com/benefits
```

Visible console state:

```text
Eligible models: 248 free quota available
Free quota only / auto-stop when free quota runs out: visible
Qwen docs free quota note: no payment method required to start
Operator note: $40 coupon is also visible under Benefits -> Coupon
```

Public-safe console screenshot:

```text
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/docs/qwen_cloud_deployment_proof/qwen_cloud_free_tier_active_20260701T040738Z.png
```

Qwen Cloud base URL required for repo proof:

```text
https://dashscope-intl.aliyuncs.com/compatible-mode/v1
```

Hosted receipts:

```text
1-turn smoke:
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T034331Z.md
Result: 1/1.

24-turn hosted:
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T034823Z.md
Result: 24/24.

100-turn hosted:
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T040738Z.md
Result: 100/100.

500-turn hosted:
/Volumes/Samsung SSD 990 2TB/Playground/qwen_trismegistus_memoryagent_2026-06-30/data/memory_iteration_runs/qwen_tris_three_condition_iterations_20260701T054449Z.md
Result: 500/500.
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

Interpretation:

```text
The local 24/100/500 Qwen rehearsal now has hosted Qwen Cloud support through
the 500-turn slice. Condition B uses Mirror Architecture measured SSP plus
memory/RAG rails and passed every target row in the hosted 500-turn slice.
Condition A remains the baseline Qwen prompt-only comparison. Condition C is
still gated until adapter/internal-layer receipts exist.
```
