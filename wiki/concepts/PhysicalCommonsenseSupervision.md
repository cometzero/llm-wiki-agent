---
title: "Physical Commonsense Supervision"
type: concept
tags: [VLA, embodied-ai, multimodal, supervision]
sources: [physbrain-1-0-2605-15298]
last_updated: 2026-05-20
---

## Overview
Physical Commonsense Supervision은 [[VLA]] 모델이 인간의 물리적 상식(contact, reachability, object state change, tool use, spatial constraint, multi-step task structure)을 이해하도록 학습시키는 방법론이다.

## Background
기존 VLA 학습은 robot trajectory 수집에 의존하지만, 이는 비용이 높고 platform-dependent하며 physical regularity 학습을 보장하지 않는다. [[physbrain-1-0-2605-15298]]은 이 한계를 극복하기 위해 human egocentric video를 supervision source로 활용한다.

## Key Properties
- **Physically explicit**: Object geometry, contact progression, relative distance, reachability 포함
- **Structured**: JSON-style meta-record로scene elements, spatial dynamics, action execution 분리
- **Language-aligned**: 자연어 QA format으로 VLM 학습 가능

## Implementation (PhysBrain)
```
Human egocentric video → Structured physical meta-record → Physically grounded QA → PhysBrain VLM
```

## Related Concepts
- [[VLA]] — 적용 대상 모델
- [[physbrain-1-0-2605-15298]] — 구현 연구
- [[CapabilityPreservingAdaptation]] — downstream transfer 방법
- [[HumanNet]] — 관련 large-scale video corpus
