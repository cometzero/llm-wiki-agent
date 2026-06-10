---
title: "World Model"
type: concept
tags: [generative-model, simulation, autonomous-driving]
sources: [nvidia-omnidreams-2606-03159]
last_updated: 2026-06-10
---

# World Model

환경의 동적 동작을 예측하고 simulating하는 generative model. 자율주행에서 policy 평가와 학습에 사용된다.

## Types
- **Reconstruction-based**: 특정 log를 photorealistic하게 재현, 새로운 scenario에 약함
- **Generative (OmniDreams)**: novel/dynamic scenario 생성 가능

## OmniDreams World Model
- [[Cosmos]] 기반 foundation model
- Action-conditioned video generation
- Real-time autoregressive generation
- Multi-view support

## Connections
- [[OmniDreams]] — 구현체
- [[WorldActionModel]] — policy backbone 변형
- [[ClosedLoopSimulation]] — 핵심 사용 사례
- [[ReconstructionBasedSimulator]] — 대비 개념
