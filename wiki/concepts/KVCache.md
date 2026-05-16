---
title: "KV Cache"
type: concept
tags: [llm, inference, autoregressive, memory]
sources: [2026-05-16-day24-ai-ml-learning-review.md]
last_updated: 2026-05-16
---

## Definition
The **KV cache** stores computed key and value matrices from previous tokens during autoregressive inference, avoiding recomputation when generating each new token.

## Why It Matters
Without cache: Each new token recomputes attention over all previous tokens (O(n²) per step)
With cache: Each new token only computes for current step, retrieves past from cache (O(1) per step per token)

## Trade-offs
- **Memory**: Cache grows linearly with context length (n × d_k × d_v)
- **Speed**: Reduces redundant computation at cost of memory
- **Long contexts**: Cache size becomes significant (e.g., 128K context)

## Implementation
```python
# Simplified concept
cache_k = []
cache_v = []
for token in generated_sequence:
    q = compute_query(token)
    k, v = compute_kv(token)
    cache_k.append(k)
    cache_v.append(v)
    # Attend to all cached K/V + current
    output = attention(q, cache_k + [k], cache_v + [v])
```

## Related Concepts
- [[Autoregressive]] — Generation paradigm KV cache enables
- [[Transformer]] — Architecture using this optimization
- Memory bottleneck — Cache contributes to memory pressure
- [[InferenceOptimization]] — Key technique for LLM serving
