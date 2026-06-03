---
title: "Embodied Benchmark"
type: concept
tags: [benchmark, robotics, embodied-AI]
sources: [robosemanticbench-2606-02277-ko, physbrain-1-0-2605-15298-learning, embodiedmidtrain-2604-20012-study-guide]
last_updated: 2026-06-03
---

## Definition

Embodied Benchmark는 물리적 agent가 환경과 상호작용하는 태스크로 [[VLA]]/[[RobotFoundationModel]]의 능력을 평가하는 benchmark이다.

## Existing Benchmarks

| Benchmark | Focus | Limitation |
|-----------|-------|------------|
| [[CALVIN]] | Multi-task manipulation | 짧은 instruction template |
| [[LIBERO]] | Task generalization | semantic reasoning 분리 어려움 |
| [[SimplerEnv]] | Manipulation | visual shortcut 가능 |
| [[RoboSemanticBench]] | Semantic grounding | **신규: semantic/action 분리** |

## RoboSemanticBench의 차별점

기존 benchmark와 달리 [[RoboSemanticBench]]는:
1. Question-Answer 블록 선택으로 semantic reasoning 요구
2. Motor execution과 semantic decision을 분리
3. nSG metric으로 semantic grounding만 측정

## Related Concepts

- [[RoboSemanticBench]] — semantic grounding 특화 benchmark
- [[VLA]] — 평가 대상
- [[SemanticGrounding]] — 핵심 측정 대상
- [[CALVIN]], [[LIBERO]], [[SimplerEnv]] — 관련 benchmark
