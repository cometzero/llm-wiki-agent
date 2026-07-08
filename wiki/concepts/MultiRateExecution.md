---
title: "Multi-Rate Execution"
type: concept
tags: [VLA, asynchronous, sensor, modality, control]
sources: [embodied-cpp-2607-02501-references, embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
VLA(Vision-Language-Action) 모델에서 서로 다른 modality(visual, language, sensor data)를 하나의 synchronous clock으로 처리하는 문제를 해결하기 위해, modality별 latent buffer를 각 sensor rate에 맞게 refresh하는 asynchronous execution 전략. [[DAM-VLA]]가 제안한 이후 [[Embodied.cpp]]에서도 perception/backbone/action head refresh policy 분리 필요성이 강조된다.

## Key Claims
- Synchronous clock 문제: VLA가 모든 modality를 동일한 주기로 처리하여 비효율 발생
- Asynchronous solution: modality별 latent buffer를 각 sensor rate에 맞게 refresh
- Performance: [[DAM-VLA]]는 100Hz reactive control 달성 보고
- Architecture implication: Embodied.cpp에서 perception/backbone/action head의 분리된 refresh policy 필요

## Related Concepts
- [[DAM-VLA]] — multi-rate execution을 제안한 핵심 논문
- [[VLA]] — 적용 대상 모델 유형
- [[SensorFusion]] — modality 통합 관련
- [[LatencyFirst]] — Embodied.cpp의 latency-first 설계와 연결

## Connections
- [[Embodied.cpp]] — multi-rate execution을 five-layer architecture에서 first-class로 지원
- [[DAM-VLA]] — multi-rate execution 제안 논문
- [[MuseVLA]] — adaptive multimodal sensing 사례
