---
title: "LearningRate"
type: concept
tags: [optimization, gradient-descent]
last_updated: 2026-04-26
sources: [2026-04-26-day04-ai-ml-learning-review]
---

## Summary
[[LearningRate]]는 [[GradientDescent]]에서 파라미터 업데이트 크기를 조절하는 하이퍼파라미터다. 너무 크면 발산, 너무 작으면 학습이 지나치게 느려진다.

## Key Claims
- 업데이트는 보통 `\(\theta_{t+1} = \theta_t - \alpha \nabla L\)` 형태이며 \(\alpha\)가 학습률이다.
- 학습률은 수렴 속도, 안정성, 최적점 근접성에 직접 영향한다.
- 스케줄링(감쇠/워밍업/사이클)과 결합하면 초기 탐색과 후반 미세조정이 균형을 이룬다.

## Relation
- [[GradientDescent]] — 학습률이 스텝 크기를 결정.
- [[VanishingGradient]]/[[ExplodingGradient]] — 적절한 학습률 설정으로 완화 가능.
- [[Optimization]] — 학습 하이퍼파라미터 조정의 핵심 변인.