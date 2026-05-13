---
title: "Embodiment Gap"
type: concept
tags: [robotics, transfer-learning, embodied-ai]
sources: [humannet-2605-06747-learning]
last_updated: 2026-05-13
---

## 정의
인간의 몸/손과 robot의 morphology/control space 사이의 차이. 인간 비디오에서 학습한 prior를 robot에 적용할 때 발생하는 핵심 도전 과제.

## 왜 발생하는가?

1. **Morphology 차이**: 인간의 손/팔 구조와 robot의 관절/엔드이펙터 구조가 다름
2. **Control space 차이**: 인간의 neuromuscular system과 robot의 motor control이 다름
3. **Perception 차이**: 인간의 시각/촉각과 robot 센서가 다른 정보를 수집

## HumanNet에서의 의미

HumanNet은 [[HumanCentricVideo]]를 [[VLA]] 사전학습에 활용하지만, [[EmbodimentGap]] 때문에:
- **Robot-specific post-training이 여전히 필요**
- Representation prior와 pretraining source로는 유용하지만 완전한 대체는 불가

## 극복 방법

- [[Retargeting]]: 인간 동작을 robot action space로 변환
- Domain adaptation: 인간-로봇 간 분포 정렬
- [[EmbodiedMidtrain]]: VLM-VLA 간 샘플 분포 정렬

## Related Concepts
- [[HumanCentricVideo]]
- [[Retargeting]]
- [[VLA]]
- [[EmbodiedMidtrain]]
