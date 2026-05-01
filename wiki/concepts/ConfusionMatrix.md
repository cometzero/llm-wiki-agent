---
title: "Confusion Matrix"
type: concept
tags:
  - classification
  - precision-recall
  - imbalanced-data
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[ConfusionMatrix]]는 분류 문제에서 예측 결과를 [[TP]], [[TN]], [[FP]], [[FN]] 네 분류로 나눠 해석하는 기본 구조다.

## Terms
- [[TP]] (True Positive): 실제 positive를 positive로 맞힘
- [[TN]] (True Negative): 실제 negative를 negative로 맞힘
- [[FP]] (False Positive): 실제 negative를 positive로 오탐
- [[FN]] (False Negative): 실제 positive를 놓침

## Why it matters
[[Accuracy]]가 높아도 [[FN]] 또는 [[FP]]가 큰 실전 실패를 숨길 수 있다.

## Related Concepts
[[Precision]], [[Recall]], [[F1Score]], [[ImbalancedData]], [[Threshold]].