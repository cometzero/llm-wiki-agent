---
title: "Five-Layer Runtime"
type: concept
tags: [robot-deployment, inference-runtime, architecture]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
Five-Layer Runtime은 [[VLA]]와 [[WAM]]을 로봇 edge에 배포하기 위한 C++ 런타임 아키텍처다. Input adapters, Sequence builders, Backbone execution, Head plugins, Deployment adapters 다섯 계층으로 구성된다.

## Layer Breakdown

| Layer | Description |
|---|---|
| Input adapters | Camera, tactile, IMU, proprioception 등 다양한 센서 입력을 표준화 |
| Sequence builders | 시퀀스 구성 및 컨텍스트 버퍼링 |
| Backbone execution | 메인 모델 추론 실행 |
| Head plugins | Action prediction head, world prediction head 등 확장 |
| Deployment adapters | Robot/simulator/controller 연동 어댑터 |

## Runtime Capabilities
- **Multi-rate execution**: 각 레이어별 다른 refresh rate 스케줄링
- **Latency-first fused execution**: low latency/low jitter 최적화
- **Extensible embodied I/O**: 로봇 특화 입출력 확장성
- **Kernel/operator warehouse**: 커널 및 연산자 공유

## Connections
- [[VLA]] — runtime target model type
- [[WAM]] — runtime target model type with future prediction
- [[EmbodiedCpp]] — implementation of this architecture
- [[MultiRateExecution]] — key capability
