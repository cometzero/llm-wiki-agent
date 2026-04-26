---
title: "2026-04-23 AI/ML Learning Day 01"
type: source
tags: [diary, ai-ml-learning, math-foundations, vector-space, linear-algebra]
date: 2026-04-23
last_updated: 2026-04-26
source_file: raw/ai_ml_learning/2026-04-23-day01-ai-ml-learning-review.md
sources: [2026-04-23-day01-ai-ml-learning-review]
---

## Summary
Day 01은 AI/ML 30일 학습 중 수학 기초를 정리한 기록으로, [[VectorSpace]]와 [[Basis]], 좌표 표현, [[Matrix]]와 [[LinearMap]], 그리고 [[DotProduct]], [[Norm]], [[CosineSimilarity]]로 구성된다.

핵심은 "벡터는 대상의 표현, 좌표는 기준축(기저) 기준의 숫자 표현"이라는 구분이다.

이 문서는 이런 기하학적 표현이 [[LLM]]의 내부 연산인 [[Embedding]], [[Attention]], [[Gradient]], [[DenseLayer]]에서 어떻게 쓰이는지 연결해준다.

## Key Claims
- [[Vector]]는 대상을 수치적으로 표현한 결과이며, 동일한 대상이라도 [[Basis]]가 바뀌면 같은 벡터의 [[Coordinate]]가 달라질 수 있다.
- [[VectorSpace]]는 벡터 덧셈과 스칼라배가 성립하는 공간이며, 좌표는 벡터의 고유값이 아니라 좌표계 선택에 따른 기록값이다.
- [[Matrix]]는 숫자표 이상으로, [[LinearMap]]의 계산 표현으로서 벡터를 다른 벡터로 변환한다.
- [[Rank]]는 [[LinearMap]]가 보존하는 독립 방향의 수로, 변환 후 정보의 유효한 차원 수를 나타낸다.
- [[DotProduct]]는 방향과 크기를 동시에 반영한 유사성/관련도 점수이며, [[Attention]] 점수 계산의 핵심이다.
- [[Norm]]은 벡터 크기(길이) 측도이며, [[Gradient]]의 [[GradientNormClipping]] 및 정규화 관점과 연결된다.
- [[CosineSimilarity]]는 벡터 크기 효과를 제거하고 방향 유사도를 비교하므로 문장 의미 유사도 기반 [[RAG]]/검색에서 자주 쓰인다.

## Key Quotes
> "좌표는 벡터 자체가 아니라, 선택한 basis에 대해 그 벡터를 어떻게 분해해서 표현하느냐를 나타내는 값이기 때문이다."

> "rank는 그 linear map이 실제로 살려내는 독립적인 정보의 차원 수를 의미한다."

> "attention은 raw interaction score로 dot product를, retrieval은 의미 유사도 비교를 위해 cosine similarity를 자주 활용한다."

## Connections
- [[VectorSpace]] — 데이터 표현의 기반 공간
- [[Basis]] — 좌표 계산의 기준축
- [[Coordinate]] — basis-dependent(기저 의존) 좌표 표현
- [[Matrix]] — [[LinearMap]]의 연산 형식화
- [[LinearMap]] — 벡터 공간 간 선형 변환
- [[Rank]] — 선형변환의 정보 보존 차원
- [[DotProduct]] — [[Attention]]의 기본 점수 연산
- [[Norm]] — [[Gradient]] 크기 제어와 정규화 지표
- [[L2Norm]] — 기하학적 거리/길이 척도
- [[CosineSimilarity]] — 의미 유사도 비교
- [[Embedding]] — 토큰/문장 표현 벡터
- [[Attention]] — Q·K 점수화 및 정보 결합 단계
- [[DenseLayer]] — [[LLM]]의 핵심 선형 변환 층
- [[LoRA]] — [[Rank]] 개념과 연결되는 저차원 업데이트 방식
- [[Gradient]] — [[LLM]] 학습에서의 방향 신호
- [[Vector]] — 계산 단위 기본 객체

## Contradictions
- 기존 [[LinearMap]]/[[Rank]] 관련 문서들과 모순되는 내용은 없다.
