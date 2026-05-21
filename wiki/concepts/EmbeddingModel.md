---
title: "Embedding Model"
type: concept
tags: [llm, embedding, vector, search]
sources: ["2026-05-21-day29-ai-ml-learning-review"]
last_updated: 2026-05-21
---

# Embedding Model

## 정의

Embedding model은 글, 이미지, 코드 같은 데이터를 "의미가 비슷하면 가까운 숫자 위치에 놓이도록" [[Embedding]] vector로 바꾸는 모델이다.

## 핵심 개념

- **Embedding vector**: 여러 개의 숫자로 이루어진 표현 (예: [0.2, 0.8, -0.1])
- **의미 기반 표현**: 단어 하나하나를 사람이 해석하기 어렵지만, 전체 벡터의 위치와 방향이 의미를 담는다
- **같은 [[EmbeddingSpace]]**: 문서와 질문은 반드시 같은 embedding space에 있어야 거리 비교 가능

## [[VectorSearch]]와의 관계

1. 입력 데이터를 embedding vector로 변환
2. [[VectorDatabase]]에 저장
3. 사용자 질문도 벡터로 변환
4. [[NearestNeighborSearch]]로 관련 문서 검색
5. [[CosineSimilarity]]로 관련성 점수 계산

## 왜 중요한가

전통적인 키워드 검색은 "같은 단어가 들어 있는가?"를 본다. 하지만 "환불", "반품", "돈을 돌려받고 싶어요"는 사람에게는 비슷한 말이다. Embedding model은 이 문제를 줄여서, 표현이 달라도 의미가 비슷한 문장을 찾을 수 있다.

## Neural Network 관점

Embedding model은 입력 token들을 [[Transformer]]나 다른 encoder에 넣고, 마지막 hidden state들을 하나의 문장 vector로 요약한다.Pooling 방식으로:
- Token별 hidden state 평균
- 특수 token의 hidden state 사용
- 별도 pooling layer

## 연관 개념

- [[VectorSearch]] — 검색 방식
- [[RAG]] — 주요 활용처
- [[CosineSimilarity]] — 거리 측정 방식
- [[VectorDatabase]] — 벡터 저장소
- [[NearestNeighborSearch]] — 검색 알고리즘

## 출처

- [[2026-05-21-day29-ai-ml-learning-review]]
