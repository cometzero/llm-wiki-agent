---
title: "Temporal Decay"
type: concept
tags: [temporal, observation-history, weighting]
sources: [qwen-robotnav-2606-18112-learning]
last_updated: 2026-07-01
---

# Temporal Decay (γ)

[[TemporalDecay]] is a parameter that determines how much weight to give to newer frames compared to older frames in observation history.

## Role in Navigation
- Higher γ: More weight on recent observations
- Lower γ: More balanced attention across temporal history
- Different tasks require different temporal attention profiles

## Connection to Task-Adaptive Encoding
Part of the (B, γ, w_c) parameter tuple for task-adaptive observation encoding in [[QwenRobotNav]].

## Related Concepts
- [[TaskAdaptiveObservationEncoding]]
- [[ObservationHistory]]
