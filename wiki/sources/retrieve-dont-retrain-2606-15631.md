---
title: "Retrieve, Don't Retrain: 테스트 시점 검색으로 VLA를 새 태스크에 확장하기"
type: source
tags: [vla, robotics, retrieval, world-action-model, cross-embodiment]
sources: []
date: 2026-06-17
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W25/retrieve-dont-retrain-2606-15631/paper-ko.md
source_hash: d64b1e2d71f3f077
---

## Summary
ReCAP은 새 VLA/robot manipulation task를 per-task fine-tuning 대신 retrieval pool 확장으로 흡수하는 test-time adaptation framework다. Cosmos Policy 기반 World-Action Model에 retrieved source-embodiment trajectory를 coarse motion prior로 주입하고 target robot residual action을 생성한다.

## Key Claims
- 새 task adaptation 비용을 target robot teleoperation + fine-tuning에서 source/pool demonstration indexing으로 전환한다.
- Retrieved trajectory는 high-level task progression을 제공하고 WAM future-image objective는 visual consistency를 보강한다.
- PushT, RoboTwin 2.0, real robot 실험으로 retrieval-conditioned residual policy의 cross-embodiment value를 보인다.

## Connections
- [[retrieve-dont-retrain-2606-15631-analysis]]
- [[RetrievalAugmentedPolicy]]
- [[ReCAP]]
- [[WorldActionModel]]
- [[VisionLanguageAction]]

## Contradictions
- 없음 — 기존 [[VisionLanguageAction]], [[ActionGrounding]], [[WorldActionModel]] 흐름을 보완한다.
