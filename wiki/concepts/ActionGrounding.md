---
title: "Action Grounding"
type: concept
tags: [vla, robot-learning, reasoning-to-action]
sources: [physbrain-1-0-2605-15298, physbrain-1-0-2605-15298-learning, physbrain-1-0-2605-15298-analysis]
last_updated: 2026-05-20
---

## Definition
Physical reasoning과 language reasoning을 executable robot action으로 연결하는 과정. [[VLA|Vision-Language-Action]] 모델의 핵심 기능.

## Challenge
- Vision-Language 모델은 rich semantic reasoning 가능
- Robot action은 specific, low-level, physically grounded해야 함
- 이 두 영역 사이의 gap을 메워야 함

## Connection to Physical Commonsense
[[PhysicalCommonsense]]는 action grounding의 기반이 된다:
- Object特性 → gripper configuration
- Depth/Reachability → approach trajectory
- Contact reasoning → manipulation strategy
- State change prediction → success detection

## Related Concepts
- [[VLA]] — action grounding을 수행하는 모델
- [[PhysicalCommonsense]] — grounding의 기반
- [[CapabilityPreservingAdaptation]] — grounding하면서도 VLM capability 유지
- [[LanguageSensitiveAdaptation]] — language instruction을 따른 action 생성
