---
title: "World Action Models: A Survey — 미래를 덜 꿈꾸고 행동을 더 잘하게 만드는 WAM 서베이"
type: source
tags: [world-model, VLA, WAM, robotics, autonomous-driving, survey]
date: 2026-06-24
source_url: "https://arxiv.org/abs/2606.20781"
arxiv_id: "2606.20781"
project_url: "https://world-action-models.github.io/"
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W26/world-action-models-survey-2606-20781/paper-ko.md
source_hash: e500fa1ffe0cf353
---

## Summary

World Action Model(WAM)은 미래 예측을 action decision에 실제로 사용할 수 있게 설계된 embodied predictive-action model이다. 이 서베이는 VLA policy, broad world model, video generation model, WAM 사이의 경계를 정리하고, 세 가지 설계 철학(Render-and-Decode, Latent-Only, Video-Generation-Free)과 네 축 해부(Predictive substrate, Backbone, Action coupling, Deployment regime)를 제시한다.

## Key Claims

- WAM은 단순히 video generator에 action head를 붙인 것이 아니라, representational richness와 compute/memory/latency/action-label cost 사이의 trade-off를 설계하는 [[PredictiveAction]] method다
- 분야는 점점 더 적은 미래를 생성하면서도 control에 필요한 정보는 보존하는 방향으로 이동하고 있다
- VLA for AD에서 좋은 WAM은 lane change, braking, yielding, cut-in 대응 같은 executable decision을 더 잘 만들게 해야 한다
- WAM 평가는 단순 video quality metric(FVD, CLIP score 등)에 머물지 않고 action utility, causality, interactability, persistence, latency, generalization을 포함해야 한다

## Key Quotes

> "A WAM requires that future to stay in the action path, either through predict-then-act cascades, action-scoring rollouts, or joint future-action prediction." — 핵심 정의

> "The field is moving toward generating less future while preserving the information needed for control." — 분야 추세

## Connections

- [[VLA]] — WAM과 밀접한 관련, VLA policy와 WAM 경계 정리 필요
- [[WorldModel]] — broad world model과 WAM 차이점 명시화
- [[VideoGeneration]] — video generation model과 WAM 경계 정리
- [[PredictiveSubstrate]] — WAM 해부 네 축 중 하나
- [[ActionCoupling]] — WAM 해부 네 축 중 하나
- [[RenderAndDecode]] — WAM 설계 철학 3가지 중 첫 번째
- [[LatentOnlyWAM]] — WAM 설계 철학 3가지 중 두 번째
- [[VideoGenerationFreeWAM]] — WAM 설계 철학 3가지 중 세 번째
- [[OmniDreams]] — NVIDIA의 WAM backbone 관련 연구와 연결
- [[ReCAP]] — retrieval-augmented WAM과 관련

## Contradictions

없음. 기존 wiki의 [[WorldActionModel]] 개념과 정합성 유지.
