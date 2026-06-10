---
title: "Distribution Matching Distillation"
type: concept
tags: [distillation, diffusion, optimization]
sources: [nvidia-omnidreams-2606-03159-references]
last_updated: 2026-06-10
---

## Overview
Generated video distribution을 real data manifold로 맞추는 holistic objective (Yin et al., 2024).

## Key Claims
- Generated distribution과 real data distribution 정렬
- Per-sample quality보다 overall distribution 개선
- Diffusion model optimization의 새로운 패러다임

## Connections
- [[DiffusionForcing]] — 관련 diffusion training 기법
- [[WorldModel]] — DMD로 최적화된 world model generation
