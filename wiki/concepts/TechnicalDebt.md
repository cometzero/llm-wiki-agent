---
title: "Technical Debt"
type: concept
tags:
  - software-quality
  - architecture
  - maintenance
sources:
  - vibe-coding-in-prod
last_updated: 2026-05-03
---

## 정의
[[TechnicalDebt]]는 단기 속도 확보를 위해 도입된 구현 방식이 장기 유지보수 비용으로 전환되는 상태를 뜻한다. [[VibeCoding]] 맥락에서 과잉 신속 구현이 리스크를 누적시킬 수 있으므로, 영향 범위를 제한해 관리한다.

## VibeCoding과의 관계
- 핵심 아키텍처보다 [[LeafNode]]에서의 변경은 누적 부채를 격리해 통제 가능성을 높인다.
- 핵심 경로에서의 부채는 즉시 가시화되어야 하며, 테스트 미비 상태에서 확산되면 치명적인 추적 비용이 발생한다.

## 운영 원칙
- 부채 허용 범위를 사전 합의한다.
- 변경 전후의 계약(입출력/오류 경계/성능 경계)을 기록한다.
- 정기적으로 [[Refactor|리팩토링]] 또는 아키텍처 정비 게이트를 둔다.

## 관련 링크
- [[VibeCoding]]
- [[LeafNode]]
- [[TestDrivenDevelopment]]
- [[AIPM]]

## Contradictions
- 기존 [[일반적 소프트웨어 유지관리]] 논의와 상반되지 않으며, 운영 위험 통제 관점에서 보완적이다.