---
title: "Hypothesis Space"
type: concept
tags: [machine-learning, model-capacity]
sources: [2026-04-25-day03-ai-ml-learning-review]
last_updated: 2026-04-26
---

## Definition
[[HypothesisSpace]]는 모델이 선택할 수 있는 후보 함수들의 집합이다. 학습은 이 집합 내부에서 데이터에 가장 적합한 함수를 고르는 과정으로 본다.

## Why it matters
- 후보 집합이 너무 작으면 bias가 크고(표현력 부족), 너무 크면 variance가 커져 과적합 위험이 증가한다.
- [[MachineLearning]]에서 [[LossFunction]] 최적화는 사실상 `어떤 함수가 가설 집합에서 가장 잘 맞는가`를 찾는 것이다.

## Related Concepts
- [[LossFunction]] — 후보 선택을 위한 평가 지표
- overfitting — [[HypothesisSpace]]가 너무 넓을 때 발생 가능
- [[Regularization]] — 탐색 공간의 안정화 장치
- model capacity — 표현력 규격의 상위 개념
- [[RepresentationLearning]] — 동일 작업에 대한 유효한 가설 공간 재설계

## Source Alignment
- 본 source에서 선형회귀/트리/뉴럴넷/트랜스포머를 각각 서로 다른 가설 공간으로 예시해 같은 문제의 다른 근사 전략을 제시한다.

## Notes
- 이 개념은 Day03의 [[MachineLearning]] 흐름에서 [[FunctionApproximation]]과 쌍으로 이해될 때 가장 명확해진다.

## Possible Conflicts
- No explicit contradiction found with existing wiki pages.