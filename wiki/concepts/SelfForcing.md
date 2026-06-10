---
title: "SelfForcing"
type: concept
tags: [training, exposure-bias, autoregressive]
sources: [nvidia-omnidreams-2606-03159, nvidia-omnidreams-2606-03159-learning]
last_updated: 2026-06-10
---

## Overview
Self Forcing은 inference self-rollout 조건을 training에 반영하여 exposure bias를 줄이는 방법론이다.

## Details
- **문제**: inference 시 모델이 자신에게서 생성된 frame을 조건으로 사용하지만, training 시에는 ground truth frame을 사용
- **해결**: training 중에도 generated frame을 조건으로 사용하여 train-test mismatch 감소
- [[OmniDreams]]의 training Pipeline에서 [[DiffusionForcing]]과 함께 사용

## 왜 중요한가?
- closed-loop evaluation에서 policy-induced future를 생성할 때, 모델은 이전에 자신이 생성한 frame을 보게 됨
- training 때 이 상황을 반영하지 않으면 cumulative error가 발생
- Self Forcing으로 이를 해결

## Connections
- [[DiffusionForcing]]과 결합하여 [[OmniDreams]]의 training pipeline 구성
- DMD(Denoising Mode Dropout)와 함께 사용
- [[OmniDreams]]의 closed-loop generation 안정성에 기여
