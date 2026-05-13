---
title: "Attention Weight"
type: concept
tags: [transformer, attention]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
**Attention Weight** represents how much each token contributes to another token's new representation. Computed via [[Softmax]] of scaled dot product scores, weights sum to 1 per query.

## Key Concepts
- Output of [[Softmax]] applied to compatibility scores
- [[WeightedSum]] of values uses attention weights
- Different for each query (each token has its own attention distribution)
- High weight = strong relationship in the model's learned representation

## Connections
- [[ScaledDotProductAttention]] — computes the weights
- [[Softmax]] — converts scores to probabilities
- [[Value]] — weighted by attention weights
- [[TokenInteraction]] — weight strength indicates interaction

## Tensor Shape
For sequence length n, attention weight matrix is `n × n`, where row `i` shows how token `i` attends to all tokens.
