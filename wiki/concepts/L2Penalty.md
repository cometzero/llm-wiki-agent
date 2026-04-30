---
title: "L2 Penalty"
type: concept
tags:
  - regularization
  - optimization
  - deep-learning
sources:
  - 2026-04-30-day08-ai-ml-learning-review
last_updated: 2026-04-30
---

## Summary
[[L2Penalty]]는 가중치 제곱 합에 대한 벌점을 주어 과도한 가중치 크기를 억제하는 정규화 방식이다. 딥러닝에서 [[WeightDecay]]와 가장 밀접하게 대응한다.

## Formula
`L2 penalty = w1² + w2² + ...`

예: w=[3, -4]일 때 penalty = 25.

## Intuition
- 큰 가중치에 비례해 강한 패널티 부여
- 매끄러운 예측 함수 선호
- 폭주/불안정한 경향 완화

## Practical implication
- 널리 사용되는 default형 정규화 중 하나
- 단점: 진짜 희소성(완전한 0) 유도보다 크기 감소에 유리

## Related
- [[L1Penalty]]
- [[WeightDecay]]
- [[Regularization]]
- [[Generalization]]

## References in this wiki
- [[2026-04-30-day08-ai-ml-learning-review]]