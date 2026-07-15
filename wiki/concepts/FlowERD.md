---
title: "Flow-ERD"
type: concept
tags: [traffic-simulation, flow-matching, closed-loop, distillation]
sources: [flow-erd-2607-06957]
last_updated: 2026-07-15
---

# Flow-ERD

## Overview
Flow-ERD는 [[FlowMatching]] 기반의 multi-agent traffic simulator로, agent-type별 kinematics와 entropy-regularized distillation을 결합하여 realism-diversity trade-off를 완화한다. E2E AD/VLA policy의 world model/evaluator 역할.

## Architecture
```
Scene History + Map/Context → Agent-Type Aware Flow Matching → Continuous Action Samples
                                                                              ↓
                                              Type-specific Kinematic Transition
                                                                              ↓
                                                         Closed-loop Multi-agent Rollout
                                                                              ↓
                                              Entropy-Regularized Distillation (ERD)
                                                                              ↓
                                                    Realistic + Diverse Traffic Simulator
```

## Key Components
1. **AFM (Agent-Type Aware Flow Matching)**: vehicle/cyclist/pedestrian type-specific state transition
2. **Transition-consistent action target**: kinematic feasibility 보장
3. **Entropy-Regularized Distillation**: reverse-KL divergence 기반 closed-loop 보정

## VLA Taxonomy Position
- **World Model / Traffic Simulator**: E2E AD/VLA policy의 closed-loop 평가 환경
- **Closed-loop Evaluation Infrastructure**: VLA policy의 robustness, diversity, deployment 가능성 평가

## Connections
- [[ABot-N1]] — policy(model) vs evaluator(simulator) 보완 관계
- [[VLA-Corrector]] — closed-loop action 보정 접근법, 다른 레벨에서 동일 문제 해결
- [[WorldActionModel]] — WAM의 evaluator/traffic simulation 차원
- [[NVIDIA OmniDreams]] — closed-loop driving simulation 관련, video generation vs flow matching 차이
