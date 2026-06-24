---
title: "DriveDreamer"
type: entity
tags: [autonomous-driving, world-model, video-generation]
sources: [nvidia-omnidreams-2606-03159-references, world-action-models-survey-2606-20781]
last_updated: 2026-06-24
---

## Overview

DriveDreamer는 자율주행 world model 연구의 대표 계열로, ego action과 driving scene context를 바탕으로 future scene을 생성하거나 simulation/planning에 활용하는 방향을 제시한다. WAM taxonomy에서는 rendered future 또는 latent future가 planner/risk evaluator와 연결되는지를 확인하는 중요한 사례다.

## Key Details

- 도메인: autonomous driving / world model / video generation.
- 역할: closed-loop simulation, counterfactual future generation, planner guidance의 배경 기술.
- WAM 관점: 단순 영상 생성이 아니라 candidate action과 future scene prediction이 action scoring에 연결될 때 [[WorldActionModel]]로 해석될 수 있다.

## Connections

- [[DriveWM]] — 관련 자율주행 world model 계열.
- [[OmniDreams]] — 더 최근의 실시간 closed-loop generative world model.
- [[WorldModel]] — DriveDreamer가 속한 미래 예측 모델 범주.
- [[VideoWorldModels]] — video generation 기반 future prediction 연구.
- [[AutonomousDriving]] — 주요 응용 도메인.
