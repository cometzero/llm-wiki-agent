---
title: "Weight Decay"
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
[[WeightDecay]]는 학습 과정에서 파라미터(특히 [[Parameter]] 가중치)의 크기를 줄이도록 유도해 [[Overfitting]]을 억제하는 정규화 기법이다.

## Definition
옵티마이저 단계에서 weight가 커지는 방향을 완만하게 막거나 감쇠시키는 형태로 구현한다. 딥러닝에서는 [[L2Penalty]]와 동형성이 자주 논의된다.

## Core role
- 큰 가중치에 의한 과한 민감도 완화
- 일반화 성능 개선
- [[GeneralizationGap]] 감소 유도

## Notes
- 현대 딥러닝에서는 [[AdamW]] 같은 방식이 [[WeightDecay]]를 손실 함수 penalty와 분리해 적용한다는 점이 중요.
- 강도가 너무 크면 모델이 필요한 규칙까지 못 배우는 [[Underfitting]]로 갈 수 있다.

## Related
- [[Regularization]]
- [[L2Penalty]]
- [[AdamW]]
- [[ModelComplexity]]

## References in this wiki
- [[2026-04-30-day08-ai-ml-learning-review]]