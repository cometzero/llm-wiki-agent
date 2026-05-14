---
title: "Multi-Head Attention"
type: concept
tags: [transformer, attention, neural-network]
sources: [2026-05-13-day21-ai-ml-learning-review, 2026-05-14-day22-ai-ml-learning-review]
last_updated: 2026-05-14
---

## Definition

**Multi-Head Attention** splits a single attention computation into multiple parallel "heads," each using different projection matrices for Query (Q), Key (K), and Value (V). This allows the model to capture diverse relationship patterns simultaneously.

## Core Mechanism

```
head_i = Attention(XW_Q_i, XW_K_i, XW_V_i)
MultiHead(X) = Concat(head_1, ..., head_h) W_O
```

Each head:
1. Projects input to its own Q, K, V subspace
2. Computes scaled dot-product attention
3. Outputs a transformed representation

## Why Multiple Heads?

Single-head attention can only capture one type of relationship pattern. Multi-head attention allows simultaneous capture of:
- Subject-verb relations
- Object-verb relations  
- Pronoun reference
- Local proximity patterns
- Semantic dependencies

## Shape Analysis

For a transformer with `n` tokens, `d_model` hidden dimension, `h` heads:

```
Input: batch × n × d_model
After split: batch × h × n × d_head (where d_model = h × d_head)
Each head computes: batch × h × n × d_head
Concat: batch × n × d_model
```

## Connections

- [[TransformerBlock]] — where multi-head attention is a sublayer
- [[Attention]] — base mechanism each head implements
- [[QKV]] — head projections generate Q, K, V matrices
- [[SelfAttention]] — multi-head is typically used for self-attention

## Key Properties

1. **Different projections per head** — each head learns different relationship patterns
2. **Parallel computation** — heads compute simultaneously on GPU
3. **Subspace specialization** — smaller d_head allows focused pattern detection
4. **Concatenation + projection** — combines head outputs back to d_model dimension

## Common Misconceptions

1. ❌ "Heads have pre-assigned roles (e.g., head 1 = subject detection)"
   ✓ Learned through training, not manually assigned

2. ❌ "More heads always better"
   ✓ When d_model is fixed, more heads means smaller d_head, potentially losing information capacity

3. ❌ "Attention visualization fully explains model reasoning"
   ✓ FFN, residual connections, and layer interactions also contribute significantly
