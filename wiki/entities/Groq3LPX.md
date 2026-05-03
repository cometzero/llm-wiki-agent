---
title: "Groq3LPX"
type: entity
tags:
  - NVIDIA
  - inference
  - accelerator
  - heterogeneous-inference
  - low-latency
sources:
  - inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform
last_updated: 2026-05-03
---

## Overview
[[Groq3LPX]]는 [[NVIDIA]]의 [[VeraRubinPlatform]]에서 low-latency interactive inference를 전담하는 rack-scale 추론 가속기 라인이다. 목표는 throughput 중심 추론과 latency-critical token-by-token loop를 분리해 운영 효율을 높이는 것이다.

## Core Role
- [[VeraRubinPlatform]]의 높은 처리량 경로와 분담해 interactive path를 구성한다.
- [[NVIDIA Groq 3 LPU]]를 기반으로 하드웨어+컴파일러 수준의 deterministic scheduling을 제공한다.
- [[NVIDIADynamo]] 조합에서 prefill/decode 경로 분리를 통해 응답성 개선에 기여한다.

## Architecture Notes
- 256개 이상 LPX rack 구성(소스에서 제시된 표 기준)을 중심으로 chip 간 C2C 통신과 스케일업 통신 대역폭을 강조한다.
- on-chip SRAM 중심 설계(고대역폭)와 explicit data movement 전략이 latency variation을 낮추는 데 사용된다.

## Operational Economics
- 소스는 [[VeraRubinPlatform]]과 결합 시 AI factory 수준의 throughput을 유지하면서 premium 응답성 구간에서의 효율/수익 확장 잠재력을 제시한다.

## Related Pages
- [[VeraRubinPlatform]]
- [[HeterogeneousInference]]
- [[InteractiveInference]]
- [[DeterministicExecution]]
- [[NVIDIADynamo]]
- [[SpeculativeDecoding]]