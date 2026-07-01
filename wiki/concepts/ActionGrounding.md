---
title: "Action Grounding"
type: concept
tags: [action, VLM, trajectory]
sources: [qwen-robotnav-2606-18112-learning]
last_updated: 2026-07-01
---

# Action Grounding

[[ActionGrounding]] is the process of converting VLM hidden states into waypoint trajectory outputs for robot/vehicle control.

## In Qwen-RobotNav
The MLP action head performs action grounding, outputting 8-step waypoint trajectories based on LLM backbone hidden states.

## Challenges
- Converting high-dimensional semantic representations to precise spatial actions
- Maintaining language/scene reasoning during action generation
- Avoiding trajectory-only training that loses reasoning capabilities

## Related Concepts
- [[WaypointTrajectory]]
- [[ActionHead]]
- [[VLN]]
