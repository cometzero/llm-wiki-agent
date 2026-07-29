---
title: "Receding Horizon"
type: concept
tags:
  - control
  - closed-loop
  - planning
  - action-chunk
last_updated: 2026-07-29
---

[[RecedingHorizon]] 제어는 긴 시계열 action plan(예: 7-step chunk)을 한 번에 예측한 뒤 일부만(예: 3-step) 실행하고, 새 관측에 기반해 다음 계획을 다시 계산하는 폐루프 운영 방식이다.

## 핵심 개념

- 긴 horizon plan의 장점을 유지하면서, 실행-관측-재계획 루프로 오차 누적을 제어한다.
- [[WorldDiT]] 계열에서 action chunk generation의 누적 오차를 관리하는 핵심 패턴으로 사용된다.
- [[Model-PredictiveControl]]과 같은 반복 최적화형 제어 사고와 결합된다.

## 장점

- 안정성-성능 trade-off를 조절하기 쉬움
- 환경 변화와 예측 오차에 대한 회복탄력성 강화
- temporal ensembling으로 추가 안정화 가능

## 주의점

- chunk 길이/실행 길이(예: 7-step predict / 3-step execute)의 조합은 task 성질에 따라 민감하게 조정되어야 한다.
- 재계획 지연(latency)과 sensing jitter가 제어 품질에 직접 영향을 준다.

## 관련 링크

[[WorldDiT]], [[ActionChunking]], [[WorldActionModel]], [[ClosedLoopPlanning]], [[Model-PredictiveControl]], [[LIBERO]]