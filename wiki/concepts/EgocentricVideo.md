---
title: "Egocentric Video (자가 중심 비디오)"
type: concept
tags: [video, robotics, human-activity]
sources: [physbrain-1-0-2605-15298-analysis, humannet-2605-06747-analysis, mobileego-anywhere-2605-05945-analysis]
last_updated: 2026-05-20
---

## Overview
Egocentric video(자가 중심 비디오)는 착용자가 보는視点で 촬영된 비디오로, [[Ego4D]], EPIC-KITCHENS 등의 대규모 데이터셋으로 공개되어 있다. 인간이 물체를 조작하고 환경을 탐색하는 자연스러운 행동 데이터를 포함하여, robot learning의 supervision source로 활용된다.

## Characteristics
- **First-person perspective**: 착용자의 시점에서 촬영
- **Action-rich**: 물체 조작, 이동, 탐색 등의 자연스러운 행동 포함
- **Scale advantages**: 수집 비용이 robot trajectory보다 저렴
- **Physical prior extraction**: scene elements, spatial dynamics, action execution 추출 가능

## Applications in Robot Learning
- [[physbrain-1-0-2605-15298]] — physical QA supervision 추출
- [[HumanNet]] — VLA pretraining corpus
- [[mobileego-anywhere-2605-05945]] — smartphone 기반 데이터 수집 인프라

## Related Datasets
- [[Ego4D]]
- EPIC-KITCHENS
- EgoDex, BuildAI
- SEA-Small, FineVision
