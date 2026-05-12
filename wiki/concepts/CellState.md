---
title: "Cell State (LSTM)"
type: concept
tags: [neural-networks, lstm, memory]
sources: [2026-05-12-day20-ai-ml-learning-review]
last_updated: 2026-05-12
---

## Definition
Cell state is the long-term memory channel in [[LSTM]] that flows through time steps with minimal modification, enabling preservation of information across long sequences.

## Key Properties

### Memory vs Computation Separation
Unlike vanilla RNN's single hidden state that must both store and compute, LSTM separates:
- **Cell state**: Long-term memory storage
- **Hidden state**: Current computation output

### Additive Update Path
The crucial innovation:
```
new_cell_state = forget_gate × previous_cell_state
               + input_gate × new_candidate
```

The **addition** of information (not overwrite) enables stable gradient flow.

## Gate Interactions

| Gate | Interaction with Cell State |
|------|----------------------------|
| Forget Gate | Multiplies cell state (what to discard) |
| Input Gate | Controls new candidate contribution |
| Output Gate | Determines what cell state exposes to hidden state |

## Contrast with [[GRU]]
GRU does NOT have a separate cell state—it uses hidden state for both storage and computation. This simplifies architecture but provides less granular memory control.

## Connections
- [[LSTM]] — the architecture that introduces cell state
- [[GRU]] — alternative that omits cell state
- [[VanishingGradient]] — cell state solves this via additive paths
- [[HiddenState]] — cell state's "output interface"
