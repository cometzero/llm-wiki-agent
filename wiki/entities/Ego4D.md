---
title: "Ego4D"
type: entity
tags: [egocentric-video, dataset, embodied-ai]
sources: [humannet-2605-06747-references, humannet-2605-06747, humannet-2605-06747-analysis]
last_updated: 2026-05-13
---

## Overview
Ego4D는 제1인칭 시점(egocentric) 비디오 데이터셋의 대표 주자로, narration, forecasting, hand-object interaction 학습에 유용한 대규모 코퍼스를 제공한다. [[HumanNet]]은 Ego4D와 같은 egocentric video corpus의 가치를 확인하며 인간 중심 비디오 학습의 기반 데이터로 활용한다.

## Key Characteristics
- **Data Type**: First-person egocentric video
- **Tasks Covered**: Narration, action forecasting, hand-object interaction
- **Scale**: 수천 시간 이상의 제1인칭 비디오
- **Role in HumanNet**: 인간 중심 비디오 학습의 대표 corpus로서 [[VLA]] pretraining 데이터 소스로 활용 가능성을 입증

## Connections
- [[EPIC-KITCHENS]] — kitchen 도메인의 egocentric activity dataset
- [[Ego-Exo4D]] — first-person과 third-person paired view를 제공하는 관련 데이터셋
- [[HOI4D]] — hand-object geometry와 dense supervision을 강조하는 데이터셋
- [[HumanNet]] — Ego4D를 인간 중심 비디오 학습 데이터로 활용
- [[R3M]] — passive human video representation의 로봇 전이 연구와 연결

## References
- https://ego4d-data.org/
