---
title: "Autoregressive Objective"
type: concept
tags: [llm, objective, generation]
sources: [2026-05-17-day25-ai-ml-learning-review]
last_updated: 2026-05-17
---

## Definition
An autoregressive objective trains a model to predict each token using only previous tokens. It is the objective behind [[NextTokenPrediction]] in [[CausalLanguageModel]] systems.

## Connections
- [[Autoregressive]] — sequence generation style using previous outputs as future context.
- [[CausalMask]] — prevents future-token leakage during training.
