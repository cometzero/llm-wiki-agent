---
title: "Xiaomi-Robotics-1"
type: entity
tags: [robotics, vla, embodied-ai, scaling]
last_updated: 2026-07-22
---

## 개요
[[Xiaomi-Robotics-1]]은 [[Xiaomi]]가 공개한 파운데이션형 [[Vision-Language-ActionModels]]으로, 100,000+ 시간 규모 real-world 조작 trajectory 기반 학습을 목표로 한 파이프라인이다.

## 핵심 기여
- UMI 기반 대규모 조작 데이터 수집.
- trajectory segment를 state transition 중심으로 자동 캡션링하여 pre-training supervision 생성.
- [[DataScaling]]/[[ModelCapacity]] 실험에서 scaling law 패턴 관찰.
- cross-embodiment post-training으로 실제 robot 형식(static arm, mobile manipulator, dual-arm)과 imperative instruction 정렬.
- RoboCasa365 및 RoboDojo benchmark에서 SOTA 수준 성능 강화.

## 출처
- arXiv: https://arxiv.org/abs/2607.15330
- Hugging Face: https://huggingface.co/papers/2607.15330
- Project: https://robotics.xiaomi.com/xiaomi-robotics-1.html

## 연결
- [[UMI]]
- [[StateTransitionCaptioning]]
- [[CrossEmbodimentLearning]]
- [[ActionChunking]]
- [[RoboCasa365]], [[RoboDojo]]
