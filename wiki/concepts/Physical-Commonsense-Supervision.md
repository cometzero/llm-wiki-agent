---
title: "Physical Commonsense Supervision"
type: concept
tags: [physical-commonsense, supervision, robotics, egocentric-video]
sources: [physbrain-1-0-2605-15298-references]
last_updated: 2026-05-20
---

## Overview
Human egocentric video에서 추출한 물리적 상식(중력, 객체 상호작용, 힘의 방향 등)에 대한 감독 신호. [[VLA]] 정책 학습에서 단순 trajectory imitation을 넘어, 물리적 근본 원리를 사전 학습하여 out-of-domain generalization을 향상시키는 접근법.

## Key Characteristics
- Human video에서 물리적 상식 정보 추출
- [[Ego4D]], [[EPIC-KITCHENS]] 등의 데이터 활용
- 단순 행동 모방이 아닌 물리적 이해 기반 학습
- [[VGGT]] depth 추정과 결합하여 3D 물리 정보 보강 가능

## Connection to PhysBrain 1.0
- [[physbrain-1-0-2605-15298]]은 egocentric video를 generic caption이 아닌 structured physical meta-information으로 변환
- Depth/spatial/action execution QA로 재주석하여 supervision 품질 향상

## Connections
- [[physbrain-1-0-2605-15298]] — physical commonsense supervision의 주요 응용 연구
- [[Ego4D]], [[EgoDex]], [[EPIC-KITCHENS]] — supervision 추출용 비디오 소스
- [[VGGT]] — depth-aware augmentation 지원