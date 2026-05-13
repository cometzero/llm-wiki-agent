---
title: "Contextual Embedding"
type: concept
tags: [transformer, nlp, representation-learning]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
A **Contextual Embedding** is a token representation that depends on its surrounding context. Unlike static word embeddings, the same word can have different representations based on its usage.

## Key Concepts
- Produced by [[SelfAttention]] and similar mechanisms
- [[ContextMixing]] creates context-dependent representations
- Same word (e.g., "bank") gets different vector in different contexts
- Foundation of modern NLP representation learning

## Example
"은행" (bank):
- With context: `돈, 계좌` (money, account) → financial institution
- With context: `강가, 앉았다` (riverbank, sat) → river embankment

## Connections
- [[SelfAttention]] — creates contextual embeddings
- [[ContextMixing]] — the mechanism of context incorporation
- [[Embedding]] — non-contextual precursor
- [[BERT]] — produces contextual embeddings
