---
title: "GRU (Gated Recurrent Unit)"
type: concept
tags: [neural-networks, sequence-models, gating]
sources: [2026-05-12-day20-ai-ml-learning-review]
last_updated: 2026-05-12
---

## Definition
GRU is a simplified [[LSTM]] variant that merges the cell state and hidden state into a single channel, using two gates (update, reset) instead of three.

## Architecture Components

### Gates
1. **Update Gate**: Controls how much previous hidden state to keep vs. how much new information to add
2. **Reset Gate**: Controls how much previous hidden state to ignore when computing new candidate state

## Mathematical Core
```
update_gate = sigmoid(W_u · [h_{t-1}, x_t])
reset_gate = sigmoid(W_r · [h_{t-1}, x_t])
new_candidate = tanh(W · [reset_gate × h_{t-1}, x_t])
h_t = (1 - update_gate) × h_{t-1} + update_gate × new_candidate
```

## Trade-offs vs LSTM

### Advantages
- Fewer parameters → faster training and inference
- Less prone to overfitting on small datasets
- Often competitive performance

### Limitations
- Coarser memory control (no separate cell state)
- May underperform LSTM on tasks requiring very fine-grained memory

## Connections
- [[LSTM]] — the more expressive variant with separate cell state
- [[VanishingGradient]] — both architectures solve this problem
- [[AttentionMechanism]] — evolved solution to sequence modeling challenges

## When to Choose
| Scenario | Recommendation |
|----------|----------------|
| Limited compute | GRU |
| Small dataset | GRU |
| Need fine memory control | LSTM |
| Very long sequences | LSTM or [[AttentionMechanism]] |
