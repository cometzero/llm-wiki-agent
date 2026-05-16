---
title: "Causal Mask"
type: concept
tags: [transformer, attention, masking, autoregressive]
sources: [2026-05-16-day24-ai-ml-learning-review.md]
last_updated: 2026-05-16
---

## Definition
A **causal mask** prevents current tokens from attending to future tokens in self-attention. It creates a lower-triangular attention pattern, ensuring each token can only see itself and previous tokens.

## Key Properties
- Used in [[Autoregressive]] language models (e.g., [[GPT]])
- Ensures training conditions match inference (no future information leakage)
- Applied before softmax as -inf values in the attention score matrix
- Creates O(n²) memory for storage, O(1) compute per position for inference (with [[KVCache]])

## Mathematical Representation
```
S_masked = S + mask
where mask[i,j] = 0 if j ≤ i (accessible), -inf if j > i (blocked)
```

## Examples
- Token position 3 in sequence: can attend to positions 1, 2, 3; blocked from 4+
- GPT-style next-token prediction: "나는 밥을" predicts next token with causal masking

## Related Concepts
- [[PaddingMask]] — Blocks attention to `<pad>` tokens
- [[AttentionMasking]] — General framework for both
- [[SelfAttention]] — Where causal mask is applied
- [[Autoregressive]] — The generation paradigm enabled by causal masking
