---
title: "Jacobian"
type: concept
tags: [calculus, optimization, multivariate]
last_updated: 2026-04-26
sources: [2026-04-26-day04-ai-ml-learning-review]
---

## Summary
[[Jacobian]]은 벡터값 함수의 미분을 행렬 형태로 정리한 것으로, 각 출력 성분을 각 입력 성분에 대해 편미분한 값으로 구성된다. 이는 스칼라 손실의 [[Gradient]]가 다변수 벡터값 함수로 일반화된 형태이다.

## Key Claims
- [[Jacobian]]은 각 출력 차원에 대한 [[PartialDerivative]]를 모아 만든 미분 행렬이다.
- [[ChainRule]]을 다변수/벡터 맥락에서 적용할 때 Jacobian 곱셈으로 국소 선형 변환을 연결한다.
- 딥러닝에서 레이어 간 민감도 전달이나 역전파의 중간 단계 설명에 쓰인다.

## Relation
- [[ComputationalGraph]] — 각 노드의 국부적 미분을 Jacobian 또는 local derivative로 본다.
- [[Backpropagation]] — [[BackwardPass]]에서 chain rule로 Jacobian 전파가 반복된다.
- [[Autograd]] — 자동 미분은 Jacobian/Gradient 계산을 그래프 기반으로 수행한다.