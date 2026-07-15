---
title: "Covariate Shift in Closed-Loop Simulation"
type: concept
tags: [simulation, distribution-shift, closed-loop]
sources: [flow-erd-2607-06957]
last_updated: 2026-07-15
---

## Overview
Closed-loop simulation에서 발생하는 covariate shift는 모델의 예측이 다음 timestep의 입력 distribution을 바꾸어, open-loop 학습 분포와 rollout 분포 사이에 불일치가 생기는 현상입니다.

## 문제
- Open-loop 학습 시점의 distribution과 closed-loop rollout 시점의 distribution이 상이
- 모델 예측이 누적됨에 따라 drift 발생
- Realism 저하로 이어짐

## Flow-ERD의 해결책
ERD(Entropy-Regularized Distillation)에서 reverse-KL objective를 사용하여 closed-loop rollout distribution을 teacher/reference distribution과 맞추되, entropy regularization으로 높은 density mode로의 붕괴를 방지합니다.

## Connections
- [[FlowERD]] — 해결책 제시
- [[MultiAgentSimulation]] — 발생하는 domain
- [[ModeCollapse]] — 관련 문제
