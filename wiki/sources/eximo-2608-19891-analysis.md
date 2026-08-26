---
title: "EXIMO 분석: VLM planner와 VLA executor의 3단계 적응"
type: source
tags: [vision-language-action, robotics, analysis, action-grounding]
date: 2026-08-26
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W34/eximo-vlm-guided-exploration-2608-19891/analysis.md
source_hash: 524e48f4a3824ea2
---

## Summary
이 분석은 EXIMO를 explicit action guidance를 쓰는 hierarchical VLA로 분류한다. language subgoal은 VLM의 explanation이 아니라 VLA diffusion action head가 실행하는 interface이며, simulator closed-loop success, latency, hallucination, distribution shift를 함께 점검한다.

## Key Claims
- VLM text가 physical success를 보장하지 않으므로 affordance validation과 feedback replan이 필요하다.
- direct VLM-to-residual distillation은 offline/online distribution shift에 취약할 수 있다.
- driving VLA에는 route/rule planner와 trajectory/controller executor의 분리라는 설계 교훈을 준다.

## Connections
- VLM reasoning, VLA execution, SFT, residual RL을 연결한다.

## Contradictions
- 없음.
