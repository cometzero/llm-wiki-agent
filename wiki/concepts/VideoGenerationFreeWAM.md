---
title: "Video-Generation-Free WAM"
type: concept
tags: [WAM, design-philosophy, LLM, VLM]
sources: [world-action-models-survey-2606-20781]
last_updated: 2026-06-24
---

## Definition

Video-Generation-Free WAM은 video generator를 predictive path에서 제거하고, language/vision-language/geometry/trajectory representation으로 action-facing future를 구성하는 설계 철학이다.

## Characteristics

- **출력**: language, geometric state, trajectory representation
- **장점**: 실시간 제어 가능, rendered future보다 compact causal evidence
- **단점**: physical grounding을 별도로 보장해야 함
- **Backbone**: LLM, VLM, JEPA, non-video diffusion 또는 hybrid

## Historical Position

VLA, world model, video generation 분야에서 가장 최근 emergence. "미래를 꼭 영상으로 꿈꿀 필요가 있는가?"라는 질문과 맞닿아 있다.

## Connections

- [[WorldActionModel]] — WAM 설계 철학 3가지 중 하나
- [[VLA]] — backbone으로 활용 가능
- [[LLM]] — backbone으로 활용 가능
- [[VLM]] — backbone으로 활용 가능
