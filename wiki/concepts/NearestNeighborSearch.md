---
title: "Nearest Neighbor Search"
type: concept
tags: [search, embedding, vector]
sources: [2026-05-21-day29-ai-ml-learning-review]
last_updated: 2026-05-21
---

## Definition
Nearest neighbor search finds the stored vector or vectors closest to a query vector under a chosen similarity or distance measure.

## In RAG
A user question is converted into an embedding vector, then nearest neighbor search finds document chunks whose vectors are closest in [[EmbeddingSpace]]. These chunks become context for [[RAG]].

## Related Concepts
- [[VectorSearch]] — semantic search workflow
- [[CosineSimilarity]] — common similarity metric
- [[ApproximateNearestNeighborSearch]] — fast approximate retrieval for large collections

## Sources
- [[2026-05-21-day29-ai-ml-learning-review]]
