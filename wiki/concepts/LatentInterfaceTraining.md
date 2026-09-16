---
title: "Latent Interface Training"
type: concept
tags: [vla, robotics, action-grounding, robustness]
sources: [latent-interface-training-2609-12641-paper-ko, latent-interface-training-2609-12641-analysis, latent-interface-training-2609-12641-learning]
last_updated: 2026-09-16
---

## Overview
Latent Interface Training (LIT)은 VLA와 world-action model에서 direct visual conditioning을 pose-supervised latent bottleneck으로 교체하는 two-stage training method다. 목표는 task-irrelevant image correlation을 줄이되 task-relevant spatial grounding을 유지하는 것이다.

## Core Mechanism
1. Image 없이 language, robot state, terminal SE(3) pose로 action expert prior를 학습한다.
2. 100 latent token이 semantic·visual feature를 집계하고 terminal pose를 reconstruct한다.
3. Action expert는 이 interface token만으로 visual condition을 받고, inference 때 pose target/decoder는 제거된다.

## Evaluation Boundary
LIBERO-Plus visual shift 및 제한된 real-robot manipulation 개선은 generalization 신호지만, language shift·contact dynamics·open-world safety를 포괄적으로 해결했다는 의미는 아니다.

## Connections
- [[VisionActionShortcut]] — LIT가 줄이려는 failure mode.
- [[VLA]] — 적용 model family.
