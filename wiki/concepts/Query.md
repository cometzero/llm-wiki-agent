---
title: "Query"
type: concept
tags: [transformer, attention, qkv]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
In attention mechanisms, the **Query** represents "what I'm looking for" or the current position's question. Each token generates a query vector that searches for relevant information from other tokens in the sequence.

## Key Concepts
- Query is one of three components in the [[QKV]] (Query, Key, Value) structure
- Generated via: `q = xW_Q` where `W_Q` is a learned weight matrix
- The query "asks" which information is relevant to the current token
- In [[Self-Attention]], queries are compared against all keys in the sequence

## Examples
- In the sentence "철수가 사과를 먹었다" (Chulsoo ate an apple), the token "먹었다" (ate) generates a query asking "what was eaten?"
- The query searches for tokens with matching keys (like "사과" = apple) to retrieve relevant context

## Connections
- [[Key]] — queries are compared against keys to compute relevance scores
- [[Value]] — selected values are weighted and mixed into output representations
- [[ScaledDotProductAttention]] — `Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V`
- [[Transformer]] — query-based attention is fundamental to Transformer architecture

## Mathematical Form
```
q = xW_Q
```
Where:
- `x` is the input embedding
- `W_Q` is a learned weight matrix
- `q` is the resulting query vector
