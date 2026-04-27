---
title: "Objective"
type: concept
tags: [optimization, objective-function, learning]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Objective는 모델이 학습 과정에서 최적화해야 할 목표 함수를 뜻한다. 보통에는 작을수록 좋은 방향으로 정의해 최소화 형태로 쓰고, 경우에 따라는 reward를 키우는 최대화 형태로 쓰기도 한다.

## Key Claims
- [[Objective]]는 특정 parameter 집합이 얼마나 좋은 성능을 내는지 수치화한 함수다.
- 최적해 표기는 보통 \(J(\theta)\) 또는 \(L(\theta)\)와 같이 쓰며, \(\theta^* = \arg\min_{\theta} J(\theta)\) 또는 \(\arg\max\) 형태로 정의한다.
- [[MachineLearning]]은 사실상 [[Optimization]] 문제로, 목표 함수를 정하고 그 함수를 낮추거나 높이는 방향으로 [[Parameter]]를 갱신하는 과정이다.
- 실전에서는 [[Regularization]] 항을 추가해 단순 적합 손실보다 안정적 목적값으로 확장한다.

## Connections
- [[Optimization]], [[EmpiricalRisk]], [[EmpiricalRiskMinimization]], [[SurrogateLoss]], [[Constraint]], [[Regularization]], [[GradientDescent]], [[Argmin]]

## Related Concepts
- [[LossFunction]]는 보통 Objective를 구성하는 한 요소이다.
- [[LLM]], [[LinearRegression]], [[Classification]] 모두 문제 특성에 맞는 Objective를 가진다.
