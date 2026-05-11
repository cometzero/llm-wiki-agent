---
title: "RNN"
type: concept
tags: [sequence-model, neural-network, recurrent]
sources: [2026-05-11-day19-ai-ml-learning-review]
last_updated: 2026-05-11
---

Recurrent Neural Network (RNN) is a neural network architecture designed for sequence data. Its core innovation is the hidden state — a memory vector that is updated at each time step by combining the current input with the previous hidden state.

## Core Update Equation

ht = tanh(Wx·xt + Wh·h(t-1) + b)

Where:
- xt: input vector at time step t
- h(t-1): previous hidden state
- Wx, Wh: weight matrices
- b: bias
- tanh: activation function squashing values to [-1, 1]

## Key Properties

- **Recurrence**: The same cell parameters are reused at every time step.
- **Sequential processing**: Time steps must be processed in order (no parallelization across time).
- **Hidden state as summary**: The final hidden state ideally contains a compressed representation of the entire sequence.

## Limitations

- [[VanishingGradient]] / gradient decay during [[BPTT]]: gradients shrink as they propagate backward through many time steps, making it hard to learn long-range dependencies.
- [[ExplodingGradient]]: gradients can grow uncontrollably.
- Sequential processing limits parallelization.
- Hidden state capacity is bounded by its dimensionality.

## Historical Significance

- RNNs were the dominant sequence model before [[Transformer]].
- Used for [[NLP]], speech recognition, time-series forecasting, machine translation.
- Led to [[LSTM]] and [[GRU]] variants that partially address vanishing gradients via gating mechanisms.
- Understanding RNN limitations motivates why [[Attention]] and [[Transformer]] became necessary.

## Related
- [[BPTT]]
- [[LSTM]]
- [[GRU]]
- [[HiddenState]]
- [[SequenceModel]]
- [[Autoregressive]]
- [[VanishingGradient]]