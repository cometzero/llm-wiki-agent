---
title: "Multi-Agent Traffic Simulation"
type: concept
tags: [simulation, autonomous-driving, traffic]
sources: [flow-erd-2607-06957]
last_updated: 2026-07-15
---

## Overview
Multi-agent traffic simulation은 autonomous vehicle의 development와 validation을 위해 multiple traffic participants(vehicle, cyclist, pedestrian)의 realistic한 행동 생성하는 기술입니다. Ego vehicle의 planning policy 학습/평가 infrastructure로 활용됩니다.

## 핵심 과제
- **Realism-Diversity Trade-off**: 단일 logged future와 유사하면서도 다양한 alternative future 생성 필요
- **Covariate Shift**: closed-loop에서 모델 예측이 다음 입력 distribution을 바꿔 open-loop 학습 분포와 불일치 발생
- **Mode Collapse**: KL divergence 기반 방법이 dominant mode로 집중되는 경향

## Flow-ERD 해결책
1. **AFM**: Agent-type aware flow matching으로 type-specific kinematic constraints 적용
2. **ERD**: Entropy-regularized distillation으로 plausible modes 보존하면서 diversity 확보

## Connections
- [[FlowERD]] — 구현체
- [[WOSAC]] — benchmark
- [[CovariateShift]] — 주요 문제
- [[ModeCollapse]] — 주요 문제
