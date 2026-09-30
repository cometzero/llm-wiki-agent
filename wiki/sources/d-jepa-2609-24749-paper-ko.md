---
title: "D-JEPA: 의사결정 정렬 잠재 world model"
type: source
tags: [world-model, latent-planning, autonomous-driving, vla]
date: 2026-09-30
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W40/d-jepa-decision-aligned-world-model-2609-24749/paper-ko.md
source_hash: b3b5bc4f0ad19d87
---

## Summary
D-JEPA는 predictive world model의 global latent distance가 실제 실행 후보의 local ordering을 보장하지 않는다는 decision-local gap을 다룬다. goal-relative descriptor와 ordinal rank를 후보 집합 전체에서 비교해 bounded score correction을 학습하고, 이 순서를 native JEPA future distance로 다시 표현한다. RoboTwin, physical robot, focused driving trajectory selection에 전이해 candidate selection의 효과를 평가한다.

## Key Claims
- action 후보 사이의 실행 outcome 관계는 average prediction fidelity와 다른 supervision target이다.
- bounded, permutation-equivariant set operator는 native planner를 전부 교체하지 않고 boundary 근처 preference를 수정한다.
- driving PDMS 개선은 shared candidate trajectory set을 re-rank한 결과이며, full-stack road safety 보장은 아니다.

## Connections
- Latent world model planning과 VLA action candidate re-ranking을 연결한다.
- Autonomous-driving trajectory scoring과 closed-loop outcome evaluation을 함께 다룬다.

## Contradictions
- 높은 latent prediction correlation이 곧 안전하거나 성공적인 action selection을 뜻한다는 가정과 충돌한다.
