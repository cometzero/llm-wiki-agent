---
title: "KV Cache"
type: concept
tags: [llm, inference, memory, optimization]
sources: [2026-05-19-day27-ai-ml-learning-review]
last_updated: 2026-05-19
---

## Definition
KV cache stores the key (K) and value (V) activations from previous tokens during autoregressive generation, avoiding recomputation of attention for already-processed tokens.

## Why It Exists
LLMs generate tokens one at a time autoregressively. Without KV cache, each new token would require recomputing attention over ALL previous tokens, leading to O(n²) computation per step. KV cache enables incremental computation.

## Key Properties
- **Trade-off**: Speed vs memory — stores K/V for each token at each layer
- **Memory grows**: Proportional to sequence length × num layers × hidden size
- **Flash Attention**: Modern technique that reduces KV cache memory footprint
- **Prefill phase**: Initial pass computes and caches K/V for input tokens
- **Decode phase**: Uses cached K/V + computes K/V for new token only

## Memory Calculation (Simplified)
For each layer: 2 × seq_len × hidden_size × 4 bytes (float32)
For 70B model with 80 layers, 8K context: significant GPU memory requirement

## Related Concepts
- [[ContextWindow]] — limits how long sequences can be
- [[Transformer]] — architecture where KV cache applies
- [[Attention]] — mechanism that generates K/V values
- Prefill/Decode — two-phase inference where KV cache is populated then used

## Production Considerations
- Limits concurrent users (memory per session)
- Affects batch size feasibility
- KV cache eviction strategies for long conversations
