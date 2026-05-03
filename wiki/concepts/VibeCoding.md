---
title: "Vibe Coding"
type: concept
tags:
  - AI 개발
  - 프로덕션 운영
  - 협업 코딩
  - 검증
last_updated: 2026-05-03
---

## Summary
[[VibeCoding]]은 AI를 통한 코드 생성 단계에서 더 나아가, 사람이 코드 자체에 집착하지 않고 제품 품질과 운영 결과에 집중하는 개발 방식이다.

## Core Idea
- AI가 작성한 결과를 전수 검토하는 접근에서, 신뢰 가능한 제약 조건, 맥락, 범위를 설계한 뒤 결과를 검증 가능한 형태로 수용하는 접근으로 패러다임이 이동한다.
- 핵심 운영 원칙은 [[LeafNode]] 위주 변경, 핵심 아키텍처 보호, 테스트 기반 정합성 확보이다.

## Implementation Guidance
- AI를 단독 실행기가 아니라 [[AIPM]] 하에서 지시·피드백 루프의 객체로 다룬다.
- 생산성 극대화보다 신뢰 가능한 배포가 우선되어야 하며, [[Verifiability]]와 [[TestDrivenDevelopment]]가 핵심이다.
- 보안/안전 민감 영역은 AI 작업 범위를 제한하고, 변경 사전 승인 및 사후 점검을 강제한다.

## Claims
- 단기에는 코드 이해 부족이 문제처럼 보일 수 있으나, 장기적으로는 변경 검증 체계가 생산성을 더 크게 높인다.
- 기하급수적 AI 발전 환경에서 전면 인력 검토 방식은 지속 불가능하다.

## Connections
- [[AIPM]]
- [[LeafNode]]
- [[Verifiability]]
- [[TestDrivenDevelopment]]
- [[Claude]]
- [[Anthropic]]

## Risks
- 비전문가가 통제 없이 사용하는 경우 보안 결함이 누적될 수 있다.
- 기술 부채를 측정·모니터링하는 체계가 없으면 리스크가 은폐될 수 있다.