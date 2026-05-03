---
title: "Leaf Node"
type: concept
tags:
  - 코드베이스 구조
  - 리스크 관리
  - 변경 통제
last_updated: 2026-05-03
---

## Summary
[[LeafNode]]는 코드베이스에서 더 이상 다른 모듈에 의존하지 않거나 의존 영향이 낮은 종단 지점 기능 단위를 말한다. 프로덕션 AI 협업에서 변경을 [[LeafNode]]로 한정하면 핵심 아키텍처로의 피해 확산을 줄일 수 있다.

## Core Principle
- 핵심 브랜치/아키텍처는 사람이 깊이 이해하고 보호한다.
- AI는 리프 노드에서 반복작업, 인터페이스 정합성, 보조 기능 수정 중심으로 투입한다.
- 기술 부채가 누적되어도 비핵심 영역에서 한정되면 운영 리스크를 낮출 수 있다.

## Why It Matters
- 전면 리뷰가 어려운 대규모 AI 생산 환경에서 변경 범위를 제한하는 실무적 방어선이 된다.

## Connections
- [[VibeCoding]]
- [[Verifiability]]
- [[AIPM]]
- [[TestDrivenDevelopment]]
- [[SecurityBoundary]]

## Caveat
- 리프 노드 판별 기준이 부정확하면 오히려 핵심 로직이 누락될 수 있으므로 사전 영향분석이 필요하다.