---
title: "Weighted Sum"
type: concept
tags: [math, attention]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
A weighted sum combines values after multiplying each value by an assigned weight. In attention, [[AttentionWeight|attention weights]] determine how much of each [[Value]] vector contributes to the final output.

## Example
If weights are `[0.25, 0.75]` and values are `[10, 20]`, the output is `0.25×10 + 0.75×20 = 17.5`.

## Connections
- [[ScaledDotProductAttention]] — produces weights and applies them to values.
- [[ContextMixing]] — uses weighted sums to create contextual token representations.
