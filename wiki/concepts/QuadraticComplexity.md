---
title: "Quadratic Complexity"
type: concept
tags: [transformer, attention, computational-complexity]
sources: [2026-05-16-day24-ai-ml-learning-review.md]
last_updated: 2026-05-16
---

## Definition
**Quadratic complexity** (O(n²)) describes how self-attention computational and memory costs grow quadratically with sequence length n, since each token attends to all n tokens.

## Impact
| Sequence Length | Attention Scores | Relative Cost |
|---:|---:|---:|
| 100 | 10,000 | 1× |
| 1,000 | 1,000,000 | 100× |
| 10,000 | 100,000,000 | 10,000× |

## Memory Calculation
For batch B, heads H, sequence n:
```
Memory = B × H × n × n × bytes_per_element
```
Example: batch=2, heads=8, n=1000, float16 (2 bytes):
~32 MB just for attention weights

## Challenges
- Limits context length in [[LLM]]
- GPU memory becomes bottleneck before compute
- Long document processing, RAG, code analysis all affected

## Mitigation Approaches
- [[FlashAttention]] — Memory-efficient attention computation
- Sparse attention — Attend to subset of positions
- Sliding-window attention — Local context only
- Linear attention — Subquadratic alternatives
- Chunking / retrieval — Process in segments

## Related Concepts
- [[SelfAttention]] — Source of O(n²) behavior
- Memory bottleneck — The practical problem it creates
- [[TransformerParallelism]] — Benefits tempered by this cost
