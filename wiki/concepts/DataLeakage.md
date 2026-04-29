---
title: "DataLeakage"
type: concept
tags: [ai-ml-learning]
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[DataLeakage]]는 학습 시 알지 말아야 할 정보가 훈련/검증/테스트에 새어 들어와 성능 추정이 과도하게 좋아 보이는 현상이다.

## Key Points
- 미래 정보를 feature에 넣는 경우 가장 대표적인 leakage이다(예: 타임 시계열에서 미래 타깃 노출).
- 분할 규칙이 어긋나면 모델이 분포별 특성이나 사용자 식별 정보를 통해 간접적으로 시험 데이터를 이용한다.
- [[BenchmarkContamination]]은 유사한 평가 누수 유형의 특수 사례다.

## Connections
- [[TrainValidationTestSplit]]
- [[TestSet]]
- [[ValidationSet]]
- [[Generalization]]
- [[DistributionShift]]
- [[Overfitting]]
