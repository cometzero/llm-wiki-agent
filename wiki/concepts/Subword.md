---
title: "Subword"
type: concept
tags: [tokenization, nlp, llm]
sources:
  - "2026-05-17-day25-ai-ml-learning-review"
last_updated: 2026-05-17
---

## Summary
A [[Subword]] is a token unit smaller than or similar to a full word, used to avoid sparse vocabulary failures while preserving sequence-level structure.

## Why it is used
- Handles unseen or rare words by composing from frequent fragments.
- Useful for Korean/URL/code-like strings with many morphology or symbol combinations.
- Trade-off: often increases token count.

## Common algorithm
- [[BytePairEncoding]] repeatedly merges frequent symbol/character pair candidates into larger units.

## Effects on LLM workflows
- Better coverage for out-of-vocabulary fragments.
- Can increase number of tokens, affecting [[Attention]]/memory and latency.

## Related Connections
- [[Tokenization]], [[BytePairEncoding]], [[Vocabulary]], [[Embedding]].

## Contradictions
- None identified.
