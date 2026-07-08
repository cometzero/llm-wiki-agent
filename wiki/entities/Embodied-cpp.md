---
title: "Embodied.cpp"
type: entity
tags: [inference-runtime, C++, embodied-ai, edge-computing]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
Embodied.cpp는 VLA(Vision-Language-Action) 모델과 WAM(World-Action Model)을 이기종 edge device에서 실행하기 위한 휴대형 C++ 추론 런타임이다. SEU-PAISys 연구팀이 개발했으며, GitHub에서 공개되어 있다.

## Key Features
- **Modular Multi-rate Execution**: 서로 다른 refresh frequency를 가진 component 분리
- **Latency-first Fused Execution**: batch-1 inference 최적화, heterogeneous hardware 지원
- **Extensible Operator and I/O Support**: camera, tactile, IMU, proprioception 등 다양한 센서 입력 지원

## Five-Layer Architecture
1. [[InputAdapters]]
2. [[SequenceBuilders]]
3. [[BackboneExecution]]
4. [[HeadPlugins]]
5. [[DeploymentAdapters]]

## Evaluation
- HY-VLA: 100.0% task success rate
- π0.5: 91.0% task success rate
- WAM Q4_K: 3.6× memory reduction (312.2 → 88.1 MiB)

## Links
- GitHub: https://github.com/SEU-PAISys/Embodied.cpp
- arXiv: https://arxiv.org/abs/2607.02501
