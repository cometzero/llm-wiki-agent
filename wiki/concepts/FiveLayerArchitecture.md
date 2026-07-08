---
title: "Five-layer Architecture"
type: concept
tags: [software-architecture, modular-design, embodied-ai]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Definition
Embodied.cpp에서 제안하는 다섯 계층 아키텍처로, 다양한 VLA/WAM architecture를 하나의 backend abstraction으로 지원한다.

## Layers

### 1. Input Adapters
- Online sensor stream 흡수
- Offline dataset sample 처리
- Camera, force/tactile, IMU, proprioception, simulator state 지원

### 2. Sequence Builders
- Heterogeneous input을 model-specific sequence로 assembling
- VLA/WAM input format 변환

### 3. Backbone Execution
- Shared execution path
- VLA와 WAM 모두 하나의 backend abstraction으로 실행
- Transformer block 기반 computation

### 4. Head Plugins
- Model-specific action head
- Pluggable design
- Discrete/continuous action generation

### 5. Deployment Adapters
- Simulator 연결(ManiSkill, LIBERO, Isaac Sim)
- Robot software stack 연결
- Platform-specific output format

## Design Philosophy
- 공통 경로는 infrastructure로, 달라지는 부분은 plugin으로 분리
- Stable core + pluggable task-specific component

## Connections
- [[Embodied-cpp]] — 적용 런타임
- [[VLA]] — 타겟 모델
- [[WAM]] — 타겟 모델
- [[ModularArchitecture]] — 설계 원칙
