---
title: "Inference Optimization"
type: concept
tags: [ai-ml, inference, optimization, mlops]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[InferenceOptimization]]은 모델이 더 빠르고 싸게 추론하도록 만드는 기술이다. [[Latency]] 줄이기, [[Throughput]] 늘리기, [[Quantization]], [[Batching]], [[KVCache]], GPU 메모리 관리 등을 포함한다.

## Key Concepts

### Core Metrics
- **[[Latency]]**: 요청 하나가 들어와 결과가 나올 때까지 걸리는 시간
- **[[Throughput]]**: 단위 시간에 처리할 수 있는 요청 수나 token 수 (requests/sec, tokens/sec)
- **[[Latency]]** vs **[[Throughput]]** 구분 중요: 한 사람에게 빨리 답하는 것과 많은 사람을 동시에 처리하는 것은 다름

### Optimization Techniques
1. **[[Quantization]]**: 숫자 표현 bit 수 줄이기 (FP16 → INT8 등), 메모리 약 절반 절감
2. **[[KVCache]]**: 이전 token의 key/value 저장하여 attention 재계산 방지
3. **[[Batching]]**: 여러 요청 묶어 GPU에서 동시 처리, throughput 향상
4. **Model routing**: 쉬운 질문은 작은 모델, 어려운 질문은 큰 모델

### Trade-offs
- [[Quantization]]은 무조건 공짜 성능 향상 아님: 품질 흔들릴 수 있음, 특히 수학/코드/긴 추론에서 민감
- [[Batching]]은 throughput는 높이지만 개별 latency 증가 가능

## Connections
- [[Serving]] — inference optimization의 적용 대상
- [[Latency]] — 최적화 핵심 지표
- [[Throughput]] — 최적화 핵심 지표
- [[Quantization]] — 메모리/비용 최적화 기법
- [[KVCache]] — attention 계산 최적화

## Practical Notes

실제 운영에서는 "가장 똑똑한 모델 하나"만 쓰지 않을 때도 많다. 쉬운 질문은 작은 모델이 처리하고, 어려운 질문만 큰 모델로 보내는 routing으로 품질과 비용 사이 균형 잡기.
