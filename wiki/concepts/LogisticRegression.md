---
title: "Logistic Regression"
type: concept
tags:
  - ai-ml
  - classification
  - probability
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Logistic Regression은 선형 점수에 [[Sigmoid]]를 적용해 이진 분류 문제를 다루는 모델이다.

실제론 회귀식이 아닌 분류 중심 모델로 쓰이며, 확률 값처럼 보이는 점수를 산출해 [[BinaryClassification]] 결정을 지원한다.

## Core Idea
1. 점수 계산: `z = wx + b`
2. 확률형 변환: `\sigma(z)=1/(1+e^{-z})`
3. 임계값 판단: 보통 `0.5` 기준.

## Key Claims
- 이름은 회귀지만 출력은 주로 두 클래스 분류에 사용한다.
- [[Logit]](raw score)과 [[Sigmoid]] 출력값을 구분해야 한다.
- 분류 손실은 보통 [[CrossEntropy]]류가 쓰인다.

## Connections
- [[Sigmoid]]: 점수→확률 변환 함수.
- [[BinaryClassification]]: 주 사용 사례.
- [[Threshold]]: 클래스 결정 기준.
- [[Logit]]: 출력 전 score 개념.
- [[LLM]]: 여러 class 확률 분해를 이해하기 위한 기본 블록.

## Notes
- 출력은 "확률"로 해석되지만, 실제 보정(calibration) 여부는 별도 검증이 필요하다.