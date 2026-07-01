---
title: "NAVSIM"
type: entity
tags: [benchmark, autonomous-driving, navigation]
sources: [qwen-robotnav-2606-18112, qwen-robotnav-2606-18112-learning]
last_updated: 2026-07-01
---

# NAVSIM

[[NAVSIM]] is a closed-loop autonomous driving benchmark that evaluates navigation models using the PDMS (PDM Score) metric, which combines progress, safety, and rule compliance.

## Key Metrics
- PDMS: Composite metric combining progress/safety/rule compliance
- Evaluates closed-loop autonomous driving performance
- Includes TTC (Time-To-Collision), drivable area compliance

## Connection to Qwen-RobotNav
[[QwenRobotNav]] achieves 91.4 PDMS on NAVSIM benchmark.

## Related Concepts
- [[ClosedLoopAutonomousDriving]]
- [[PDMS]]
