---
title: "2026-04-28 AI/ML Learning Day 06"
type: source
tags: [diary, ai-ml-learning, optimization, gradient-descent, learning-rate, optimizer, sgd]
date: 2026-04-28
source_file: raw/ai_ml_learning/2026-04-28-day06-ai-ml-learning-review.md
sources: [2026-04-28-day06-ai-ml-learning-review]
last_updated: 2026-04-28
---

## Summary
Day 06는 [[Optimization]] 기반 [[MachineLearning]] 학습에서 핵심인 [[GradientDescent]]의 실전 구현을 다룬다. 전체 데이터를 한 번에 쓰는 BatchGradientDescent 대신 [[SGD]]의 [[MiniBatch]]를 사용해 [[Gradient]] 추정치를 자주 계산하고, 이를 통해 속도와 계산 효율을 확보한다. 이어서 [[LearningRate]]가 [[Convergence]], [[Divergence]], Oscillation에 미치는 영향을 정리하고, 마지막으로 [[Optimizer]]의 대표 기법인 [[Momentum]]과 [[Adam]]의 동작 원리를 정리해 [[LLM]] 학습에서의 안정성과 수렴 품질을 설명한다.

## Key Claims
- [[SGD]]는 한 번에 전체 데이터가 아니라 샘플 또는 소규모 배치를 사용해 [[Gradient]]를 추정하고 업데이트를 반복하는 방법이며, 실전에서는 보통 [[MiniBatch]] 형식(예: 16/32/128)을 쓴다.
- [[MiniBatch]]는 전체 데이터 기울기와 다를 수 있지만, 표본이 잘 뽑히면 장기적으로는 [[EmpiricalRisk]] 최소화 방향을 가리키는 StochasticEstimate로 작동한다.
- [[LearningRate]](= [[StepSize]])가 작으면 학습이 느려지고, 크면 [[Divergence]]·Oscillation이 쉽게 발생해 실패할 수 있다.
- [[Convergence]]는 손실이 장기적으로 안정적으로 내려가는 상태이며, mini-batch 특성상 한 스텝마다 손실 오르내림이 있어도 전체 추세가 중요하다.
- [[Momentum]]는 이전 gradient 방향의 이동 평균(`v`)을 누적해 학습을 부드럽게 하며, [[Adam]]은 FirstMoment와 SecondMoment을 추적해 AdaptiveLearningRate 형태로 파라미터별 업데이트를 조절한다.
- AdamW는 [[Adam]]에서 WeightDecay 처리 방식을 개선한 변형으로, Transformer/LMM 계열 학습에서 자주 사용된다.

## Key Quotes
a) "전체 데이터 gradient와 정확히 같지는 않지만, 미니배치 gradient는 무작위 표본으로 계산한 대략적인 추정치이다." — mini-batch 개념의 핵심을 요약한 정의

b) "학습률이 너무 크면 좋은 지점을 지나쳐 튕기고, 너무 작으면 거의 안 움직인다." — [[LearningRate]]의 수렴/발산 트레이드오프

c) "Adam은 first moment(방향 평균)와 second moment(크기 평균)를 동시에 보며, parameter별 업데이트 크기를 다르게 만든다." — [[Adam]]의 적응형 업데이트 핵심

## Connections
- [[MachineLearning]] — 파라미터 최적화를 통한 학습의 기본 문제
- [[Optimization]] — 목적함수를 줄이는 반복 계산의 상위 틀
- [[LossFunction]] — 학습 신호의 기초
- [[EmpiricalRisk]] — 데이터 집합 단위 손실 평균으로의 연결
- [[GradientDescent]] — 업데이트 규칙의 중심
- [[SGD]] — 미니배치 기반 확률적 경사 하강
- [[MiniBatch]] — 연산 단위와 잡음(noise) 조절 장치
- [[Variance]] — mini-batch 추정치 흔들림의 원인 및 특성
- [[LearningRate]] — 스텝 크기 제어 변수
- [[Convergence]] — 안정적 수렴 목표
- [[Divergence]] — 손실이 발산하는 실패 양상
- Oscillation — 최적점 주변 왕복 현상
- [[Optimizer]] — gradient 반영 규칙의 실행기
- [[Momentum]] — 누적 관성 기반 업데이트
- [[Adam]] — 1차/2차 모멘트 기반 적응형 옵티마이저
- AdamW — [[LLM]] fine-tuning에서 빈도 높은 변형
- [[Tensor]] / [[TensorShape]] — 배치/시퀀스 연산의 구현적 기반
- [[Embedding]] — [[LLM]] 학습 적용 예시
- [[LLM]] — mini-batch 학습과 optimizer 적용의 대표 대상
- [[Parameter]] — 업데이트 대상 모델 변수들
- [[Backpropagation]] — gradient 계산 경로와 결합된 학습 파이프라인
- Epoch — 데이터셋 반복 단위

## Contradictions
- No explicit contradiction with existing wiki content was identified during this ingest pass.