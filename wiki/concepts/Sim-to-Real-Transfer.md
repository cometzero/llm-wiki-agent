---
title: "Sim-to-Real Transfer"
type: concept
tags: [robotics, domain-adaptation, simulation]
sources: [object-centric-residual-rl-vla-enhancement-2606-18953-references, object-centric-residual-rl-vla-enhancement-2606-18953]
last_updated: 2026-07-01
---

## Definition
Sim-to-Real(S2R) transfer는 simulation에서 학습한 policy를 실제 로봇에 배포하는 과정이며, domain gap을 극복하는 것이 핵심 과제이다.

## Key Challenges
1. Visual gap — simulator rendering vs real camera
2. Physics gap — simulator dynamics vs real world
3. Action noise and latency

## Methods
- [[ResidualRL]] — Sim policy의 residual을 real 환경에서 보정
- [[SAM2]] — Real-time object segmentation으로 perception 일관성 확보
- Domain randomization

## Connections
- [[VLA]] — S2R의 대상 모델
- [[ResidualRL]] — S2R gap을 줄이는 핵심 방법론
- [[PhysicalIntelligence]] — [[Pi06]]에서 zero-shot sim-to-real 연구
