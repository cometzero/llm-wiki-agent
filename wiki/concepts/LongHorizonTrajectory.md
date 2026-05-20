---
title: "Long-Horizon Trajectory"
type: concept
tags: [trajectory, planning, robotics, VLA]
sources: [mobileego-anywhere-2605-05945, mobileego-anywhere-2605-05945-learning]
last_updated: 2026-05-20
---

# Long-Horizon Trajectory

Long-horizon trajectory는 수십 분 이상 이어지는 연속 행동/상태 경로를 말하며, [[VLA]] 학습에서 중요한 데이터 유형이다.

## 왜 중요한가?

- **Planning 학습**: 장기 목표 달성을 위한 다단계 계획 수립 능력 학습
- **State tracking**: object/scene state의 시간에 따른 변화를 추적
- **Action grounding**: 언어/시각 reasoning을 실제 행동으로 연결

## 단기 clip의 한계

짧은 egocentric clip(수 초)만으로는:
- Object state와 sub-goal dependency 축적이 불가
- Planning/memory/action grounding 학습이 어려움

## 관련 소스

- [[mobileego-anywhere-2605-05945]]
