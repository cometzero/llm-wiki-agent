---
title: "Qwen-Drive-1.0 학습 노트: VLM, BEV, trajectory planner를 잇는 법"
type: source
tags: [autonomous-driving, learning, bev, flow-matching, planning]
date: 2026-09-09
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/qwen-drive-1-0-2609-00111/learning.md
source_hash: 17bfe0f85f2fb0f4
---

## Summary
이 학습 노트는 multi-view VLM representation, external BEV head, flow-matching Planning Expert를 단계별로 설명한다. offline trajectory error와 interactive safety/progress metric을 구분하고 production planner의 confidence·feasibility·fallback 검증을 강조한다.

## Key Claims
- BEV/occupancy는 geometry-aware driving representation의 핵심 선행지식이다.
- Numerical trajectory action은 prose action보다 모호성·control interface 비용을 줄인다.
- Closed-loop benchmark가 있어도 real vehicle safety case를 대체하지 않는다.

## Connections
- VLM representation sharing을 actual trajectory deployment 검증과 연결하는 학습 자료다.

## Contradictions
- 낮은 ADE만으로 collision avoidance나 comfort를 보장할 수 없다.
