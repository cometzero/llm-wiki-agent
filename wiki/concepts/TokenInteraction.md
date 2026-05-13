---
title: "Token Interaction"
type: concept
tags: [transformer, attention, nlp]
sources: [2026-05-13-day21-ai-ml-learning-review]
last_updated: 2026-05-13
---

## Definition
**Token Interaction** refers to the direct connections and information exchange between tokens in a sequence. In [[Self-Attention]], every token can interact with every other token in a single layer, regardless of distance.

## Key Concepts
- Enables direct references between any pair of tokens
- Handles subject-verb agreement, coreference, long-range dependencies
- In [[Self-Attention]], interaction is weighted by attention scores
- [[ContextMixing]] is the result of token interactions

## Why It Matters
- "He gave the book to her. She thanked him." — model must link "She" to "her"
- "The trophy would not fit in the suitcase because it was too large" — "it" could refer to trophy or suitcase
- Enables semantic relationships regardless of word order

## Connections
- [[SelfAttention]] — enables direct token interactions
- [[ContextualEmbedding]] — representations built from interactions
- [[AttentionWeight]] — weight determines interaction strength
- [[LongRangeDependency]] — efficiently handled via interactions

## Examples
- Subject-verb: "The cats eating..." — "cats" interacts with "eating"
- Coreference: "John went to the store. He bought milk." — "He" → "John"
- Semantic: "은행" (bank) interacts with either "돈" (money) or "강가" (river bank)
