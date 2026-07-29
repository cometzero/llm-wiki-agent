---
title: "WorldDiT"
type: entity
tags: [robotics, embodied-ai, diffusion, world-model, action-generation, vision-language-action]
sources: ["worlddit-2607-23909-paper-ko", "worlddit-2607-23909-references"]
last_updated: 2026-07-29
---

## Summary
[[WorldDiT]]는 shared [[DiffusionTransformer]]로 continuous [[ActionChunking]]과 future visual prediction을 함께 학습하는 compact world-action model이다. 학습 시에는 world supervision을 활용하지만, 추론 시에는 action-only 경로로 전환해 latency와 파라미터 효율을 높인다.

## Key Traits
- 하나의 백본으로 action generation과 future RGB patch prediction을 공동 학습한다.
- 추론에서는 future prediction branch를 제거하고 action chunk만 실행한다.
- [[LIBERO]]에서 compact Pareto 효율을 강조한다.
- [[DiffusionPolicy]] 계열과 달리 future world supervision을 결합한다.

## Connections
- [[DiffusionTransformer]]
- [[FlowMatching]]
- [[ActionChunking]]
- [[WorldActionModel]]
- [[LIBERO]]
- [[Model-PredictiveControl]]
- [[DiffusionPolicy]]
- [[UnifiedDiffusionVLA]]
- [[VLA-0]]
- [[VLAAdapter]]
- [[MemoryVLA]]

## Notes
- 이 페이지는 [[WorldDiT]]의 모델/프로젝트 엔티티 역할을 한다.
