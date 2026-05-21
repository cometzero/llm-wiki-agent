---
title: "Chunking"
type: concept
tags: [rag, preprocessing, document]
sources: ["2026-05-21-day29-ai-ml-learning-review"]
last_updated: 2026-05-21
---

# Chunking

## 정의

Chunking은 [[RAG]]에서 긴 문서를 검색하기 좋게 작은 chunk(조각)로 분할하는 과정이다.

## 왜 필요한가

- [[LLM]]의 [[ContextWindow]]는 유한하다
- 전체 문서를 넣으면 비용이 크고 중요한 정보가 묻힐 수 있다
- 작은 chunk为单位로 검색하면 더 정밀한 [[VectorSearch]] 가능

## 고려 사항

| 문제 | 원인 |
|------|------|
| chunk太小 | 문맥 부족 |
| chunk太大 | 필요 없는 내용까지 포함, prompt 혼잡 |

## 전략

- 고정 크기 chunking: 500토큰 단위
- 문장 단위 chunking
- 문단 단위 chunking
-Overlap 있는 chunking: 인접 chunk와 겹치게

## 연관 개념

- [[RAG]] — 주요 활용처
- [[VectorSearch]] — 검색 방식
- [[ContextWindow]] — 입력 제한
- [[EmbeddingModel]] — 벡터 변환

## 출처

- [[2026-05-21-day29-ai-ml-learning-review]]
