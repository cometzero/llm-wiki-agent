---
title: "Disaggregated Prefill"
type: concept
tags:
  - inference
  - serving
  - scheduling
  - prefill
  - decode
sources:
  - inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform
last_updated: 2026-05-03
---

## Definition
[[DisaggregatedPrefill]] separates the prefill phase from decode phase responsibilities across hardware and scheduling layers. The NVIDIA source frames it as a practical necessity for agentic, long-context, high-concurrency inference.

## In This Source
- Prefill: longer-context KV/cache construction is routed to high-throughput GPU path ([[VeraRubinPlatform]]/NVL72).
- Decode: per-token step and FFN/MoE heavy functions are routed for low-latency execution via [[Groq3LPX]].
- Loop design resembles AFD-like behavior where intermediate activations cross boundaries between engines.

## Consequence
- Prevents a single architecture from being forced to optimize competing regimes.
- Reduces response jitter for interactive users while preserving aggregate output scale.

## Related Sources
- [[inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform]
- [[HeterogeneousInference]]
- [[InteractiveInference]]
- [[NVIDIADynamo]]