---
title: "D-JEPA 참고 레퍼런스"
type: source
tags: [world-model, jepa, planning, references]
date: 2026-09-30
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W40/d-jepa-decision-aligned-world-model-2609-24749/references.md
source_hash: 49af5f528321912a
---

## Summary
D-JEPA의 reference map은 PlaNet/Dreamer/TD-MPC의 latent control, V-JEPA 2·DINO-WM·TD-JEPA의 predictive representation, OpenVLA의 action-policy interface를 연결한다. 핵심은 world model의 prediction quality보다 planner-reachable candidate의 decision quality를 별도 문제로 보는 것이다.

## Key Claims
- ordinal rank는 heterogeneous predictive geometry를 함께 쓰기 위한 scale-free interface다.
- representation learning, MPC, VLA policy의 역할을 candidate selection 관점에서 분리한다.

## Connections
- Latent control, JEPA, VLA, autonomous-driving planner 문헌 지도.

## Contradictions
- 단일 predictive backbone의 native distance가 충분한 universal action score라는 관점을 제한한다.
