---
title: "KV Cache"
type: concept
tags: [ai-ml, transformer, attention, memory-optimization]
sources: [2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-22
---

## Definition

The [[KVCache]] (Key-Value Cache) stores the key and value matrices from previous tokens during autoregressive generation, allowing the model to reference them without recomputation for each new token.

## Why It Matters

Transformer attention requires each token to attend to all previous tokens. Without caching:
- Token 100 generation recomputes keys/values for all 99 previous tokens
- Token 101 generation recomputes keys/values for all 100 previous tokens
- Massive redundant computation

With KVCache:
- Keys/values computed once, stored in cache
- Each new token reuses cached values
- Dramatic speedup for long contexts

## Memory Trade-off

KVCache trades compute for memory. For:
- **Long contexts**: Cache grows linearly with context length
- **Many concurrent users**: Cache memory multiplies by number of users
- **GPU memory pressure**: Long-context LLMs require careful memory management

## Connections
- [[Serving]] — critical for efficient LLM serving
- [[Latency]] — reduces per-token generation time
- [[Throughput]] — enables more efficient batching
- [[Attention]] — the mechanism that KVCache optimizes
- [[InferenceStack]] — memory management is a key design consideration
