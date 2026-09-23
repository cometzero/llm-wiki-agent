---
title: "THAW-VLA: World Model 표현을 Compact VLA 정책으로 증류하기"
type: source
tags: [vla, world-model, representation-distillation, robotics]
date: 2026-09-23
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W39/thaw-vla-world-model-distillation-2609-24682/paper-ko.md
source_hash: babec23122ed663f
---

## Summary
THAW-VLA는 frozen Cosmos3-Nano world model의 cached hidden feature를 VLA student intermediate state에 align하고, teacher/projector는 deployment에서 제거하는 representation distillation 방법이다. 0.8B student의 LIBERO 97.9%, RoboCasa-GR1 48.2%→50.5%, RTX 5090에서 32 ms/1.86 GB를 보고한다.

## Key Claims
- World-model future-generation objective가 형성한 feature는 rollout 없이도 action policy의 physical prior가 될 수 있다.
- Deployed policy는 base VLA와 같은 graph이므로 test-time compute 증가가 없다.
- Manipulation closed-loop gain은 driving safety·multi-agent uncertainty 보장이 아니다.

## Connections
- [[THAWVLA]] — world-model representation distillation 방법.
- [[WorldActionModel]] — predictive-action model 비교 축.

## Contradictions
- Feature alignment는 causal physical understanding을 보장하지 않는다.
