---
title: "Imitation Learning"
type: concept
tags: [robotics, reinforcement-learning, policy-learning]
sources: [humannet-2605-06747-references, humannet-2605-06747]
last_updated: 2026-05-13
---

## Definition
Imitation Learning(모방 학습)은 전문가의 행동 시연으로부터 로봇 정책을 학습하는 방법으로, [[EgoMimic]]은 제1인칭 인간 궤적과 로봇 데모의 정렬을 통해 이 접근을 구현한다.

## Role in Human Video Transfer
[[EgoMimic]]은 인간 비디오의 행동 패턴을 로봇으로 전이하는 구체적 메커니즘으로, [[HumanNet]]의 인간 중심 비디오 → [[VLA]] 학습 접근의 선행 연구가 된다.

## Connections
- [[EgoMimic]] — egocentric human trace와 robot demonstration alignment
- [[R3M]] — passive human video representation의 전이
- [[HumanNet]] — 인간 비디오의 모방 학습 기반 전이 가능성 시사
- [[VLA]] — 모방 학습으로 학습된 행동 정책의 통합 대상

## Summary
모방 학습은 [[HumanNet]]의 인간 비디오 → [[VLA]] 접근에서 핵심 메커니즘으로, [[R3M]]과 [[EgoMimic]]이 이 방향의 가능성을 검증했다.
