---
title: "Gini Impurity"
type: concept
tags:
  - impurity
  - decision-tree
  - split-quality
sources:
  - 2026-05-03-day11-ai-ml-learning-review
last_updated: 2026-05-03
---

## Definition
[[GiniImpurity]]는 클래스가 섞인 정도를 측정하는 또 다른 분할 지표로, [[Entropy]]와 유사한 역할을 한다.

## Binary view
\(Gini = 1 - p(A)^2 - p(B)^2\)

## Characteristics
- 완전 순수 노드에서는 0에 가까워짐
- 분류에서 순수도를 높이는 분할을 선호하도록 사용 가능
- [[DecisionTree]] 학습에서 split 평가 지표로 널리 쓰임