---
title: "Compounding Error"
type: concept
tags: [robotics, imitation-learning, vla]
sources: ["object-centric-residual-rl-vla-enhancement-2606-18953"]
last_updated: 2026-07-01
---

## Definition
Compounding error는 [[ImitationLearning]] 기반 [[VLA]]가 sequential decision에서 각 step의微小한 오차가 누적되어 최종 task 실패로 이어지는 현상이다. 특히 precise contact, grasp, placement task에서 문제가 된다.

## This Paper's Solution
Object-centric residual RL로 frozen VLA action에 corrective residual을 더해 precision recovery를 달성한다. Base VLA는 open-loop imitation으로 학습되고, residual은 closed-loop RL로 task success를 직접 optimize한다.

## Connections
- [[VLA]] — affected policy type
- [[ObjectCentricResidualRL]] — solution
- [[ImitationLearning]] — root cause
- [[ClosedLoopControl]] — residual's optimization approach
