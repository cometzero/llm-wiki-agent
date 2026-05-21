---
title: "Approximate Nearest Neighbor Search"
type: concept
tags: [search, embedding, vector-database, scalability]
sources: [2026-05-21-day29-ai-ml-learning-review]
last_updated: 2026-05-21
---

## Definition
Approximate nearest neighbor search finds vectors that are very close to the query without exhaustively comparing every stored vector.

## Why It Matters
For small collections, exact [[NearestNeighborSearch]] can compare every vector. For millions or billions of vectors, a [[VectorDatabase]] often uses approximate indexing to trade a small amount of recall for much lower latency.

## Related Concepts
- [[VectorSearch]] — user-facing semantic retrieval
- [[VectorDatabase]] — storage and indexing layer
- [[EmbeddingModel]] — creates the vectors being indexed

## Sources
- [[2026-05-21-day29-ai-ml-learning-review]]
