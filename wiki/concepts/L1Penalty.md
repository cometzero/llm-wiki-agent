---
title: "L1 Penalty"
type: concept
tags:
  - regularization
  - statistics
  - feature-selection
sources:
  - 2026-04-30-day08-ai-ml-learning-review
last_updated: 2026-04-30
---

## Summary
[[L1Penalty]]는 가중치 크기에 대한 벌점을 절댓값 합으로 부과해 일부 가중치를 0에 가깝게 만들며, feature 선택과 희소화에 유리한 정규화 방식이다.

## Formula
`L1 penalty = |w1| + |w2| + ...`

예: w=[3, -4]일 때 penalty = 7.

## Intuition
- 작은 가중치를 유지
- 불필요한 feature를 거의 0으로 줄임
- 모델을 간결화

## Practical implication
- feature가 매우 많은 문제에서 의미가 큼
- 실제로는 완전한 zero-out이 강하면 해석성이 좋아질 수 있으나, 과도한 사용은 성능 저하 가능

## Related
- [[L2Penalty]]
- [[Regularization]]
- [[WeightDecay]]
- [[FeatureAnalysis]]

## References in this wiki
- [[2026-04-30-day08-ai-ml-learning-review]]