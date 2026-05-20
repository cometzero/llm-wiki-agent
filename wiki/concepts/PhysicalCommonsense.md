---
title: "Physical Commonsense"
type: concept
tags: [physical-reasoning, robot-learning, vla]
sources: [physbrain-1-0-2605-15298, physbrain-1-0-2605-15298-learning, physbrain-1-0-2605-15298-analysis]
last_updated: 2026-05-20
---

## Definition
Object, depth, contact, reachability, state change에 관한 상식적 물리 이해. [[VLA|Vision-Language-Action]] 모델이 물리적으로 타당한 행동을 계획하기 위해 필요한 핵심 prior.

## Key Properties
- **Object understanding**: 물체의 특성, 질감, 크기에 대한 이해
- **Depth awareness**: 공간 내 거리와 깊이 순서 인식
- **Contact reasoning**: 물체 간 물리적 접촉과 힘의 상호작용
- **Reachability**: 특정 위치/물체에 도달 가능성 판단
- **State change**: 행동에 따른 환경 상태 변화 예측

## Role in VLA Training
[[physbrain-1-0-2605-15298]]은 human egocentric video에서 이러한 [[PhysicalCommonsense]]를 추출하여 [[PhysicalQA]] 형태로 [[VLA]]에 supervision으로 제공한다. Raw video나 caption만으로는 이러한 physical reasoning을 충분히 학습시키기 어렵다.

## Related Concepts
- [[PhysicalQA]] — Physical commonsense를 학습하기 위한 Q&A 형식
- [[CapabilityPreservingAdaptation]] — Physical commonsense prior를 유지하면서 VLA로 전이
- [[ActionGrounding]] — Physical reasoning을 executable robot action으로 연결
