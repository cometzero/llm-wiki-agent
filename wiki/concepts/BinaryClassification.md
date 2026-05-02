---
title: "Binary Classification"
type: concept
tags:
  - ai-ml
  - classification
  - supervised-learning
sources:
  - 2026-05-02-day10-ai-ml-learning-review
last_updated: 2026-05-02
---

## Summary
Binary Classification은 두 개 클래스 중 하나를 선택하는 분류 문제다.

예/아니오, 정상/스팸, 긍정/부정처럼 class가 2개인 문제에서 자주 사용된다.

## Core Idea
- 점수(또는 logit)를 확률로 바꾼 뒤 threshold로 최종 라벨 결정.
- 모델 출력과 실제 라벨 간 불일치를 손실로 정량화.

## Connections
- [[LogisticRegression]]: 대표적 기본 모델.
- [[Sigmoid]], [[Logit]], [[Threshold]]: 판별 과정의 핵심 구성요소.
- [[ConfusionMatrix]], [[Precision]], [[Recall]], [[Accuracy]], [[F1Score]]: 성능 지표 계열.
- [[CrossEntropy]]: 학습 손실의 전형적 후보.
