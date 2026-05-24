---
title: "Quantization"
type: concept
tags: [ai-ml, optimization, memory, inference]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[Quantization]]은 모델의 숫자 표현 bit 수를 줄여 메모리와 비용을 낮추는 기법이다. 예를 들어 FP16(16-bit) 가중치를 INT8(8-bit)으로 변환하여 메모리를 약 절반으로 줄인다.

## Key Concepts

### How it Works
- 원래 가중치 하나를 16-bit로 저장 → 8-bit로 줄이면 메모리 약 50% 절감
- 1,000개 숫자 × 16-bit = 16,000bit → 1,000개 × 8-bit = 8,000bit

### Trade-offs
- 메모리 감소 + 속도 향상 가능
- 품질 손실(정밀도 감소) 가능성
- 특히 수학, 코드, 긴 추론 작업에서 정밀도 손실이 민감할 수 있음

### Common Formats
- FP32 → FP16 → BF16 → INT8 → INT4 등 다양한 precision 수준

## Connections
- [[Serving]] — 메모리/비용 최적화
- [[InferenceOptimization]] — 핵심 최적화 기법
- [[Latency]] — 속도 향상 가능

## Practical Notes

70B 모델을 FP16으로 올리면 GPU 메모리 매우 크게 필요. [[Quantization]]으로 memory burden 경감 가능하지만, 너무 aggressive하면 출력 품질 저하 발생.
