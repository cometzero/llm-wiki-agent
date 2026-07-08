---
title: "Heterogeneity-Aware Orchestration"
type: concept
tags: [heterogeneous-hardware, inference-planning, memory-management, edge]
sources: [embodied-cpp-2607-02501-references]
last_updated: 2026-07-08
---

## Overview
여러 유형의 hardware(CPU, GPU, NPU 등)를 효율적으로 활용하기 위한 inference planning 기법. [[H2O]]에서 제안된 것으로, 모델 weight orchestration, I/O-compute parallelism, memory-efficient execution을 포함한다.

## Key Claims
- Problem: heterogeneous device 환경에서 효율적인 inference planning 필요
- Solution: hierarchical weight orchestration
- Optimization: zero-copy I/O-compute parallelism
- Target: memory-efficient on-device LLM inference
- Embodied.cpp 적용: heterogeneous device support의 핵심 요소

## Related Concepts
- [[OnDeviceInference]] — 상위 도메인
- [[H2O]] — 제안 논문
- [[MemoryManagement]] — 핵심 자원
- [[InferencePlanning]] — planning 대상

## Connections
- [[Embodied.cpp]] — heterogeneous device support 구현
- [[H2O]] — theoretical background
- [[NPU]] — target hardware
