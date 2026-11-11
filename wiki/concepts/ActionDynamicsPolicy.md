---
title: "Action Dynamics Policy"
type: "concept"
tags: ["VLA", "robotics", "continuous-control"]
sources: ["ode-policy-2611-01729-paper-ko", "ode-policy-2611-01729-analysis", "ode-policy-2611-01729-learning", "ode-policy-2611-01729-references"]
last_updated: "2026-11-11"
---

# Action Dynamics Policy
Command a를 직접 예측하지 않고 condition z·측정 상태 s와 현재 command a에서 변화율 f(a,s,z)를 구한 뒤 physical time에 적분하는 policy parameterization. [[ODEPolicy]]가 대표 예다.

## 구분
- Environment/state dynamics 모델과 달리 적분 상태는 desired command다.
- Diffusion/flow의 generation time과 physical execution time은 별개다.
- Seamless chunking은 직전 desired command를 보존한다. Measured state를 버리는 것이 아니라 field condition으로 사용한다.
- Multi-modal behavior에는 chunk별 sampled offset 등 별도 설계가 필요하다.

## 경계
연속 command는 global contraction, bounded jerk, robot tracking stability나 collision safety를 자동 보장하지 않는다. Chunk 내부 condition freshness·discrete events·rate conversion·reset semantics를 따로 검증한다.

## Sources
- [[ode-policy-2611-01729-analysis]]
- [[ode-policy-2611-01729-learning]]
