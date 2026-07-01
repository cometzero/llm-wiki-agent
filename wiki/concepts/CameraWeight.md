---
title: "Camera Weight"
type: concept
tags: [multi-view, perception, autonomous-driving]
sources: [qwen-robotnav-2606-18112-learning]
last_updated: 2026-07-01
---

# Camera Weight (w_c)

[[CameraWeight]] is an importance weighting parameter for each multi-view camera in autonomous driving or robot navigation systems.

## Importance in Autonomous Driving
Camera importance varies by driving situation:
- Lane following
- Intersection handling
- Merging
- Rear vehicle awareness

## Application in Qwen-RobotNav
The upper planner can send updated camera weights to [[QwenRobotNav]] based on current navigation context.

## Connection to Multi-View Perception
Essential for handling diverse camera configurations in self-driving vehicles.

## Related Concepts
- [[MultiViewPerception]]
- [[TaskAdaptiveObservationEncoding]]
- [[AutonomousDriving]]
