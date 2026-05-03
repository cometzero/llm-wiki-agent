---
title: "Decode Disaggregation"
type: concept
tags:
  - InferenceOptimization
  - HeterogeneousInference
  - LPU
  - GPU
  - SpeculativeDecoding
sources:
  - nvidia-groq-3-lpx-everything-we-know-storagereview-com
last_updated: 2026-05-03
---

## Definition
디코드 분리는 [[prefill]]/초기 토큰 생성 준비 단계와 매 토큰 디코드 생성 단계를 분리하고, 서로 다른 하드웨어 경로에 할당해 운영 효율과 응답성 균형을 맞추는 추론 아키텍처 전략이다. 본 소스에서는 이를 [[NVIDIA]] GPU와 [[LPU]]의 역할 분리 관점으로 다룬다.

## Core Mechanism
- prefill(large context accumulation) 단계는 GPU가 담당해 KV 캐시/attention 처리 규모의 유연성을 유지.
- 매 토큰 디코드 단계는 LPX 같은 FFN/MoE 처리 엔진으로 이동해 latency-sensitive 응답 경로를 정교화.
- 중간 활성화는 토큰 단위로 전환되어 GPU-LPU 간 왕복되며, [[NVIDIADynamo]]가 전환 오케스트레이션을 수행.

## Why It Matters
문맥 길이가 증가할수록 prefill 비용 증가곡선이 가파른 반면, FFN/MoE 연산량은 문맥 길이와 선형적으로 비례하지 않아, 문맥 독립 비용을 LPX에 고정적으로 맡기는 설계가 유효하다는 주장.

## Connections
- [[HeterogeneousInference]] — 이 전략의 상위 아키텍처.
- [[NVIDIADynamo]] — 분리된 디코드 루프의 운영 레이어.
- [[DeterministicExecution]] — 디코드 구간의 예측 가능성 개선.
- [[SpeculativeDecoding]] — LPX draft / GPU verifier 분리로 확장.