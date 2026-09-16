---
title: "Latent Interface Training 분석"
type: source
tags: [vla, robustness, action-prior, latent-interface]
date: 2026-09-16
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W38/latent-interface-training-2609-12641/analysis.md
source_hash: ac5faf838776ae01
---

## Summary
이 분석은 LIT를 direct visual conditioning을 terminal-pose-supervised bottleneck으로 대체하는 action-grounding 설계로 해석한다. four-model LIBERO/LIBERO-Plus 및 세 real-robot manipulation task의 결과를 ID/OOD/latency/safety 관점에서 구분한다.

## Key Claims
- Pose reconstruction은 action-relevant geometry를 남기려는 auxiliary constraint이며 control correctness 자체의 보장은 아니다.
- OOD viewpoint/noise 개선은 shortcut 완화 가설의 근거지만, text instruction shift는 별도 bottleneck이다.
- 100 latent token의 layerwise attention은 target control-rate에서 latency profiling이 필요하다.

## Connections
- [[LatentInterfaceTraining]] — design and evaluation analysis.
- [[VisionActionShortcut]] — nuisance-versus-causal cue separation.

## Contradictions
- LIBERO rollout success를 vehicle closed-loop safety 또는 open-world reliability와 동치로 둘 수 없다.
