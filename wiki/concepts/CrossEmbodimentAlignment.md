---
title: "Cross-Embodiment Alignment"
type: concept
tags:
  - embodiment
  - policy-transfer
  - generalization
sources:
  - data-pyramid-for-embodied-manipulation-2607-24744
last_updated: 2026-07-29
---

## 정의

**Cross-Embodiment Alignment**는 서로 다른 로봇 형태/구동 방식에서 동일 과제 정책을 공유 가능한 형태로 정렬하는 과정이다.

## 핵심 요소

- action representation 정규화
- 관측 space 정합 (sensor/state projection)
- 목표 표현의 geometry consistency

## 관계

이 개념은 기존 [[CrossEmbodimentLearning]]의 정렬·일반화 이슈를 더 구체적으로 실행 단계로 묶은 하위 프레임이다.
실무에서는 [[UMI]]로 생성한 일반화 가능한 표현을 [[RealRobotData]]로 보정한다.

## 반응 신호

- 실데이터 적응 속도
- OOD task에서 action feasibility
- recovery 동작의 전이 안정성

## 연결

- [[DataPyramidForEmbodiedManipulation]]
- [[Xiaomi-Robotics-1]]
- [[CrossEmbodimentLearning]]
- [[RealRobotData]]
