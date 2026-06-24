---
title: "OmniDreams"
type: entity
tags: [autonomous-driving, world-model, NVIDIA, generative]
sources: [tbd-vla-2606-07895, nvidia-omnidreams-2606-03159, world-action-models-survey-2606-20781-analysis]
last_updated: 2026-06-24
---

# OmniDreams

NVIDIA가 제안한 real-time action-conditioned generative world model. Cosmos 기반으로 720p에서 68~105 FPS 수준의 sensor generation을 수행하며, 자율주행 closed-loop simulation에서 [[AlpaSim]]과 [[Alpamayo]] policy에 연결된다.

## WAM Context

World Action Models survey 관점에서 OmniDreams는 generated future가 closed-loop evaluation과 policy/planner interaction에 쓰일 수 있는 자율주행 world model 사례다. 중요한 질문은 영상 품질 자체보다, ego action에 따른 traffic/world dynamics가 action selection과 risk evaluation에 얼마나 유용한가이다.

## Connections

- [[WorldActionModel]] — WAM backbone으로 해석 가능한 action-conditioned future model.
- [[ClosedLoopSimulation]] — 주요 deployment/evaluation setting.
- [[Cosmos]] — 기반 생성형 world foundation model.
- [[AutonomousDriving]] — 주요 적용 도메인.
