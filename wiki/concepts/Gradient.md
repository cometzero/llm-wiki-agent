---
title: "Gradient"
type: concept
tags: [ml, optimization, training]
sources: [2026-04-23-day01-ai-ml-learning-review]
last_updated: 2026-04-25
---

[[Gradient]]는 손실이 각 파라미터 방향으로 얼마나 변하는지 나타내는 벡터다. 학습은 보통 이 정보를 이용해 [[LossFunction]]을 줄이는 방향으로 진행된다.

## Connections
- [[LossFunction]] — gradient가 계산되는 기준 함수
- [[Norm]] — gradient 크기 측정과 안정화에 사용됨
- [[GradientNormClipping]] — exploding gradient를 억제하는 대표 기법
- [[LLM]] — 대규모 모델 학습에서 gradient 안정화가 중요함
