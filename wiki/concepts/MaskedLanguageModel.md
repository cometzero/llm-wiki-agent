---
title: "Masked Language Model"
type: concept
tags: [language-model, pretraining, nlp]
sources:
  - "2026-05-17-day25-ai-ml-learning-review"
last_updated: 2026-05-17
---

## Summary
A [[MaskedLanguageModel]] learns to recover masked tokens from surrounding context, using both left and right context around each masked position.

## Core idea
- Input token is replaced by `[MASK]`.
- Model predicts the missing token(s) from context.
- Commonly associated with bidirectional understanding setups.

## Contrast with [[CausalLanguageModel]]
- Causal: predicts next token from history only, natural for generation.
- Masked: predicts hidden tokens with both-side context, strong for representation learning in understanding tasks.

## Common association
- [[BERT]] and related encoder-style training designs.

## Related Connections
- [[SelfSupervisedLearning]], [[Pretraining]], [[Objective]], [[CrossEntropyLoss]].

## Contradictions
- None identified.
