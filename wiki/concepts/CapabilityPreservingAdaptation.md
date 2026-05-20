---
title: "Capability-Preserving Adaptation"
type: concept
tags: [vla, fine-tuning, transfer-learning]
sources: [physbrain-1-0-2605-15298, physbrain-1-0-2605-15298-learning, physbrain-1-0-2605-15298-analysis]
last_updated: 2026-05-20
---

## Definition
[[VLM]]의 일반 multimodal capability(텍스트 이해, 비전 reasoning 등)를 잃지 않도록 하는 [[VLA]] fine-tuning 기법.

## Challenge
VLA adaptation 과정에서 robot-specific action prediction에 최적화하면 VLM이 가지고 있던 일반적 능력이 저하될 수 있다(catastrophic forgetting).

## Solution in PhysBrain 1.0
1. **Retention data mixing**: 일반 multimodal 데이터와 robot trajectory 데이터를 섞어서 학습
2. **Language-sensitive adaptation**: policy가 language instruction을 무시하지 않도록 유지
3. **Language ablation testing**: language를 제거해도 성능이 비슷하다면 visual shortcut에 빠진 것

## Related Concepts
- [[PhysicalCommonsense]] — 보존해야 할 핵심 prior
- [[VLA]] — adaptation의 타겟 모델
- [[VLM]] — source model
- [[CatastrophicForgetting]] — 방지해야 하는 현상
