---
title: "Recall"
type: concept
tags:
  - classification
  - metric
sources:
  - 2026-05-01-day09-ai-ml-learning-review
last_updated: 2026-05-01
---

## Summary
[[Recall]]은 실제 positive 중에서 모델이 positive로 찾아낸 비율이다.

## Formula
- recall = TP / (TP + FN)

## Interpretation
- recall이 높으면 실제 양성 샘플을 놓치지 않는 성능이 좋다.
- 질병 탐지, 사기 탐지처럼 놓침 비용이 큰 문제에서 핵심 지표다.

## Trade-off
- threshold를 낮추면 보통 recall이 올라가고 precision은 내려갈 수 있다.