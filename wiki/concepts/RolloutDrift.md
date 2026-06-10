---
title: "Rollout Drift"
type: concept
tags: [autoregressive, error-accumulation]
sources: [nvidia-omnidreams-2606-03159-analysis]
last_updated: 2026-06-10
---

# Rollout Drift

Long-horizon autoregressive generation에서 prediction error가 누적되어 ground truth에서 점차 멀어지는 현상.

## Overview
Rollout drift는 특히 closed-loop simulation에서 심각한 문제로, policy evaluation의 신뢰성을 저하시킨다. OmniDreams는 60초 long-term consistency evaluation으로 이를 측정한다.

## Mitigation in OmniDreams
1. **Self Forcing**: Model이 자신의 prediction에 robust하게 학습
2. **DMD (Diffusion Model Distillation)**: Teacher knowledge로 drift 억제
3. **Diffusion Forcing**: 부드러운 denoising process

## Evaluation
- 300 clips × 60s long-term consistency test
- Collision metric trend over time

## Connections
- [[OmniDreams]] — 측정 및 완화 대상
- [[ExposureBias]] — 근본 원인
- [[ClosedLoopSimulation]] — 영향받는 환경
- [[SelfForcing]] — 완화 기법
