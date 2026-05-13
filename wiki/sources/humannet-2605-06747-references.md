---
title: "HumanNet: 인간 중심 비디오 학습을 100만 시간 규모로 확장하기 — references"
type: source
tags: [references, humanoid-robotics, embodied-ai, VLA, video-learning]
date: 2026-05-13
sources: [humannet-2605-06747, humannet-2605-06747-analysis]
last_updated: 2026-05-13
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W20/humannet-2605-06747/references.md
source_hash: c8a99853141e086c
---

## Summary
HumanNet 논문(arXiv 2605.06747)의 참고 문헌을 정리한 페이지로, Semantic Scholar references가 아직 반환되지 않아 원문의 Related Work와 본문 인용을 기반으로 주요 레퍼런스를 정리했다. Ego4D, EPIC-KITCHENS 등 제3인칭 데이터셋부터 [[Open X-Embodiment]], [[DROID]] 등 로봇 데이터셋, 그리고 [[R3M]], [[EgoMimic]] 등 인간 비디오의 로봇 전이 연구까지 포괄한다.

## Key References

### Egocentric Video Datasets
- **[[Ego4D]]** — egocentric video가 narration, forecasting, hand-object interaction 학습에 유용함을 보여준 대표 corpus
- **[[EPIC-KITCHENS]]** — kitchen egocentric activity dataset; actor-centered intent와 hand-object contact의 중요성을 보여줌
- **[[Ego-Exo4D]]** — first-person과 third-person paired view가 skilled activity 이해에 중요함을 제시
- **[[HOI4D]]** — hand-object geometry와 dense interaction supervision을 강조하는 dataset

### Robot Data & Foundation Models
- **[[Open X-Embodiment]] / [[RT-X]]** — heterogeneous robot logs를 통한 robot foundation model scaling의 대표 사례; HumanNet은 human-video side scaling으로 보완
- **[[DROID]]** — real-world robot manipulation dataset; HumanNet의 "robot 데이터는 비싸다"는 문제의식과 연결
- **[[GR00T N1]]** — heterogeneous robot/human data mixture를 사용하는 [[VLA]]/robot foundation model 계열
- **[[LingBot-VLA]]** — HumanNet validation에서 사용한 VLA post-training architecture/protocol의 기반

### Human-to-Robot Transfer
- **[[R3M]]** — passive human video representation이 robot manipulation에 transfer될 수 있음을 보인 선행 연구
- **[[EgoMimic]]** — egocentric human trace와 robot demonstration alignment를 통한 imitation learning 방향

## Reading Priority

1. **R3M / [[EgoMimic]]**: human video가 robot policy prior가 되는 원리
2. **[[Ego4D]] / [[Ego-Exo4D]]**: egocentric/exocentric viewpoint 설계
3. **[[Open X-Embodiment]] / [[DROID]]**: robot data scale의 현실적 한계
4. **[[GR00T N1]] / [[LingBot-VLA]]**: heterogeneous data를 [[VLA]] post-training에 섞는 방법

## Connections
- [[HumanNet]] — 이 참조 페이지가 속한 메인 소스
- [[VLA]] — HumanNet이 목표로 하는 Vision-Language-Action 모델
- [[EgocentricVideo]] — 인간 중심 비디오 학습의 핵심 데이터 모달리티
- [[RobotFoundationModel]] — [[Open X-Embodiment]], [[GR00T N1]]과 공유하는 목표

## Contradictions
- 없음. 기존 wiki에서 [[R3M]]과 [[EgoMimic]]은 이미 [[EmbodiedAI]] 맥락으로 등장한 바 있으며, HumanNet의 관점(robot data 병목 우회)을 보완하는 내용으로 일관됨.
