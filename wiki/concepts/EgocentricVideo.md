---
title: "Egocentric Video"
type: concept
tags: [video, first-person, robotics]
sources: [humannet-2605-06747-learning]
last_updated: 2026-05-13
---

## 정의
행위자 시점의 1인칭 비디오. 카메라를 착용한 사람의 시점에서 촬영된 영상으로, 손과 물체의 직접적인 상호작용을 가까이서 볼 수 있다.

## 왜 VLA에 중요한가?

1. **손-물체 접촉 정보**: 물체 잡기, 조작 동작의 시각적 단서가 프레임에 직접 담김
2. **Actor intent**: 행위자가 무엇을 하려는지 시점에서 직접 유추 가능
3. **Action visual consequence**: 동작의 시각적 결과가 즉각적으로 관찰됨

## 관련 데이터셋
- [[Ego4D]]: 대규모 egocentric video benchmark
- [[EgoExo4D]]: egocentric + exocentric view 통합 데이터셋

## HumanNet에서의 활용
HumanNet은 Egocentric video에서 **action-centric visual prior**를 추출하여 [[VLA]] 모델의 사전학습에 활용한다.

## Related Concepts
- [[ExocentricVideo]]
- [[HumanCentricVideo]]
- [[VLA]]
- [[R3M]]
