---
title: "Egocentric Video"
type: concept
tags: [egocentric-video, computer-vision, robotics, data-collection]
sources: [physbrain-1-0-2605-15298-references]
last_updated: 2026-05-20
---

## Overview
첫인칭 시점(Head-mounted camera)으로 촬영된 비디오로, 인간이 일상에서 경험하는 물리적 상호작용을 직접적으로 캡처한다. [[VLA]] 정책 학습에서 robot trajectory 데이터의 비용 효율적 대안으로 주목받으며, [[physbrain-1-0-2605-15298]]에서는 이를 physical commonsense supervision 추출의 원천으로 활용한다.

## Key Datasets
- [[Ego4D]] — CVPR 2022, 대규모 egocentric video dataset
- [[EPIC-KITCHENS]] — Egocentric kitchen activity video
- [[EgoDex]] — Egocentric dexterous manipulation

## Key Characteristics
- 인간의 자연스러운 행동 패턴 캡처
- Robot data보다 수집 비용이 저렴하고 규모의 확장성이 높음
- [[mobileego-anywhere-2605-05945]] 프로젝트처럼 commodity hardware로 대규모 수집 가능

## Applications
- [[VLA]] policy의 pretraining 데이터
- [[Physical-Commonsense-Supervision]] 추출
- [[EgoDex]] 같은 dexterous manipulation 학습

## Connections
- [[physbrain-1-0-2605-15298]] — egocentric video를 physical supervision으로 변환
- [[Ego4D]], [[EPIC-KITCHENS]], [[EgoDex]] — 주요 egocentric video 데이터셋
- [[mobileego-anywhere-2605-05945]] — commodity hardware 기반 egocentric 데이터 수집 인프라
- [[HumanNet]] — 100만 시간 규모의 human-centric video corpus