# Qwen Buildout Agent Instructions

Recover the spine before acting.

This repo exists to build Qwen Cloud hackathon submissions from the existing
Renaissance Field Lite agent stack without breaking, exposing, or compacting
the source builds.

## Mandatory First Read

Before editing or implementing in this repo, read:

1. `QWEN_BUILDOUT_LOG.md`
2. `docs/FIVE_THREAD_HANDOFF.md`
3. `docs/LOCKED_LANGUAGE_AND_BOUNDARIES.md`
4. `source_inventory/PLAYGROUND_SOURCE_MAP.md`
5. The track packet for your assigned lane under `track_packets/`

## Core Rules

- No toy data.
- No public push, upload, or submission without explicit Architect D approval.
- Do not copy secrets, `.env`, private memory DBs, JSONL interaction history,
  raw captures, biometric exports, model checkpoints, or claim-sensitive
  mechanics.
- Do not steal or reuse live source ports: Quadro `8867`, B.A.S.I.S. `8788`,
  Golden Field Lite `8797`.
- Treat source projects as siblings/provenance. Do not live-pipe this repo into
  their runtime state.
- If code is copied, it must be copied into this repo as a clean, renamed,
  Qwen-specific clone with source notes and a boundary check.
- Separate private operator-state context from public-safe demo material.
- Public-safe language must lead with mechanism, evidence, controls, gates, and
  exact artifacts.

## Qwen Requirement

Each track must show a real Qwen Cloud integration path, not just a local
wrapper:

- Qwen model call path or adapter.
- Qwen Cloud API/credential boundary.
- Tool/MCP/skill invocation story if applicable.
- Logs showing calls, fallbacks, errors, and human checkpoints.
- Demo script and README section for the track.

