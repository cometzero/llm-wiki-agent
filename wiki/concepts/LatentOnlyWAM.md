---
title: "Latent-Only WAM"
type: concept
tags: [WAM, design-philosophy, latent-space]
sources: [world-action-models-survey-2606-20781]
last_updated: 2026-06-24
---

## Definition

Latent-Only WAM은 미래를 pixel로 복원하지 않고 latent/feature space에서 유지하고, action decoder가 이 latent future를 사용하는 설계 철학이다.

## Characteristics

- **출력**: latent representation, feature space
- **장점**: rendered video보다 가볍고 action-relevant representation에 집중 가능
- **단점**: latent가 실제 물리적 causal structure를 담는지 검증이 어려움

## Historical Position

Render-and-Decode 이후 emergence, pixel decoding을 control path에서 제거하는 방향의 진화.

## Connections

- [[WorldActionModel]] — WAM 설계 철학 3가지 중 하나
- [[PredictiveSubstrate]] — feature-grounded substrate 활용
