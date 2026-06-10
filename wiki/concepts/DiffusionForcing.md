---
title: "DiffusionForcing"
type: concept
tags: [diffusion, autoregressive, video-generation, training]
sources: [nvidia-omnidreams-2606-03159, nvidia-omnidreams-2606-03159-learning]
last_updated: 2026-06-10
---

## Overview
Diffusion Forcing은 diffusion/video generation을 causal autoregressive하게 학습시키는 방법론이다.

## Details
- **핵심 아이디어**: 각 frame prediction이 과거 observation과 일부 noise version에 의존하도록 학습
- causal masking과 결합하여 closed-loop autoregressive generation 가능
- 이전 frame의 noisy version도 조건으로 사용하여 generation 안정성 향상
- [[OmniDreams]]의 training pipeline에서 핵심 구성 요소

## 수학적 표현

```text
p(x_1:T) = Π_i p(x_i | x_<i)
```

Video latent sequence를 causal factorization하여 closed-loop rollout에서 과거 observation과 current state/action만 보게 함.

## Self-Forcing과의 관계
- [[DiffusionForcing]]과 [[SelfForcing]]을 결합하여 train-test mismatch를 줄임
- Self Forcing: inference self-rollout 조건을 training에 반영

## Connections
- [[OmniDreams]]의 training Pipeline 핵심 구성
- [[SelfForcing]]과 결합하여 training/inference 일관성 확보
- [[Cosmos]] video backbone의 adaptation에 사용
