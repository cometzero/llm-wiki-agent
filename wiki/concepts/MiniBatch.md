---
title: "MiniBatch"
type: concept
tags: [optimization, stochastic-optimization, deep-learning, gradient-descent]
sources: [2026-04-28-day06-ai-ml-learning-review]
last_updated: 2026-04-28
---

## Summary
[[MiniBatch]]는 학습에서 한 번의 업데이트에 사용되는 데이터의 작은 부분 집합이다. 전체 데이터셋 전체를 사용할 때보다 계산이 빠르고, 순수 [[SGD]]의 단일 샘플 학습보다 안정적인 통계적 추정을 제공한다.

## Key Idea
전체 데이터셋 gradient와 동일하지 않지만, mini-batch로 계산한 gradient는 무작위 표본 기반의 StochasticEstimate로서 반복적으로 누적될 때 [[EmpiricalRisk]] 감소 방향으로 수렴하는 경향이 있다.

## Relationship to Prior Knowledge
- [[MachineLearning]]에서 [[Objective]]를 최적화할 때 비용-속도-안정성의 교점
- [[GradientDescent]]를 실무에서 실행 가능하게 만드는 핵심 구현 단위
- [[Variance]]와 학습 안정성의 중심 요인
- [[TensorShape]] 측면에서는 batch 축에 해당 (예: `[batch_size, sequence_length]`)

## Key Terms
- BatchSize: mini-batch 내 샘플 개수
- [[Variance]]: mini-batch gradient의 흔들림 크기
- [[LearningRate]]: 더 큰 batch에서는 보통 더 큰 step-size가 가능할 수 있지만, model/hardware 상황에 따라 튜닝 필요
- StochasticGradientDescent: mini-batch 기반의 확률적 경사 업데이트

## Key Equations
전체 데이터셋 평균 loss를 \(L(\theta)=\frac{1}{N}\sum_{i=1}^{N}L_i(\theta)\)로 두면,

\[
\nabla L_B(\theta) = \frac{1}{|B|}\sum_{i \in B} \nabla L_i(\theta)
\]

\(B\)는 mini-batch 인덱스 집합이며, \(\nabla L_B\)는 추정 gradient이다.

## Connections
- [[SGD]] — mini-batch는 [[SGD]]의 실무 표준 형태
- [[Optimizer]] — mini-batch gradient를 받아 실제 갱신 적용
- [[Convergence]] — 흔들림이 있으나 평균적으로 안정적 감소 가능
- GPU/TPU — 병렬 처리 효율을 위한 mini-batch 적합성

## Why this matters
모델 학습은 연산 비용, 메모리, 하드웨어 파이프라인 때문에 완전 배치가 비현실적이다. mini-batch는 학습자원과 수렴 속도의 균형점이다.