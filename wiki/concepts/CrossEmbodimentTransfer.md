---
title: "Cross-Embodiment Transfer"
type: concept
tags: [Embodiment, Robotics, Generalization, PolicyTransfer]
last_updated: 2026-05-10
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
---

## Definition
서로 다른 로봇 신체(관절 수, 팔 수, 센서 배치, 제어 인터페이스) 사이에서 동작 지식이나 정책을 전이하는 능력.

## Why it matters
로봇별로 대규모 새 데이터를 수집해야 하는 비용 문제를 완화하고, 하나의 학습 집약 전략을 다중 플랫폼으로 확장한다.

## In this source
- [[NVIDIAGR00T]]는 인바디먼트 스페시픽 적응 모듈을 둔다.
- [[GeminiRobotics]]는 모션 전이를 통해 상호 이전을 강화한다.
- [[PhysicalIntelligencePi]]는 다형태 학습 구성을 통해 지속적으로 강화한다.
