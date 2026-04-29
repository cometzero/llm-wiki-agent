---
title: "TestSet"
type: concept
tags: [ai-ml-learning]
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[TestSet]]는 최종 모델 성능을 평가하는 데 쓰는 보류 데이터다. 훈련 과정에 관여시키지 않아야 한다는 점이 핵심이다.

## Key Points
- 학습과 하이퍼파라미터 튜닝에서 독립적으로 유지되어야 한다.
- 반복 열람은 [[DataLeakage]] 또는 간접 튜닝 효과를 유발한다.
- 최종 보고용 성능은 [[OutOfSample]] 성능의 근사로 간주한다.

## Connections
- [[TrainValidationTestSplit]]
- [[Generalization]]
- [[DataLeakage]]
- [[GeneralizationGap]]
