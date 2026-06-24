---
title: "Latent World Models"
type: concept
tags: [world-model, latent-space, autonomous-driving]
sources: [world-action-models-survey-2606-20781]
last_updated: 2026-06-24
---

## Summary
Latent World Models는 pixel rendering을 생략하여 latency를 낮추는 world model 설계 접근법이다. WAM survey에서는 Latent-only WAM으로 분류되며, latent space에서 action-conditioned dynamics를 예측한다. 핵심 과제는 latent의 causal validity와 interpretability를 별도로 검증해야 한다는 점이다.

## Key Characteristics
- **장점**: pixel rendering 생략으로 inference latency 감소
- **과제**: latent가 traffic participant state, lane topology, route goal을 충분히 보존하는지 검증 필요
- **WAM 분류**: rendered/latent/video-free WAM 중 latent WAM 축

## Connections
- [[WorldActionModel]] — WAM taxonomy의 세 축(rendered/latent/video-free) 중 latent 축
- [[Autonomous Driving]] — latent 보존성이 특히 중요한 도메인
- [[VideoWorldModels|Video World Models]] — pixel rendering 포함 버전과 대비
