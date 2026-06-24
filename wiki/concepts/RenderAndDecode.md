---
title: "Render-and-Decode"
type: concept
tags: [world-model, architecture, action-generation]
sources: [world-action-models-survey-2606-20781-learning]
last_updated: 2026-06-24
---

## Definition

Render-and-Decode는 [[WorldActionModel]]의 action coupling 패턴 중 하나로, "미래 영상을 생성한 뒤 그 결과에서 action을 추출"하는 방식이다.

## Process

```
Observation → Predictive Model → Future Video → Action Decoder → Executable Action
```

## Characteristics

- **장점**: 직관적, visual inspection 가능
- **단점**: pixel generation latency 높음, 불필요한 visual detail 포함

## Related Concepts

- [[WorldActionModel]]
- [[ActionCoupling]]
- [[LatentOnly]]
- [[VideoGenerationFree]]
- [[DiffusionModel]]
