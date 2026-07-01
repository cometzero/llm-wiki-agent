---
title: "NAVSIM (Navigation Simulation)"
type: concept
tags: [benchmark, autonomous-driving, closed-loop, evaluation]
sources: [qwen-robotnav-2606-18112]
last_updated: 2026-07-01
---

## Summary
NAVSIM is a closed-loop autonomous driving evaluation benchmark. Qwen-RobotNav reports 91.4 PDMS (close to human 94.8) on NAVSIM navtest. It evaluates Navigation Compliance, Drivable Area Compliance, Time-to-Collision, Comfort, Ego Progress, and overall PDMS.

## Metrics
- **PDMS** (Planning Disengagement Metric Score): Overall driving quality
- Navigation Compliance: Following route commands
- Drivable Area Compliance: Staying within drivable regions
- Time-to-Collision (TTC): Safety metric
- Comfort: Smoothness of trajectory
- Ego Progress: Distance toward goal

## Note
NAVSIM is a closed-loop planner metric. Paper notes safety validation for real-world road deployment is separate.

## Connections
- [[Qwen-RobotNav]] — evaluated on NAVSIM (91.4 PDMS)
- [[OnDeviceInference]] — edge deployment relevance
- [[Benchmark]] — general evaluation framework
