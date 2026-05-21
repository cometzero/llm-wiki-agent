---
title: "Vector Search"
type: concept
tags: [llm, vector, search, retrieval]
sources: ["2026-05-21-day29-ai-ml-learning-review"]
last_updated: 2026-05-21
---

# Vector Search

## 정의

Vector search는 [[EmbeddingModel]]로 변환한 embedding vector들 중에서 질문 벡터와 가장 가까운 항목을 찾는 검색 방식이다.

## 키워드 검색과의 차이

| 구분 | 키워드 검색 | [[VectorSearch]] |
|------|-------------|-------------------|
| 기준 | "같은 단어가 들어 있는가?" | "의미가 비슷한가?" |
| 한계 | 동의어, 표현 차이 무시 | 의미를 숫자로 표현 |

## 핵심 개념

### [[CosineSimilarity]]
두 벡터의 방향이 얼마나 비슷한지 재는 값:
- 같은 방향 → similarity ≈ 1
- 직각 → similarity ≈ 0
- 반대 방향 → similarity ≈ -1

### [[NearestNeighborSearch]]
질문 벡터와 가장 가까운 벡터를 찾는 검색:
- 문서가 적으면 전수 비교 가능
- 문서가 많으면 [[ApproximateNearestNeighborSearch]] 사용

## [[RAG]]에서의 역할

Vector search는 [[RAG]]의 **retrieval 단계**에서 질문과 가장 관련 있는 문서를 찾는 역할을 한다.

1. 질문: "환불 가능한가요?" → q = [1.0, 0.0]
2. 문서 A: "환불은 7일 이내" → dA = [0.9, 0.1]
3. 문서 B: "배송은 2~3일" → dB = [0.1, 0.8]
4. q와 dA의 similarity가 높으므로 문서 A 선택

## 연관 개념

- [[EmbeddingModel]] — 벡터 변환
- [[RAG]] — 주요 활용처
- [[CosineSimilarity]] — 거리 측정
- [[VectorDatabase]] — 벡터 저장소
- [[NearestNeighborSearch]] — 검색 알고리즘

## 출처

- [[2026-05-21-day29-ai-ml-learning-review]]
