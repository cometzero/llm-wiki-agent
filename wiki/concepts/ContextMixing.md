---
title: "Context Mixing"
type: concept
tags: [transformer, attention]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
**Context Mixing** is the process by which information from multiple tokens is combined via [[AttentionWeight|attention weights]] to create context-dependent representations. The output is a [[WeightedSum]] of value vectors.

## Key Concepts
- Tokens blend information from multiple sources
- [[SelfAttention]] performs context mixing within a single sequence
- Output is not a single value but a weighted combination
- [[ContextualEmbedding]] is the result of context mixing

## Connections
- [[SelfAttention]] — performs context mixing
- [[AttentionWeight]] — determines mixing ratios
- [[Value]] — mixed content comes from value vectors
- [[WeightedSum]] — mathematical operation for mixing
- [[ContextualEmbedding]] — the resulting representation

## Example
For "사과를 먹었다" (ate an apple):
```
attention_weights: [0.2, 0.6, 0.2]  # (나는, 사과를, 먹었다)
values: [1, 10, 5]
output = 0.2×1 + 0.6×10 + 0.2×5 = 7.2
```
"먹었다"'s new representation heavily incorporates "사과를" (60% weight).
