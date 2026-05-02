---
title: "Logit"
type: concept
tags:
  - ai-ml
  - classification
  - logistic-regression
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Logit은 sigmoid 이전의 raw score(로짓 값)로, 양의 큰 수일수록 해당 클래스가 높게 선호된다는 의미를 가지는 실수 값이다.

로지스틱 회귀에서는 `z=wx+b`가 logit으로 해석된다.

## Core Claim
- logit은 확률이 아니며, [[Sigmoid]]를 통과해야 `0~1` 값으로 해석이 가능해진다.

## Connections
- [[LogisticRegression]]의 핵심 입력 값.
- [[Sigmoid]]의 입력.
- [[BinaryClassification]] 의사결정 파이프라인의 중간 값.
- [[CrossEntropy]]에서 예측 분포 형성의 기준점.
