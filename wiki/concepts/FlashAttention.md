---
title: "FlashAttention"
type: concept
tags: [transformer, attention, optimization]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
FlashAttention is an optimized implementation strategy for Transformer attention that reduces memory movement and improves throughput while computing exact attention. It targets the high memory and compute cost of [[ScaledDotProductAttention]] on long sequences.

## Connections
- [[ScaledDotProductAttention]] — the core operation FlashAttention optimizes.
- [[SelfAttention]] — often implemented with FlashAttention in modern LLM systems.
- [[Transformer]] — model family that benefits from faster attention kernels.
