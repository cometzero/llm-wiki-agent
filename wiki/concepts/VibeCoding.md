---
title: "VibeCoding"
type: concept
tags: [ai, engineering, workflow]
sources: [vibe-coding-in-prod]
last_updated: 2026-04-19
---

## Definition
[[VibeCoding]]은 AI를 활용해 코드를 생성하되, 개발자가 코드의 모든 세부를 이해하려 하기보다 제품 품질과 운영 결과로 책임을 완결하는 개발 방식이다. 단순 자동 생성이 아니라, AI 협업 체계(요구사항, 제약, 컨텍스트 전달)와 검증 체계를 포함한다.

## Core Principles
- 개발자는 `AI의 PM`이 되어 목표, 경계, 품질 기준을 제공한다.
- 코드베이스의 핵심 아키텍처는 사람이 보호하고, `[[LeafNode]]` 중심으로 변경을 집중한다.
- 코드 리뷰를 전면 대체하지 않고, [[TestDrivenDevelopment]] 또는 E2E 검증을 통해 신뢰 가능한 체크포인트를 만든다.
- 보안·운영 리스크가 큰 영역은 AI 코딩 적용 범위를 제한하고 감독 정책을 두어 운영한다.

## Operational Guidance
- 작업 초반에 목표/제약/입출력 규격을 한 번에 정리해 프롬프트 맥락을 강화한다.
- 스트레스 테스트, 핵심 경로 테스트, 에러 케이스를 선제 설계한다.
- 과도한 보수/개발자 과신 대신, 반복 가능한 검증 경로를 설계해 확장성 있는 협업 구조를 만든다.

## Connections
- [[LLMAgents]] — AI를 보조자 이상으로 운영하기 위한 패턴.
- [[TestDrivenDevelopment]] — 코드 신뢰성 보장을 위한 핵심 실행 메커니즘.
- [[LeafNode]] — 리스크 구간 분리에 사용되는 적용 단위.
- [[ClaudeCode]] — 실제 적용 사례에서 자주 동반되는 도구.

## Notes
- 본 개념은 [[AIAutomation]]의 단순 자동화 프레임과 달리, **검증 중심의 운영 시스템 설계**를 본질로 둔다.
