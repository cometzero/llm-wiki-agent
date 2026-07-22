---
title: "Diffusion Policy"
type: concept
tags: [action-generation, policy-learning, visuomotor]
sources:
  - xiaomi-robotics-1-2607-15330-references
last_updated: 2026-07-22
---

## 요약

[[Diffusion Policy]]는 연속 동작을 생성할 때 diffusion 계열의 생성 방식으로 action sequence를 모델링하는 VLA/로보틱스 정책 접근이다. [[Xiaomi-Robotics-1]] 레퍼런스 맥락에서는 action diffusion 계열의 기초 흐름으로 정리되며, [[Xiaomi-Robotics-1]]의 DiT/flow 기반 설계와 비교되는 축이다.

## 주요 쟁점

- Continuous action space에서 노이즈 기반 생성의 정밀도와 안정성.
- action grounding 신뢰도와 시퀀스 일관성 확보.
- [[FlowMatching]] 기반 접근 및 other VLA flow model과의 구현/성능 트레이드오프.

## 링크드 항목

- [[pi0]], [[pi0.5]], [[Qwen3-VL]]: 생성형 VLA 계열 비교군.
- [[StateTransitionCaptioning]]: 데이터 supervision 관점에서의 보완 축.
