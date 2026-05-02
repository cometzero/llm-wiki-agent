---
title: "2026-05-02 AI/ML Learning Day 10"
type: source
tags:
  - diary
  - ai-ml-learning
  - linear-regression
  - logistic-regression
  - decision-boundary
  - least-squares
  - binary-classification
source_file: raw/ai_ml_learning/2026-05-02-day10-ai-ml-learning-review.md
sources:
  - 2026-05-02-day10-ai-ml-learning-review
date: 2026-05-02
last_updated: 2026-05-02
---

## Summary
Day 10은 고전 ML의 핵심 3개 단계를 다룬다: 수치 예측의 [[LinearRegression]], 이진 확률 분류의 [[LogisticRegression]], 그리고 모델이 class를 나누는 방식인 [[DecisionBoundary]]. 각 개념은 [[Loss]] 기반의 학습 목표를 동일한 뼈대로 연결한다.

첫째, [[LinearRegression]]은 입력-출력 관계를 직선/초평면 형태로 가정하고 [[LeastSquares]]로 오차를 측정해 [[Parameter]]를 학습한다. 둘째, [[LogisticRegression]]은 선형 점수에 [[Sigmoid]]를 씌워 확률(또는 확률처럼 쓰이는 값)로 바꾸고 [[BinaryClassification]] 문제를 푼다. 셋째, 두 모델 모두 실제로는 임계면에서 분류를 만들며, 이는 [[DecisionBoundary]]가 되는 지점이며, 선형 모델의 경우 [[Hyperplane]] 형태로 나타난다.

또한 이번 학습은 딥러닝과 연결해, LLM과 같은 복잡 모델도 내부에서 다수의 선형 변환([[DenseLayer]]), 확률 변환([[Logit]], [[Softmax]]류), 경계 형성 관점으로 이해할 수 있음을 강조한다.

## Key Claims
- [[LinearRegression]]은 `\hat{y}=wx+b` 같은 선형 함수로 연속값을 예측하는 기본 모델이며, [[Residual]]의 제곱합을 최소화하는 것이 기본 학습 기준이다.
- 제곱합을 최소화할 때 단순 합보다 큰 오차가 훨씬 큰 벌점으로 반영되므로 실제로는 큰 오차를 더 강하게 줄이게 유도된다.
- [[LogisticRegression]]은 이름과 달리 분류 중심이다. 먼저 선형 점수 `z=wx+b`를 만든 뒤 [[Sigmoid]]로 `0~1` 구간 값으로 바꾸어 분류 판단 및 확률해석을 수행한다.
- [[BinaryClassification]] 문제에서 로짓(`z`)은 raw score이고, sigmoid 출력은 확률 해석값이지만 항상 완전 보정(calibrated)되어야 하는 것은 아니다.
- [[DecisionBoundary]]는 모델이 class를 바꾸는 기준면이고, 선형 분류기는 기본적으로 `w^Tx+b=0` 형태의 경계를 만든다.
- [[LinearSeparability]]는 한 개의 선형 경계로 데이터가 완전히 분리되는 성질이며, 현실 데이터는 고차원 변환 없이 분리되지 않는 경우가 흔하다.
- 신경망은 여러 층의 비선형 변환을 통해 feature를 재표현해서 더 복잡한 경계를 만들 수 있으므로 선형 분리 불가능한 문제를 더 잘 다룰 수 있다.
- [[LogisticRegression]]의 학습 손실은 일반적으로 분류용의 [[CrossEntropy]] 계열이 적합하며, [[LinearRegression]]은 보통 [[MSE]] 계열이 기본이다.

## Key Quotes
> "residual을 그냥 더하면 양수 오차와 음수 오차가 서로 상쇄될 수 있다. 그래서 제곱해서 합한다." — Day 10 핵심 직관

> "logit은 sigmoid 이전의 raw score이고, sigmoid 출력이 0과 1 사이 확률처럼 보이는 값이다." — 로지스틱 회귀 핵심 구분

> "decision boundary는 모델이 직접 그리는 '여기는 클래스 A, 여기부터는 클래스 B' 선(또는 평면, 또는 고차원 경계)이다." — 분류 이해의 핵심

## Connections
- [[LinearRegression]]: 직선/평면 가정의 회귀 기본 모델.
- [[LeastSquares]]: residual의 제곱합 최소화.
- [[Residual]]: 실제값 `y`와 예측값 `\hat{y}`의 오차.
- [[MSE]]: 평균 제곱 오차.
- [[LogisticRegression]]: `z=wx+b` 후 [[Sigmoid]].
- [[Sigmoid]]: 실수를 0~1로 압축하는 S자 함수.
- [[Logit]]: sigmoid 이전 점수.
- [[BinaryClassification]]: 두 클래스 분류.
- [[CrossEntropy]]: 분류 학습에서 흔히 쓰는 손실.
- [[DecisionBoundary]]: 클래스 분할 기준 경계.
- [[LinearSeparability]]: 선형 경계 하나로 분리가 가능한 성질.
- [[Hyperplane]]: 고차원 선형 경계.
- [[Margin]]: 경계로부터 점의 거리/안정성 직관.
- [[FeatureSpace]]: 데이터를 feature 축으로 표현한 공간.
- [[DotProduct]]: [[DecisionBoundary]] 식에서의 핵심 연산.
- [[Threshold]]: 확률 임계값으로 클래스 결정.
- [[DenseLayer]]: 선형변환 + bias(`Wx+b`)의 기본 연산 구조.
- [[LLM]]: 선형 계산과 로그잇/확률 변환의 연결점.

## Contradictions
- No explicit contradiction with existing wiki content was identified.

## 今日の 3 Concepts

### 1) 선형회귀와 최소제곱

- 선형 가정: `\hat{y}=wx+b` (또는 다변량형 `W` 형식).
- 예측 오차: `residual = y - \hat{y}`.
- 성능 기준: `MSE = \frac{1}{n}\sum(y_i-\hat{y}_i)^2`.
- closed form가 이론상 가능할 때도 실무 규모에서는 [[GradientDescent]]가 기본.

### 2) 로지스틱 회귀와 확률적 분류

- 기본 형태: `z=wx+b`, `p = \sigma(z)`.
- `\sigma(z)=1/(1+e^{-z})`.
- `p>=0.5`를 기준으로 class 결정은 일반적이나 임계값 조정 가능.
- loss: 회귀보다 분류 전용의 [[CrossEntropy]]가 더 자연스럽다.

### 3) 결정경계와 선형분리성

- 선형 분류기는 `w^Tx+b=0`에서 경계를 만든다.
- [[LinearSeparability]]가 안 되면 복잡한 변환/모델이 필요.
- [[NeuralNetwork]]은 비선형 변환으로 경계를 굽히고 다층으로 분할 가능.

## 복습 질문 정답

1. 선형회귀에서 residual을 그냥 더하지 않고 제곱해서 더하는 이유는?
- 양수/음수 상쇄를 피하고, 큰 오차를 더 강하게 벌점화하기 때문이다.

2. 로지스틱 회귀에서 logit과 sigmoid 출력값의 차이는?
- logit은 `z`처럼 raw score(부호와 크기를 가진 실수), sigmoid 출력은 `0~1` 범위의 확률 해석값이다.

3. 데이터가 linearly separable하지 않다는 의미와 NN의 강점은?
- 한 개의 선형 경계로 완전 분리가 어렵다는 뜻이며, [[NeuralNetwork]]은 여러 층의 비선형 변환으로 feature를 바꿔 분리 가능성을 높인다.
