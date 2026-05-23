---
title: "Inference Stack"
type: concept
tags: [ai-ml, system-design, serving]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
Inference stack은 학습된 모델을 실제 요청에 응답하도록 운영하는 serving 구조이다. 모델을 API로 배포하고 실제 요청을 처리하며, serving, batching, KV cache, quantization, monitoring이 포함된다.

## Components
1. **모델 배포**: 학습된 weight를 서버에 올림
2. **API 서버**: 사용자 요청을 받아 모델에 전달
3. **Batching**: 여러 요청을 묶어 GPU 효율화
4. **KV Cache**: attention 계산 재사용
5. **Quantization**: 메모리/속도 최적화
6. **Monitoring**: latency, error rate, 품질 관찰

## Key Metrics
- [[Latency]]: 응답 시간
- [[Throughput]]: 처리량
- Error rate: 실패율
- Cost per request: 요청당 비용

## Connections
- [[TrainingStack]] — 학습된 모델의 도착지
- [[Serving]] — inference stack의 핵심 기능
- [[InferenceOptimization]] — 최적화 기법 적용
- [[FeedbackLoop]] — 모니터링 결과가 개선에 반영
