---
title: "Paired Sim/Real Training"
type: concept
tags: [robotics, training, simulation]
sources: ["object-centric-residual-rl-vla-enhancement-2606-18953"]
last_updated: 2026-07-01
---

## Definition
Paired sim/real training은 동일한 teleoperation action을 reality와 simulation 양쪽에 적용하여 base VLA failure mode를 맞추는 기법이다. 이를 통해 sim에서 학습한 residual policy가 real 환경에서도 효과적으로 작동할 수 있게 한다.

## Pipeline
1. Teleop demo 수집 (real)
2. Real VLA training (imitation)
3. Same actions replayed in simulation
4. Sim VLA training (paired)
5. Simulation-only residual TD3 training

## Connections
- [[ObjectCentricResidualRL]] — main application
- [[VLA]] — both real and sim versions
- [[MuJoCo]] — simulation environment
- [[TD3]] — residual policy in simulation
