---
title: "Pretraining"
type: concept
tags: [model-training, llm]
sources:
  - "2026-05-17-day25-ai-ml-learning-review"
last_updated: 2026-05-17
---

## Summary
[[Pretraining]] is a large-scale upstream training stage where a model learns generalizable sequence representations from raw text before task-specific tuning.

## Why pretraining is necessary
- Real-world labels for every downstream task are sparse.
- Raw corpora contain abundant implicit signal for language structure.

## Typical property
Pretraining objectives are often [[SelfSupervisedLearning]]-compatible:
- [[CausalLanguageModel]] objective: next-token prediction.
- [[MaskedLanguageModel]] objective: masked-token recovery.

## Role in downstream quality
A strong pretraining stage improves [[TransferLearning]] potential to tasks like Q&A, summarization, translation, code generation, and classification.

## Related Connections
- [[NextTokenPrediction]], [[Objective]], [[Loss]], [[Optimizer]], [[InstructionTuning], [[PreferenceOptimization]] (as later stages).

## Contradictions
- None identified.
