---
title: "Representation Alignment"
type: concept
tags: [RepresentationLearning, DistributionShift, TransferLearning, VLM, VLA]
last_updated: 2026-05-10
---

## Definition
[[RepresentationAlignment]]는 사전학습 표현공간이 목표 도메인 분포와 얼마나 잘 일치하는지를 의미한다.

## Importance in Embodied Systems
[[EmbodiedMidtrain]]류 접근에서 가장 중요한 축은 모델 크기 자체가 아니라,
- [[VLM]] feature 공간에서의 분포 정합성,
- target domain(특히 [[RobotManipulation]])의 샘플 정합성,
- downstream task 성능과의 상관이다.

## Note
loss 자체는 유사해도 표현 정렬이 다르면 downstream 성능은 크게 달라질 수 있다.