---
title: "Spatial Memory for Navigation"
type: concept
tags: [navigation, spatial-memory, VLN, planner, persistent-memory]
sources: [embodied-cpp-2607-02501-references]
last_updated: 2026-07-08
---

## Overview
Visual Language Navigation(VLN) 및 robot navigation에서 3D semantic map, revisiting penalty, LLM reflective correction을 결합하여 agent의 inefficiency를 줄이는 기법. [[Stop Wandering]]이 제안하며, 자율주행/로봇 navigation에서는 policy 호출뿐 아니라 persistent memory와 planner state도 runtime object가 되어야 함을 보여준다.

## Key Claims
- 3D semantic map: 공간적 정보 구조화
- Revisiting penalty: 효율적인 경로 탐색
- LLM reflective correction: 언어 기반 자기纠正
- Runtime object: persistent memory와 planner state도 runtime에서 관리
- Agent architecture: policy + memory + planner 통합

## Related Concepts
- [[VLN]] — 적용 도메인
- [[PersistentMemory]] — memory 관리
- [[PlannerState]] — planning state
- [[ReflectiveReasoning]] — LLM 기반 correction

## Connections
- [[Stop Wandering]] — 기법 제안 논문
- [[QwenRobotNav]] — navigation 관련 기존 연구
- [[EmbodiedAI]] — 적용 도메인
