---
title: "Sequence Length"
type: concept
tags: [transformer, tokenization, efficiency]
sources: [2026-05-17-day25-ai-ml-learning-review]
last_updated: 2026-05-17
---

## Definition
Sequence length is the number of tokens in a model input or generated output. It directly affects Transformer compute because full self-attention grows roughly with the square of sequence length.

## Connections
- [[Tokenization]] — determines how much text becomes how many tokens.
- [[QuadraticComplexity]] — attention cost increases rapidly as sequence length grows.
