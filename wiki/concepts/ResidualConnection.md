---
title: "Residual Connection"
type: concept
tags: [deep-learning, neural-network, architecture]
sources: [2026-05-07-day15-ai-ml-learning-review, 2026-05-14-day22-ai-ml-learning-review]
last_updated: 2026-05-14
---

## Definition

A **Residual Connection** (or skip connection) adds the input of a sublayer directly to its output, creating a pathway for information to flow unchanged through deep networks.

## In Transformer Block

```
X_after_attention = X + Attention(X)
X_after_ffn = X_after_attention + FFN(X_after_attention)
```

## Benefits

1. **Information preservation** — original information never fully lost
2. **Gradient flow** — direct path helps gradients propagate in backpropagation
3. **Training stability** — easier optimization of deeper networks
4. **Identity learning** — network can learn to "skip" if sublayer isn't useful

## Connections

- [[TransformerBlock]] — key component alongside attention and FFN
- [[LayerNorm]] — typically used with residual connections
- [[FFN]] — residual added after FFN output
- [[MultiHeadAttention]] — residual added after attention output

## Mathematical Intuition

Without residual: `output = sublayer(input)` — small changes could dramatically alter output

With residual: `output = input + sublayer(input)` — at minimum, output can equal input (identity)
