---
title: "Hidden State"
type: concept
tags: [neural-networks, rnn, representation]
sources: [2026-05-12-day20-ai-ml-learning-review, 2026-05-11-day19-ai-ml-learning-review]
last_updated: 2026-05-12
---

## Definition
Hidden state is the model's internal representation that compresses all processed information into a fixed-size vector, updated at each time step.

## Role Across Architectures

### Vanilla RNN
Single hidden state must:
- Encode all past information
- Serve as input for next step
- Output prediction at final step

### [[LSTM]]
- **Cell state**: Long-term memory (separate)
- **Hidden state**: Current computational output

### [[GRU]]
Only hidden state exists—no separate cell state.

## Bottleneck Problem
Hidden state has fixed capacity. For long sequences:
- Important early information gets overwritten
- Compression loses detail
- Model struggles with long-range dependencies

This bottleneck motivated both gated architectures and [[AttentionMechanism]].

## Shape
Typically `[batch_size, hidden_size]` or `[batch_size, sequence_length, hidden_size]` depending on context.

## Connections
- [[LSTM]] — uses hidden state alongside cell state
- [[GRU]] — uses hidden state as sole memory
- [[AttentionMechanism]] — alternative to hidden state compression
- [[CellState]] — LSTM's specialized memory channel
