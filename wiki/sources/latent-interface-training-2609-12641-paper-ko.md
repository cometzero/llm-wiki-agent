---
title: "LIT: 일반화 가능한 Robot Foundation Model을 위한 Latent Interface Training"
type: source
tags: [vla, robotics, world-action-model, generalization, action-grounding]
date: 2026-09-16
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W38/latent-interface-training-2609-12641/paper-ko.md
source_hash: 83d9854436f4e4de
---

## Summary
Latent Interface Training은 VLA/WAM이 scene의 task-irrelevant visual correlation으로 action을 정하는 vision–action shortcut을 줄이는 two-stage procedure다. image 없이 terminal SE(3) pose-conditioned action prior를 만들고, 이후 pose reconstruction을 받는 latent token만이 visual backbone과 action expert를 연결한다.

## Key Claims
- Image-free action pretraining은 action expert를 visual nuisance correlation에서 분리한다.
- Pose-supervised latent interface는 spatially relevant visual information을 action conditioning에 보존하려 한다.
- Pi0.5, MolmoAct2, FAST-WAM, ImageWAM에서 LIBERO-Plus OOD success 개선이 보고되지만 language shift는 일관되게 개선되지 않는다.

## Connections
- [[LatentInterfaceTraining]] — two-stage VLA/WAM interface method.
- [[VisionActionShortcut]] — LIT가 직접 겨냥하는 generalization failure.

## Contradictions
- Visual robustness 향상은 contact dynamics, long-horizon recovery 또는 모든 language shift에 대한 보장이 아니다.
