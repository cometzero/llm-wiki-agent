---
title: "Dot Product"
type: concept
tags: [math, attention, linear-algebra]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
**Dot Product** (inner product) of two vectors is the sum of element-wise products: `a·b = Σ a_i × b_i`. In attention, it measures similarity between query and key vectors.

## Key Concepts
- Higher dot product = vectors point in similar directions = more relevant
- Used to compute [[AttentionWeight|compatibility scores]]
- `QK^T` computes all query-key dot products simultaneously

## Example
```
q = [1, 2]
k = [3, 1]
q·k = 1×3 + 2×1 = 5
```

## Connections
- [[ScaledDotProductAttention]] — computes QK^T
- [[Query]], [[Key]] — vectors whose similarity is measured
- [[CompatibilityScore]] — the resulting similarity measure
