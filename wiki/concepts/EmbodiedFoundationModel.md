---
title: "Embodied Foundation Model"
type: concept
tags:
  - embodied-ai
  - foundation-model
last_updated: 2026-07-29
sources:
  - data-pyramid-for-embodied-manipulation-2607-24744
---

# Embodied Foundation Model

[[EmbodiedFoundationModel]]은 로봇 과업에서 perception, reasoning, planning, action을 통합하려는 대규모 모델 계열을 통칭한다. [[DataPyramidForEmbodiedManipulation]] 분석에서는 아래 3가지로 나뉜다.

- [[EmbodiedBrainModel]]: 감각·공간·기억 기반 추론, affordance 추정, planning
- [[VisionLanguageAction]]: 관측+명령을 실행 가능한 행동으로 매핑
- [[WorldActionModel]]: action-conditioned state prediction, action-free 시계열 예측, 환경 변화 모델링

## 핵심 정렬 문제
- [[ActionSpaceAlignment]]
- [[RepresentationAlignment]]

## 실무적 함의
- 웹 scale semantic 학습만으로는 robot 실행 정밀도가 자동으로 올라가지 않으며, source별 supervised 신호의 정렬 설계가 모델 family별 성능 이전을 좌우한다.
