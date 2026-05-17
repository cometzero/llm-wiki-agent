---
title: "Next-Token Prediction"
type: concept
tags: [language-model, sequence-model, llm]
sources:
  - "2026-05-17-day25-ai-ml-learning-review"
last_updated: 2026-05-17
---

## Summary
[[NextTokenPrediction]] is the core training and inference objective for most GPT-like models: predict the most likely next [[Token]] given all previous tokens.

## Key Definition
Given token sequence `x_1, x_2, ..., x_t`, model estimates

`P(x_t | x_1, x_2, ..., x_{t-1})`.

The model outputs a probability distribution over [[Vocabulary]] for every position, not a single deterministic word.

## Why it matters
- Works with raw text without requiring human label tasks.
- Scales with large corpora to learn lexical, syntactic, and some factual/coherence priors.
- Enables [[Autoregressive]] generation by repeatedly appending one token at a time.

## Process
1. Start with prompt tokens.
2. Predict distribution for next token.
3. Sample or choose one token.
4. Append it and repeat until stop token.

## Related Connections
- [[LanguageModel]], [[Autoregressive]], [[CausalLanguageModel]], [[CrossEntropyLoss]], [[Optimizer]], [[Gradient]], [[Autoregressive Objective]].

## Common Pitfalls
- Interpreting as "single-answer classification": it is actually distributional prediction over all tokens.
- Ignoring tokenization effects: token boundaries change this model’s exact input surface.

## Contradictions
- None identified.
