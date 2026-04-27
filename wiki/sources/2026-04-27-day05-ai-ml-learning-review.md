---
title: "2026-04-27 AI/ML Learning Day 05"
type: source
tags: [diary, ai-ml-learning, optimization, objective, loss, empirical-risk, gradient-descent]
date: 2026-04-27
source_file: raw/ai_ml_learning/2026-04-27-day05-ai-ml-learning-review.md
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Day 05는 AI/ML 학습을 [[Optimization]] 관점으로 재정의한다. 핵심은 모델 성능을 수치화한 [[Objective]]를 최소화/최대화하도록 설정하고, 데이터 전체의 성능을 반영하는 [[LossFunction]] 집계로부터 [[EmpiricalRisk]]를 만들며, 이를 반복적으로 줄여가는 [[GradientDescent]] 학습 과정을 다루는 구조다.

특히 [[Objective]]와 [[Argmin]], [[LossFunction]]과 [[EmpiricalRisk]], 그리고 [[SurrogateLoss]]의 차이를 분명히 구분하고, [[LearningRate]]/[[StepSize]]가 [[UpdateRule]]의 안정성과 속도를 좌우하는 핵심 요인임을 예제를 통해 설명한다.

또한 모델 파라미터([[Parameter]])와 제약 조건인 [[Constraint]]이 결합되는 현실적 최적화 문제 형태로 정리하며, 실제 AI 학습이 왜 단일 해답 공식을 찾는 문제가 아니라 반복적 업데이트 문제인지 보여준다.

## Key Claims
- [[MachineLearning]]은 [[Parameter]]를 조정해 모델의 [[Objective]]를 가장 좋게 만드는 [[Optimization]] 문제이며, 종종 목적이 최소화인지 최대화인지에 따라 다르게 정식화된다.
- [[Objective]]는 전체 학습 목표를 숫자로 표현한 함수로, 최적점은 \theta^* = [[Argmin]]_{\theta} J(\theta) 같은 형태로 나타낼 수 있다.
- [[LossFunction]]은 개별 샘플 또는 배치의 오차를 재는 기준이고, [[EmpiricalRisk]]는 데이터셋 전체의 평균 오차로, 실무 학습은 보통 이 값을 줄이는 과정이다.
- [[EmpiricalRiskMinimization]]은 전체 분포를 알 수 없을 때 [[EmpiricalRisk]]를 최소화해 학습 파라미터를 찾는 기본 원리다.
- [[GradientDescent]]의 핵심 업데이트는 \theta_{t+1} = \theta_t - \eta \nabla J(\theta_t)이며, [[Gradient]]는 방향, [[StepSize]](또는 [[LearningRate]])는 이동 거리 크기를 정한다.
- [[SurrogateLoss]]는 최종 평가 지표가 비미분 가능할 때 안정적으로 최적화 가능한 대체 손실로, [[CrossEntropy]]·[[MSE]]처럼 미분 가능한 손실이 실전에서 자주 쓰인다.
- [[Regularization]] 항을 쓰면 [[Objective]]는 단순한 데이터 적합 오차가 아니라 일반화 성능까지 반영한 확장 형태가 된다.

## Key Quotes
> "최소값 자체와 그 값을 만드는 입력은 다르다. 최소값은 함수값, argmin은 그 최적 위치다."

> "한 샘플의 손실과 데이터 전체의 평균 손실은 다르며, 학습 신호는 결국 [[EmpiricalRisk]]를 줄이는 방향으로 모아진다."

> "Gradient는 어디로 가야 하는지 알려주고, [[StepSize]]는 얼마나 가야 하는지 정한다. 둘 다 없으면 학습은 성립하지 않는다."

## Connections
- [[Optimization]] — 학습 전체를 설명하는 상위 틀
- [[Objective]] — 학습의 목표 함수
- [[Argmin]] — 최적점 위치의 정의
- [[LossFunction]] — 샘플 단위 오차 함수
- [[EmpiricalRisk]] — 전체 데이터 집합 기반의 평균 손실
- [[EmpiricalRiskMinimization]] — 실전 학습의 기본 전략
- [[SurrogateLoss]] — 대체 최적화 손실
- [[GradientDescent]] — 반복적 파라미터 업데이트 기반 학습 방법
- [[LearningRate]] — 한 스텝 크기를 결정하는 핵심 하이퍼파라미터
- [[StepSize]] — 경사 하강에서 이동 폭 개념
- [[Constraint]] — 실무 최적화의 제한 조건
- [[Regularization]] — 과적합 억제 목적의 항 추가
- [[Parameter]] — 모델이 학습하는 변수
- [[LinearRegression]] — 손실 기반의 예시 모델
- [[Classification]] — 클래스 예측에서 [[CrossEntropy]]가 흔히 사용되는 사례
- [[LLM]] — [[CrossEntropy]] 기반 학습으로 [[EmpiricalRisk]] 최소화 구조를 따르는 대규모 학습
- [[ReinforcementLearning]] — reward를 최대화하는 관점의 반대형 최적화
- [[Backpropagation]] — [[Gradient]] 계산의 계산 그래프 기반 경로
- [[Optimizer]] — [[UpdateRule]]을 실시간 적용하는 엔진

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this ingest pass.
