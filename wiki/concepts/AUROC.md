---
title: "AUROC"
type: concept
tags:
  - classification
  - ranking
  - metric
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[AUROC]]는 다양한 threshold에서 positive와 negative의 구분 능력을 종합한 값이다.

## Core idea
단일 threshold 성능만 보지 않고, 점수의 순위 기반 구분 능력을 전체적으로 요약한다.

## Typical interpretation
- AUROC가 높으면 임계값이 바뀌어도 전체적으로 구분이 좋은 모델 경향이 있다.
- 다만 특정 운영 임계값에서의 precision/recall 성능은 별도로 점검해야 한다.

## Relation
- [[Threshold]], [[Precision]], [[Recall]], [[Classification]], [[Decision Boundary]].