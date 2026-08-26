---
title: "RISE: World Action Model을 위한 적응형 imagination"
type: source
tags: [autonomous-driving, world-action-model, adaptive-imagination, korean-translation]
date: 2026-08-26
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W35/rise-adaptive-imagination-2608-20430/paper-ko.md
source_hash: 82c5fc2f33860160
---

## Summary
RISE는 자율주행 World Action Model의 fixed future-rollout horizon을 scene별 sequential Roll/Stop decision으로 바꾼다. CounterDrive counterfactual clips로 risk와 future planning gain을 감독하고, NAVSIM·nuScenes에서 planning quality와 rollout cost의 균형을 평가한다.

## Key Claims
- Latent Evaluator가 current prefix의 risk와 deeper rollout의 expected planning gain을 예측한다.
- Rollout Gate는 gain과 computation cost를 비교해 variable-prefix diffusion planner로 routing한다.
- CounterDrive는 factual driving log의 단일 미래 한계를 human-verified counterfactual clips로 보완한다.

## Connections
- 자율주행 WAM의 adaptive compute와 safety-aware trajectory planning을 다룬다.

## Contradictions
- 없음. 논문의 simulation 기반 결과는 real-world deployment safety 보증과 구분해야 한다.
