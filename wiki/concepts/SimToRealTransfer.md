---
title: "Sim-to-Real Transfer"
type: concept
tags: [robotics, transfer-learning, simulation]
sources: ["object-centric-residual-rl-vla-enhancement-2606-18953"]
last_updated: 2026-07-01
---

## Definition
Sim-to-real transfer는 simulation에서 학습한 정책을 real robot에 배포하는 과정이다. 주요 challenge는 sim/real gap이다.

## This Paper's Approach
- **Object pose abstraction**: raw visual gap 대신 object 6-DoF pose 사용
- **Paired training**: 같은 teleop action으로 sim/real VLA를 paired 학습
- **Robustness training**: pose noise/dropout으로 pose estimator error에 robust하게 학습
- **Zero-shot**: real robot fine-tuning 없음

## Connections
- [[ObjectCentricResidualRL]] — zero-shot approach
- [[ImageBasedSimToReal]] — traditional visual gap approach
- [[VLA]] — base policy
- [[PoseEstimation]] — abstraction mechanism
