---
title: "Flow Matching"
type: concept
tags: [Robotics, PolicyGeneration, ContinuousControl, VLA]
last_updated: 2026-05-10
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
---

## Definition
연속 상태 공간에서 동작 궤적을 노이즈 초기값에서 정교한 동작 상태로 점진적으로 정합시키는 생성 방식. 자기회귀 토큰 생성 대비 연속성 있는 행동 표현에 유리하다.

## In robotics
정밀한 동작 제어, 짧은 간격의 연속 제스처, 손-팔 조작에서 부드러운 궤적을 만드는 데 강점이 있다.

## In this source
[[PhysicalIntelligencePi]]는 [[Fast]] 계열과 결합해 학습 효율을 크게 높이며 동작 성능을 유지하려는 전략으로 강조된다.
