---
title: "THAW-VLA 핵심 기술 학습 자료"
type: source
tags: [vla, world-model, learning-guide, distillation]
date: 2026-09-23
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W39/thaw-vla-world-model-distillation-2609-24682/learning.md
source_hash: dc58c6723372d242
---

## Summary
학습 자료는 offline teacher feature cache, student projector alignment, action loss, deployment-time teacher removal을 구현 순서와 ablation 축으로 설명한다. AD로의 전이에서는 BEV/occupancy feature를 trajectory policy에 distill한 뒤 closed-loop safety/latency를 검증해야 한다고 제안한다.

## Key Claims
- Teacher layer, student alignment layer, \(\lambda\)는 representation distillation의 주요 ablation이다.
- projector를 버려도 student representation이 action backbone에 남는다는 것이 방법의 전제다.

## Connections
- [[THAWVLA]] — 학습 대상.
- [[WorldActionModel]] — model-family 비교 축.

## Contradictions
- Cached feature loss가 teacher의 generative planning 능력 전체를 보존하지는 않는다.
