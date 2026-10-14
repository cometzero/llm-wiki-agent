---
title: "GroundingPI 참고문헌"
type: source
tags: [huggingface-weekly, robotics, vla, grounding, references]
sources: [groundingpi-2609-39601]
date: 2026-10-14
last_updated: 2026-10-14
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W42/groundingpi-2609-39601/references.md
source_hash: fb2d02d2655571cf
arxiv_id: "2609.39601"
---

## Summary
Semantic Scholar references endpoint는 성공했으나 data가 비어 원문 bibliography로 핵심 9편을 선정했다. Pix2Seq coordinate generation, π0/π0.5 및 knowledge insulation, Flow Matching, StarVLA, RoboTwin/nuScenes, GRPO의 연결을 한국어로 설명한다.

## Key Claims
- Pix2Seq는 coordinate를 autoregressive output으로 표현하는 배경이며 Flow Matching은 continuous action expert의 velocity objective를 이해하는 기반이다.
- StarVLA를 토대로 foundation-to-action interface와 downstream capacity를 맞춰 backbone representation을 비교한다.
- 각 reference의 이번 full-PDF deep-read와 전체 reference API coverage를 주장하지 않으며 확인하지 못한 identifier를 만들지 않았다.

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
