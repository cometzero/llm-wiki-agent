---
title: "TD3 (Twin Delayed DDPG)"
type: concept
tags: [reinforcement-learning, off-policy]
sources: ["object-centric-residual-rl-vla-enhancement-2606-18953"]
last_updated: 2026-07-01
---

## Definition
TD3 (Twin Delayed Deep Deterministic Policy Gradient)는 off-policy, model-free, continuous action RL algorithm이다. DDPG의 overestimation bias를 완화하기 위해 twin Q-networks와 delayed policy update를 사용한다.

## This Paper's Usage
Simulation에서 residual policy 학습에 사용. Dense shaped reward, clipped exploration noise 적용. Pose noise/dropout으로 robustness 확보.

## Connections
- [[ObjectCentricResidualRL]] — algorithm used
- [[ResidualRL]] — application context
- [[OffPolicyRL]] — algorithm type
