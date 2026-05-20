---
title: "PhysBrain"
type: entity
tags: [VLA, embodied-ai, robotics, multimodal]
sources: [physbrain-1-0-2605-15298]
last_updated: 2026-05-20
---

## Overview
PhysBrain은 대규모 human egocentric video에서 [[PhysicalCommonsenseSupervision]]을 추출하여 [[VLA]]로 전이하는 연구 프레임워크다. [[ShijieLian]] 등이 주도하며 arXiv 2605.15298으로 발표되었다.

## Key Components
1. **PhysBrain Data Engine**: Human egocentric video를 structured physical meta-record로 변환
2. **Physically Grounded QA**: 물리적 정보를 자연어 QA supervision으로 렌더링
3. **PhysBrain Base VLM**: Physical commonsense를 학습한 multimodal 모델
4. **Capability-Preserving VLA Adaptation**: 기존 VLM capability를 보존하며 robot policy로 적응

## Related Entities
- [[VLA]] — Vision-Language-Action modeling paradigm
- [[PhysicalCommonsenseSupervision]] — 핵심 학습 방법론
- [[HumanNet]] — 관련 large-scale human video corpus
