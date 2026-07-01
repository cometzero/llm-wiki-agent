---
title: "MuJoCo"
type: entity
tags: [simulation, physics-engine]
sources: ["object-centric-residual-rl-vla-enhancement-2606-18953"]
last_updated: 2026-07-01
---

## Description
MuJoCo는 본 논문에서 paired sim/real VLA training을 위한 physics simulation environment이다. Real teleop demo를 replay하여 sim VLA를 학습하고, simulation에서 residual TD3 policy를 학습한 후 zero-shot으로 [[FR3]]에 배포한다.

## Connections
- [[ObjectCentricResidualRL]] — simulation environment
- [[FR3]] — real robot counterpart
- [[TD3]] — residual policy training in simulation
