---
title: "AI Product Management (AIPM)"
type: concept
tags:
  - AI 운영
  - 소프트웨어 거버넌스
  - 요구사항 엔지니어링
  - 협업 설계
last_updated: 2026-05-03
---

## Summary
[[AIPM]]는 AI를 작업자(코드 작성자)로 활용할 때 사람의 역할을 "관리자/PM"로 재정의한 운영 개념이다. 작업지시를 넘어서 목표, 제약, 품질기준, 범위, 우선순위를 제공해 AI 결과의 생산성을 높인다.

## Core Definition
- AI에게 단일 요청만 전달하는 방식 대신, 맥락 맵, 변경 범위, 검증 기준을 함께 제시한다.
- 사람은 작업 산출물의 형식/검증 포인트/릴리즈 기준을 설계한다.
- 결과의 품질은 구현 상세 읽기보다 시스템이 기대 동작을 수행하는지 판단하는 검증 체인으로 판단한다.

## Operational Pattern
- 요구사항 정제 후 한 번에 제출하는 세션형 프롬프트.
- 변경 대상 파일/모듈 경계 설정.
- 코드 변경 후 즉시 테스트·스트레스 테스트·리스크 구간 체크포인트 검증.

## Connections
- [[VibeCoding]]
- [[Verifiability]]
- [[LeafNode]]
- [[TestDrivenDevelopment]]
- [[Claude]]
- [[Anthropic]]

## Notes
- 본 위키에서는 [[AIPM]]을 [[AI의PM]]의 동의어로도 사용한다.