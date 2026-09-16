---
title: "DriveZero: 인간 시연을 넘어서는 End-to-End 자율주행"
type: source
tags: [autonomous-driving, end-to-end, closed-loop-rl, vision-foundation-model]
date: 2026-09-16
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W37/drivezero-end-to-end-driving-2609-06055/paper-ko.md
source_hash: 9110c657a1a0a301
---

## Summary
DriveZero는 사람 운전 궤적의 imitation supervision 대신, log-initialized mixed-agent simulator에서 PPO로 학습한 privileged DriveRL teacher의 rollout을 camera-only planner로 증류한다. DriveVFM은 DINOv3, SigLIP2, SAM, Depth Anything V2의 feature를 raw image에서 하나의 driving backbone으로 모으며, 최종 planner는 multi-view image·ego state·command에서 trajectory proposal과 score를 낸다.

## Key Claims
- Closed-loop RL teacher는 policy-induced state와 human log의 단일-future 제약을 보완한다.
- Perception과 action은 서로 다른 pretraining regime으로 학습한 뒤 trajectory distillation으로 결합할 수 있다.
- nuPlan reactive/non-reactive, NAVSIM, HUGSIM 평가는 서로 다른 closed-loop 근거이며 real-road safety guarantee와는 구분해야 한다.

## Connections
- [[DriveZero]] — privileged RL behavior를 camera-only planner로 옮기는 system.
- [[ClosedLoopReinforcementLearning]] — interactive rollout과 value-guided test-time search의 학습 축.

## Contradictions
- 순수 imitation E2E driving과 달리 사람 trajectory를 student의 직접 action target으로 쓰지 않는다.
