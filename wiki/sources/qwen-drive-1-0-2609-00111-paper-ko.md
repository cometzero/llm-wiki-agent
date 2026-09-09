---
title: "Qwen-Drive-1.0 한국어 기술 번역"
type: source
tags: [autonomous-driving, vision-language-model, bev, occupancy, motion-planning]
date: 2026-09-09
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W36/qwen-drive-1-0-2609-00111/paper-ko.md
source_hash: 254bde5e65993504
---

## Summary
Qwen-Drive-1.0은 pretrained vision-language model의 shared representation을 기반으로 3D perception, driving VQA, motion planning을 통합한다. 외부 BEV perception head가 3D detection·semantic occupancy·BEV map을 예측하고, Planning Expert가 VLM cached key/value에 조건부로 numerical ego trajectory를 생성한다.

## Key Claims
- Staged training은 driving adaptation과 general VLM capability preservation을 함께 목표로 한다.
- Planning은 flow matching 후 source-specific reward optimization으로 학습한다.
- 평가가 open-loop, pseudo-closed-loop, simulator closed-loop를 모두 포함하지만 real-road safety guarantee는 아니다.

## Connections
- Qwen-Drive는 shared semantic representation을 inspectable 3D interface와 executable trajectory로 동시에 연결한다.

## Contradictions
- Pure text-action VLA와 달리 Qwen-Drive는 external BEV head와 numerical Planning Expert를 유지하는 hybrid system이다.
