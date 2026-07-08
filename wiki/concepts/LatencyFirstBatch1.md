---
title: "Latency-First Batch-1 Optimization"
type: concept
tags: [robot-deployment, inference-optimization, latency]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
Latency-First Batch-1 Optimization은 [[VLA]]/[[WAM]]의 로봇 closed-loop 제어를 위한 추론 최적화 접근법이다. Batch processing 대신 batch-1 (single request) 추론에 최적화하여 low latency, low jitter, buffer reuse, backend abstraction을 달성한다.

## Key Properties
- **Batch size**: 1 (실시간 단일 요청 처리)
- **Target**: Low latency + low jitter
- **Techniques**: Buffer reuse, backend abstraction for heterogeneous hardware
- **Goal**: Real-time closed-loop robot control

## Why Not Batching?
일반 LLM serving은 batch processing으로 throughput을 높이지만, 로봇 제어는:
1. Sensor feedback → action output이 반복되는 closed-loop
2. Worst-case latency가 평균 latency만큼 중요
3. Jitter(변동성) 통제가 safety에 영향

## Connections
- [[VLA]] — optimization target
- [[WAM]] — optimization target
- [[ClosedLoopRobot]] — target deployment scenario
- [[FiveLayerRuntime]] — architectural support
