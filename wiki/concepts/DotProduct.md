---
title: "DotProduct"
type: concept
tags: [math, linear-algebra, ml-foundations]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
The dot product (inner product) of two vectors is a scalar that combines their magnitudes and the cosine of the angle between them: a·b = ||a|| ||b|| cos(θ).

## Key Properties
- Measures the combined directional alignment and magnitude of two vectors.
- Positive when vectors point in similar directions, negative when opposite, zero when orthogonal.
- Symmetric: a·b = b·a.
- Related to [[Norm]]: a·a = ||a||².

## Relevance to AI/ML
- [[Attention]] mechanisms in [[LLM]] use dot product to compute raw interaction scores between query and key vectors.
- Scaled dot-product attention normalizes by √d_k to prevent vanishing gradients.
- Dot product is the fundamental operation in linear layers (matrix multiplication is a collection of dot products).
- Used in [[Gradient]] computations throughout neural network training.

## Related Concepts
- [[CosineSimilarity]] — dot product normalized by magnitudes (direction-only comparison)
- [[Norm]] — derived from dot product (||a|| = √(a·a))
- [[Attention]] — uses dot product for query-key scoring
- [[Embedding]] — dot products between embeddings can measure relatedness
