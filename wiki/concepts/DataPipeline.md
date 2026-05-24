---
title: "Data Pipeline"
type: concept
tags: [ai-ml, data, mlops, system-design]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[DataPipeline]]은 원천 데이터가 정리되어 학습이나 검색에 쓸 수 있는 형태로 되는 흐름이다. 데이터 수집, 중복 제거, 개인정보 처리, label 부착, train/validation/test 분리, RAG에서는 문서 chunking과 embedding 저장을 포함한다.

## Key Concepts

### Pipeline Stages
1. 데이터 수집 (웹 크롤링, 로그 수집, 문서 모으기 등)
2. 정제 (중복 제거, 노이즈 필터링)
3. 개인정보 처리 (anonymization)
4. Labeling (필요시)
5. Split (train/validation/test)
6. (RAG 경우) Chunk → Embedding → Vector DB 저장

### Importance
- 데이터가 나쁘면 모델이 좋아지기 어렵다
- [[TrainingStack]]의 품질은 [[DataPipeline]]에 의존
- [[Evaluation]]의 품질도 적절한 평가 데이터 분리 필요

## Connections
- [[TrainingStack]] — 학습의 재료 공급
- [[InferenceStack]] — 추론 시 데이터 공급 (RAG 등)
- [[FeedbackLoop]] — 실패 사례 데이터 재收集
- [[Evaluation]] — 평가 데이터 준비

## Practical Notes

AI 고객상담 봇 예시: 회사 FAQ, 환불 정책, 배송 안내 문서를 모으고 → 너무 긴 문서는 chunk로 나누고 → embedding 만들어 vector DB에 저장 = [[DataPipeline]]의 일부.
