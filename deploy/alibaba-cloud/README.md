# Alibaba Cloud Deployment Proof Runbook

This runbook prepares the short deployment-proof recording required by the
Qwen Cloud submission.

## What Must Be Shown In The Recording

1. The backend is running on Alibaba Cloud.
2. The container or service has `QWEN_API_KEY`, `QWEN_API_BASE`, and
   `QWEN_MODEL` configured without revealing the secret value.
3. The backend returns a live status response.
4. A request through the deployed backend reaches Qwen Cloud / Alibaba Model
   Studio and returns a model response.

## Build

```bash
docker build -t qwen-tris-memoryagent:latest .
```

## Run Locally Before Cloud Upload

```bash
docker run --rm \
  -p 9471:9471 \
  -e QWEN_API_KEY="$QWEN_API_KEY" \
  -e QWEN_API_BASE="https://dashscope-intl.aliyuncs.com/compatible-mode/v1" \
  -e QWEN_MODEL="qwen-plus" \
  qwen-tris-memoryagent:latest
```

Open:

```text
http://127.0.0.1:9471/api/health
http://127.0.0.1:9471/api/state
```

## Alibaba Cloud Target

Use any Alibaba Cloud route that can run a Python container or process, for
example:

- Elastic Compute Service with Docker;
- Container Registry plus a container runtime;
- Function Compute custom container, if available in the account.

The repo proof code for Alibaba/Qwen API usage is:

```text
src/qwen_agent_buildout/trini_recall/alibaba_qwen_cloud_client.py
```

Public boundary: do not show the raw API key in the recording.
