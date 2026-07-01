---
title: "PDMS"
type: concept
tags: [metric, autonomous-driving, evaluation]
sources: [qwen-robotnav-2606-18112-learning]
last_updated: 2026-07-01
---

# PDMS (PDM Score)

[[PDMS]] is NAVSIM's composite metric for closed-loop autonomous driving evaluation.

## Components
- **Progress**: How much distance toward the goal is covered
- **Safety**: Collision avoidance, TTC compliance
- **Rule compliance**: Traffic rules, drivable area adherence

## Qwen-RobotNav Performance
Achieves 91.4 PDMS on the NAVSIM benchmark.

## Related Concepts
- [[NAVSIM]]
- [[ClosedLoopAutonomousDriving]]
- [[MetricEvaluation]]
