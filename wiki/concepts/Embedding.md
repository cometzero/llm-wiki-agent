---
title: "Embedding (Word/Token Embedding)"
type: concept
tags: [nlp, representation-learning, vector-space]
sources: [2026-05-12-day20-ai-ml-learning-review]
last_updated: 2026-05-12
---

## Definition
Embedding transforms discrete tokens (words, subwords) into dense numerical vectors in a continuous space, enabling semantic relationships to be represented as geometric proximity.

## Core Properties

### vs One-Hot Vector
| Aspect | One-Hot | Embedding |
|--------|---------|----------|
| Dimensions | Vocabulary size (e.g., 50,000) | Compact (e.g., 256, 768) |
| Density | Sparse (single 1) | Dense (all non-zero) |
| Semantic info | None | Encoded |
| Learnable | No | Yes |

### Semantic Similarity
Semantically similar words cluster together in embedding space. For example:
- `cat` and `dog` → nearby vectors
- `car` and `bus` → nearby vectors
- `cat` and `car` → distant vectors

## Mathematical View
Embedding is a lookup operation:
```
output = embedding_table[token_id]  # Shape: [embedding_dim]
```

The embedding table E has shape `[V, D]` where V = vocabulary size, D = embedding dimension.

### Learning Signal
Embedding vectors are learned parameters—adjusted during backpropagation to minimize task loss. Words appearing in similar contexts tend to acquire similar vectors.

## Key Metrics
- **Cosine Similarity**: Measures directional alignment (ignores magnitude)
  ```
  cos_sim(a, b) = (a · b) / (||a|| × ||b||)
  ```
- **Euclidean Distance**: Absolute position difference

## Applications

### In [[LLM]]
Token IDs → Embedding vectors → [[Transformer]] layers

### In [[RAG]]
- Query embedding + Document embedding → Semantic similarity search
- Enables finding "refund policy" when user asks about "반품 정책"

### Other Domains
- Recommendation systems (user/item embeddings)
- Image-text models (cross-modal alignment)
- Code search (code snippet embeddings)

## Contextual vs Static Embedding

| Type | Description | Example |
|------|-------------|----------|
| Static | Fixed vector per token | Word2Vec |
| Contextual | Varies by context | [[Transformer]] layer outputs |

Note: "bank" in "river bank" vs "bank account" gets different contextual embeddings.

## Connections
- [[LLM]] — embeddings are the input layer
- [[AttentionMechanism]] — attention operates over embedded tokens
- [[RAG]] — embedding-based semantic search
- [[CosineSimilarity]] — common similarity metric
