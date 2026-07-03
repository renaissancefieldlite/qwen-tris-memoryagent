# Trini Recall NemoClaw / OpenClaw Gate

Status: optional autonomy integration gate. Not active in the local UI yet.

## Verified Read

NVIDIA NemoClaw is a sandbox/onboarding stack for OpenClaw agents. The official
quickstart describes a guided installer that creates a sandbox, configures
inference, applies network policy, and can expose a browser dashboard.

Qwen-Agent is the Qwen-native framework lane for function calling, tool usage,
planning, memory, RAG, MCP, and code-interpreter style applications.

Alibaba Cloud Model Studio documents OpenClaw using an OpenAI-compatible
interface with Qwen proprietary and open-source model options.

Primary sources:

- `https://docs.nvidia.com/nemoclaw/user-guide/openclaw/get-started/quickstart`
- `https://github.com/QwenLM/Qwen-Agent`
- `https://www.alibabacloud.com/help/en/model-studio/openclaw`

## Trini Decision

Do not make NemoClaw a blocker for Track 1.

Trini Recall should first prove:

- SQL memory;
- RAG evidence;
- JSONL event ledger;
- web fetch ingest;
- architecture-off/on comparison;
- recursive autonomous research cycles;
- Qwen Cloud provider swap after credits/API key land.

Then NemoClaw/OpenClaw can become a deployment or autonomy wrapper if the install
environment is clean.

## Install Gate

Before installing NemoClaw, verify:

- Docker Desktop or Colima is ready on macOS;
- the install will not collide with active local ports;
- provider route is selected intentionally;
- Qwen-compatible inference is configured;
- dashboard URL and sandbox ports are logged;
- credentials stay outside the repo.

## Public-Safe Language

Use:

```text
NemoClaw/OpenClaw is an optional sandboxed autonomy lane for a later deployment
gate.
```

Do not say:

```text
Trini already runs in NemoClaw.
```

