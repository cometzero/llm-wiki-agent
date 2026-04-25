---
title: "2026-04-23 AI/ML Learning Day 01"
type: source
tags: [foundation-model, linear-algebra, embeddings, learning-notes]
date: 2026-04-23
source_file: raw/2026-04-23-day01-ai-ml-learning-review.md
last_updated: 2026-04-25
sources: [2026-04-23-day01-ai-ml-learning-review]
---

## Summary
이 학습 노트는 LLM 및 AI 실무에서 반복적으로 쓰이는 수학 기초를 정리한다. 핵심은 [[Vector]]를 고정된 실체가 아니라 **공간의 대상**으로 두고, 이를 [[Coordinate]]로 표현할 때는 [[Basis]]에 따라 값이 달라진다는 점이다.

또한 [[Matrix]]를 단순 표가 아니라 [[LinearMap]](선형변환)으로 해석하고, [[Rank]]를 이 변환이 독립적으로 보존하는 방향 수로 이해한다. 이어서 [[DotProduct]], [[Norm]], [[L1Norm]], [[L2Norm]], [[CosineSimilarity]]를 통해 벡터 간 관계를 비교하는 기준을 정리하고, 이것들이 [[LLM]]의 [[Embedding]], [[Attention]], [[Regularization]], [[EmbeddingRetrieval]], [[Gradient]] 처리에서 실제로 어떻게 쓰이는지 연결한다.

## Key Claims
- [[Vector]]는 공간의 대상이고 [[Coordinate]]는 선택한 [[Basis]]에 따라 달라지는 표현값이다.
- 같은 벡터라도 basis가 바뀌면 좌표 표현이 바뀌므로 representation은 basis-dependent이다.
- [[Matrix]]는 [[Vector]]를 다른 공간으로 보내는 [[LinearMap]]이며, 덧셈과 스칼라배를 보존한다.
- [[Rank]]는 선형변환이 실제로 살려내는 독립 정보의 차원을 나타내고, 저랭크는 정보 손실 또는 압축을 시사한다.
- [[DotProduct]]는 방향성과 크기의 결합 유사도로 [[Attention]] 스코어의 핵심 지표가 된다.
- [[L2Norm]]은 벡터 길이, [[L1Norm]]은 요소 절대값 합으로 서로 다른 정규화·최적화 성질을 갖는다.
- [[CosineSimilarity]]는 벡터의 크기 영향이 제거된 방향 유사도이기 때문에 [[EmbeddingRetrieval]]/[[SemanticRetrieval]]에 적합하다.

## Key Quotes
> "좌표는 벡터 자체가 아니라, 선택한 basis 기준에서 벡터를 수치로 표현한 방식이다."

> "행렬은 단순한 숫자표가 아니라, 벡터를 다른 벡터로 보내는 linear map의 계산 표현이다."

> "dot product는 방향성과 크기가 결합된 관련도, L2 norm은 크기, cosine similarity는 크기 제거 후 방향 유사도다."

## Connections
- [[LLM]] — [[Embedding]], [[HiddenState]], [[Gradient]]가 모두 [[Vector]] 기반으로 취급됨.
- [[VectorSpace]] — 학습 노트의 전체 논리가 성립하는 기반 구조.
- [[Basis]] / [[Coordinate]] — 표현 좌표의 의존성 핵심.
- [[Matrix]], [[LinearMap]], [[DenseLayer]], [[Projection]], [[Attention]], [[QKVProjection]] — 선형 변환 관점의 공통 계산축.
- [[Rank]], [[LoRA]], [[PCA]] — 정보 보존/축소 해석 축.
- [[DotProduct]], [[Norm]], [[L1Norm]], [[L2Norm]], [[CosineSimilarity]] — 유사도·거리·안정성 지표군.
- [[EmbeddingRetrieval]], [[SemanticSearch]], [[Regularization]], [[GradientNormClipping]] — 실제 AI 파이프라인 적용처.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this ingest pass.