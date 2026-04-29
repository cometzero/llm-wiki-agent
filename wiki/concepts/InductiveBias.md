---
title: "InductiveBias"
type: concept
tags: [ai-ml-learning]
sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[InductiveBias]]는 모델이 학습 전부터 갖는 가정/우선순위다. 즉 어떤 함수 형태를 더 선호하고 어떤 구조를 더 쉽게 채택하는지의 모델 고유 성향이다.

## Key Points
- [[LinearRegression]]은 선형 관계를 선호하는 bias를 갖는다.
- [[CNN]]은 지역적 상관성과 평행 이동 불변성 같은 image-specific bias를 반영한다.
- [[Transformer]]는 토큰 간 관계를 attention으로 동적으로 추출하는 구조적 bias를 갖는다.
- 데이터가 제한적일 때 적절한 inductive bias는 오히려 일반화에 도움이 된다.

## Connections
- [[HypothesisSpace]]
- [[Capacity]]
- [[Generalization]]
- [[Regularization]]
- [[Transformer]]
- [[CNN]]
- [[LinearRegression]]
