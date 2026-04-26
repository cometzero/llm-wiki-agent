---
title: "2026-04-23 AI/ML Learning Day 01"
type: source
tags: [diary, ai-ml-learning, math-foundations]
date: 2026-04-23
source_file: raw/ai_ml_learning/2026-04-23-day01-ai-ml-learning-review.md
---

## Event Summary
AI/ML 30일 학습 여정의 첫째 날. 수학 표현과 확률 기초를 주제로 [[VectorSpace]], [[LinearMap]], [[DotProduct]], [[Norm]], [[CosineSimilarity]]의 핵심 개념을 학습하고, 이들이 [[LLM]]의 [[Embedding]], [[Attention]], [[Gradient]] 연산과 어떻게 연결되는지 정리했다.

## Key Decisions
- 학습 레벨을 beginner-intermediate로 설정
- 첫날은 벡터·행렬·내적 기초에 집중
- 복습 질문 3개를 통해 개념 체화 목표

## Energy & Mood
- Day 01/30 — 기초 개념 리뷰에 집중한 구조화된 학습 세션

## Key Claims
- [[VectorSpace]]는 벡터의 덧셈과 스칼라배가 정의되는 공간이며, 좌표(coordinate)는 선택한 [[Basis]]에 의존하는 수치 표현이다. 같은 벡터라도 basis가 바뀌면 coordinate는 달라진다.
- [[Matrix]]는 단순한 숫자표가 아니라 벡터를 다른 벡터로 보내는 [[LinearMap]]의 계산 표현이다. [[Rank]]는 변환이 실제로 보존하는 독립 정보의 차원 수를 의미한다.
- [[DotProduct]]는 두 벡터의 방향성과 크기가 결합된 관련도를 측정하며, [[Attention]]에서 query-key 점수화에 쓰인다.
- [[Norm]]은 벡터의 크기를 나타내며, L1과 L2는 서로 다른 기하학적 성질을 갖는다. [[Gradient]] norm clipping, regularization에 연결된다.
- [[CosineSimilarity]]는 크기를 제거하고 방향 유사도에 집중하므로 [[Embedding]] retrieval, semantic similarity에 자주 쓰인다.
- [[LLM]]의 token embedding, hidden state, gradient는 모두 벡터 표현으로 다룰 수 있다.
- Dense layer, projection layer, [[Attention]]의 Q/K/V projection은 모두 행렬 곱 관점으로 이해할 수 있다.

## Key Quotes
> "좌표(coordinate)는 벡터 자체가 아니라, 선택한 basis에 대해 그 벡터를 어떻게 분해해서 표현하느냐를 나타내는 값이기 때문이다."
> "rank는 그 linear map이 실제로 살려내는 독립적인 정보의 차원 수를 의미한다."
> "attention은 raw interaction score로 dot product를, retrieval은 의미 유사도 비교를 위해 cosine similarity를 자주 활용한다."
> "벡터공간은 표현의 대상, 행렬은 그 표현을 바꾸는 선형변환, dot product·norm·거리는 표현 사이의 관계를 수치화하는 도구다."

## Connections
- [[VectorSpace]] — 벡터 표현의 기반 공간
- [[Basis]] — 좌표 표현을 결정하는 기준축
- [[LinearMap]] — 행렬의 본질적 해석
- [[Rank]] — 선형변환의 정보 보존 차원
- [[DotProduct]] — [[Attention]] 메커니즘의 점수 함수 기반
- [[Norm]] — [[Gradient]] clipping, regularization의 기초
- [[CosineSimilarity]] — [[Embedding]] 검색 및 의미 유사도 측정
- [[LLM]] — 학습한 수학 개념이 적용되는 대상 시스템
- [[Embedding]] — 벡터 표현의 구체적 응용
- [[Attention]] — dot product 기반 관련도 계산 메커니즘
- [[Gradient]] — norm 기반 clipping 대상
- [[LoRA]] — low-rank approximation과 rank 개념의 응용
- [[PCA]] — basis change 관점의 응용

## Contradictions
- None identified with existing wiki content.
