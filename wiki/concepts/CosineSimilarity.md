---
title: "CosineSimilarity"
type: concept
tags: [similarity, retrieval, embedding]
last_updated: 2026-04-26
sources: [2026-04-23-day01-ai-ml-learning-review]
---

## 핵심 정의
[[CosineSimilarity]]는 두 벡터의 내적을 각 벡터의 크기로 정규화해 방향 유사도만 비교한다.

## 직관
- 크기(스케일)가 다르더라도 방향이 비슷하면 높은 유사도를 준다.
- 의미 검색에서 표현 벡터 간 "유사도" 판단으로 자주 쓰인다.

## AI/ML 연결
- [[Embedding]] retrieval에서 질의-문서 문장 유사도 비교
- [[RAG]] 검색 정렬
- [[LLM]] 기반 의미 검색 파이프라인에서 [[Attention]]의 직접 점수화 방식과는 다른 쓰임새를 가진다.

## 관련 개념
- [[DotProduct]]
- [[Norm]]
- [[Embedding]]
- [[RAG]]
