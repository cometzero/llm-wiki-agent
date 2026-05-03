---
title: "Interactive Inference"
type: concept
tags:
  - LLM
  - latency
  - user-experience
  - inference
sources:
  - inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform
last_updated: 2026-05-03
---

## Definition
[[InteractiveInference]] prioritizes predictable, low per-token latency and responsiveness for user-facing generation. It becomes more important as workloads become feedback-dense and iterative rather than single-shot batch outputs.

## Why It Matters More Now
- Agentic workflows (multiple tool calls, reasoning steps, and short cycles) expose latency per token as direct UX cost.
- As context lengths and output depth increase, a larger share of cost moves into the decode phase where jitter and stalls are visible.

## Infrastructure Pattern
- Pair throughput hardware with latency hardware.
- Keep interactive path from queueing and tail-latency inflation through better routing and scheduling.
- [[Groq3LPX]] + [[VeraRubinPlatform]] pattern is a concrete example in the updated source.

## Related Sources
- [[inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform]
- [[HeterogeneousInference]]
- [[SpeculativeDecoding]]
- [[NVIDIADynamo]]