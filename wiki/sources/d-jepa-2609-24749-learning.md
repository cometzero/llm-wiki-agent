---
title: "D-JEPA 핵심 기술 학습 자료"
type: source
tags: [world-model, learning, candidate-ranking, autonomous-driving]
date: 2026-09-30
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W40/d-jepa-decision-aligned-world-model-2609-24749/learning.md
source_hash: 1a48857318d5e276
---

## Summary
이 학습 자료는 latent distance planner가 top-k 후보에서 왜 실패할 수 있는지, ordinal evidence와 set Transformer가 어떤 역할을 하는지, bounded correction과 native latent realization을 단계적으로 설명한다. 마지막에는 candidate generator–reranker–safety shield 분리라는 autonomous-driving 적용 프레임을 제시한다.

## Key Claims
- descriptor는 geometry를, rank는 model 간 비교 가능성을 제공한다.
- bounded correction은 safety mechanism이 아니라 preference overcorrection을 제한하는 trust region이다.
- production driving에는 uncertainty, hard rule, fallback validation이 추가로 필요하다.

## Connections
- World-model planning, action grounding, trajectory evaluation 학습 자료.

## Contradictions
- reranking만으로 safe candidate가 없는 planning problem을 해결할 수 없음을 명시한다.
