---
title: "2026-04-26 AI/ML Learning Day 04 — Derivatives, Gradients, and Backpropagation"
type: source
tags: [diary, ai-ml-learning, derivative, gradient, backpropagation]
date: 2026-04-26
source_file: raw/ai_ml_learning/2026-04-26-day04-ai-ml-learning-review.md
sources: [2026-04-26-day04-ai-ml-learning-review]
last_updated: 2026-04-26
---

## Summary
Day 04는 AI/ML 30일학습에서 최적화의 수학 기반을 다룬다. 핵심은 [[Derivative]], [[PartialDerivative]], [[Gradient]]의 직관을 정리하고, 이들을 결합해 [[LossFunction]]을 줄이는 방식으로 연결하는 [[GradientDescent]]의 출발점을 잡는 것이다. 또한 합성함수 미분 규칙인 [[ChainRule]]을 [[ComputationalGraph]]로 확장해 모델 학습의 실제 구현인 [[Backpropagation]]과 [[Autograd]] 관점에서 정리한다.

## Key Claims
- [[Derivative]]는 함수 한 점에서의 즉시 변화율(local rate of change)로, 작은 구간에서의 변화 예측에 쓰이며 [[Optimization]]의 1차 근사 기반을 만든다.
- 다변수 함수에서 [[PartialDerivative]]는 한 변수만 움직였을 때 민감도를 측정하고, 이를 모은 벡터가 [[Gradient]]가 된다.
- [[Gradient]]는 [[DirectionalDerivative]]와 연결되어 가장 큰 양의 증가 방향을 가리키며, [[GradientDescent]]는 반대 방향으로 이동해 손실을 줄인다.
- [[ChainRule]]은 합성함수의 미분을 국부 기울기들의 곱으로 전달하는 규칙으로, 이를 [[ComputationalGraph]]에 적용해 큰 모델도 미분 가능하게 만든다.
- [[Backpropagation]]는 [[ComputationalGraph]] 위에서의 효율적 역전파 알고리즘이며, [[ForwardPass]]/[[BackwardPass]]로 단계적으로 수행된다.
- 학습에서 [[LearningRate]]를 크게 잡으면 [[VanishingGradient]]/[[ExplodingGradient]]이 아닌 진동이나 발산이 발생할 수 있고, 너무 작으면 수렴이 느려지는 트레이드오프가 생긴다.

## Key Quotes
> "Derivative는 한 점에서의 local rate of change다."

> "경사(gradient)는 각 방향으로의 편미분을 한꺼번에 모은 벡터다."

> "계산 그래프에서는 각 노드의 local gradient만 알면 전체 미분을 chain rule로 전달할 수 있다."

## Connections
- [[Derivative]] — 순간 변화율의 기본 단위
- [[PartialDerivative]] — 다변수 민감도 측정
- [[Gradient]] — 변화율 벡터 및 최적화 방향
- [[DirectionalDerivative]] — 방향별 변화율과의 연결
- [[ChainRule]] — 합성함수 미분의 전달 규칙
- [[ComputationalGraph]] — 계산 단계를 노드로 분해
- [[ForwardPass]] — 순전파 계산
- [[BackwardPass]] — 역전파 계산
- [[Backpropagation]] — 전체 모델 학습의 핵심 기울기 전달
- [[Autograd]] — 자동 미분/미분 기록 엔진
- [[LossFunction]] — 최적화 대상 함수
- [[GradientDescent]] — 파라미터 갱신 방법
- [[LearningRate]] — 스텝 크기 제어
- [[VanishingGradient]] — 기울기 소실 문제
- [[ExplodingGradient]] — 기울기 폭주 문제
- [[Jacobian]] — 벡터값 함수의 일반화 미분
- [[2026-04-25-day03-ai-ml-learning-review]] — [[LossFunction]], [[MachineLearning]] 맥락을 연결
- [[2026-04-23-day01-ai-ml-learning-review]] — [[Vector]], [[Gradient]], [[Norm]] 등 수학적 기반 연결
- [[2026-04-24-day02-ai-ml-learning-review]] — 통계 기반에서 확률적 모델링으로 확장되는 학습 체계와의 연결

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this ingest pass.