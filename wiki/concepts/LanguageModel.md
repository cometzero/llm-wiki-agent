---
title: "Language Model"
type: concept
tags: [llm, nlp, sequence-modeling]
sources: [2026-05-17-day25-ai-ml-learning-review]
last_updated: 2026-05-17
---

## Definition
A [[LanguageModel]] assigns probabilities to token sequences and predicts likely next tokens from context. In modern LLMs this is usually implemented with a Transformer trained on [[NextTokenPrediction]].

## Connections
- [[NextTokenPrediction]] — common training objective for decoder-only models.
- [[Tokenization]] — converts text into the tokens language models score.
- [[Pretraining]] — large-scale self-supervised stage where language models learn broad patterns.
