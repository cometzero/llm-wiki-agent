---
title: "Entropy-Regularized Distillation"
type: concept
tags: [distillation, closed-loop, entropy, KL-divergence]
sources: [flow-erd-2607-06957]
last_updated: 2026-07-15
---

# Entropy-Regularized Distillation (ERD)

## Overview
Entropy-Regularized Distillation은 reverse-KL divergence 기반 distillation으로, closed-loop 환경에서 발생하는 covariate shift와 error accumulation을 보정하는 기법. Flow-ERD에서 multi-agent rollout distribution을 현실적 분포로 정렬하는 역할을 한다.

## Key Characteristics
- **Reverse-KL divergence**: teacher의 경계를 존중하면서 student adaptation
- **Entropy regularization**: exploration과 exploitation 균형 유지
- **Closed-loop correction**: open-loop evaluation의 한계를 보완

## Connections
- [[FlowERD]] — 핵심 구성요소, AFM backbone과 결합
- [[VLA-Corrector]] — closed-loop action 보정이라는 동일한 목표, 다른 접근법
