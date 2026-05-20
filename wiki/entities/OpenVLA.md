---
title: "OpenVLA"
type: entity
tags: [vla, robot-policy, baseline]
sources: [physbrain-1-0-2605-15298-references]
last_updated: 2026-05-20
---

## Overview
VLM(Vision-Language Model)을 robot policy로 전이하는 대표적 baseline 모델. 단순 robot trajectory imitation를 넘어 [[PhysicalCommonsenseSupervision|physical commonsense pretraining]] 후 adaptation을 강조하는 [[physbrain-1-0-2605-15298]]의 주요 비교 대상.

## Key Characteristics
- VLM 기반 robot policy의 초기 성공적 시연
- Pretrained vision-language model의 zero-shot 또는 fine-tuned robotic control으로 확장
- [[VLA]](Vision-Language-Action) 패러다임의 대표 baseline

## Connections
- [[physbrain-1-0-2605-15298]] — 주요 비교 baseline; PhysBrain은 OpenVLA보다 superior physical commonsense 적용 효과 입증
- [[VLA]] — OpenVLA가 채택한 핵심 패러다임
- [[Pi0]] — 또 다른 VLA policy baseline; 상호 비교 가능
- [[GR00T-N1]] — NVIDIA의 대규모 robotics foundation model; 유사한 영역