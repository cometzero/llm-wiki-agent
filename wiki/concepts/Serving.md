---
title: "Serving"
type: concept
tags: [ai-ml, serving, inference, deployment]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
서빙(serving)은 학습이 끝난 모델을 실제 사용자가 쓸 수 있게 제공하는 전체 과정이다. 모델 파일을 서버에 올리고, API를 만들고, 여러 사용자의 요청을 처리하며, 속도와 비용을 관리하는 일이 포함된다.

## Serving Components
1. **모델 로딩**: 학습된 weight를 GPU/CPU 메모리에 올림
2. **입력 전처리**: 텍스트를 token으로, 이미지를 tensor로 변환
3. **Forward Pass**: 모델이 입력을 layer별로 계산
4. **Decoding**: LLM은 다음 token을 하나씩 예측 (greedy, sampling, beam search)
5. **동시 요청 처리**: 여러 요청을 batch로 묶어 GPU 효율적으로 사용

## Serving vs Inference
- **Inference**: 모델이 입력을 받아 예측/답변을 만드는 과정
- **Serving**: inference를 실제 서비스 형태로 제공하는 것

## Key Metrics
- **Latency**: 요청 하나가 들어와서 응답이 나올 때까지 걸리는 시간
- **Throughput**: 단위 시간에 처리할 수 있는 요청 수 또는 token 수

## Connections
- [[InferenceOptimization]] — 서빙 최적화 기법
- [[Latency]] — 응답 대기 시간
- [[Throughput]] — 처리량
- [[Quantization]] — 메모리/속도 최적화
- [[KVCache]] — attention 계산 재사용
- [[InferenceStack]] — 서빙을 운영하는 기술 스택
