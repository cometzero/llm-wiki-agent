---
title: "Tokenization"
type: concept
tags: [nlp, preprocessing, llm]
sources:
  - "2026-05-17-day25-ai-ml-learning-review"
last_updated: 2026-05-17
---

## Summary
[[Tokenization]] is the process of converting raw text to token sequences used as model inputs. It is a deterministic pre-processing boundary before neural computations.

## Why it matters
- Determines the sequence of [[Token id]] values fed into [[Embedding]].
- Strongly influences sequence length, coverage of rare words, and compute cost.
- Same text can lead to different token boundaries depending on tokenizer version.

## Main Steps (typical)
1. Text normalization (공백/기호 처리).
2. Pre-tokenization.
3. Segmentation rule application (e.g., [[Subword]], [[BytePairEncoding]]).
4. Token id lookup in [[Vocabulary]].
5. Add [[SpecialToken]]s such as `<bos>`, `<eos>`, `<pad>`.

## Effects
- Smaller token pieces improve unknown-word handling but may increase token count.
- Fewer tokens reduce sequence length and can reduce [[ContextLength]] pressure.

## Related Connections
- [[Subword]], [[Vocabulary]], [[Embedding]], [[EmbeddingLookup]], [[SpecialToken]].
- [[Attention]] and [[ContextLength]] efficiency in the downstream model.

## Contradictions
- None identified.
