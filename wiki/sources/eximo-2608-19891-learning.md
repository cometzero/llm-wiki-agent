---
title: "EXIMO 학습 노트: VLM planner–VLA executor–RL refinement"
type: source
tags: [vision-language-action, robotics, learning, reinforcement-learning]
date: 2026-08-26
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W34/eximo-vlm-guided-exploration-2608-19891/learning.md
source_hash: 8fbbf7cd95880646
---

## Summary
이 학습 노트는 VLM planner가 immediate subgoal을 만들고, VLA executor가 continuous action을 내며, SFT와 residual RL이 standalone policy로 증류·보정하는 흐름을 도식과 식으로 설명한다.

## Key Claims
- effective action grounding은 free-form reasoning이 아니라 constrained intermediate instruction과 feedback loop에 달려 있다.
- SFT는 planner call cost를 줄이지만 rare failure/recovery coverage를 따로 평가해야 한다.
- residual action에는 velocity/force/collision limit 및 emergency stop이 필요하다.

## Connections
- VLA adaptation과 deployment safety 학습 자료다.

## Contradictions
- 없음.
