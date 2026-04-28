---
title: "Divergence"
type: concept
tags: [optimization, training-stability]
sources: [2026-04-28-day06-ai-ml-learning-review]
last_updated: 2026-04-28
---

## Summary
[[Divergence]]는 학습 중 파라미터 업데이트가 발산해 [[LossFunction]]이 줄지 않고 커지거나 수치가 폭주하는 상태다. [[LearningRate]]가 과도하게 크거나, gradient 스케일이 과도한 경우 자주 나타난다.

## Typical Symptoms
- loss가 반복적으로 급증
- 값이 `NaN`으로 터짐
- 학습이 오히려 불안정해져 출력 품질이 급격히 악화

## Distinction
[[Divergence]]는 Oscillation과 다르다. Oscillation이 최적점 주변을 왔다 갔다 하는 현상이라면, [[Divergence]]는 안정 궤도를 벗어나 멀어지는 추세다.

## Causes in Practice
- 과도한 [[LearningRate]]
- GradientExplosion 성향이 큰 구간
- 데이터 정규화 문제, 버그, 학습률 스케줄 미설정
- 불안정한 [[Optimizer]] 설정

## Mitigations
- [[LearningRate]] 감소
- [[LearningRate]] schedule 적용
- [[Optimizer]] 전환(예: [[Adam]], AdamW)
- [[GradientNormClipping]], 정규화, 배치 안정성 점검