---
title: "Cross-Embodiment Learning"
type: concept
sources:
  - xiaomi-robotics-1-2607-15330
tags: [robotics, embodiment, transfer, vla]
last_updated: 2026-07-22
---

## 정의

**Cross-Embodiment Learning**은 한 형태의 센서·기구 조합으로 수집한 경험을 다른 robot embodiment에 맞게 재정렬해 성능을 이전하는 학습 전략이다. pre-training과 post-training의 분리 또는 점진적 정렬을 통해 실현한다.

## 본 소스에서의 구현

[[Xiaomi-Robotics-1]]은 UMI 기반 pre-training에서 학습한 broad 조작 능력을 mobile manipulator, dual-arm, static arm로 확장하는 post-training을 수행해 embodiment gap을 줄인다.

## 핵심 요소

- 공통 표현 언어 확보(예: [[StateTransitionCaptioning]]).
- 액션 생성기에서 robot state를 조건으로 받아 embodiment별 제약 반영.
- pre-training objective와 post-training objective의 목적 분리.

## 관련 연결

- [[ActionGrounding]]: 상태 전이 언어가 embodiment 간 목표 정렬을 지원.
- [[Qwen3-VL]] + [[DiffusionTransformer]]: 멀티-모달 표현을 통한 transfer 기반 제공.
- [[Xiaomi-Robotics-1]]: 대규모 UMI pre-training→cross-embodiment post-training의 실증 사례.