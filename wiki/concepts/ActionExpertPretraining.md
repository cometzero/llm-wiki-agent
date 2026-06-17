---
title: "Action Expert Pretraining"
type: concept
tags: [vla, robotics, training]
sources: [apt-action-expert-pretraining-2606-12366]
last_updated: 2026-06-17
---

## Definition
Action Expert Pretraining은 continuous action expert를 language-conditioned VLA training 전에 vision-action prior로 먼저 안정화하는 training pattern이다.

## Current State
[[APT]]는 VLA policy를 VA prior와 language-conditioned likelihood로 factorization한다. 먼저 visual tokens만으로 action expert를 pretrain하면 language imbalance와 visual shortcut으로 인한 noisy gradient를 줄일 수 있다.

## Open Questions
- Pretraining 단계에서 어떤 visual/state representation이 가장 robust한가.
- Gated fusion이 saturation되거나 language를 무시하는지 감시하는 metric.
- 자율주행 trajectory planner에서 VA prior와 route/language likelihood를 어떻게 분리할지.

## Related
- [[VisionLanguageAction]]
- [[ActionGrounding]]
- [[apt-action-expert-pretraining-2606-12366]]
