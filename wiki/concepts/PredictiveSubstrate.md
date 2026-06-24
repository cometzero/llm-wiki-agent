---
title: "Predictive Substrate"
type: concept
tags: [world-model, representation, future-prediction]
sources: [world-action-models-survey-2606-20781-learning]
last_updated: 2026-06-24
---

## Definition

Predictive substrate는 [[WorldActionModel]]에서 "미래가 표현되는 공간"을 의미한다. 다양한 표현 수준을 포함한다:

- **Pixel**: video generation model의 원시 영상 출력
- **Latent**: compressed representation 공간 (VAE, diffusion latent)
- **Language**: text description으로 미래 상태 표현
- **Geometric state**: 3D geometry, occupancy, pose 등의 구조적 표현

## Trade-offs

| Substrate | 장점 | 단점 |
|-----------|------|------|
| Pixel | Visual fidelity 높음 | 높은 latency, 불필요한 detail 포함 |
| Latent | 효율적 압축, task-relevant features | 해석 어려움 |
| Language | 추상적 추론 가능 | 세밀한 행동 표현 한계 |
| Geometric | 정확한 물리 표현 | perception 오류 전파 |

## Related Concepts

- [[WorldActionModel]]
- [[LatentOnly]]
- [[VideoGeneration]]
- [[RenderAndDecode]]
