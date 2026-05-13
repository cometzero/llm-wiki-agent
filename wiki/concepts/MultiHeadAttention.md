---
title: "Multi-Head Attention"
type: concept
tags: [transformer, attention]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
**Multi-Head Attention** extends self-attention by running multiple attention heads in parallel, each learning different types of relationships (e.g., syntactic vs. semantic) within the same layer.

## Key Concepts
- Splits Q, K, V into multiple heads: `head_i = Attention(QW_i^Q, KW_i^K, VW_i^V)`
- Concatenates all heads: `MultiHead(Q,K,V) = Concat(head_1, ..., head_h)W^O`
- Each head can learn different relationship patterns
- Increases model capacity and representational diversity

## Connections
- [[SelfAttention]] — base mechanism for each head
- [[ScaledDotProductAttention]] — per-head computation
- [[Transformer]] — stacks multi-head attention layers
- [[GPT]], [[BERT]] — use multi-head attention
