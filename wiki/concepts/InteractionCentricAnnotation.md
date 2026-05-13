---
title: "Interaction-Centric Annotation"
type: concept
tags: [annotation, robotics, video]
sources: [humannet-2605-06747-learning]
last_updated: 2026-05-13
---

## 정의
단순한 caption을 넘어서, 손/몸/물체/동작/상태 변화 정보를 모두 담는 비디오 어노테이션 방식.

## 구성 요소

| 요소 | 설명 |
|---|---|
| Caption | 자연어로 동작 서술 |
| Hand pose | 손의 자세/위치 정보 |
| Body pose | 몸의 자세/위치 정보 |
| Object information | 상호작용하는 물체 정보 |
| Action labels | 동작 유형 라벨 |
| State changes | 상태 변화 정보 |

## 왜 중요한가?

- Robot manipulation task에 필요한 세밀한 동작 정보 제공
- [[Retargeting]] 시 인간 동작을 robot action space로 매핑하는 데 필수
- Egocentric view에서의 세밀한 상호작용 정보 추출 가능

## Related Concepts
- [[HumanCentricVideo]]
- [[Retargeting]]
- [[EmbodimentGap]]
- [[VLA]]
