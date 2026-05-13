---
title: "Scaled Dot-Product Attention"
type: concept
tags: [transformer, attention, foundational]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
**Scaled Dot-Product Attention** is the fundamental attention computation in Transformers. It computes relevance via dot product, scales by `sqrt(d_k)` to prevent numerical instability, applies softmax to get attention weights, and mixes values accordingly.

## Key Concepts
- Core formula: `Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V`
- `d_k` = dimension of key/query vectors
- Scaling prevents dot product scores from becoming too large with high dimensions
- Without scaling, softmax becomes too extreme (near one-hot), harming learning
- [[Softmax]] converts scores to probability-like attention weights summing to 1

## Why Scaling Matters
- High dimensions cause larger dot products naturally (adding more terms)
- Large scores make softmax too extreme, blocking gradient flow
- Example: with `d_k=64`, `sqrt(d_k)=8`, dividing keeps softmax smooth
- Scaling is crucial for [[Transformer]] training stability

## Process Flow
1. Compute compatibility scores: `QK^T` (dot product of queries and keys)
2. Scale by `sqrt(d_k)` to prevent numerical issues
3. Apply softmax to get attention weights (sum to 1)
4. Weight and sum values: `weights × V`

## Connections
- [[Query]], [[Key]], [[Value]] — the three inputs
- [[Softmax]] — converts scores to attention weights
- [[DotProduct]] — computes compatibility scores
- [[WeightedSum]] — mixes value vectors
- [[Transformer]] — built on this attention mechanism
- [[BERT]], [[GPT]] — use scaled dot-product attention

## Tensor Shapes
```
Q shape: (seq_len, d_k)
K shape: (seq_len, d_k)
V shape: (seq_len, d_v)
QK^T shape: (seq_len, seq_len) — attention score matrix
output shape: (seq_len, d_v)
```
