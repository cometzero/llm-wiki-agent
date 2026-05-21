---
title: "Vector Database"
type: concept
tags: [embedding, search, rag]
sources: [2026-05-21-day29-ai-ml-learning-review]
last_updated: 2026-05-21
---

## Definition
A vector database stores embedding vectors together with source text and metadata, then supports fast similarity search over those vectors.

## Role in AI Systems
In [[RAG]], document chunks are embedded by an [[EmbeddingModel]] and stored in a vector database. At query time, the system retrieves nearby chunks with [[VectorSearch]] before sending them to an [[LLM]].

## Related Concepts
- [[VectorSearch]] — retrieval mechanism
- [[NearestNeighborSearch]] — basic search objective
- [[ApproximateNearestNeighborSearch]] — scalable large-index variant
- [[Chunking]] — prepares documents for storage

## Sources
- [[2026-05-21-day29-ai-ml-learning-review]]
