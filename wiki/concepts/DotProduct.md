---
title: "DotProduct"
type: concept
tags: [linear-algebra, similarity]
last_updated: 2026-04-26
sources: [2026-04-23-day01-ai-ml-learning-review]
---

## 핵심 정의
[[DotProduct]]는 두 벡터의 대응 성분곱을 합산한 값으로, 방향성과 크기 정보를 동시에 반영한다.

`a · b = Σ_i a_i b_i`

## AI/ML 연결
- [[Attention]]에서 Query와 Key의 연산 점수로 자주 사용된다.
- 값이 크면 일반적으로 방향 정합 + 크기 요인이 모두 강하게 작동한다.
- 단순 유사도 비교만으로는 크기 영향이 섞이므로, [[CosineSimilarity]]로 정규화하기도 한다.

## 관련 개념
- [[CosineSimilarity]]
- [[Norm]]
- [[Embedding]]
- [[Attention]]
