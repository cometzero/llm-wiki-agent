---
title: "Residual RL"
type: concept
tags: [reinforcement-learning, robotics, policy-refinement]
sources: [object-centric-residual-rl-vla-enhancement-2606-18953-references, object-centric-residual-rl-vla-enhancement-2606-18953]
last_updated: 2026-07-01
---

## Definition
Residual RL은 pre-trained policy(주로 behavior cloning)의 residual(잔차)을 학습하여 정확한 제어를 달성하는 RL 방법론이다.

## Key Papers
- [[Residual-Off-Policy-RL]] (2025) — Behavior Cloning policy fine-tuning을 위한 off-policy method
- [[Residual-RL-Precise-Assembly]] (2024) — Precision assembly에서 imitation에서 refinement로 전환
- PLD (2025) — Probe, Learn, Distill framework
- [[Refined-Policy-Distillation]] (2025) — VLA generalist에서 RL expert로 distillation

## Why Residual?
1. SFT/BC policy의 quality limitation 해결
2. Costly human demonstration 의존성 줄이기
3. Sim-to-real distribution shift 완화

## Connections
- [[VLA]] — Residual RL의 주요 적용 대상
- [[Sim-to-Real-Transfer]] — Residual RL의 핵심 활용场景
