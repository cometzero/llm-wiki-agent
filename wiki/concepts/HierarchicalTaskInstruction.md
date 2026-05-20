---
title: "Hierarchical Task Instruction"
type: concept
tags: [instruction-following, VLA, language, planning]
sources: [mobileego-anywhere-2605-05945-analysis, reflectdrive-2-2605-04647-analysis]
last_updated: 2026-05-20
---

## Definition
복잡한 과업을 상위 instruction → sub-goals → atomic actions으로 계층 구조화한 언어 태그 체계.

## Role in VLA Training
1. **Instruction following**: high-level goal language 이해
2. **Sub-goal planning**: 중간 목표 시퀀스 생성
3. **Long-horizon memory**: 긴 시퀀스에서 일관성 유지
4. **Action segmentation**: continuous video → discrete action spans 분리

## Connection to Other Concepts
- [[VLA]] — hierarchical supervision 신호 제공
- [[LongHorizonTrajectory]] — 계층 구조가 필요한 연속 동작
- [[InstructionTuning]] — hierarchical instruction 학습 방법론
- [[ReflectDrive2]] — driving에서의 hierarchical planning
