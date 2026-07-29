---
title: "WorldDiT"
type: concept
tags:
  - world-action
  - diffusion
  - embodied-ai
  - vision-language-action
  - action-generation
  - flow-matching
  - receding-horizon
last_updated: 2026-07-29
---

[[WorldDiT]]는 하나의 shared [[DiffusionTransformer]](또는 DiT 계열 백본)로 연속 제어용 액션 시퀀스와 미래 시각 예측 신호를 동시에 학습하는 [[WorldActionModel]] 계열 설계이다. 핵심은 학습 시 `action`과 `future RGB patch`를 동일한 generative objective로 공동 학습한 뒤, 추론 시에는 action path만 사용해 폐루프 지연을 낮추는 것이다.

## 핵심 아이디어

- `world-supervision + action-generation`을 단일 백본에서 처리해 파라미터 사용 효율을 높인다.
- `action chunk`(예: 7-step)를 생성하고 receding-horizon 방식(예: 3-step 실행 후 재관측/재계획)으로 closed-loop를 구성한다.
- future visual prediction은 보조 손실로 학습을 강화하지만, 추론에서는 action-only 경로를 남겨 latency를 관리한다.

## 위치

- [[Diffusion Policy]] 계열의 연속 액션 생성과 [[ActionChunking]]을 연결한다.
- [[WorldActionModel]], [[LatentWorldModels]], [[Model-PredictiveControl]]형 운영에서 액션-미래 동시 학습의 실전형 변형으로 분류된다.

## 구성 요소(대표)

- Conditioning: frozen [[CLIP]] text encoder, frozen [[MAE]] image encoder, trainable state encoder
- Core: shared [[DiffusionTransformer]]
- Heads: action velocity head, RGB patch velocity head
- Loss: `action velocity loss + future RGB patch velocity loss` 가중합

## 사용 규칙

- 시뮬레이션 성능 지표([[LIBERO]])만으로 실 배포를 단정하지 말고, real transfer 및 safety 신뢰성 점검이 동반되어야 한다.
- 체크포인트 선택/평가 방식이 과대해석될 수 있으므로 비교 실험의 로그 투명성이 중요하다.

## 관련 링크

[[WorldDiT]], [[DiffusionTransformer]], [[FlowMatching]], [[ActionChunking]], [[LIBERO]], [[RecedingHorizon]], [[AutonomousVehicle]], [[WorldActionModel]], [[VisionLanguageAction]], [[VLA4AD]]