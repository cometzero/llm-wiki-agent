---
title: "AI/ML Learning Review — Day 19 (2026-05-11): Sequence Models, RNN, BPTT"
type: source
tags: [sequence, rnn, bptt, attention, transformer, autoregressive]
date: 2026-05-11
source_file: raw/ai_ml_learning/2026-05-11-day19-ai-ml-learning-review.md
source_hash: 20a37a799d8acf2a
---

## Summary

Day 19 of the AI/ML learning series covers three foundational concepts for understanding sequence models: (1) sequence data and the [[Autoregressive]] perspective, (2) [[RNN]]'s recurrent hidden state, and (3) [[BPTT]] and the long-term dependency problem. The material explains why [[Attention]] and [[Transformer]] architectures emerged as solutions to RNN limitations in handling long contexts and parallelization.

## Key Claims

- Sequence data is defined by order — the same tokens in different order carry different meaning.
- Autoregressive modeling frames sequence learning as predicting the next token given context: P(next token | context).
- [[RNN]] uses a hidden state that is updated at each time step via: ht = tanh(Wx·xt + Wh·h(t-1) + b).
- The same RNN cell parameters are reused across all time steps (recurrence).
- [[BPTT]] (Backpropagation Through Time) unfolds the RNN across time steps for gradient computation.
- Long-term dependency learning is difficult because gradients decay (vanish) when multiplied across many time steps — this is the vanishing gradient problem.
- Gradient explosion (exploding gradient) is the counterpart problem when gradients grow too large.
- [[LSTM]] and [[GRU]] use gate mechanisms to better preserve long-range information.
- [[Attention]] and [[Transformer]] directly address RNN limitations by allowing direct access to any past position and enabling parallel processing.

## Key Quotes

> "Sequence learning is training to predict the next token at each position." — Lesson summary

> "The current hidden state is the result of mixing the current input and the past hidden state." — Lesson on RNN

> "In long sequences, if the gradient keeps shrinking, the earlier time steps receive almost no learning signal about how they affected the final loss." — On BPTT and gradient decay

> "Sequence models emerged to handle order and context; RNN summarizes the past via hidden state, but BPTT's gradient decay makes long dependencies hard to learn, driving the need for attention and Transformer." — Day's one-line summary

## Connections

- [[Autoregressive]] — core framing for next-token prediction used by all modern [[LLM]]s
- [[RNN]] — foundational sequence model using hidden state recurrence
- [[BPTT]] — training algorithm for RNNs
- [[LSTM]] — RNN variant with gates to mitigate vanishing gradients
- [[GRU]] — simpler gated RNN variant
- [[Attention]] — mechanism that allows direct access to any past position
- [[Transformer]] — architecture built on attention, enabling parallelization and long context
- [[LLM]] — modern language models are autoregressive transformers
- [[SequenceModel]] — general category for models handling ordered data
- [[VanishingGradient]] — core problem in training deep/sequential models
- [[HiddenState]] — RNN's internal memory vector
- [[Context]] — the preceding tokens used for prediction
- [[Token]] — atomic unit in sequence processing
- [[Embedding]] — vector representation of tokens
- [[CrossEntropyLoss]] — loss function used for next-token prediction
- [[GradientClipping]] — technique to prevent exploding gradients
- [[ResidualConnection]] — technique to improve gradient flow
- [[Normalization]] — technique to stabilize training

## Contradictions

- None identified with existing wiki content.

## Domain-Specific Template

This source is an AI/ML learning review (diary/journal format).