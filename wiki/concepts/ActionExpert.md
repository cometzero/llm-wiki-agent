---
title: "Action Expert"
type: concept
tags: [VLA, dual-system, action]
sources: [robosemanticbench-2606-02277-ko]
last_updated: 2026-06-03
---

## Definition

Action Expert는 [[Pi0]] 계열 [[VLA]] 모델에서 실제 로봇 행동을 생성하는 구성 요소이다. Dual-system 아키텍처에서 high-frequency System-1 모듈로 동작한다.

## The Problem

[[RoboSemanticBench]] 연구 결과:
- Action Expert는 block grasp primitive를 성공적으로 학습함
- 하지만 target selection 시 semantic information을 활용하지 못함
- "잡기는 하지만 무엇을 잡아야 하는지 모른다"

## Semantic Expert와의 Integration Failure

Action Expert가 [[SemanticExpert]]의 semantic decision을 제대로 통합하지 못하는 이유:
1. Imitation learning loss는 trajectory distribution 매칭에 집중
2. Semantic decision → action mapping을 명시적으로 학습하지 않음
3. Visual/position shortcut으로 대체 가능

## Implications

单纯的 모터 제어 개선이 아닌, semantic information의 action pathway 통합이 필요하다.

## Related Concepts

- [[SemanticExpert]] — paired concept
- [[SemanticGrounding]] — integration target
- [[VLA]] — 전체 시스템
- [[ActionPrediction]] — action expert의 출력
