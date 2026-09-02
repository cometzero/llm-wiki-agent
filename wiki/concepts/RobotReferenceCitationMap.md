---
title: "Robot Reference Citation Map"
type: concept
tags: [reference-map, benchmark, vla, cross-embodiment]
last_updated: 2026-09-02
---

## 개념

[[Robot Reference Citation Map]]는 특정 VLA 논문이나 시스템을 이해할 때, 코드 계보, backbone 출처, 벤치마크, head 구성, 실측 protocol을 한 번에 연결해 읽는 비교 프레임이다.

## 핵심 주장

- 단일 논문 성능을 해석할 때는 데이터량만 보지 않고, 출발 backbone([[VisionLanguageModel]]), action head family([[OFT]], [[PI]], [[GR00T]]), action-space 정렬 전략([[ActionSpaceAlignment]])을 함께 읽어야 한다.
- [[RoboDojo]], [[VLA-Arena]] 같은 benchmark protocol은 점수 비교의 전제 조건이며, leaderboard split와 metric 정의가 동일해야 한다.

## 예시 적용

- [[VLAct]]의 성능 주장은 [[StarVLA]], [[StarVLA-Alpha]], [[pi0.5]], [[GR00T-N1]], [[ABot-M0]], [[Xiaomi-Robotics-1]], [[RoboDojo]], [[VLA-Arena]], [[Xiaomi-Robotics-0]]를 함께 묶은 레퍼런스 맵에서 더 견고하게 해석된다.

## 연결

- [[CrossEmbodimentLearning]]
- [[ActionSpaceAlignment]]
- [[RepresentationLearning]]
- [[DataRecipe]]
- [[VLAct]]