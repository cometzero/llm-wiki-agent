---
title: "SequenceModel"
type: concept
tags: [sequence, machine-learning, nlp]
sources: [2026-05-11-day19-ai-ml-learning-review]
last_updated: 2026-05-11
---

A sequence model is any machine learning model designed to process data where the order of elements matters. Examples include sentences, speech, time-series data, DNA sequences, and code.

## Key Concepts

- **Time step**: Each position in the sequence (e.g., a token position in a sentence, a time point in a sensor reading).
- **Context**: The preceding elements used to predict the next element.
- **Autoregressive**: Predicting the next element given the context.

## Major Architectures

- [[RNN]]: Processes sequentially with a hidden state.
- [[LSTM]] / [[GRU]]: Gated RNN variants.
- [[Transformer]]: Processes all positions in parallel using [[Attention]].
- [[CNN]] for sequences: Temporal convolutions (e.g., WaveNet, TCN).

## Applications

- [[NLP]]: language modeling, translation, summarization.
- Speech recognition.
- Time-series forecasting.
- Music generation.
- Code generation.
- Recommendation systems (click sequences).

## Related
- [[Autoregressive]]
- [[RNN]]
- [[Transformer]]
- [[Attention]]
- [[Token]]
- [[Context]]