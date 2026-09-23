---
title: "THAW-VLA 분석"
type: source
tags: [vla, world-model, distillation, analysis]
date: 2026-09-23
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W39/thaw-vla-world-model-distillation-2609-24682/analysis.md
source_hash: 16f100b3586cff5f
---

## Summary
분석은 THAW-VLA를 expensive test-time imagination 대신 world-model representation만 student policy에 전달하는 implicit transfer로 분류한다. Fast WAM의 rollout 효율화와 달리 teacher cache/feature alignment로 real-time control budget을 지킨다.

## Key Claims
- \(\mathcal L_{act}+\lambda\lVert P(z^S)-z^W\rVert^2\)가 action supervision과 physical feature prior를 결합한다.
- LIBERO/RoboCasa/real robot success는 closed-loop evidence지만 long-horizon autonomous driving evidence가 아니다.

## Connections
- [[THAWVLA]] — 방법 분석 대상.
- [[WorldActionModel]] — 관련 비교 축.

## Contradictions
- Teacher feature의 quality와 coverage가 student robustness를 자동 보장하지 않는다.
