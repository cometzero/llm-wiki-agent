---
title: "Flow Matching"
type: concept
tags: [Robotics, PolicyGeneration, ContinuousControl, VLA, diffusion, generative-model, action-generation]
last_updated: 2026-07-22
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
  - xiaomi-robotics-1-2607-15330
---

## Definition

연속 상태 공간에서 동작 궤적을 노이즈 초기값에서 정교한 동작 상태로 점진적으로 정합시키는 생성 방식이다. 분포 사이의 vector field를 학습해 샘플이 목표 분포를 따르도록 만들며, 자기회귀 토큰 생성 대비 연속성 있는 행동 표현에 유리하다.

## In robotics

정밀한 동작 제어, 짧은 간격의 연속 제스처, 손-팔 조작에서 부드러운 궤적을 만드는 데 강점이 있다. Action chunk 예측처럼 연속 제어 신호를 생성할 때 diffusion/denoising 계열과 함께 중요한 선택지다.

## In prior source

[[PhysicalIntelligencePi]]는 [[Fast]] 계열과 결합해 학습 효율을 크게 높이며 동작 성능을 유지하려는 전략으로 flow/action generation을 강조한다.

## In Xiaomi-Robotics-1

[[Xiaomi-Robotics-1]]은 [[Qwen3-VL]] context와 robot state를 조건으로 [[DiT]]/[[DiffusionTransformer]] action generator를 학습하며, [[ActionChunking]] 대상인 short-horizon control trajectory를 flow matching objective로 생성한다. 이 경우 open-loop action MSE와 closed-loop robot success를 함께 해석해야 한다.

## Related links

- [[ActionChunking]] — flow matching의 생성 대상.
- [[FlowERD]] — traffic simulation에서 flow matching 계열을 사용한 비교 축.
- [[DiffusionPolicy]] — visuomotor action generation의 diffusion 계열 선행 흐름.
