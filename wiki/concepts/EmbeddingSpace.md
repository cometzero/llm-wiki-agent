---
title: "Embedding Space"
type: concept
tags: [embedding, vector, representation]
sources: [2026-05-21-day29-ai-ml-learning-review]
last_updated: 2026-05-21
---

## Definition
Embedding space is the vector coordinate system where an [[EmbeddingModel]] places texts, images, code, or other inputs so that semantically similar items are close together.

## Why It Matters
[[VectorSearch]] only works reliably when the query and documents are embedded into the same space. Mixing embeddings from incompatible models makes distances such as [[CosineSimilarity]] difficult to compare.

## Related Concepts
- [[EmbeddingModel]] — produces vectors in the space
- [[VectorSearch]] — searches within the space
- [[CosineSimilarity]] — measures directional similarity

## Sources
- [[2026-05-21-day29-ai-ml-learning-review]]
