---
title: "Latent World Action Model"
type: concept
tags: [WAM, latent-space, action-generation, video-prediction, robot]
sources: [embodied-cpp-2607-02501-references, world-action-models-survey-2606-20781]
last_updated: 2026-07-08
---

## Overview
Pixel-space video rollout 대신 compact latent visual subgoal을 예측하여 action generation에 제공하는 world action model 변형. [[LaWAM]]과 [[Being-H0.7]]이 대표적인 latent WAM 사례로, LIBERO, RoboTwin, real-world manipulation에서 높은 success rate와 낮은 latency를 보고한다.

## Key Claims
- Pixel-space video rollout의 한계: high computation, slow inference
- Latent solution: compact latent visual subgoal prediction
- Performance: 높은 success rate, 낮은 latency
- Inference: action head뿐 아니라 latent future prediction branch도 schedule 필요
- Training-only vs deployable: posterior branch(training-only)와 prior branch(deployable) 경계 관리 중요

## Related Concepts
- [[WorldActionModel]] — 상위 개념
- [[ActionGeneration]] — 출력 생성 대상
- [[LatentSpace]] — 예측 공간
- [[VideoPrediction]] — pixel-space 대비 방식

## Connections
- [[LaWAM]] — latent WAM의 대표 사례
- [[Being-H0.7]] — WAM/VLA hybrid로 future-aware reasoning 포함
- [[Embodied.cpp]] — WAM first-class support
- [[vla.cpp]] — WAM 미지원으로 대비
