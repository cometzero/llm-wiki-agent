---
title: "NVIDIA Dynamo"
type: entity
tags:
  - NVIDIA
  - orchestration
  - inference
  - scheduling
sources:
  - inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform
last_updated: 2026-05-03
---

## Overview
[[NVIDIADynamo]]는 heterogeneous inference 운영을 가능하게 하는 오케스트레이션 소프트웨어 계층이다. GPU와 [[Groq3LPX]] 같은 이종 backend 간 prefill/decode 경로를 분리하고 routing, scheduling, activation 이동을 조정한다.

## Key Responsibilities
- 요청의 latency/throughput 요구에 따라 [[VeraRubinPlatform]](또는 유사 GPU path)와 LPX path로 분기.
- interactive session에서 긴 queueing 지연과 tail latency 확산을 줄이기 위한 저오버헤드 경로 관리.
- KV-aware routing 및 중간 activation 교환의 반복 루프 운영 제어.

## Value
- 동일 인프라에서 ai factory throughput과 사용자 체감 responsiveness를 동시에 다루려는 시스템에서 운영 안정성의 핵심 제어점이다.

## Related Pages
- [[HeterogeneousInference]]
- [[DisaggregatedPrefill]]
- [[InteractiveInference]]
- [[SpeculativeDecoding]]
- [[VeraRubinPlatform]]
- [[Groq3LPX]]