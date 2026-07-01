---
title: "Task-Adaptive Observation Encoding"
type: concept
tags: [navigation, observation, token-allocation]
sources: [qwen-robotnav-2606-18112-learning]
last_updated: 2026-07-01
---

# Task-Adaptive Observation Encoding

[[TaskAdaptiveObservationEncoding]] is a method that adjusts visual history and token allocation based on task mode and context parameters (B, γ, w_c).

## Parameters
- **B**: Context budget (visual token budget)
- **γ (Temporal decay)**: Determines weight distribution between older and newer frames
- **w_c (Camera weight)**: Importance weighting for each multi-view camera

## Application in Qwen-RobotNav
Different navigation subtasks require different observation strategies. The upper planner can specify different context parameters for different sub-goals.

## Connection to Edge Deployment
Visual token budget and quantization are key bottlenecks for edge deployment.

## Related Concepts
- [[TemporalDecay]]
- [[CameraWeight]]
- [[TokenBudget]]
