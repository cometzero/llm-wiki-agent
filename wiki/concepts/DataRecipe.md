---
title: "Data Recipe"
type: concept
tags:
  - data-engineering
  - embodied-ai
  - training-pipeline
  - scaling
last_updated: 2026-07-29
---

## 개요
`Data Recipe`는 하나의 모델 성능을 위해 heterogeneous data source를 어떤 비율, 어떤 우선순위, 어떤 정렬 손실로 결합할지에 대한 실무 설계 규칙이다.

## 핵심 구성요소
- source mix: [[RealRobotData]], [[UMI]], egocentric/exocentric, [[Simulation]], general [[VisionLanguageModel]] data
- alignment objective: [[ActionSpaceAlignment]], [[GeometricAlignment]]
- cost/quality balance: 수집 비용, annotation 품질, 분포 이동, 재사용성
- 평가 스펙트럼: [[OpenLoop]] vs [[ClosedLoop]], 안전성, 실패/복구 커버리지

## 왜 지금 중요한가
일반 VLM pretraining 중심 전략은 semantic 성능을 빠르게 올리지만, embodied execution에서는 recipe가 없으면 성능이 폐루프 제약으로 손실될 수 있다.

## Open Questions
- 실패·복구 궤적을 recipe에 어떻게 포함할지
- tactile/접촉 신호를 합성/실측으로 보완할지
- embodiment 간 re-targeting 비용을 어떻게 낮출지
- 드문 사건 데이터의 분포 보강 여부

## Related
- [[DataPyramidForEmbodiedManipulation]]
- [[ActionSpaceAlignment]]
- [[GeometricAlignment]]
- [[CrossEmbodimentLearning]]