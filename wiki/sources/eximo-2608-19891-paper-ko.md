---
title: "EXIMO: VLM 안내 탐색으로 VLA policy를 미세조정하기"
type: source
tags: [vision-language-action, robotics, reinforcement-learning, korean-translation]
date: 2026-08-26
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W34/eximo-vlm-guided-exploration-2608-19891/paper-ko.md
source_hash: c8c2d34a7e7459fa
---

## Summary
EXIMO는 Explore–Imitate–Optimize 3단계로 VLA policy를 새 long-horizon manipulation task에 data-efficient하게 적응시킨다. VLM은 observation history와 full goal에서 next instruction을 생성하고, VLA는 이를 closed loop로 실행하며, collected data는 SFT와 residual off-policy RL에 쓰인다.

## Key Claims
- high-level VLM planner와 low-level VLA executor의 역할 분리가 autonomous exploration을 돕는다.
- orchestrated trajectory SFT는 deployment-time VLM dependency를 줄이는 distillation 단계다.
- SFT 이후 residual RL은 initial success region에서 online refinement를 시작하게 한다.

## Connections
- hierarchical VLA, language-guided action grounding, robot policy post-training을 다룬다.

## Contradictions
- 없음. simulation ALOHA 결과는 real-robot reliability를 보증하지 않는다.
