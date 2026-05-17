---
title: "Causal Language Model"
type: concept
tags: [llm, pretraining, language-model]
sources:
  - "2026-05-17-day25-ai-ml-learning-review"
last_updated: 2026-05-17
---

## Summary
A [[CausalLanguageModel]] predicts each token from previous tokens only, matching autoregressive generation behavior.

## Core definition
- Objective: estimate `P(x_t | x_{<t})` at every step.
- Uses [[CausalMask]] so future tokens cannot influence current prediction.

## Typical models
- [[GPT]], [[LLaMA]], [[Mistral]], [[Claude]] (in their chat/decoding modes).

## Why causal ordering matters
- In training and inference, the model must not access future targets.
- Matches left-to-right generation in conversational and generative settings.

## Related Connections
- [[NextTokenPrediction]], [[Autoregressive]], [[Softmax]], [[CrossEntropyLoss]], [[Logit]], [[CausalMask]].

## Contradictions
- None identified.
