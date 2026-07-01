---
title: "FR3 Robot"
type: entity
tags: [robot, hardware]
sources: ["object-centric-residual-rl-vla-enhancement-2606-18953"]
last_updated: 2026-07-01
---

## Description
FR3는 본 논문의 zero-shot sim-to-real 실험에 사용된 real robot platform이다. [[VLA]] + [[ResidualRL]] 기반 residual correction이 적용되어 [[MuJoCo]] simulation에서 학습된 정책을 fine-tuning 없이 real world에 직접 배포한다.

## Connections
- [[ObjectCentricResidualRL]] — deployment target
- [[VLA]] — base policy
- [[MuJoCo]] — paired simulation environment
- [[ResidualRL]] — correction methodology
