---
title: "Heterogeneous Inference"
type: concept
tags:
  - AIInfrastructure
  - inference
  - latency
  - throughput
sources:
  - inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform
last_updated: 2026-05-03
---

## Definition
[[HeterogeneousInference]] is an inference pattern that routes different inference sub-steps to specialized hardware classes. In this source, [[VeraRubinPlatform]]/[[NVIDIA]] GPU handles context-heavy prefill and large-batch attention work, while [[Groq3LPX]] handles latency-sensitive decode segments.

## Key Mechanism
- **Split by phase**: prefill/attention vs FFN-MoE decode.
- **Split by optimizer path**: high-throughput path retains aggregate efficiency while a dedicated low-latency path keeps user-facing responsiveness stable.
- **Orchestration**: [[NVIDIADynamo]] schedules workload and intermediate activation exchange under latency objectives.

## Implications
- Useful for long-context and agentic loop workloads where per-token latency accumulates.
- Helps preserve AI factory throughput while expanding interactive operating points.
- Can change economics by enabling higher value per-user tokens without fully sacrificing utilization.

## Sources
- [[inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform]