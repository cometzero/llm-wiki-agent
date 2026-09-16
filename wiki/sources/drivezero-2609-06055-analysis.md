---
title: "DriveZero 분석"
type: source
tags: [autonomous-driving, trajectory-planning, closed-loop-evaluation]
date: 2026-09-16
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W37/drivezero-end-to-end-driving-2609-06055/analysis.md
source_hash: b3f2b16a7083b7ab
---

## Summary
이 분석은 DriveZero의 핵심을 RL teacher, multi-VFM backbone, WTA multi-trajectory student로 분해하고, student가 open-loop frame에서 학습되지만 target behavior는 closed-loop rollout에서 온다는 점을 구분한다. reward·simulator·privileged input의 품질이 action-grounding과 안전성의 상한을 정한다.

## Key Claims
- camera-only deploy policy의 행동 신호는 human log가 아니라 privileged teacher rollout이다.
- TTS candidate search는 fixed checkpoint의 action quality를 높일 수 있지만 critic calibration에 의존한다.
- multi-view feature와 proposal scorer의 실제 vehicle latency는 별도 계측이 필요하다.

## Connections
- [[DriveZero]] — system analysis.
- [[ClosedLoopReinforcementLearning]] — open-loop training label과 interactive policy learning의 차이.

## Contradictions
- NAVSIM의 pseudo closed-loop 결과를 actual reactive road safety 검증으로 해석할 수 없다.
