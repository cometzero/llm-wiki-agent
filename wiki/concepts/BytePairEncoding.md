---
title: "Byte Pair Encoding (BPE)"
type: concept
tags: [tokenization, nlp]
sources:
  - "2026-05-17-day25-ai-ml-learning-review"
last_updated: 2026-05-17
---

## Summary
[[BytePairEncoding]] is a frequency-based method for building subword units by iteratively merging high-frequency adjacent symbol pairs.

## Core idea
- Start with fine-grained symbols.
- Count adjacent pair frequencies.
- Merge the most common pairs repeatedly.
- Result: common sequences become single tokens while rare pieces stay segmented.

## Why it is useful
- Reduces OOV stress.
- Enables shared token units across inflected or compound forms.
- Supports a practical balance between dictionary size and context length.

## Trade-off
- Merge too aggressively: vocabulary grows and memory pressure can increase.
- Merge too little: sequences get longer and [[QuadraticComplexity]] in attention becomes more visible.

## Related Connections
- [[Subword]], [[Tokenization]], [[Vocabulary]], [[ContextLength]], [[QuadraticComplexity]].

## Contradictions
- None identified.
