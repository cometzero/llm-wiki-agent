---
title: "Goal Predicate Evaluation"
type: concept
tags: [evaluation, closed-loop, physical-agency, constraints]
sources: [worldleague-2611-30989-paper-ko, worldleague-2611-30989-analysis, worldleague-2611-30989-learning]
last_updated: 2026-11-25
---

# Goal Predicate Evaluation

[[WorldLeague]]의 평가 방식에서 핵심은 timestamped trajectory에 대해 원하는 결과와 수행 제약을 검사하는 것이다. Natural-language goal을 item별 predicate로 분해하고 partial progress와 complete success를 따로 보고한다.

## Metric

Interactive Score는 각 task의 item progress p_j를 평균해 100을 곱한다. Physical success는 모든 goal predicate와 constraint가 성립할 때만 1이다. 그러므로 I=100도 constraint 위반 시 S=0이다. Task 평균을 dimension/overall에서 동등 가중하며 item-pooling과 다르다.

## Diagnostic Meaning

물체의 destination 도달과 release 후 stability, 이전 scene의 정확한 보고와 그 identity에 근거한 delivery, stopped-command 뒤 재이동과 원래 장애 해결을 각각 구분한다. Terminal QA나 agent의 DONE, controller의 completed receipt를 외부 성공 검증 대신 쓰지 않는다.

## Boundaries

[[ClosedLoopEvaluation]]의 finite simulation predicate 통과는 real-world safety certificate가 아니다. Predicate coverage·threshold·initially-satisfied control task·robot/interface 차이·seed sensitivity가 결과 해석에 필요하다. AD 전이는 goal/constraint·timing을 새로 정의해야 하는 분석 제안이며 원문의 실차 검증이 아니다.

## Connections
- [[VisionLanguageAction]] — executable policy의 outcome 평가.
- [[MotorMind]] — runtime harness와 실행 검증의 접점.
- [[Echo]] — internal status signal과 independent goal success의 구분.
- [[worldleague-2611-30989-learning]] — progress/constraint·weighting·time-window toy.
