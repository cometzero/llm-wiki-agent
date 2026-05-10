---
title: "Gemini Robotics"
type: entity
tags: [Google, Gemini, VLA, Robotics, EmbodiedReasoning]
last_updated: 2026-05-10
sources:
  - nvidia-gr00t-vs-gemini-robotics-vs-pi-로봇의-뇌는-어떻게-다르게-설계됐을까-vla-모델-3대장-비교-분석
---

## Summary
[[Google]]이 제시한 로봇 제어 아키텍처 계열로, 거대 모델 기반의 추론과 로봇 실행을 분리해 실시간성과 일반화를 같이 확보하려는 접근을 가진다.

### 핵심 특징
- [[ThinkingBeforeActing]]을 통해 추론(계획) → 실행(행동) 흐름을 강화한다.
- 클라우드 기반 대형 추론 백본과 로봇 온보드의 짧은 지연 디코더를 결합한다.
- [[MotionTransfer]]는 서로 다른 로봇으로 동작 지식과 전략을 이동시키기 위한 핵심 장치다.
- 인바디먼트가 다양한 환경에서 재학습 비용을 낮추기 위한 구조로 확장성을 겨냥한다.

### 연결
- [[Gemini]], [[Google]], [[EmbodiedReasoning]], [[VLA]] 및 [[Robotics]] 맥락에서 중요하다.
