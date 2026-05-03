---
title: "Entropy"
type: concept
tags:
  - uncertainty
  - classification
  - decision-tree
sources:
  - 2026-05-03-day11-ai-ml-learning-review
last_updated: 2026-05-03
---

## Definition
[[Entropy]]는 클래스 분포의 혼합 정도(불확실성)를 측정하는 값이다.

## Intuition
- 한 클래스만 있으면 불확실성은 거의 0
- 반반 섞이면 불확실성이 커짐
- [[DecisionTree]]에서 분할 좋은 정도를 판단할 때 사용됨

## Binary example
클래스 A/B가 반반이면 불확실성이 높고, 정보이득 계산에서 큰 개선 여지를 가진 split을 찾게 된다.