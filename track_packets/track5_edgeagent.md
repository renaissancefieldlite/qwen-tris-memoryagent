# Track 5 Packet - EdgeAgent

## Submission Thesis

Qwen EdgeAgent coordinates an edge device or sensor-facing runtime that
perceives locally, filters private data, calls Qwen Cloud for reasoning when
available, and acts locally with graceful offline degradation.

## Existing Overlap

- B.A.S.I.S. Phase 12C capture/manifest discipline.
- B.A.S.I.S. Mac/MLX versus Orin trace split.
- Jetson Orin local edge lane.
- Home Node local runtime/probe patterns.

## Build Plan

1. Define privacy-safe edge event summary schema.
2. Build local edge event reader using sanitized manifests/status summaries.
3. Add Qwen Cloud reasoning call over the summary, not raw private data.
4. Add local action policy: recommend, queue, defer, or execute only allowed
   local action.
5. Add offline/weak-network fallback behavior and latency/bandwidth logging.

## Real Evidence Gate

Use a real sanitized B.A.S.I.S. or Orin status manifest. Do not use raw capture
or biometric exports.

Metrics:

- bytes sent to cloud
- fields withheld by privacy filter
- Qwen call latency
- local fallback result
- action gate status
- packet-continuity/readiness status

## Network Boundary

Do not change Mac network services, adapters, DHCP/static IP state, routes,
DNS, or Wi-Fi. If Orin is used, preserve the two-IP lane:

- Mac Ethernet: `10.67.0.1`
- Jetson Orin: `10.67.0.2`

