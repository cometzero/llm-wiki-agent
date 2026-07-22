---
title: "Action Chunking"
type: concept
tags: [Control, Robotics, VLA, PolicyLearning, action-generation]
last_updated: 2026-07-22
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
  - xiaomi-robotics-1-2607-15330
---

## Definition

작은 단위 액션을 여러 프레임 동안 묶어 한 번에 예측하는 제어 전략이다. 저수준 제어를 매 타임스텝 재산출하지 않고, 짧은 구간의 동작 묶음을 처리해 지연/떨림/불안정성을 줄인다. Xiaomi-Robotics-1 맥락에서는 horizon \(H\) 길이의 연속 trajectory/action chunk를 [[DiT]] 기반 generator가 생성한다.

## Why it matters

로봇 조작에서 고빈도 제어와 안정성 사이의 트레이드오프를 완화한다. 특히 연속 동작이 많은 조작에서 유연성과 제어 품질을 동시에 높인다. 다만 action chunk가 길수록 stale action이나 tail error가 누적될 수 있어 [[ClosedLoopEvaluation]] 및 online correction이 중요하다.

## In prior VLA sources

- [[NVIDIAGR00T]]과 [[GeminiRobotics]] 모두 액션 청크 개념으로 반응성/안정성 문제를 다뤘다.
- [[PhysicalIntelligencePi]]는 높은 동작 주파수를 구현하기 위한 연속 제어 표현과 함께 맥락적으로 사용한다.

## In Xiaomi-Robotics-1

- [[Xiaomi-Robotics-1]]은 [[Qwen3-VL]]이 만든 observation/language context와 robot state를 조건으로 [[DiffusionTransformer]]/[[FlowMatching]] action branch에서 action chunk를 생성한다.
- Pre-training의 [[StateTransitionCaptioning]]은 action chunk가 달성해야 할 state change를 언어로 지정해 action grounding을 강화한다.

## Connections

- [[Vision-Language-ActionModels]]
- [[ActionGrounding]]
- [[Xiaomi-Robotics-1]]
- [[VLA-Policy]]
