---
title: "Capacity"
type: concept
tags: [ai-ml-learning]
 sources:
  - 2026-04-29-day07-ai-ml-learning-review
last_updated: 2026-04-29
---

## Summary
[[Capacity]]는 모델이 가질 수 있는 [[HypothesisSpace]]의 크기와 복잡성으로, 데이터의 패턴을 얼마나 복잡하게 표현할 수 있는지를 나타낸다. 대체로 매개변수 수, 계층 수, 은닉 차원, [[Attention]] 헤드 수 같은 설계 요소가 용량에 영향을 준다.

## Key Points
- capacity가 낮으면 복잡한 규칙을 놓쳐 [[Underfitting]]이 발생한다.
- capacity가 너무 높으면 훈련 데이터의 noise까지 맞추는 [[Overfitting]]이 커질 수 있다.
- 좋은 모델은 문제에 맞는 capacity와 적절한 [[Regularization]]·데이터 품질 조합을 갖는다.
- capacity는 표현 가능성의 상한을 다루는 반면, 실제 성능은 최적화, 데이터, 편향, regularization이 함께 좌우한다.

## Key Claims
- 같은 문제라도 [[InductiveBias]]가 맞는 구조와 결합한 capacity는 일반화 성능이 더 안정적이다.
- capacity는 무조건 높을수록 좋은 것이 아니며, [[Generalization]] 신호와 함께 판단해야 한다.

## Connections
- [[HypothesisSpace]]
- [[Expressivity]]
- [[InductiveBias]]
- [[Overfitting]]
- [[Underfitting]]
- [[Regularization]]
- [[LLM]]
- [[Transformer]]

## See also
- [[ModelCapacity]] (동일 주제 맥락에서 하위 논의를 정리할 수 있는 보조 페이지)
