---
title: "Inference Optimization"
type: concept
tags: [ai-ml, inference, optimization, serving]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
추론 최적화(inference optimization)는 모델의 품질을 크게 해치지 않으면서 더 빠르게, 더 적은 메모리로, 더 많은 요청을 처리하도록 만드는 방법이다.

## Key Techniques

### Quantization (양자화)
- Weight나 activation의 숫자 정밀도를 낮춤
- 예: 32-bit float → 8-bit integer (약 1/4 크기)
- 속도와 메모리는 좋아지지만 품질이 조금 떨어질 수 있음

### KV Cache
- Transformer attention에서 이전 token들의 key/value 중간값을 저장
- 다음 token 생성 시 재사용하여 계산 낭비 줄임
- "나는 밥을" 다음에 "먹었다"를 생성한 뒤, 다시 전체를 처음부터 계산하지 않음

### Batching
- 여러 요청을 묶어서 한 번에 계산
- GPU를 효율적으로 사용하여 throughput 향상
- 단, batch가 모일 때까지 기다리면 개별 latency 증가 가능

### Other Techniques
- Speculative decoding
- Model parallelism
- Tokenizer/prompt 최적화

## Trade-offs
모델 품질, 속도, 비용, 안정성은 서로 trade-off가 있다. 가장 큰 모델이 항상 서비스에 적합한 것은 아니다. 작은 모델을 잘 fine-tuning하고 [[RAG]]를 붙이는 편이 더 빠르고 안정적일 수 있다.

## Connections
- [[Serving]] — 최적화가 적용되는 영역
- [[Quantization]] — 대표적인 최적화 기법
- [[KVCache]] — attention 최적화 기법
- [[Latency]] — 최적화의 주요 대상
- [[Throughput]] — 최적화의 주요 대상
- [[InferenceStack]] — 최적화가 통합되는 기술 스택
