---
title: "GeneralizationGap"
type: concept
tags: [ai-ml-learning]
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[GeneralizationGap]]은 훈련 성능과 미보지 못한 데이터 성능 사이 차이를 뜻한다. 손실 기준이면 `validation loss - train loss`, 정확도 기준이면 `train accuracy - test accuracy`로 표현한다.

## Key Interpretation
- gap이 크면 과적합 신호일 수 있다.
- gap이 작아도 성능이 모두 낮으면 [[Underfitting]]일 수 있다.
- gap 진단은 과적합뿐 아니라 데이터 분할 오염, 분포 이동의 힌트를 제공한다.

## Connections
- [[TrainLoss]]
- [[ValidationLoss]]
- [[TrainSet]]
- [[TestSet]]
- [[Overfitting]]
- [[Underfitting]]
- [[DistributionShift]]
