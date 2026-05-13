---
title: "HumanNet: 인간 중심 비디오 학습을 100만 시간 규모로 확장하기 — learning"
type: source
tags: [vla, embodied-learning, video-dataset, robotics]
date: 2025-05-13
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W20/humannet-2605-06747/learning.md
source_hash: 002375b1219fb89e
---

## Summary
HumanNet은 100만 시간 규모의 인간 중심 비디오 코퍼스를 구축하여 VLA(Vision-Language-Action) 모델의 사전학습에 활용하는 방법을 제시한다. Robot 데이터의 비용 및 스케일 한계를 인간 비디오로 우회하여 [[Embodied Learning]]의 데이터 병목을 해소하는 접근이다.

## Key Claims
- Robot 데이터는expensive하고limited distribution을 가진다
- Human video는 internet scale에서 풍부한 physical interaction 신호를 포함한다
- Egocentric video는 손-물체 접촉, actor intent, visual consequence를 직접 담는다
- Human-centric filtering과 viewpoint taxonomy가 필수적이다
- Pose, motion, hand-object contact, caption, retargetability annotation이 action grounding에 필요하다

## Key Quotes
> "Human activity at internet scale → HumanNet videos → Ego view(exo view) → Action-centric visual prior(motion/context prior) → VLM/VLA continued training → Robot post-training"

## Prerequisites (선수 지식)
- Egocentric video vs exocentric video 구분
- VLM pretraining / continued training / post-training 파이프라인
- VLA policy: vision-language observation을 executable action으로 연결하는 모델
- Pose estimation, motion retargeting, SLAM
- Dataset curation: filtering, deduplication, annotation, privacy review

## Core Concepts

| 용어 | 설명 |
|---|---|
| [[HumanCentricVideo]] | 인간 활동이 clip의 중심 신호인 비디오 |
| Egocentric Video | 행위자 시점의 1인칭 비디오 |
| Exocentric Video | 관찰자 시점의 3인칭 비디오 |
| [[Retargeting]] | 인간 motion을 robot/humanoid skeleton 또는 action space로 옮기는 과정 |
| [[InteractionCentricAnnotation]] | caption뿐 아니라 손/몸/물체/동작/상태 변화 정보를 담는 annotation |
| [[EmbodimentGap]] | 인간 몸/손과 robot morphology/control space 사이의 차이 |

## Implementation Notes
- Human video를 robot policy에 직접 넣기보다 VLM encoder 또는 video-language representation을 먼저 pretrain하는 방식이 현실적
- Retargeting threshold나 pose confidence를 metadata로 유지해야 downstream mixture에서 sample weighting 가능
- Privacy filtering은 기술 문제가 아니라 release policy와 결합된 운영 문제

## Study Questions

1. **왜 first-person video가 VLA에 특히 중요한가?**  
   손-물체 접촉, actor intent, action의 시각적 결과가 한 프레임 시퀀스에 직접 담기기 때문이다.

2. **HumanNet은 robot data를 완전히 대체하는가?**  
   아니다. Representation prior와 pretraining source로 유용하지만 [[EmbodimentGap]] 때문에 robot-specific post-training은 여전히 필요하다.

3. **Closed-loop 성능이 아닌 validation loss만으로 충분한가?**  
   초기 data-value 검증으로는 의미 있지만, 실제 배포 성능 판단에는 closed-loop success/safety metric이 추가로 필요하다.

## Reading Roadmap
- Day 1: [[Ego4D]]/[[EgoExo4D]]로 viewpoint 개념 이해
- Day 2: [[R3M]]/[[EgoMimic]]으로 human video → robot learning transfer 이해
- Day 3: [[OpenXEmbodiment]]/[[DROID]]로 robot data scale 한계 파악
- Day 4: HumanNet 본문과 validation experiment 복습

## Connections
- [[Ego4D]] — egocentric video benchmark, HumanNet의 viewing taxonomy 기반
- [[R3M]] — human video → robot learning transfer 관련 선행 연구
- [[OpenXEmbodiment]] — robot data scale 한계 인식의 참고
- [[VLA]] — HumanNet이 사전학습하는 대상 모델
- [[EmbodiedMidtrain]] — VLM과 VLA 사이의 간극을 mid-training으로 메우는 관련 연구

## Contradictions
- None identified with existing wiki content
