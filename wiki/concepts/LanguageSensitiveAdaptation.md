---
title: "Language-Sensitive Adaptation"
type: concept
tags: [vla, language-instruction, adaptation]
sources: [physbrain-1-0-2605-15298, physbrain-1-0-2605-15298-learning]
last_updated: 2026-05-20
---

## Definition
Policy가 language instruction을 무시하지 않도록 유지하는 [[VLA]] adaptation 기법.

## Problem
VLA 학습 시 visual shortcut이나 other biases로 인해 language instruction이 무시될 수 있다.

## Verification Method
**Language ablation**: language를 제거해도 성능이 비슷하다면 policy가 visual shortcut에 빠진 것. Language가 실제 영향력을 가지는지 검증하는 핵심 테스트.

## Related Concepts
- [[CapabilityPreservingAdaptation]] — broader capability 보존과의 연관
- [[VLA]] — adaptation 타겟
- [[ActionGrounding]] — language instruction을 action으로 변환
