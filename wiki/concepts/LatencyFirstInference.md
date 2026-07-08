---
title: "Latency-first Fused Inference"
type: concept
tags: [inference-optimization, edge-computing, real-time-systems]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Definition
로봇 deployment에서 throughput이 아닌 stable control performance를 목표로 하는 최적화 전략. 낮은 latency, 낮은 jitter, heterogeneous edge hardware에서의 효율적 batch-1 execution을 우선한다.

## Key Challenges
1. **Batch-1 Inference**: 단일 robot 또는 simulator가 action을 지속적으로 받아야 함
2. **Heterogeneous Hardware**: Jetson, RK-based platform, x86 edge box, workstation 등
3. **Small-batch Optimization**: backend-specific fusion, graph replay, buffer reuse
4. **Host-Device Data Movement**: 최적화 필요

## Optimization Techniques
- **Graph Replay**: 실행 그래프 재사용
- **Buffer Reuse**: 메모리 할당 최소화
- **Operator Fusion**: 커널 융합
- **Backend-specific Dispatch**: 하드웨어별 최적화 경로

## Connections
- [[Embodied-cpp]] — 구현 사례
- [[EdgeInference]] — 적용 분야
- [[ClosedLoopControl]] — 목표 시나리오
- [[Quantization]] — memory reduction 기법(Q4_K)
