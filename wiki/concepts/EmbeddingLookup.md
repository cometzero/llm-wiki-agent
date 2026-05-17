---
title: "Embedding Lookup"
type: concept
tags: [embedding, tokenization, neural-networks]
sources: [2026-05-17-day25-ai-ml-learning-review]
last_updated: 2026-05-17
---

## Definition
Embedding lookup maps a [[TokenId]] to a learned vector by selecting the corresponding row of an embedding matrix. It is the bridge between discrete tokenizer output and continuous neural network computation.

## Connections
- [[Embedding]] — the learned vector representation produced by lookup.
- [[Tokenization]] — supplies the token IDs to be looked up.
