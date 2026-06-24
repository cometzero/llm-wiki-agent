---
title: "Action Coupling"
type: concept
tags: [world-model, action-generation, architecture]
sources: [world-action-models-survey-2606-20781-learning]
last_updated: 2026-06-24
---

## Definition

Action coupling은 [[WorldActionModel]]에서 action이 미래 예측에 어떻게 관여하는지를 정의한다. 핵심 질문:
1. **Input coupling**: candidate action/action history가 predictive substrate에 조건으로 들어가는가?
2. **Output coupling**: 예측된 미래에서 action을 어떻게 추출하는가?

## Patterns

- **Render-and-Decode**: 미래 영상을 생성 → 영상에서 action decoding
- **Latent-Only**: pixel 복원 없이 latent future에서 직접 action 예측
- **Video-Generation-Free**: 영상 생성 없이 reasoning/geometry/state로 action-facing future 구성

## Related Concepts

- [[WorldActionModel]]
- [[PredictiveSubstrate]]
- [[RenderAndDecode]]
- [[LatentOnly]]
- [[VideoGenerationFree]]
