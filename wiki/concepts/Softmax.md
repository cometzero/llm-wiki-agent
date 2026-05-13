---
title: "Softmax"
type: concept
tags: [attention, machine-learning, activation-function]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
**Softmax** converts a vector of real numbers into a probability distribution (sum to 1, all values positive). In attention, it converts compatibility scores into [[AttentionWeight|attention weights]].

## Key Concepts
- Formula: `softmax(x)_i = exp(x_i) / Σexp(x_j)`
- Output values are in (0,1) and sum to 1
- Amplifies differences: larger inputs get disproportionately higher weights
- Used to create [[AttentionWeight]] from scores

## Example
```
scores = [2, 4]
softmax(scores) ≈ [0.12, 0.88]
```

## Connections
- [[ScaledDotProductAttention]] — softmax converts scores to weights
- [[AttentionWeight]] — result of softmax application
- Large score differences → more extreme attention (why scaling helps)
