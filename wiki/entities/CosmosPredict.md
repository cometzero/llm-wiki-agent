---
title: "Cosmos Predict"
type: entity
tags: [NVIDIA, world-model, video-generation]
sources: [nvidia-omnidreams-2606-03159-analysis]
last_updated: 2026-06-10
---

# Cosmos Predict

NVIDIA의 비디오 생성 모델 제품군. OmniDreams의 백본으로 사용됨.

## Overview
Cosmos Predict는 NVIDIA가 개발한 비디오 예측 생성 모델로, OmniDreams에서 Cosmos-Predict 2.5를 출발점으로 21k hours의 driving data로 mid/post-training하여 autonomous driving용 world model을 구축함.

## Key Properties
- Cosmos-Predict 2.5: OmniDreams의 base model
- Multi-view adaptation 가능
- 2B parameter规模的 경량 모델로 real-time inference 가능

## Connections
- [[OmniDreams]] — 백본으로 사용
- [[NVIDIA]] — 개발사
- [[GenerativeWorldModel]] — 비디오 생성 기반 world modeling
