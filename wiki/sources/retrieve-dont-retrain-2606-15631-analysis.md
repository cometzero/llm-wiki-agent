---
title: "Retrieve, Don't Retrain — analysis"
type: source
tags: [vla, robotics, retrieval, analysis, action-grounding]
sources: []
date: 2026-06-17
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W25/retrieve-dont-retrain-2606-15631/analysis.md
source_hash: bd68197cd63de11b
---

## Summary
ReCAP의 문제 정의, retrieval-conditioned residual architecture, input/output/action representation, training/deployment risk를 VLA for AD 관점에서 정리한다.

## Key Claims
- VLA scaling 병목은 일부 parameter update 문제가 아니라 behavior memory 구축·검색 문제로 바뀔 수 있다.
- 자율주행 적용에는 waypoint/trajectory/BEV planner output과 safety verifier가 필요하다.

## Connections
- [[retrieve-dont-retrain-2606-15631]]
- [[ActionGrounding]]
- [[RetrievalAugmentedPolicy]]
- [[ReflectDrive2]]
- [[VisualThink-VLA]]

## Contradictions
- 없음 — 기존 [[VisionLanguageAction]], [[ActionGrounding]], [[WorldActionModel]] 흐름을 보완한다.
