---
title: "Exocentric Video"
type: concept
tags: [video, third-person, robotics]
sources: [humannet-2605-06747-learning]
last_updated: 2026-05-13
---

## 정의
관찰자(제3자) 시점의 3인칭 비디오. 행위자가 착용한 카메라가 아닌, 외부에 설치된 카메라로 촬영된 영상.

## 왜 필요한가?

1. **전체적인 몸의 움직임**: 팔, 다리, 몸통의 전체적인 동작 패턴 관찰 가능
2. **공간적 맥락**: 환경 내에서의 위치와 관계 정보 제공
3. **Social interaction**: 행위자 간의 상호작용 기록 가능

## HumanNet에서의 활용
HumanNet은 Exocentric video에서 **motion/context prior**를 추출하여 [[VLA]] 모델의 사전학습에 활용한다.

## Related Concepts
- [[EgocentricVideo]]
- [[HumanCentricVideo]]
- [[EgoExo4D]]
- [[VLA]]
