---
title: "GroundingPI 분석"
type: source
tags: [huggingface-weekly, robotics, vla, grounding, analysis]
sources: [groundingpi-2609-39601]
date: 2026-10-14
last_updated: 2026-10-14
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W42/groundingpi-2609-39601/analysis.md
source_hash: b3cf7ac1e6fbd2bf
arxiv_id: "2609.39601"
---

## Summary
Precise grounding을 action data 이전의 reusable perceptual foundation으로 보는 연구다. AD numerical trajectory generation과 robot representation-to-control 경로를 taxonomy·language role·action grounding·training·metric 관점에서 구분했다. 실험 성과와 OCR/architecture/System-1 hypothesis, 분석자의 deployment proposal을 분리한다.

## Key Claims
- nuScenes L2는 cumulative-horizon mean으로 closed-loop vehicle performance나 endpoint-only metric과 다르다.
- RoboTwin Full 66.20%와 Clean2Random 17.60%는 다른 protocol이다. RoboCasa-GR1 full ID 최고는 GroundingPI가 아니라 RynnBrain이다.
- F group의 OCR/Layout/GUI complementarity는 OCR-only causal effect가 아니다. Serialized tokens/box는 matched action latency speedup이 아니다.

## Key Quotes
긴 원문 인용 대신 CC BY 4.0 원문과 raw 번역/분석을 참조한다.

## Connections
- [[GroundingPI]] — 네 deliverable과 연구 방법을 연결하는 중심 페이지.
- [[PreciseGroundingTransfer]] — native spatial perception과 downstream action learning의 연결.
- [[VisionLanguageModel]] — language-conditioned target perception.
- [[AutonomousDrivingVLA]] — metric numerical waypoint interface와 open-loop 평가 경계.
- [[FlowMatching]] — robot continuous action generation.

## Contradictions and Boundaries
- 평균 grounding 우위는 모든 benchmark에서의 dominance가 아니다. Backbone 비교는 scale/architecture/pretraining의 인과를 isolate하지 않는다.
- OCR catalyst와 System-1/2 division은 hypothesis이며 실제 차량/로봇 배포 및 integrated latency는 검증하지 않았다.
- 기존 위키의 closed-loop driving 연구와 충돌하는 결과가 아니라 다른 평가 범위의 evidence다.

## Source
https://arxiv.org/html/2609.39601v1
