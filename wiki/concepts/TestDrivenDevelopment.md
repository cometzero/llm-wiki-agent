---
title: "TestDrivenDevelopment"
type: concept
tags: [quality, testing]
sources: [vibe-coding-in-prod]
last_updated: 2026-04-19
---

## Definition
[[TestDrivenDevelopment]](TDD)은 테스트를 먼저 정의하거나 실행 경로를 선행 설계해 구현 코드의 정확성을 검증하는 방식이다. 본 소스에서는 AI 생성 코드 신뢰성 확보를 위해 특히 유용한 운영 규칙으로 제시된다.

## Source-specific framing
- AI가 생성한 구현을 먼저 읽는 방식에서 벗어나, “테스트가 통과하면 신뢰를 가진다”는 방식으로 품질 판단의 기준을 전환한다.
- 테스트는 단순 단위 테스트를 넘어 성공 경로·에러 케이스·엔드투엔드 체크를 포함해야 한다.
- E2E 테스트 설계 시 핵리스하게 보이는 부분을 사람이 검증할 수 있는 입출력 지점으로 만든다.

## Connections
- [[VibeCoding]] — AI 기반 개발 신뢰성의 핵심 보완 축.
- [[ClaudeCode]] — 구현 생성 이후 테스트 우선 검증 루프의 대상 도구.
- [[LeafNode]] — 리스크가 낮은 단위에서 테스트 기반 증명을 쉬운 단위로 적용하기 적합함.
