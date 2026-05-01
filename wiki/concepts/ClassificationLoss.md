---
title: "Classification Loss"
type: concept
tags:
  - classification
  - loss
  - optimization
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[ClassificationLoss]]는 정답 클래스에 얼마만큼의 확률 질량을 주었는지에 따라 학습 신호를 내는 손실군이다. 보통 class별 예측 분포에서 정답 클래스 확률을 높이는 방향으로 동작한다.

## Core idea
- 예측 점수(logit)를 확률로 바꾸고 정답 클래스 확률을 높이도록 업데이트한다.
- 분류 문제의 핵심은 “가까운 값”이 아니라 “정답 class를 얼마나 확신 있게 맞히는지”다.

## Typical
- [[CrossEntropy]], log loss

## Relation
- [[LLM]], [[Classification]], [[Softmax]], [[Logit]], [[Gradient]], [[Optimizer]].