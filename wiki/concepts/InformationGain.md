---
title: "Information Gain"
type: concept
tags:
  - entropy
  - tree-split
  - uncertainty-reduction
sources:
  - 2026-05-03-day11-ai-ml-learning-review
last_updated: 2026-05-03
---

## Definition
[[InformationGain]]는 노드 분할 전후의 불확실성 감소량을 정량화한 값이다.

## Formula intuition
\(Information\ Gain = \text{Entropy before split} - \text{weighted entropy after split}\)

## Role in models
- [[DecisionTree]]에서 split 후보를 비교할 때 기준 점수로 사용됨
- 클수록 분할 후 노드들이 더 순수해짐

## Relations
- [[Entropy]], [[GiniImpurity]]
- [[DecisionTree]], RandomForest에서 split quality의 근간