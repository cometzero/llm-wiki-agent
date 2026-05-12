---
title: "Vanishing Gradient Problem"
type: concept
tags: [neural-networks, training, optimization]
sources: [2026-05-12-day20-ai-ml-learning-review, 2026-05-11-day19-ai-ml-learning-review]
last_updated: 2026-05-12
---

## Definition
The vanishing gradient problem occurs when gradients become extremely small during backpropagation through time (BPTT) or deep networks, making it difficult to learn long-range dependencies.

## Root Cause
In RNNs, the recurrence multiplication of gradient terms:
```
∂L/∂h_t = ∂L/∂h_{t+n} × Π(∂h_{i+1}/∂h_i)
```

If the product of derivatives is < 1, gradients shrink exponentially as they propagate backward through time.

## Consequences
- Early time steps receive almost zero gradient updates
- Model cannot learn dependencies between distant positions
- Long sequences behave like short sequences

## Solutions

| Approach | Mechanism |
|----------|----------|
| [[LSTM]]/[[GRU]] | Additive paths + gating to preserve gradient flow |
| Residual Networks | Skip connections for gradient bypass |
| [[AttentionMechanism]] | Direct connections between all positions |
| Careful initialization | Heuristic to keep gradients in healthy range |

## Why LSTM/GRU Help
LSTM's cell state uses **additive updates**:
```
new_cell_state = forget_gate × old_state + input_gate × new_info
```

The addition means gradient can flow unchanged (not multiplied repeatedly), preventing exponential decay.

## Connections
- [[LSTM]] — first major practical solution
- [[GRU]] — simplified solution
- [[AttentionMechanism]] — eventual solution in [[Transformer]]
- BPTT — the backprop method that reveals the problem
