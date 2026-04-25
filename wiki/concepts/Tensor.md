---
title: "Tensor"
type: concept
tags: [ml, deep-learning, data-structure]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-25
---

[[Tensor]]는 행렬의 일반화인 다차원 배열 표현이다. [[FeatureMatrix]]가 2차원 표현이라면 tensor는 배치·시퀀스·채널 축까지 함께 다룬다.

## Connections
- [[FeatureMatrix]] — tensor의 2차원 특수형
- [[TensorShape]] — 각 축의 의미와 크기를 읽는 규칙
- [[Embedding]] — 토큰 표현이 tensor shape 위에서 배치됨
- [[Attention]] — 시퀀스 tensor를 상호작용시키는 연산
