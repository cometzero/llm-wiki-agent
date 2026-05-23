---
title: "AI/ML Learning Review — Day 30 (2026-05-23): Evaluation, Serving, and AI System Design"
type: source
tags: [ai-ml, evaluation, serving, inference, system-design]
date: 2026-05-23
source_file: raw/ai_ml_learning/2026-05-23-day30-ai-ml-learning-review.md
source_hash: f8d0b598c3ed97f0
---

## Summary
Day 30 of the AI/ML learning series covers three foundational concepts for transitioning from model development to production AI systems: evaluation and benchmarks for measuring model quality, serving and inference optimization for deployment, and the complete AI system design picture including data pipeline, training stack, inference stack, and feedback loop.

## Key Claims
- Benchmark scores alone do not represent a model's full capability; real-world performance depends on data distribution, latency, cost, safety, and user satisfaction
- Serving and inference optimization require balancing latency, throughput, memory, and quality through techniques like [[Quantization]], [[KVCache]], and batching
- AI systems must be viewed as interconnected loops of data collection, training, evaluation, serving, and user feedback rather than a single model artifact
- LLM evaluation requires both task metrics (accuracy, F1, pass@k) and human evaluation or LLM-as-a-judge due to the open-ended nature of generative outputs

## Key Quotes
> "좋은 benchmark는 실제로 풀고 싶은 문제를 잘 대표해야 한다" — benchmark의 대표성 중요성 강조

> "모델 품질, 속도, 비용, 안정성은 서로 trade-off가 있다" — 서빙 최적화의 핵심 균형

> "좋은 AI 제품은 모델을 잘 학습시키는 것에서 끝나지 않고, 올바르게 평가하고, 빠르고 안정적으로 serving하며, 실제 사용자 feedback으로 계속 개선되는 전체 시스템이다" — Day 30 핵심 요약

## Connections
- [[Evaluation]] — 모델 성능 측정 과정의 핵심 개념
- [[Benchmark]] — 모델 비교를 위한 공통 시험 프레임워크
- [[Serving]] — 학습된 모델을 실제 서비스로 운영하는 것
- [[InferenceOptimization]] — 속도, 메모리, 비용 최적화 기법
- [[Latency]] — 요청부터 응답까지의 대기 시간
- [[Throughput]] — 단위 시간당 처리량
- [[Quantization]] — 모델 가중치 정밀도 감소 기법
- [[KVCache]] — Attention 계산 재사용을 위한 캐싱
- [[DataPipeline]] — 데이터 수집, 정제, 저장 흐름
- [[TrainingStack]] — 모델 학습에 필요한 도구 묶음
- [[InferenceStack]] — 모델 추론을 운영하는 serving 구조
- [[FeedbackLoop]] — 사용자 반응을 개선에 반영하는 순환
- [[RAG]] — 검색 증강 생성 시스템 예시
- [[HumanEvaluation]] — 사람이 직접 평가하는 방식
- [[LLMasJudge]] — LLM을 평가자로 활용하는 방법

## Contradictions
- None identified; this source complements and extends the previous Day 30 (2026-05-22) source with more detailed examples and mathematical foundations.

## Review Questions
1. Why can't we say a model with high benchmark scores is always good for real services?
2. Explain the difference between latency and throughput using a restaurant analogy.
3. Why should we view AI systems as data pipeline, training stack, inference stack, and feedback loop rather than just one model?
