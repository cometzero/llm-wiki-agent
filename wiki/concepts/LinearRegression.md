---
title: "Linear Regression"
type: concept
tags:
  - ai-ml
  - optimization
  - regression
  - supervised-learning
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Linear Regression은 입력 특성과 출력 간의 관계를 선형 결합으로 근사해 연속값을 예측하는 고전 지도 학습 방법이다.

모델은 일반적으로 `\hat{y}=wx+b` 또는 다변량 형태 `\hat{y}=W\mathbf{x}+b`로 표현되며, 목적은 예측 오차를 줄이는 것이다.

## Core Idea
- 선형 가정: 각 feature의 영향이 가중치로 선형적으로 합산된다.
- 학습: [[LossFunction]] 또는 [[MSE]]/[[LeastSquares]] 기반으로 파라미터 `w,b`를 조정한다.
- 해석성: 결과 계수 `w`와 `b`가 입력별 영향도를 직관적으로 보여 준다.

## Key Claims
- 선형회귀는 분류보다 기본적으로 연속값 예측에 적합하다.
- 오차는 단순 합산보다 제곱합(또는 평균 제곱합)으로 누적하는 경우가 일반적이다.
- 규모가 크고 모델이 복잡한 경우에는 [[GradientDescent]] 또는 다른 최적화기로 손실을 줄인다.

## Connections
- [[LeastSquares]]: 대표 손실 기준.
- [[MSE]]: 평균 제곱 오차 표현.
- [[Residual]]: 실제값과 예측값의 차이.
- [[GradientDescent]]: 파라미터 학습의 반복 최적화.
- [[LLM]]: 네트워크 내부의 [[DenseLayer]]와 내적 기반 연산의 기본 뼈대.

## Notes
- [[LinearRegression]]은 [[MachineLearning]]의 문법적 출발점이자 딥러닝의 기본 계산 구조 해석에 유효하다.