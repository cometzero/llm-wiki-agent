---
title: "Flow-ERD"
type: entity
tags: [traffic-simulation, multi-agent, autonomous-driving]
sources: [flow-erd-2607-06957]
last_updated: 2026-07-15
---

## Overview
Flow-ERD는 autonomous driving용 multi-agent traffic simulator로, Agent-Type Aware Flow Matching(AFM)과 Entropy-Regularized Distillation(ERD)를 결합하여 realistic하면서도 diverse한 traffic simulation을実現합니다.

## Key Components
1. **AFM (Agent-Type Aware Flow Matching)**: flow matching backbone으로 multi-modal action distribution 생성, type-specific kinematics로 physical motion 실행
2. **ERD (Entropy-Regularized Distillation)**: reverse-KL 기반 closed-loop distillation에 entropy regularization을 더해 mode collapse 방지

## Performance
- WOSAC benchmark에서 RMM 0.7840 달성
- UniMM, SMART, TrajTok 대비 Pareto frontier 지배

## Connections
- [[MultiAgentSimulation]]
- [[FlowMatching]]
- [[WorldActionModel]] — VLA/E2E AD policy 평가용 world simulator로 활용 가능
