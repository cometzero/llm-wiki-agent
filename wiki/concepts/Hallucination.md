---
title: "Hallucination"
type: concept
tags: [llm, reliability, generation]
sources: ["2026-05-21-day29-ai-ml-learning-review", "2026-05-19-day27-ai-ml-learning-review"]
last_updated: 2026-05-21
---

# Hallucination

## 정의

Hallucination(환각)은 [[LLM]]이 근거 없는 내용을 그럴듯하게 생성하는 현상이다.

## 왜 발생하는가

모델이 "거짓말을 하려는 것이 아니라", 다음 토큰을 자연스럽게 예측하다 보니 없는 내용을 진짜처럼 만들 수 있다.

## 주요 원인

1. **학습 데이터에 없는 정보**: 학습 시점 이후의 데이터
2. **모델의 확률적 생성**: 다음 token 확률분포 기반 생성
3. **문맥 부족**: 충분한 정보 없이 추측

## 완화 방법

- **[[RAG]]**: 검색된 문서를 근거로 답변 생성
- **[[PromptEngineering]]**: "제공된 context에 없는 내용은 추측하지 마라"
- **[[Calibration]]**: 모델의 불확실성 인식
- **[[Grounding]]**: 외부 지식과 연결

## [[FineTuning]]과 [[RAG]]의 비교

| 구분 | [[RAG]] | [[FineTuning]] |
|------|---------|-----------------|
| Hallucination 완화 | ✅ 검색된 문서 기반 | ⚠️ 패턴 학습 |
| 최신 정보 반영 | ✅ 즉시 | ❌ 재학습 필요 |

## 연관 개념

- [[RAG]] — 완화 방법
- [[PromptEngineering]] — 지시 설계
- [[Calibration]] — 불확실성 인식
- [[Grounding]] — 외부 연결
- [[ContextWindow]] — 입력 제한

## 출처

- [[2026-05-21-day29-ai-ml-learning-review]]
- [[2026-05-19-day27-ai-ml-learning-review]]
