---
title: "FP8"
type: concept
tags:
  - Precision
  - TensorCores
  - AI
  - Inference
  - Training
sources:
  - nvidia-hopper-아키텍처-심층-분석하기-nvidia-technical-blog
last_updated: 2026-05-03
---

## Definition
[[FP8]]는 8비트 부동소수점 표현군으로, [[Hopper]] 시대에서 특히 대규모 AI 연산에서 메모리/처리 효율을 개선하기 위해 활용된다.

## 형식과 동작
- 이 소스에서 [[FP8]]는 두 가지 입력 서식(예: E4M3, E5M2 성격의 구성)을 전제로, 메모리 사용량 절감과 처리량 증가를 도모한다.
- [[TransformerEngine]]는 [[FP16]]/[[BF16]]와 함께 동적 사용 전략을 통해 정확도와 속도의 균형을 맞춘다.

## 역할
- 메모리 대역폭 비용이 큰 대형 모델에서 저장·이동 부담을 낮춘다.
- 텐서 연산 throughput을 높이고, 특히 LLM 추론/훈련에서 지연·비용 측면에 영향이 크다.

## 위키 연결
- [[TensorCores]]
- [[TransformerEngine]]
- [[H100]]
- [[Precision]]
