---
title: "Autoregressive"
type: concept
tags: [sequence-model, llm, generation]
sources: [2026-05-11-day19-ai-ml-learning-review]
last_updated: 2026-05-11
---

Autoregressive modeling frames sequence generation as predicting the next token given all previous tokens (the context). The core formulation is P(next token | context).

## Key Idea

- The model does not generate an entire sequence at once; it predicts one token at a time, appending each prediction to the context for the next step.
- The probability of a full sequence is the product of per-step conditional probabilities: P(x1, x2, x3) = P(x1) × P(x2|x1) × P(x3|x1,x2).
- Training uses [[CrossEntropyLoss]] to maximize the probability of the correct next token at each position.

## Connection to Modern LLMs

- All major [[LLM]]s ([[GPT]], [[Claude]], [[DeepSeek]]) are autoregressive [[Transformer]] decoders.
- Generation proceeds token by token, with the model outputting a probability distribution over the vocabulary at each step.
- Sampling strategies (greedy, top-k, top-p, temperature) select from this distribution.

## Historical Context

- Autoregressive modeling is not tied to [[RNN]] specifically — both RNNs and Transformer decoders can be autoregressive.
- The concept predates deep learning and appears in classical time-series models (AR, ARIMA).

## Related
- [[RNN]]
- [[Transformer]]
- [[SequenceModel]]
- [[Context]]
- [[Token]]