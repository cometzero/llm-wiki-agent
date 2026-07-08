---
title: "Heterogeneous Scheduling"
type: concept
tags: [robot-deployment, hardware-acceleration, scheduling]
sources: [embodied-cpp-2607-02501]
last_updated: 2026-07-08
---

## Overview
Heterogeneous Scheduling은 [[VLA]]/[[WAM]] 런타임에서 action head, perception encoder, world prediction branch를 서로 다른 NPU/accelerator device에 나누어 실행하는 스케줄링 전략이다.

## Why Heterogeneous?
- Action head: 낮은 연산량, 빠른 응답 필요
- Perception encoder: 높은 연산량, 병렬 처리 가능
- World prediction branch: 중간 수준의 연산, 배치 가능

## Key Considerations
1. **Device affinity**: 각 모듈의 특성에 맞는 가속기 선택
2. **Data transfer**: device 간 통신 비용
3. **Synchronization**: multi-rate execution과의 조화
4. **Power efficiency**: edge 환경에서의 에너지 관리

## Connections
- [[VLA]] — scheduling target
- [[WAM]] — scheduling target with multiple branches
- [[MultiRateExecution]] — temporal coordination
- [[EmbodiedCpp]] — runtime support for heterogeneous execution
