---
title: "Human-centric Video"
type: concept
tags: [video, robotics, embodied-learning]
sources: [humannet-2605-06747-learning]
last_updated: 2026-05-13
---

## 정의
인간 활동이 비디오 clip의 중심 신호인 비디오 데이터. 행위자의 동작, 물체와의 상호작용, 환경 내 활동이 핵심 콘텐츠로 담긴다.

## Human-centric Video의 두 가지 시점

### Egocentric Video (1인칭 시점)
- 행위자 시점의 비디오
- 손-물체 접촉, actor intent, action의 시각적 결과가 한 프레임에 직접 담김
- 예: [[Ego4D]], GoPro 영상

### Exocentric Video (3인칭 시점)
- 관찰자(제3자) 시점의 비디오
- 전체적인 몸의 움직임과 맥락 정보 제공
- 예: [[EgoExo4D]]의 exo 뷰

## HumanNet에서의 역할
HumanNet은 이 두 시점의 비디오를 통합하여:
- **Action-centric visual prior**: Egocentric view에서 추출
- **Motion/context prior**: Exocentric view에서 추출

이를 결합하여 VLM/VLA continued training에 활용한다.

## Related Concepts
- [[EgocentricVideo]]
- [[ExocentricVideo]]
- [[VLA]]
- [[EmbodimentGap]]
- [[Retargeting]]
