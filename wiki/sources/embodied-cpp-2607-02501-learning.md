---
title: "Embodied.cpp 학습 노트: VLA/WAM runtime contract"
type: source
tags: [huggingface-weekly, vla, robotics]
date: 2026-07-08
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W28/embodied-cpp-portable-inference-runtime-2607-02501/learning.md
source_hash: 87e3aab13096bb32a6dd3723f22dc6efd19ba2e148d9877c9ced1b21e8e4edce
---

## Summary
Embodied.cpp를 학습하기 위한 glossary, Mermaid pipeline, 구현 체크리스트, 자율주행 VLA 확장 질문을 정리한 학습 자료다. Runtime contract와 deployment adapter, NPU/heterogeneous scheduling 관점을 공부하도록 구성되어 있다.

## Key Claims
- Five-layer runtime은 input adapter부터 deployment adapter까지 embodied control loop를 계층화한다.
- 자율주행 VLA에서는 BEV/occupancy encoder, route command, planner/action head의 실행 주기와 device partitioning이 핵심 질문이다.
- 일반 LLM serving과 달리 robot runtime은 sensor feedback, persistent state, low jitter를 포함해야 한다.

## Key Quotes
> "Runtime contract는 런타임이 만족해야 하는 실행 가정과 인터페이스다." — 용어집
> "모든 module을 같은 device/주기로 실행하는 것이 최적이 아닐 수 있다." — 학습 문제 답변

## Connections
- [[FiveLayerRuntime]] — Embodied.cpp의 계층화된 runtime architecture
- [[HeterogeneousScheduling]] — CPU/GPU/NPU partitioning 관점
- [[ClosedLoopRobot]] — feedback loop 안에서 실행되는 robot deployment
- [[WAM]] — world/action prediction이 runtime object가 되는 모델군

## Contradictions
- 없음.
