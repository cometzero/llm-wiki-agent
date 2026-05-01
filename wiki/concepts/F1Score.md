---
title: "F1 Score"
type: concept
tags:
  - classification
  - metric
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[F1Score]]는 precision과 recall의 조화평균이다. 두 지표가 한쪽으로 치우친 분류기를 완화해 균형 감각을 주는 값이다.

## Formula
- F1 = 2 × precision × recall / (precision + recall)

## Usage
- positive 클래스가 중요한데, precision과 recall을 동시에 관리해야 하는 시나리오에서 많이 쓰인다.
- [[Class imbalance]] 환경에서 유용하게 해석된다.

## Relation
- [[Precision]], [[Recall]], [[Threshold]], [[ConfusionMatrix]].