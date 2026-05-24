---
title: "AI/ML Learning Review — Day 30 (2026-05-24): Evaluation, Serving, and AI System Design"
type: source
tags: [ai-ml, evaluation, serving, inference-optimization, system-design]
date: 2026-05-24
source_file: raw/ai_ml_learning/2026-05-24-day30-ai-ml-learning-review.md
source_hash: 92fdc2b86c8aa369
---

## Summary
Day 30 마일스톤으로 [[Evaluation]]과 [[Benchmark]], [[Serving]]과 [[InferenceOptimization]], 그리고 AI 시스템 설계의 전체 그림을 통합 정리한다. 좋은 모델 하나만으로는 실제 AI 제품이 완성되지 않으며, 평가로 품질을 확인하고, 서빙으로 빠르게 제공하며, [[FeedbackLoop]]로 계속 개선되는 전체 구조가 필요함을 강조한다.

## Key Claims
- [[Benchmark]] 점수가 높아도 실제 서비스에서 모델이 항상 좋은 것은 아니다. data contamination, 실제 사용자와 benchmark 문제의 불일치 등이 원인이다.
- [[Serving]]은 학습된 모델을 실제 사용자가 부를 수 있게 운영하는 일이며, [[InferenceOptimization]]은 더 빠르고 싸게 답하도록 만드는 기술이다.
- LLM [[Serving]]에서 [[KVCache]]는 이전 token의 attention 정보를 재사용하여 중복 계산을 줄이는 핵심 최적화 기법이다.
- AI 시스템은 [[DataPipeline]], [[TrainingStack]], [[InferenceStack]], [[FeedbackLoop]] 네 층이 모두 연결되어야 안정적으로 작동한다.
- [[Latency]]는 요청 하나에 대한 체감 대기 시간이고, [[Throughput]]은 전체 시스템의 처리량이다. 둘은 같은 개념이 아니다.

## Key Quotes
> "모델 성능만 보고 시스템을 만들면 실제 운영에서 자주 막힌다. 문제는 모델 구조 하나가 아니라 데이터, 전처리, 평가, 서빙, 모니터링 전체에 있다."

> "LLM은 답변을 한 토큰씩 생성하기 때문에 KV cache를 잘 쓰지 않으면 이미 계산한 attention 정보를 계속 다시 계산하게 되어 매우 비효율적이다."

> "현대 AI 엔지니어링은 모델 이해와 시스템 이해가 함께 필요하다."

## Connections
- [[Evaluation]] — 오늘의 핵심 개념 1: 모델 성능 측정
- [[Benchmark]] — 표준화된 평가 세트로 모델 비교
- [[Serving]] — 학습된 모델을 제품에서 운영
- [[InferenceOptimization]] — 추론 속도와 비용 최적화 기법
- [[Latency]] — 개별 요청 응답 시간
- [[Throughput]] — 시스템 전체 처리량
- [[Quantization]] — 모델 숫자 표현 bit 수 줄여 메모리/비용 절감
- [[KVCache]] — Transformer attention 계산 결과 재사용 캐시
- [[DataPipeline]] — 데이터 수집·정리·저장 흐름
- [[TrainingStack]] — 모델 학습 인프라 (loss, gradient, optimizer)
- [[InferenceStack]] — 모델 추론/서빙 인프라
- [[FeedbackLoop]] — 사용자 반응 → 개선으로의 순환 구조

## Contradictions
- 기존 Day 30 (2026-05-22, 2026-05-23) 소스와 동일한 주제를 다루나, 오늘 날짜(2026-05-24)의 최종 버전으로 업데이트. 기존 페이지의 내용을 this source로 대체 권장.
