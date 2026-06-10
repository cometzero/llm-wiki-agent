---
title: "Exposure Bias"
type: concept
tags: [autoregressive, training-inference-mismatch]
sources: [nvidia-omnidreams-2606-03159-analysis]
last_updated: 2026-06-10
---

# Exposure Bias

Autoregressive generation에서 training 시 ground truth를 조건으로 사용하지만 inference 시에는 model's own prediction을 조건으로 사용하여累积 오차가 발생하는 현상.

## Overview
Exposure bias는 autoregressive model의 공통 문제로, 특히 long rollout에서 심화된다. OmniDreams는 Diffusion Forcing과 Self Forcing + DMD를 통해 이 문제를 완화한다.

## Impact in Closed-Loop Simulation
- Policy evaluation에서 accumulated error가 policy 판단을 왜곡
- Long-horizon scenario에서 fidelity 저하
- Evaluation 신뢰성 감소

## Solutions in OmniDreams
1. **Diffusion Forcing**: Denoising process로 부드러운 error propagation
2. **Self Forcing**: Model이 자신의 prediction에 적응하도록 학습
3. **DMD (Diffusion Model Distillation)**: Teacher model knowledge distillation

## Connections
- [[OmniDreams]] — 해결려는 문제
- [[DiffusionForcing]] — 해결 기법
- [[RolloutDrift]] — 심화问题时 발생
- [[ClosedLoopSimulation]] — 영향받는 도메인
