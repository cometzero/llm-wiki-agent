---
title: "Video-Generation-Free"
type: concept
tags: [world-model, architecture, reasoning]
sources: [world-action-models-survey-2606-20781-learning]
last_updated: 2026-06-24
---

## Definition

Video-Generation-Free는 [[WorldActionModel]]의 action coupling 패턴으로, "영상 생성 없이 reasoning/geometry/state로 action-facing future를 구성"하는 방식이다.

## Approach Examples

- Language-based reasoning
- Geometric state prediction (3D occupancy, pose)
- Physics-based simulation
- Symbolic reasoning

## Characteristics

- **장점**: 가장 낮은 latency 가능, interpretable
- **단점**: rich perceptual information 손실 가능성

## Related Concepts

- [[WorldActionModel]]
- [[ActionCoupling]]
- [[RenderAndDecode]]
- [[LatentOnly]]
- [[VisualReasoning]]
