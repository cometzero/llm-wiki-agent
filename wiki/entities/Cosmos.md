---
title: "Cosmos"
type: entity
tags: [video-generation, backbone, NVIDIA]
sources: [nvidia-omnidreams-2606-03159, nvidia-omnidreams-2606-03159-learning]
last_updated: 2026-06-10
---

## Overview
NVIDIA의 video generation backbone으로, OmniDreams의foundation model로 활용된다.

## Details
- **Cosmos-Predict 2.5**: OmniDreams의 pre-trained video generation backbone
- autonomous vehicle multi-view 영상에 적응(adaptation)되어 사용
- raw driving data에서 학습된 realistic video generation 능력 보유

## Connections
- OmniDreams에서 AV multi-view generation backbone으로 사용
- [[WorldActionModel]]과 결합하여 closed-loop simulation 구현
- [[DiffusionForcing]] 학습의 기반이 되는 video latent model
