---
title: "VLA-Precision 핵심 기술 학습 자료"
type: source
tags: [vla, learning, online-rl, systems]
date: 2026-09-30
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W40/vla-precision-real-world-online-rl-2609-04355/learning.md
source_hash: dde036a1f6edb7c5
---

## Summary
이 학습 자료는 ACoB의 TD/ranking/relative-advantage/BC/reference objective와 ACoB-Stream의 KV context lifecycle을 단계적으로 설명한다. 안전한 real-world online RL을 위해 correction validity, buffer integrity, partial-state versioning, impedance constraint를 함께 점검하도록 구성했다.

## Key Claims
- TD loss는 overwrite된 proposal의 quality를 직접 교정하지 못하므로 state-matched ranking이 필요하다.
- context cache는 frozen prefix가 truly invariant할 때만 안전하게 재사용할 수 있다.
- partial action-expert synchronization은 policy freshness를 개선하지만 control safety layer를 대체하지 않는다.

## Connections
- Real-world online RL, VLA deployment, context cache, flow action generation 학습 자료.

## Contradictions
- large VLA를 online update하면 자연히 real-time closed loop가 된다는 단순 가정을 반박한다.
