---
title: "Embodied Interface"
type: concept
tags: [embodied-ai, I/O-interfaces, sensor-integration]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Definition
Embodied AI 런타임에서 사용하는 확장 가능한 입력/출력 인터페이스. 고정 token I/O를 넘어서 다양한 센서 입력과 동작 출력을 지원한다.

## Input Types
- **Image**: camera stream
- **Language**: instruction, natural language command
- **Proprioception**: robot joint states
- **History**: past actions, observations
- **Force/Tactile**: contact sensing
- **IMU**: inertial measurement
- **Simulator State**: virtual environment state

## Output Types
- **Discrete Action Token**: autoregressive generation
- **Continuous Action Vector**: direct control
- **Action Chunk**: buffered future actions
- **Predicted Future**: world model prediction
- **Latent Future**: compact latent representation

## Implementation in Embodied.cpp
- Typed interface abstraction
- Pluggable head design
- Operator/kernel warehouse

## Connections
- [[Embodied-cpp]] — 구현 사례
- [[VLA]] — 적용 모델
- [[WAM]] — 적용 모델
