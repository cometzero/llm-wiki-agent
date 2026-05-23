---
title: "Quantization"
type: concept
tags: [ai-ml, optimization, model-compression]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
양자화(quantization)는 weight나 activation의 숫자 정밀도를 낮춰 메모리와 계산 비용을 줄이는 방법이다. 예를 들어 weight를 32-bit float로 저장하면 숫자 하나가 32비트를 쓰지만, 8-bit integer로 줄이면 약 1/4 크기로 줄어든다.

## How It Works
- 32-bit float (FP32) → 16-bit float (FP16) 또는 bf16
- 32-bit float → 8-bit integer (INT8)
- 더 낮은 정밀도로 갈수록 더 큰 압축이지만 품질 손실 증가

## Trade-offs
- **장점**: 메모리 사용량 감소, 계산 속도 향상, 더 많은 요청을 같은 GPU에서 처리 가능
- **단점**: 너무 낮은 정밀도는 모델 품질(정확도, 생성 품질) 하락 가능

## When to Use
- 모바일 AI처럼 메모리와 배터리가 제한적인 환경
- 대규모 API 서비스에서 GPU 비용 절감
- latency와 throughput 개선이 필요한 경우

## Connections
- [[InferenceOptimization]] — 대표적인 최적화 기법
- [[Serving]] — 양자화된 모델을 서빙
- [[Latency]] — 양자화로 latency 감소
- [[Throughput]] — 양자화로 throughput 향상
