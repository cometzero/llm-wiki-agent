---
title: "Latent-Only"
type: concept
tags: [world-model, architecture, latent-representation]
sources: [world-action-models-survey-2606-20781-learning]
last_updated: 2026-06-24
---

## Definition

Latent-Only는 [[WorldActionModel]]의 action coupling 패턴으로, "pixel 복원 없이 latent future로 직접 action을 만드는" 방식이다.

## Process

```
Observation → Latent Prediction → Latent Action Decoder → Executable Action
```

## Characteristics

- **장점**: pixel-level보다 낮은 latency, 압축된 representation 활용
- **단점**: latent space의 해석 어려움, perceptual fidelity 확인 곤란

## Related Concepts

- [[WorldActionModel]]
- [[ActionCoupling]]
- [[PredictiveSubstrate]]
- [[RenderAndDecode]]
- [[VideoGenerationFree]]
