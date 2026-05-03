---
title: "VeraRubin Platform"
type: entity
tags:
  - NVIDIA
  - GPU
  - AIInfrastructure
  - platform
  - inference
sources:
  - inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform
last_updated: 2026-05-03
---

## Overview
[[VeraRubinPlatform]]은 [[NVIDIA]]의 랙 단위 AI 인프라 라인으로, 높은 throughput의 context-heavy 추론을 처리하는 기반이 된다. 본 소스에서 NVL72는 유연하고 범용적인 workhorse로 설명되며, 대용량 prefill 및 attention 경로에 강점이 있다.

## Role in Heterogeneous Inference
- [[Groq3LPX]]와 결합해 [[HeterogeneousInference]]를 구성한다.
- 긴 context input을 위한 prefill/attention 처리에서 효율성과 처리량을 담당한다.
- LPX가 빠른 decode loop를 보완해 interactive session 품질을 높인다.

## Relationship to Software
- [[NVIDIADynamo]]의 prefill/decode 오케스트레이션에서 핵심 backend node로 위치한다.
- 고동시성, 요청 패턴 변동, 사용자별 latency 요구가 큰 환경에서 [[DisaggregatedPrefill]] 성격의 운영 설계가 유효하다.

## Related Pages
- [[Groq3LPX]]
- [[NVIDIADynamo]]
- [[HeterogeneousInference]]
- [[InteractiveInference]]
- [[SpeculativeDecoding]]