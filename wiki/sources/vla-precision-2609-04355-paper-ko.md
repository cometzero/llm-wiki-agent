---
title: "VLA-Precision: real-world online RL로 VLA 정밀 작업을 개선하는 ACoB"
type: source
tags: [vla, reinforcement-learning, real-world-robotics, systems]
date: 2026-09-30
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W40/vla-precision-real-world-online-rl-2609-04355/paper-ko.md
source_hash: 0e8961d812c60bcc
---

## Summary
VLA-Precision은 large VLA의 real-world online RL에서 human correction 기반 빠른 behavior cloning과 TD/local ranking 기반 점진적 value calibration을 결합한 ACoB를 제안한다. ACoB-Stream은 frozen multimodal prefix context를 재사용·persist·on-demand fetch하고 trainable action-expert state만 동기화해 actor–learner cycle을 줄인다.

## Key Claims
- correction은 executed action의 return뿐 아니라 original proposal과의 state-matched preference signal을 제공한다.
- relative-advantage update와 frozen reference regularization은 critic error에 의한 policy drift를 줄이려 한다.
- reported real-world success/throughput은 task-specific high-precision chemistry manipulation 설정의 evidence다.

## Connections
- VLA post-training, human-in-the-loop RL, flow action policy, KV-context serving을 연결한다.

## Contradictions
- simulator-scale throughput 기법이 real-robot actor–learner loop에 그대로 적용된다는 가정을 제한한다.
