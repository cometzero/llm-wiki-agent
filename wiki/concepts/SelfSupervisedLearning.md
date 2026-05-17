---
title: "Self-Supervised Learning"
type: concept
tags: [machine-learning, pretraining]
sources: [2026-05-17-day25-ai-ml-learning-review]
last_updated: 2026-05-17
---

## Definition
Self-supervised learning creates training targets from the data itself rather than relying on manually labeled examples. For language models, raw text can supply targets for [[NextTokenPrediction]] or [[MaskedLanguageModel]] objectives.

## Connections
- [[Pretraining]] — large-scale self-supervised learning is the usual first stage for LLMs.
- [[CausalLanguageModel]] — predicts future tokens from left context.
- [[MaskedLanguageModel]] — predicts masked tokens from bidirectional context.
