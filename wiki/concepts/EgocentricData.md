---
title: "Egocentric Data"
type: concept
tags: [vision, robotics, dataset, first-person]
sources: [mobileego-anywhere-2605-05945, humannet-2605-06747]
last_updated: 2026-05-20
---

## Definition
First-person view(1인칭 시점)에서 촬영된 영상 및 센서 데이터. 머리 착용 카메라로 촬영하며, 사용자의 손과 작업 공간을 포함하는 것이 특징.

## Key Characteristics
- **시점**: Head-mounted camera로 촬영하는 1인칭
- **콘텐츠**: 인간의 손 작업, object manipulation, household activity
- **어플리케이션**: [[VLA]] policy learning, robotics manipulation, human activity recognition

## Related Datasets
- [[mobileego-anywhere-2605-05945]] — 200시간, commodity smartphone 기반
- [[HumanNet]] — 100만 시간 규모
- [[Ego4D]] — 초기 대규모 egocentric dataset, action recognition 중심
- [[EPIC-KITCHENS]] — 주방 activity 중심 egocentric dataset

## VLA Connection
VLA pretraining에는 long-horizon human interaction trajectory가 필요하며, egocentric video는 robot demonstration data의 비용 효율적 대체재로 활용 가능.
