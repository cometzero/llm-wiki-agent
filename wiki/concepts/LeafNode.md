---
title: "LeafNode"
type: concept
tags: [architecture, engineering]
sources: [vibe-coding-in-prod]
last_updated: 2026-04-19
---

## Definition
[[LeafNode]]는 의존성이 적거나 하위 단위 기능으로, 변경이 다른 핵심 경로에 즉시 확산되지 않는 코드 지점이다. 해당 소스에서는 AI 코딩 적용 시 기술 부채를 통제하기 위한 우선 변경 단위로 제안된다.

## Why it matters
- 핵심 아키텍처를 건드리지 않고도 기능 개선을 진행할 수 있어 배포 리스크가 낮다.
- 변경 영향도를 낮춰 생산성/속도와 안정성을 동시에 확보할 수 있다.
- 리프 노드 중심 전략은 [[VibeCoding]] 운영에서 “빠른 적용 + 통제 가능한 책임 범위”를 만들 수 있게 한다.

## Connections
- [[VibeCoding]] — 핵심 적용 단위 전략.
- [[TestDrivenDevelopment]] — 리프 노드의 동작 보증을 위한 테스트 설계.
- [[FunctionalSafety]] — 핵심 안전 경로를 분리해 변경 위험을 낮추는 사고 실무와 정합성 있음.
