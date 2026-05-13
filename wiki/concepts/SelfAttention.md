---
title: "Self-Attention"
type: concept
tags: [transformer, attention, sequence-modeling]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
**Self-Attention** allows each token in a sequence to attend to (reference) all other tokens in the same sequence, enabling context-dependent representations. The "self" refers to attending within the same sequence, not just to oneself.

## Key Concepts
- Q, K, V all come from the same input sequence: `Q = XW_Q`, `K = XW_K`, `V = XW_V`
- Enables [[TokenInteraction]] between any pair of tokens directly
- Handles [[LongRangeDependency]] that challenges RNNs
- Produces [[ContextualEmbedding]]: same word gets different representation based on context
- [[ContextMixing]] combines information from multiple tokens

## Why It Matters
- Same word (e.g., "은행") can mean bank (financial) or river bank depending on context
- "먹었다" (ate) needs to reference "사과" (apple) to understand what was eaten
- Enables parallel computation (unlike sequential RNN)

## Connections
- [[ScaledDotProductAttention]] — the computation mechanism
- [[Query]], [[Key]], [[Value]] — derived from same input X
- [[ContextualEmbedding]] — output representation depends on context
- [[TokenInteraction]] — direct token-to-token relationships
- [[Transformer]] — stack self-attention layers for strong representation
- [[BERT]], [[GPT]] — use self-attention differently (bidirectional vs. causal)
- [[MultiHeadAttention]] — multiple attention heads for different relationship types
- [[PositionalEncoding]] — needed because self-attention lacks inherent order

## Comparison with RNN
| Aspect | RNN | Self-Attention |
|--------|-----|----------------|
| Information flow | Sequential | Direct |
| Long-range dependency | Difficult (vanishing gradient) | Easy (direct connection) |
| Parallelization | Limited | Full (within layer) |
| Path length | O(n) per step | O(1) for any pair |

## Example
For "철수가 사과를 먹었다":
- `먹었다` attends heavily to `사과를` (what was eaten)
- Attention weight might be: `먹었다→사과를 = 0.6`
- Result: `먹었다`'s new representation incorporates "apple" information
