---
title: "HumanNet"
type: concept
tags: [dataset, vla, embodied-ai, video-learning]
last_updated: 2026-05-13
---

# HumanNet

[[HumanNet]]은 "100만 시간 규모의 인간 중심 비디오 corpus"를 제안하는 데이터 중심 논문(arXiv:2605.06747)이다. [[VLA]]의 action grounding을 robot log 밖에서 확장하는 "data-centric approach"를 제시하며, 인간 비디오를 물리적으로 구조화하여 VLA pretraining substrate로 활용한다.

## Overview
100만 시간의 인간 중심 비디오를 수집·처리· annoation하여 VLM/VLA 학습에 활용하는 데이터셋 및 방법론.

## Connections
- [[VLA]] — 주요 타겟 모델
- [[Qwen]] — VLM backbone으로 사용
- [[LingBot]] — 검증에 사용된 VLA 모델
- [[Embodied AI]] — 핵심 응용 도메인

## Key Contributions
1. **100만 시간 human-centric video corpus** 제안
2. **First-person/third-person viewpoint taxonomy** — Egocentric vs Exocentric 비디오 분류
3. **Interaction-centric annotation**: pose, motion, caption, activity label, retargetability
4. **Privacy/license/quality filtering** — 데이터셋 설계의 일부

## Technical Pipeline
- Keyword/channel/dataset 기반 수집 → Raw human-centric videos
- Dedup + normalization
- Content & quality filtering
- Scene splitting + clipping
- 3D hand/body pose estimation
- Monocular SLAM
- LLM-assisted captions
- Motion annotations
- Retargetable robot-ready subset 추출

## Significance
Robot data 부족 → human video + motion annotation + retargeting + VLA post-training이라는 scalable route를 제시. 자율주행에서의 driving video 활용에도 힌트 제공.

## Limitations
- Human-to-robot embodiment gap 여전히 존재
- Dataset noise, geographic/social bias 가능성
- Closed-loop robot success 직접 증명되지 않음
