---
title: "Positional Encoding"
type: concept
tags: [transformer, sequence-modeling]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
Positional encoding is a mechanism that injects order information into Transformer inputs. Since [[SelfAttention]] compares tokens by content and does not inherently know their sequence positions, positional information helps the model distinguish the same tokens appearing in different orders.

## Connections
- [[Transformer]] — uses positional information alongside attention.
- [[SelfAttention]] — requires position information to represent token order.
- [[Embedding]] — positional encodings are added to or combined with token embeddings.
