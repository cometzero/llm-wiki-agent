---
title: "Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an Agentic Navigation System"
type: source
tags: [VLA, autonomous-driving, navigation, vision-language-action]
date: 2026-07-01
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W27/qwen-robotnav-2606-18112/analysis.md
source_hash: bb22d903d8edca0f
---

## Summary
Qwen-RobotNav는 [[Qwen3-VL]] 백본에 task-adaptive observation interface와 waypoint action head를 붙여 instruction following, object search, target tracking, autonomous driving을 하나의 scalable navigation model로 통합한 논문이다. [[NAVSIM]] closed-loop 평가에서 91.4 PDMS를 달성하며 [[VisionLanguageAction]] 모델의 cross-embodiment navigation capability를 입증했다.

## Key Claims
- Task-specific head explosion 없이 다양한 navigation family 통합 가능
- [[ParameterizedNavigationInterface]]를 통해 inference time에 task mode, token budget, temporal decay, camera weights, frame sampling 조절 가능
- [[VisionLanguageCoTraining]]으로 trajectory-only collapse를 방지하고 reasoning ability 유지
- 15.6M mixed navigation corpus (VLN, PointNav, ObjNav, tracking, autonomous driving, synthetic video-generated data)
- [[AgenticNavigationHarness]]로 upper planner가 sub-goal과 observation configuration을 동적으로 변경하는 dual-system interface 제시
- VLN-CE 76.5%, NAVSIM 91.4 PDMS 성능 달성

## Architecture
```
Multi-view RGB + history → SigLIP-2/Qwen3-VL vision encoder
↓
Embodiment prompt + task mode + instruction → Qwen3-VL LLM
↓
Final action hidden state → 4-layer MLP action head
↓
8 waypoint trajectory: (x, y, θ)
```

## Key Quotes
> "Parameterizd navigation interface: task mode, token budget, temporal decay, camera weights, frame sampling을 inference time에 조절" — 핵심 설계 철학

> "NAVSIM PDMS는 trajectory가 simulated closed-loop에서 얼마나 안전하고 규칙을 지키는지 반영" — closed-loop 평가 중요성

## Connections
- [[Qwen3VL]] — backnone vision-language model
- [[VisionLanguageAction]] — 모델 패밀리
- [[NAVSIM]] — autonomous driving 평가 benchmark
- [[AgenticNavigation]] — dual-system upper planner interface
- [[WaypointTrajectory]] — action representation
- [[ParameterizedNavigationInterface]] — inference-time configurable interface

## Contradictions
- 없음 (신규 source)
