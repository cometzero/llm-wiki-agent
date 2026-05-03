---
title: "An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog"
type: source
tags:
  - LLM
  - InferenceOptimization
  - SpeculativeDecoding
  - NVIDIA
  - EAGLE3
  - DeepSeek
  - TensorRTModelOptimizer
  - Latency
date: 2026-05-03
source_file: raw/Nvidia/LilysAI/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference-nvidia-technical-blog.md
last_updated: 2026-05-03
sources:
  - an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference-nvidia-technical-blog
---

## Summary
이 문서는 [[SpeculativeDecoding]]을 통해 [[LLM]] 추론 지연 시간을 줄이는 핵심 동작 원리를 정리한다. [[NVIDIA]]는 경량 드래프트 경로와 더 큰 타겟 검증 경로를 결합해 여러 토큰을 한 번에 제안/검증하도록 설계해, 기존 자기회귀의 단계별 토큰 생성 병목을 완화한다. 

드래프트-타겟 방식은 후보 토큰을 여러 개 생성한 뒤 [[TargetModel]]이 단일 포워드 패스로 이 후보를 검증하고, 일치 확률이 높은 최장 접두사만 채택한다. 이 과정은 출력 품질을 유지하면서 처리량과 체감 응답 속도를 동시에 개선하는 방향으로 동작한다. 

또한 문서는 [[DraftTarget]] 구조의 진화형으로 [[EAGLE3]]의 피처 기반 자체 드래프팅, 그리고 [[DeepSeek]]의 MTP(Multi-Token Prediction)와 같은 다중 토큰 예측 기반 기법을 비교한다. 마지막으로 구현 실습은 [[TensorRTModelOptimizer]] 파이프라인을 통해 실제 모델 적용 방향을 제시한다.
