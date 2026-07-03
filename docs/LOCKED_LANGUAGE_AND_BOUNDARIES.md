# Locked Language And Boundaries

## Locked Build Read

This is a Qwen Cloud hackathon buildout, not a rewrite of the source systems.

Use this language:

```text
Standalone Qwen Cloud agent buildout seeded from existing Renaissance Field
Lite agent architectures, with clean-room Qwen adapters, source-boundary logs,
and public-safe demo artifacts.
```

## Source Build Boundary

Existing systems are source/provenance and sibling builds:

- Quadro provides multi-agent role division, SQLite/FTS memory, JSONL audit,
  source packet handling, and human signoff gates.
- B.A.S.I.S. provides real capture/trace discipline, sensor-facing manifests,
  Mac/MLX versus Orin lane separation, and edge privacy gates.
- Golden Field Lite provides persistent AI partner memory, local runtime
  discipline, browser/web fetch routes, and state-continuity partner behavior.
- Home Node/Golden Mirror prototype provides local model/probe patterns and
  chronology discipline.

Do not live-pipe this repo into those projects. Copy only the minimal cleared
guts into this repo, rename them for Qwen, document the source, and verify the
new copy independently.

## Public/Private Boundary

Public-safe:

- architecture diagrams
- source summaries
- cleared source-packet examples
- API integration logs with secrets redacted
- demo screenshots/videos
- benchmark tables with real tasks and no private raw data
- human-in-the-loop gate descriptions
- result pathways: what was measured, what changed, what factor was tested,
  which receipt supports it, and what the next gate is

Private:

- raw B.A.S.I.S. captures
- biometric exports
- device identifiers
- private memory DBs
- JSONL interaction history
- `.env`, API keys, credentials
- claim-sensitive mechanics
- operator-state continuity material
- private prompts, raw state recipes, adapter internals, and any unpublished
  proprietary implementation detail that would give away the working sauce

## IP Lock / Results Pathway

The public Qwen Tris package may show:

- the benchmark family or task class
- the public-safe input shape
- the measured result
- the scored factors, such as recall, stale-memory suppression, boundary
  retention, source citation, next-gate quality, and approval-gate discipline
- the public receipt path or public issue link
- the honest continuation gate

The public package must not show:

- private source-build databases
- raw interaction JSONL logs
- hidden prompt recipes
- exact adapter/tuning internals unless separately cleared
- private capture files
- secrets, credentials, payment tokens, or account identifiers
- any claim-sensitive mechanics that explain how to clone the proprietary
  Mirror Architecture / SSP lane

Short form:

```text
Show the result path and scored factors. Keep the proprietary implementation
path locked.
```

## No Toy Data Rule

Support claims require real tasks, real traces, real source packets, real API
calls, real controls, real audit logs, or a marked continuation gate.

Acceptable continuation language:

```text
Current support: scaffold and source map are seated.
Next gate: attach Qwen Cloud API calls and run the first real task packet.
```

Do not call a scaffold a benchmark. Do not call a local wrapper a Qwen system
until Qwen Cloud calls are logged.

## Port Boundary

Reserved source ports:

- `8867`: Quadro.
- `8788`: B.A.S.I.S.
- `8797`: Golden Field Lite.

Allowed new demo block if needed:

- `8891`: MemoryAgent.
- `8892`: AI Showrunner.
- `8893`: Agent Society.
- `8894`: Autopilot Agent.
- `8895`: EdgeAgent.
