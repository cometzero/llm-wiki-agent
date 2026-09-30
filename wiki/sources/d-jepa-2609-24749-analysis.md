---
title: "D-JEPA 분석"
type: source
tags: [world-model, candidate-ranking, autonomous-driving, analysis]
date: 2026-09-30
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W40/d-jepa-decision-aligned-world-model-2609-24749/analysis.md
source_hash: 1fae2a0a1f71d542
---

## Summary
이 분석은 D-JEPA를 candidate-set decision alignment layer로 해석한다. world model/VLA가 만든 action 또는 trajectory 후보는 유지하고, descriptor·rank·executed outcome으로 순위를 보정한 뒤 native planner interface로 복귀시키는 구성을 정리한다.

## Key Claims
- candidate generator의 coverage와 ranking layer의 quality는 분리된 병목이다.
- driving 평가에는 score correction, native fallback, collision/TTC risk readout이 포함되지만 rare-event safety certificate는 아니다.
- action representation을 바꾸지 않아 기존 VLA/planner 위에 붙일 수 있다.

## Connections
- VLA, latent world model, E2E driving trajectory selection의 interface 관점 비교.

## Contradictions
- offline ranking metric만으로 closed-loop reliability를 판단할 수 없다는 한계를 명시한다.
