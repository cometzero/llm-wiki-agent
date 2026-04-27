---
title: "Empirical Risk"
type: concept
tags: [risk, loss, generalization, statistics]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Empirical Risk는 train 데이터에서 계산한 평균 손실로, 전체 데이터 분포에 대한 참값을 알 수 없을 때 실무에서 사용되는 대용 기준이다.

## Key Claims
- [[EmpiricalRisk]]는 보통 [[LossFunction]] 값의 데이터셋 평균: \(\hat{R}(\theta)=\frac{1}{N}\sum_i \ell(f_\theta(x_i), y_i)\)로 계산한다.
- [[EmpiricalRiskMinimization]]의 중심은 이 값을 최소화하는 parameter를 찾는 것이다.
- [[EmpiricalRisk]]는 train 성능을 요약하기 때문에 validation/일반화 성능과 다를 수 있다.
- 실전 objective는 [[Regularization]] 항을 더해 \(J(\theta)=\hat{R}(\theta)+\lambda \Omega(\theta)\) 형태가 되기도 한다.

## Connections
- [[LossFunction]], [[EmpiricalRiskMinimization]], [[MachineLearning]], [[Regularization]], [[Optimization]], [[GradientDescent]]

## Notes
- [[Expectation]] 관점에서의 전체 분포 평균과 다르며, 데이터 표본 기반 추정량이라는 점에서 편향과 분산의 영향을 받는다.
