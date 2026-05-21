---
title: "RAG"
type: concept
tags: [llm, retrieval, generation, ai-systems]
sources: ["2026-05-21-day29-ai-ml-learning-review"]
last_updated: 2026-05-21
---

# RAG (Retrieval-Augmented Generation)

## 정의

RAG는 **Retrieval-Augmented Generation**의 약자로, "검색(retrieval)으로 보강(augmentation)한 생성(generation)"을 의미한다. [[LLM]]이 문장을 만들어 답하는 generation能力과, 질문과 관련 있는 문서를 찾아오는 retrieval 과정을 결합한 방식이다.

## 핵심 원리

RAG는 "찾기"와 "쓰기"를 분리한다:
- **Retrieval**: 관련 문서를 검색하는 단계
- **Generation**: 검색된 문서를 바탕으로 [[LLM]]이 답변을 생성하는 단계

## 왜 필요한가

1. **학습 시점 이후 정보 부족**: [[LLM]]은 학습 데이터 이후의 정보를 모른다
2. **[[Hallucination]] 감소**: 근거 없는 답변을 줄일 수 있다
3. **비용 효율**: 매일 [[FineTuning]]하는 것보다 문서 저장소만 업데이트

## RAG 파이프라인

1. **문서 준비**: PDF, 웹페이지, 매뉴얼, FAQ 수집
2. **[[Chunking]]**: 긴 문서를 작은 chunk로 분할
3. **[[Embedding]]**: 각 chunk를 [[EmbeddingModel]]로 벡터 변환
4. **저장**: [[VectorDatabase]]에 저장
5. **질문 처리**: 사용자 질문을 벡터로 변환
6. **Retrieval**: 질문 벡터와 가까운 문서 벡터 검색
7. **Prompt 구성**: 검색된 문서를 [[LLM]] prompt에 삽입
8. **Generation**: [[LLM]]이 답변 생성

## [[RAG]] vs [[FineTuning]]

| 구분 | [[RAG]] | [[FineTuning]] |
|------|---------|-----------------|
| 변경 대상 | 입력 [[Context]] | 모델 [[Weight]] |
| 업데이트 주기 | 문서만 업데이트 | 모델 재학습 |
| 비용 | 낮음 | 높음 |

## 연관 개념

- [[EmbeddingModel]] — 문서를 벡터로 변환
- [[VectorSearch]] — 관련 문서 검색
- [[Chunking]] — 문서 분할
- [[PromptEngineering]] — 검색된 문서 활용 방식 설계
- [[ContextWindow]] — 입력 길이 제한

## 출처

- [[2026-05-21-day29-ai-ml-learning-review]]
