---
title: "DriveZero"
type: concept
tags: [autonomous-driving, end-to-end, closed-loop-rl, trajectory-planning]
sources: [drivezero-2609-06055-paper-ko, drivezero-2609-06055-analysis, drivezero-2609-06055-learning]
last_updated: 2026-09-16
---

## Overview
DriveZero는 privileged structured-state policy인 DriveRL의 closed-loop RL behavior를 multi-view camera-only trajectory planner로 distill하는 end-to-end autonomous-driving system이다. Perception은 multiple vision foundation model distillation, action은 mixed-agent PPO training으로 분리한다.

## Core Mechanism
- DriveRL은 ego/agent/map/light/goal structured state에서 jerk·steering-rate를 낸다.
- DriveVFM은 DINOv3, SigLIP2, SAM, Depth Anything V2의 feature를 driving representation으로 압축한다.
- DriveZero는 4-view image·ego state·command로 multi-proposal trajectory 및 quality score를 예측한다.

## Constraints
Teacher의 privileged state, simulator traffic response, reward/critic calibration과 pseudo closed-loop benchmark는 실제 차량의 end-to-end safety guarantee를 대체하지 않는다.

## Connections
- [[ClosedLoopReinforcementLearning]] — behavioral supervision source.
- [[VLA]] — representation-to-executable-action grounding의 비교 계열.
