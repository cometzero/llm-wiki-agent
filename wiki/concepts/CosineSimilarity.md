---
title: "Cosine Similarity"
type: concept
tags: [vector, similarity, math]
sources: ["2026-05-21-day29-ai-ml-learning-review"]
last_updated: 2026-05-21
---

# Cosine Similarity

## 정의

Cosine similarity는 두 벡터의 방향이 얼마나 비슷한지 재는 값이다.

## 수학적 정의

$$\text{cosine\_similarity}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}$$

## 해석

| 값 범위 | 의미 |
|---------|------|
| 1.0 | 같은 방향 (완전히 동일) |
| 0.0 | 직각 (관련 없음) |
| -1.0 | 반대 방향 (완전히 다름) |

## [[VectorSearch]]에서의 역할

- [[EmbeddingModel]]로 변환된 벡터 간 거리를 측정
- 질문 벡터와 문서 벡터의 similarity가 높은 문서를 선택
- 예: similarity 0.92는 강하게 관련, 0.11은 거의 관련 없음

## 직관적 이해

2차원 벡터로 생각하면:
- "환불하고 싶어요" → [1.0, 0.1]
- "돈을 돌려받고 싶어요" → [0.9, 0.2]
- 방향이 비슷하므로 높은 similarity

## 연관 개념

- [[VectorSearch]] — 검색 방식
- [[EmbeddingModel]] — 벡터 변환
- [[NearestNeighborSearch]] — 검색 알고리즘
- [[ApproximateNearestNeighborSearch]] — 대규모용

## 출처

- [[2026-05-21-day29-ai-ml-learning-review]]
