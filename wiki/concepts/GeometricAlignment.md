---
title: "GeometricAlignment"
type: concept
tags: [robotics, geometry, perception, embodiment, world-model]
sources: ["data-pyramid-for-embodied-manipulation-2607-24744", "data-pyramid-for-embodied-manipulation"]
last_updated: 2026-07-29
---

## Definition

**GeometricAlignment**는 관측된 장면·자세·좌표계 정보가 정책의 action prediction 및 rollout dynamics와 일관되게 일치하는 정도다. 즉, 같은 장면을 로봇이 서로 다른 embodiment에서 읽었을 때 추론되는 공간관계가 일치해야 함을 뜻한다.

## Why it matters

- semantic prior가 강해도 coordinate drift가 존재하면 행동 궤적이 실패로 이어질 수 있다.
- [[WorldActionModel]]/state transition 기반 supervision은 geometric 정합을 통해 행동의 물리적 실현 가능성을 높인다.
- [[Ego4D]], [[EPIC-KITCHENS]] 같은 egocentric prior를 action-centric 모델에 합칠 때 특히 중요함.

## Relations

- Influences [[ActionSpaceAlignment]]
- Supports robust [[VisionLanguageAction]] closed-loop transfer
- Complements [[Simulation]]-based counterfactual testing

## Open issues

- monocular 비디오 기반 prior의 depth ambiguity
- contact dynamics 미반영으로 인한 기하 오차 축적
- tactile/force feedback이 없어 미끄러짐/마찰 특성 반영이 약함
