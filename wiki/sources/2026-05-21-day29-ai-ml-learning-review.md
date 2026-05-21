---
title: "AI/ML Learning Review — Day 29 (2026-05-21): RAG, Embedding Search, Prompt Engineering"
type: source
tags: [llm, rag, embedding, prompt-engineering, ai-systems]
date: 2026-05-21
source_file: raw/ai_ml_learning/2026-05-21-day29-ai-ml-learning-review.md
source_hash: 99674dcc1ddd7744
---

## Summary
3개의 핵심 AI 시스템 개념을 통합적으로 정리: [[RAG]]의 검색-생성 결합 구조, [[EmbeddingModel]]과 [[VectorSearch]]의 의미 기반 검색 원리, [[PromptEngineering]]의 역할과 한계. 이 세 개념이 어떻게 "LLM + 검색 시스템 + 문서 저장소 + prompt 구성"으로 실제 AI 서비스 시스템을 구성하는지 설명한다.

## Key Claims
- [[RAG]]는 "찾기(retrieval)"와 "쓰기(generation)"를 분리하여 모델 파라미터外面的 최신 정보를 활용하는 핵심 패턴이다
- [[EmbeddingModel]]은 문장의 "의미"를 숫자 벡터로 표현하여 키워드가 달라도 관련 문서를 검색할 수 있게 한다
- [[PromptEngineering]]은 [[LLM]]의 답변 방향과 형식을 조절하는 인터페이스이지만, 모델이 모르는 지식을 만들지는 못한다
- [[Hallucination]]은 모델이 거짓말을 하려는 것이 아니라, 다음 토큰을 자연스럽게 예측하다 보니 없는 내용을 진짜처럼 만들 수 있는 현상이다
- [[FineTuning]]과 [[RAG]]는 다르다: fine-tuning은 모델 weight를 바꾸고, [[RAG]]는 입력 context를 바꾼다

## Key Quotes
> "RAG는 [[LLM]]에게 '기억만 믿고 답하지 말고, 먼저 관련 자료를 찾아본 뒤 그 자료를 보고 답하게 하는 방식'입니다."

> "Embedding model은 문장의 '겉으로 보이는 단어'만 보는 것이 아니라, 문장의 '의미'를 숫자 vector로 표현합니다."

> "Prompt engineering은 마법 주문이 아닙니다. 모델이 가진 능력과 입력 정보의 범위 안에서 결과를 조절합니다."

## Connections
- [[RAG]] — 오늘의 핵심 개념, 검색-생성 결합 시스템
- [[EmbeddingModel]] — [[VectorSearch]]의 기반 기술
- [[VectorSearch]] — [[RAG]]의 retrieval 단계核心技术
- [[PromptEngineering]] — [[RAG]]와 결합하여 답변 품질 조절
- [[LLM]] — generation을 담당하는 핵심 모델
- [[Hallucination]] — [[RAG]]가 해결하려는 문제 중 하나
- [[FineTuning]] — [[RAG]]와 비교되는 모델 파라미터 변경 방식
- [[ToolUse]] — prompt engineering의 한계를 보완하는 방법
- [[ContextWindow]] — [[LLM]]의 입력 길이 제한
- [[Chunking]] — [[RAG]]에서 긴 문서를 검색하기 좋게 분할하는 과정

## Contradictions
없음. 이전 wiki 콘텐츠와 일치하며 기존 [[LLM]] 관련 페이지를 보완하는 내용이다.
