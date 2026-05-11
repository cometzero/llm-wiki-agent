---
title: "VanishingGradient"
type: concept
tags: [training, optimization, deep-learning]
sources: [2026-05-11-day19-ai-ml-learning-review]
last_updated: 2026-05-11
---

The vanishing gradient problem occurs when gradients become extremely small as they are backpropagated through many layers or time steps, causing early layers or time steps to receive negligible learning signal.

## Cause

- In deep networks, gradients are multiplied by weight matrices at each layer.
- In [[RNN]]s, the same weight matrix is multiplied at each time step during [[BPTT]].
- If the eigenvalues of the weight matrix are less than 1, repeated multiplication causes exponential decay.

## Consequences

- Early layers / time steps learn very slowly or not at all.
- The model fails to capture [[LongTermDependency|long-term dependencies]].
- Performance on tasks requiring long-range context is poor.

## Mitigations

- [[LSTM]] / [[GRU]]: gating mechanisms create paths where gradients can flow with less attenuation.
- [[ResidualConnection]]: skip connections allow gradients to bypass layers.
- [[Normalization]]: keeps activations in a reasonable range.
- Careful weight initialization (e.g., Xavier, He).
- [[Attention]]: eliminates the need to propagate gradients through many time steps.

## Related
- [[BPTT]]
- [[RNN]]
- [[LongTermDependency]]
- [[ExplodingGradient]]
- [[ResidualConnection]]