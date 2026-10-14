---
title: "GroundingPI 한국어 기술 번역"
type: source
tags: [huggingface-weekly, robotics, vla, grounding, paper-ko]
sources: [groundingpi-2609-39601]
date: 2026-10-14
last_updated: 2026-10-14
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W42/groundingpi-2609-39601/paper-ko.md
source_hash: 13c3173a1831ce3a
arxiv_id: "2609.39601"
---

## Summary
본문 1–6의 구조와 핵심 수식·benchmark 수치를 보존하고 부록 protocol·training·downstream interface·limitations를 상세히 번역했다. 모델은 language-conditioned precise perception foundation이며 driving과 manipulation에는 서로 다른 numerical action learner를 사용한다. 무생략 PDF 대역본은 아니며 dense tables·장문 조건부 유도는 명시적으로 축약했다.

## Key Claims
- Point/box는 1,000 atomic coordinate token과 semantic/protocol vocabulary를 공유한다. 전체 multimodal parameter는 약 4.844B이며 4B는 language-backbone 계열명이다.
- nuScenes front camera와 ego history에서 3초 동안 여섯 cumulative metric waypoint를 생성하며 평균 open-loop L2 0.296 m를 보고한다.
- Robot branch는 여덟 depth의 hidden feature를 fixed Action DiT로 공급한다. Scene/entity OOD와 limited-demonstration efficiency를 평가했지만 real-world deployment는 없다.

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
