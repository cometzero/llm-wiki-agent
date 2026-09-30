---
title: "VLA-Precision 분석"
type: source
tags: [vla, online-rl, policy-drift, analysis]
date: 2026-09-30
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W40/vla-precision-real-world-online-rl-2609-04355/analysis.md
source_hash: e63fac31716decb4
---

## Summary
이 분석은 VLA-Precision을 online-RL algorithm과 runtime system을 함께 설계한 사례로 정리한다. action chunk는 impedance controller로 ground되고, correction/replay/context buffer가 critic calibration과 LoRA action-expert update를 연결한다.

## Key Claims
- human correction은 BC data이면서 original proposal을 교정하는 pairwise critic supervision이다.
- frozen prefix/KV persistence와 partial-state synchronization은 compute와 policy freshness의 핵심 병목이다.
- real-world closed-loop success는 open-loop action loss만으로 대체할 수 없다.

## Connections
- VLA action grounding, online RL, context-cache serving, real-robot deployment.

## Contradictions
- high task success가 broad compositional generalization 또는 certified safety를 의미하지 않는다는 한계를 기록한다.
