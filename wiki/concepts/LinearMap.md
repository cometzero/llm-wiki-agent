---
title: "LinearMap"
type: concept
tags: [linear-algebra, llm]
last_updated: 2026-04-26
sources: [2026-04-23-day01-ai-ml-learning-review]
---

## 핵심 정의
[[LinearMap]]은 한 벡터공간에서 다른 벡터공간으로 벡터를 보내는 함수로, 덧셈과 스칼라배를 보존한다.

## 핵심 수식
- `f(x + y) = f(x) + f(y)`
- `f(a x) = a f(x)`

## AI/ML 연결
- 신경망의 [[Matrix]] 곱(예: `W x`)은 [[LinearMap]]로 해석할 수 있다.
- [[DenseLayer]], [[Attention]]의 Q/K/V 투영, 선형 프로젝션은 모두 선형변환 구성이다.
- [[LLM]] 내부에서는 표현 공간에서 표현 공간으로의 변환을 단계적으로 수행한다.

## 관련 개념
- [[VectorSpace]]
- [[Matrix]]
- [[Rank]]
- linear transformation
