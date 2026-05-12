---
title: "LSTM (Long Short-Term Memory)"
type: concept
tags: [neural-networks, sequence-models, gating]
sources: [2026-05-12-day20-ai-ml-learning-review]
last_updated: 2026-05-12
---

## Definition
LSTM is an RNN variant that uses **gate mechanisms** (forget, input, output) and a separate **cell state** to selectively preserve long-term information, addressing the [[VanishingGradient]] problem in vanilla RNNs.

## Architecture Components

### Cell State
- Long-term memory channel that flows with minimal modification through time steps
- Mathematical key: additive path enables stable gradient propagation

### Gates (all use sigmoid → 0-1 range)
1. **Forget Gate**: What to discard from previous cell state
2. **Input Gate**: What new information to add
3. **Output Gate**: What to expose to hidden state

## Mathematical Core
```
new_cell_state = forget_gate × previous_cell_state + input_gate × new_candidate
new_hidden_state = output_gate × tanh(new_cell_state)
```

The **addition path** is crucial—it allows gradients to flow unchanged through time, solving vanishing gradients.

## Why It Matters
- First practical solution for learning long-range dependencies
- Foundation for understanding why [[AttentionMechanism]] emerged
- Still used in resource-constrained or streaming scenarios

## Connections
- [[GRU]] — simpler variant with fewer gates
- [[VanishingGradient]] — the problem it solves
- [[AttentionMechanism]] — evolved solution to same problem
- [[Embedding]] — often applied to input tokens before LSTM

## Key Distinction from GRU
| Aspect | LSTM | GRU |
|--------|------|-----|
| Memory channel | Separate cell state | Hidden state only |
| Gate count | 3 gates | 2 gates |
| Complexity | Higher | Lower |
| Control granularity | Finer | Coarser |

## Historical Note
Introduced by Hochreiter & Schmidhuber (1997) to address the fundamental difficulty of learning long-term dependencies in vanilla RNNs.
