---
title: "CosineSimilarity"
type: concept
tags: [math, linear-algebra, ml-foundations]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

## Definition
Cosine similarity measures the cosine of the angle between two vectors, computed as the [[DotProduct]] divided by the product of their [[Norm]]s: cos(θ) = (a·b) / (||a|| ||b||).

## Key Properties
- Range: [-1, 1], where 1 = identical direction, 0 = orthogonal, -1 = opposite direction.
- Removes magnitude information — focuses purely on directional similarity.
- Invariant to scalar multiplication: cos_sim(a, c·a) = 1 for any c > 0.

## Relevance to AI/ML
- [[Embedding]] retrieval and semantic search use cosine similarity to find semantically similar items regardless of embedding magnitude.
- Document similarity, recommendation systems, and clustering frequently use cosine similarity.
- Contrasts with raw [[DotProduct]] used in [[Attention]]: attention cares about both direction and magnitude (raw interaction strength), while retrieval typically cares only about direction (semantic similarity).
- Sentence embeddings (e.g., Sentence-BERT) are often compared using cosine similarity.

## Related Concepts
- [[DotProduct]] — the unnormalized version that includes magnitude
- [[Norm]] — used for normalization in cosine similarity
- [[Embedding]] — the vector representations compared via cosine similarity
- [[Attention]] — uses dot product (not cosine similarity) for raw scoring
