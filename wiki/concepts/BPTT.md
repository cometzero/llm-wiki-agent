---
title: "BPTT"
type: concept
tags: [training, rnn, gradient]
sources: [2026-05-11-day19-ai-ml-learning-review]
last_updated: 2026-05-11
---

Backpropagation Through Time (BPTT) is the standard algorithm for training [[RNN]]s. It unfolds the RNN across time steps and applies standard backpropagation through the resulting computational graph.

## How It Works

1. **Forward pass**: Process the sequence step by step, computing hidden states h1, h2, ..., hT.
2. **Loss computation**: Compute loss at the final time step (or at each step).
3. **Backward pass**: Propagate gradients backward from loss → hT → h(T-1) → ... → h1 → parameters.

## Key Challenge: Gradient Decay

- Gradients are multiplied by the same weight matrix at each time step during backpropagation.
- If the spectral norm of the weight matrix is < 1, gradients vanish (approach zero) over many steps.
- If > 1, gradients explode.
- This makes it difficult for the model to learn [[LongTermDependency|long-term dependencies]].

## Mitigation Techniques

- [[LSTM]] / [[GRU]]: gated architectures that allow gradients to flow more easily.
- [[GradientClipping]]: cap gradient norms to prevent explosion.
- [[ResidualConnection]]: provide shortcut paths for gradient flow.
- [[Normalization]]: stabilize activation scales.
- [[Attention]]: bypass the need to compress all history into a single hidden state.

## Related
- [[RNN]]
- [[VanishingGradient]]
- [[ExplodingGradient]]
- [[Backpropagation]]
- [[LongTermDependency]]