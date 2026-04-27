---
title: "Surrogate Loss"
type: concept
tags: [loss, optimization]
sources: [2026-04-27-day05-ai-ml-learning-review]
last_updated: 2026-04-27
---

## Summary
Surrogate Loss는 직접 최적화가 어려운 목표를 대신해 사용되는, 미분 가능하거나 수치적으로 다루기 쉬운 대체 손실이다.

## Key Claims
- 정답과의 불연속 비교처럼 미분이 어려운 지표를 대신할 때 surrogate가 쓰인다.
- surrogate는 최종 평가 지표와 동일하지 않을 수 있지만, 학습 안정성과 최적화 가능성을 확보하기 위한 실무적 설계이다.
- [[CrossEntropy]], [[MSE]], 로그 손실류는 분류/회귀에서 자주 쓰이는 대체 또는 기본 손실 패턴의 예시다.

## Connections
- [[LossFunction]], [[EmpiricalRisk]], [[Optimization]], [[GradientDescent]], [[Backpropagation]], [[CrossEntropy]], [[MSE]]

## Risk
- surrogate를 택하면 최종 평가 지표와의 정렬성(calibration)을 별도 검토해야 한다.
