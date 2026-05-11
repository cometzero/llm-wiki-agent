---
title: "LongTermDependency"
type: concept
tags: [sequence-model, rnn, attention]
sources: [2026-05-11-day19-ai-ml-learning-review]
last_updated: 2026-05-11
---

A long-term dependency in sequence modeling refers to a situation where information appearing early in a sequence is critical for predicting an output much later in the sequence.

## Example

In the sentence "Chulsoo put a laptop in his bag in the morning... What should Chulsoo take out?", the answer "laptop" depends on information given many tokens earlier.

## Why It's Hard for RNNs

- [[RNN]]s compress all past information into a fixed-size [[HiddenState]].
- During [[BPTT]], gradients must propagate backward through many time steps.
- [[VanishingGradient]] causes the learning signal for early positions to become negligible.
- The model may fail to learn that early information matters for later predictions.

## Solutions

- [[LSTM]] / [[GRU]]: gating mechanisms help preserve information over longer distances.
- [[Attention]]: allows direct access to any past hidden state, bypassing the compression bottleneck.
- [[Transformer]]: built entirely on attention, eliminating the recurrence bottleneck.

## Related
- [[RNN]]
- [[BPTT]]
- [[VanishingGradient]]
- [[Attention]]
- [[Transformer]]
- [[LSTM]]