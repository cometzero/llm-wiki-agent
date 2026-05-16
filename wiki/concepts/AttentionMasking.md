---
title: "Attention Masking"
type: concept
tags: [transformer, attention, masking]
sources: [2026-05-16-day24-ai-ml-learning-review.md]
last_updated: 2026-05-16
---

## Definition
**Attention masking** is a general technique that prevents certain token positions from contributing to attention weight calculations by adding -inf values before softmax.

## Types
1. **[[CausalMask]]** — Blocks future tokens in autoregressive models
2. **[[PaddingMask]]** — Blocks meaningless `<pad>` tokens
3. **[[EncoderDecoderAttention]]** — Optional masking in cross attention for specific positions

## Mechanism
```
Attention(Q,K,V) = softmax(QK^T/√d_k + mask) V
```
- mask = 0 for accessible positions
- mask = -inf for blocked positions
- softmax(exp(-inf)) = 0, effectively removing contribution

## Purpose
- Defines "what information is accessible" per token
- Enables [[Autoregressive]] generation
- Maintains clean batch representations
- Prevents information leakage during training

## Related Concepts
- [[SelfAttention]] — Where masking is applied
- [[Softmax]] — The function that converts -inf to zero weight
- [[Transformer]] — Architecture using attention masking
