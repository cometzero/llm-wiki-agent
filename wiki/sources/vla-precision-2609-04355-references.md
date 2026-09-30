---
title: "VLA-Precision 참고 레퍼런스"
type: source
tags: [vla, real-world-rl, intervention-learning, references]
date: 2026-09-30
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W40/vla-precision-real-world-online-rl-2609-04355/references.md
source_hash: baa43c189e17bdb8
---

## Summary
이 reference map은 HIL-SERL/ConRFT 계열 intervention learning, OpenVLA/Octo/π0 계열 action backbone, simulation VLA-RL과 real-world systems를 대비한다. VLA-Precision은 human feedback, critic calibration, KV cache/data lifecycle을 한 online post-training loop로 묶는다.

## Key Claims
- real-world correction learning은 simulation VLA-RL과 data quality·safety·throughput 조건이 다르다.
- action expert만 온라인으로 갱신하는 design은 prior preservation과 deployment synchronization 비용에 직접 연결된다.

## Connections
- Human-in-the-loop RL, VLA post-training, teleoperation, efficient serving 문헌 지도.

## Contradictions
- full-model end-to-end update가 항상 더 나은 adaptation이라는 관점을 비용·drift 측면에서 제한한다.
