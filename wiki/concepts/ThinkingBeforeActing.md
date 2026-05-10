---
title: "Thinking Before Acting"
type: concept
tags: [Robotics, Reasoning, Planning, GeminiRobotics]
last_updated: 2026-05-10
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
---

## Definition
행동 수행 전, 내부적으로 다단계 추론/계획을 수행해 하위 단계 동작으로 분해한 뒤 실행하는 제어 철학.

## Contrast
단순 반응형 제어와 달리 의도 분해를 통해 오류 전파를 줄이고 장기 과업을 안정적으로 수행한다.

## In this source
[[GeminiRobotics]]는 이 원리를 중심으로 추론 계층과 행동 계층을 분리했다. 
