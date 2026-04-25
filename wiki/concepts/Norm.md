---
title: "Norm"
type: concept
tags: [math, linear-algebra, ml-foundations]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
A norm is a function that assigns a non-negative length or size to vectors in a [[VectorSpace]], satisfying positivity, homogeneity, and the triangle inequality.

## Key Properties
- L2 norm (Euclidean): ||x||₂ = √(Σ x_i²) — the standard Euclidean distance from origin.
- L1 norm (Manhattan): ||x||₁ = Σ |x_i| — sum of absolute values, induces sparsity.
- Different norms have different geometric properties and optimization characteristics.
- L2 norm is derived from [[DotProduct]]: ||x||₂ = √(x·x).

## Relevance to AI/ML
- L2 regularization (weight decay) penalizes large L2 norms of weights to prevent overfitting.
- [[Gradient]] norm clipping limits the L2 norm of gradients to stabilize training.
- L1 regularization (Lasso) encourages sparse solutions by penalizing L1 norm.
- Distance metrics in [[Embedding]] spaces often use L2 distance (derived from L2 norm).
- Batch normalization uses statistics related to norms.

## Related Concepts
- [[DotProduct]] — L2 norm squared equals dot product with itself
- [[CosineSimilarity]] — uses L2 norm for normalization
- [[Gradient]] — norm clipping is a key training stabilization technique
- [[VectorSpace]] — the space where norms are defined
