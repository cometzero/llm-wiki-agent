---
title: "Egocentric Video Dataset"
type: concept
tags: [egocentric-vision, dataset, first-person]
sources: [mobileego-anywhere-2605-05945-references, humannet-2605-06747-references]
last_updated: 2026-05-20
---

## Overview
Egocentric Video Dataset은 1인칭 시점에서 촬영된 비디오를 기반으로 한 데이터셋으로, VLA(Vision-Language-Action) 모델의 pretraining에 핵심적인 역할을 한다.

## Related Datasets
- [[Ego4D]] — 대규모 egocentric video의 대표 데이터셋
- [[EPIC-KITCHENS]] — 주방 환경의 egocentric action recognition
- [[Ego-Exo4D]] — first-person/third-person paired skilled activity
- [[HOI4D]] — 4D human-object interaction
- [[HumanNet]] — 100만 시간 규모 인간 중심 비디오 코퍼스

## Key Characteristics
- 연속 6-DoF pose 추적 능력
- RGB-D 깊이 정보
- Long-horizon state tracking
- Hand trajectory 및 object interaction 주석

## Connections
- [[mobileego-anywhere-2605-05945]] — commodity smartphone 기반 장기 수집 인프라
- [[VLA]] — pretraining용 데이터 소스
- [[HandTracking]] — 핸드 트래킹 관련 기술
