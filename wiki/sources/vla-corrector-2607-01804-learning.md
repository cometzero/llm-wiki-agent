---
title: "VLA-Corrector 학습 노트: Adaptive action horizon과 latent dynamics monitoring"
type: source
tags: [huggingface-weekly, vla, robotics]
date: 2026-07-08
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W28/vla-corrector-adaptive-action-horizon-2607-01804/learning.md
source_hash: 58d6388749575659203edf4572c232f9b2fd7640441a6856b524ec7f282be167
---

## Summary
VLA-Corrector를 공부하기 위한 학습 노트다. Action chunk, LVM, OGG, robust threshold, 자율주행 trajectory planning analog, 구현 절차와 study questions를 포함한다.

## Key Claims
- Action chunk는 계속 믿어도 되는 구간에서는 효율적이지만 stale해지면 위험하다.
- LVM은 expected latent residual과 actual latent residual의 cosine mismatch를 이용한다.
- 자율주행에서는 trajectory segment invalidation과 planned/observed scene evolution consistency monitor로 확장 가능하다.

## Key Quotes
> "chunk를 무조건 짧게 만들지 않고, 신뢰할 수 없게 된 순간만 감지해서 짧게 만드는 것이다." — 핵심 intuition
> "Action generator가 강하더라도 execution 중 action이 계속 valid한지 검증해야 한다." — 학습 문제 답변

## Connections
- [[AdaptiveActionHorizon]] — 학습 노트의 핵심 개념
- [[LatentSpaceVisionMonitor]] — drift detection module
- [[OpenLoopBlindSpot]] — 문제 상황
- [[AutonomousDrivingVLA]] — 자율주행 VLA analog

## Contradictions
- 없음.
