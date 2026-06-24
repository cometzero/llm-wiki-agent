---
title: "WorldActionModel"
type: concept
tags: [autonomous-driving, policy, world-model, architecture, vla, wam]
sources: [nvidia-omnidreams-2606-03159, nvidia-omnidreams-2606-03159-learning, world-action-models-survey-2606-20781, world-action-models-survey-2606-20781-analysis, world-action-models-survey-2606-20781-learning]
last_updated: 2026-06-24
---

## Overview

World Action Model(WAM)은 future prediction을 action decision path 안에 남기는 predictive-action model이다. 기존 [[VLA]]가 language/vision context에서 action을 직접 예측한다면, WAM은 world dynamics나 future representation을 예측하고 그 표현을 planner, scorer, action decoder가 실제로 사용하게 만든다.

## WAM vs VLA

| Aspect | [[VLA]] | [[WorldActionModel]] |
|---|---|---|
| Focus | language/vision-conditioned action | action-facing future prediction |
| Representation | semantic/linguistic/visual tokens | pixel, latent, geometric, language-state future |
| Typical output | action chunk, waypoint, trajectory, control | action score, future-conditioned action, planner guidance |
| Deployment concern | grounding, hallucination, latency | causality, closed-loop utility, memory/latency trade-off |

## Key Characteristics

1. **Action-facing future**: visual fidelity보다 action decision에 필요한 future evidence를 우선한다.
2. **Predictive substrate**: 미래가 pixel, latent, language, geometry 중 어디에 표현되는지 명시한다.
3. **Action coupling**: action이 prediction에 어떻게 들어가고, predicted future가 action decoder로 어떻게 나오는지 정의한다.
4. **Closed-loop utility**: open-loop prediction이 아니라 policy success, safety, latency, controllability가 중요하다.

## Design Families

- [[RenderAndDecode]]: rendered future를 만든 뒤 action을 decode한다.
- [[LatentOnly]] / [[LatentOnlyWAM]]: pixel 복원 없이 latent future를 action에 사용한다.
- [[VideoGenerationFree]] / [[VideoGenerationFreeWAM]]: video generator 없이 reasoning, geometry, memory, state representation을 사용한다.

## Autonomous Driving Context

[[OmniDreams]]와 [[AlpaSim]] 계열에서는 generative world model이 closed-loop simulation을 지원하고, [[Alpamayo]] 같은 policy model이 WAM-like architecture로 world dynamics와 action을 함께 다룬다. 자율주행에서는 WAM이 route, traffic participant dynamics, safety verifier, candidate trajectory scoring에 연결될 때 의미가 크다.

## Connections

- [[PredictiveSubstrate]] — future representation의 공간.
- [[ActionCoupling]] — action과 prediction이 결합되는 방식.
- [[VideoWorldModels]] — rendered/latent future를 생성하는 world model 계열.
- [[Model-PredictiveControl]] — 예측 기반 action selection의 전통적 프레임.
- [[PolicyTrim]] — WAM은 아니지만 VLA deployment efficiency의 action-side 병목을 보여주는 관련 연구.
