---
title: "Precision"
type: concept
tags:
  - classification
  - metric
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[Precision]]는 모델이 positive라고 한 예측 중 실제 positive의 비율이다.

## Formula
- precision = TP / (TP + FP)

## Interpretation
- precision이 높으면 positive로 예측한 항목의 신뢰도가 높다.
- [[SpamFiltering]], 이상탐지, 의료 진단 등에서 오탐을 줄이는 것이 중요할 때 유용하다.

## Trade-off
[[Recall]]과 상보적으로 작동하며 threshold 변화에 따라 트레이드오프가 발생한다.