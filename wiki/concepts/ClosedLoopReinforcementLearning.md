---
title: "Closed-Loop Reinforcement Learning"
type: concept
tags: [reinforcement-learning, autonomous-driving, robotics, policy-learning]
sources: [drivezero-2609-06055-paper-ko, drivezero-2609-06055-analysis, drivezero-2609-06055-learning]
last_updated: 2026-09-16
---

## Overview
Closed-loop reinforcement learning trains a policy on state transitions caused by its own actions rather than only fixed expert trajectories. In autonomous driving this requires an interactive simulator or real environment whose background actors, vehicle dynamics, safety events and goals continue to evolve after each ego action.

## Design Requirements
- The world model/simulator must react plausibly to ego interventions; pure log replay alone has limited counterfactual coverage.
- Reward must balance hard safety constraints, route completion and driving quality without making unsafe reward hacks attractive.
- Evaluation should separate reactive and non-reactive traffic, open-loop proxy metrics and actual closed-loop rollout.

## Constraints
Closed-loop optimization removes neither simulator bias nor privileged-observation transfer gap. Deployment still needs perception uncertainty handling, rule validation, latency bounds and conservative fallback.

## Connections
- [[DriveZero]] — privileged mixed-agent PPO teacher.
- [[VLA]] — interactive action grounding also matters for language-conditioned policies.
