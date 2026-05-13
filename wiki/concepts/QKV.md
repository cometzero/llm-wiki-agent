---
title: "QKV"
type: concept
tags: [transformer, attention]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
QKV is the Query-Key-Value role separation used in Transformer attention. A token's embedding is projected into [[Query]], [[Key]], and [[Value]] vectors so the model can separate what it is looking for, how candidates are matched, and what content is carried forward.

## Connections
- [[Query]] — represents the current token's information need.
- [[Key]] — represents searchable features of candidate tokens.
- [[Value]] — carries the content mixed into the attention output.
- [[ScaledDotProductAttention]] — computes attention over Q, K, and V.
