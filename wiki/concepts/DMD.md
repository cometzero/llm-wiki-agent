---
title: "Distribution Matching Distillation (DMD)"
type: concept
tags: [distillation, diffusion, optimization]
sources: [nvidia-omnidreams-2606-03159]
last_updated: 2026-06-10
---

# Distribution Matching Distillation (DMD)

Generated video distribution을 real data manifold에 정렬하는 distillation 기법.

## OmniDreams에서의 역할
- [[SelfForcing]]으로 학습된 모델의 quality 향상
- Training-free model optimization
- Real data 분포와 generated data 분포 매칭

## 목적
- Autoregressive generation의 drift 방지
- Long rollout에서도 realism 유지

## Connections
- [[OmniDreams]] — 사용처
- [[SelfForcing]] — 전단계
- [[DiffusionModel]] — 기반 기술
