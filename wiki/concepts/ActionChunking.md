---
title: "Action Chunking"
type: concept
tags: [Control, Robotics, VLA, PolicyLearning]
last_updated: 2026-05-10
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
---

## Definition
작은 단위 액션을 여러 프레임 동안 묶어 한 번에 예측하는 제어 전략이다. 저수준 제어를 매 타임스텝 재산출하지 않고, 짧은 구간의 동작 묶음을 처리해 지연/떨림/불안정성을 줄인다.

## Why it matters
로봇 조작에서 고빈도 제어와 안정성 사이의 트레이드오프를 완화한다. 특히 연속 동작이 많은 조작에서 유연성과 제어 품질을 동시에 높인다.

## In this source
- [[NVIDIAGR00T]]과 [[GeminiRobotics]] 모두 액션 청크 개념으로 반응성/안정성 문제를 다뤘다.
- [[PhysicalIntelligencePi]]는 또한 높은 동작 주파수를 구현하기 위한 연속 제어 표현과 함께 맥락적으로 사용한다.
