---
title: "RoboSemanticBench"
type: entity
tags: [benchmark, robotics, VLA]
sources: [robosemanticbench-2606-02277-ko]
last_updated: 2026-06-03
---

## Overview

RoboSemanticBench(RSB)는 [[VLA]] 모델의 [[SemanticGrounding]] 능력을 진단하기 위한 embodied benchmark이다. Question-Answer 블록 선택 과제를 통해 semantic expert와 action expert 간의 격차를 정량화한다.

## Key Properties

- **목적**: [[VLA]] 모델이 instruction semantics를 행동 예측에 올바르게 연결하는지 측정
- **Task**: multiple-choice 수학/상식 문제 → 정답 블록을 answer zone으로 pick-and-place
- **Metrics**: GSR, TSR, nSG(normalized Semantic Grounding)
- **Implementation**: Aloha-AgileX dual-arm tabletop simulator

## Key Finding

대표 [[VLA]] 모델들은 block grasp는 성공하지만, 정답 block 선택은 near-random ~ below-random 수준으로 semantic grounding gap이 존재함을 보여준다.

## Related Entities

- [[VLA]] — 진단 대상
- [[SemanticGrounding]] — 진단 개념
- [[EmbodiedBenchmark]] — 카테고리
