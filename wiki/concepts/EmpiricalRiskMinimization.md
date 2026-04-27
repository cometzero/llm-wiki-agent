---
title: "Empirical Risk Minimization"
type: concept
tags: [optimization, learning, statistics, risk]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Empirical Risk Minimization(ERM)은 전체 데이터 분포의 미지의 기대 손실 대신 train 데이터의 [[EmpiricalRisk]]를 최소화해서 학습 모델을 구하는 실전적 원리다.

## Key Claims
- ERM은 실제 분포 평균을 직접 계산할 수 없다는 제약을 해결하기 위한 현실적 근사 전략이다.
- 핵심은 [[LossFunction]] 값을 샘플별로 계산한 뒤 평균해 만드는 [[EmpiricalRisk]]를 줄이는 것이다.
- 분류, 회귀, LLM 학습, 추천, 임베딩 학습까지 대부분의 supervised 학습 파이프라인이 이 틀로 동작한다.

## Connections
- [[LossFunction]], [[EmpiricalRisk]], [[Optimization]], [[GradientDescent]], [[SurrogateLoss]], [[Overfitting]]

## Formula
- \(\hat{R}(\theta)=\frac{1}{N}\sum_{i=1}^N \ell(f_\theta(x_i), y_i)\)
- \(\theta^* = \arg\min_\theta \hat{R}(\theta)\)
