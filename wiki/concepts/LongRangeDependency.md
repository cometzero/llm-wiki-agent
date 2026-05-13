---
title: "Long-Range Dependency"
type: concept
tags: [sequence-modeling, attention]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
A long-range dependency is a relationship where information far earlier or later in a sequence affects how another token should be interpreted or predicted. [[SelfAttention]] helps model these dependencies because tokens can directly attend to distant tokens in the same sequence.

## Connections
- [[SequenceModel]] — long-range dependencies are a central challenge in ordered data.
- [[SelfAttention]] — creates direct token-to-token paths across long contexts.
- [[TokenInteraction]] — captures relationships between distant tokens.
