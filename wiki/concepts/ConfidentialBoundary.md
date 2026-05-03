---
title: "ConfidentialBoundary"
type: concept
tags:
  - security
  - governance
  - production-safety
sources:
  - vibe-coding-in-prod
last_updated: 2026-05-03
---

## 개요
[[ConfidentialBoundary]]는 AI 협업 환경에서 기밀 영역(인증, 결제, 권한, 민감 데이터 등)을 분리하여 사고 확산을 막는 운영 경계다.

## 핵심 통제
- 고위험 정보는 AI 작업 프롬프트 범위를 제한한다.
- 작업자/도구 접근권한을 분리하고, 로그와 승인 경로를 명시한다.
- AI가 처리 가능한 범위와 사람이 직접 승인해야 할 범위를 사전에 선언한다.

## 실무 적용
- [[VibeCoding]]에서 고위험 기능에 바로 AI를 투입하기보다 [[LeafNode]] 우선 변경과 [[AIPM]] 기반 정보 최소화로 통제해야 한다.
- 정적 규칙만으로 충분하지 않으며, 변경 후 [[TestDrivenDevelopment]] 검증과 운영 모니터링이 병행되어야 한다.

## 연결
- [[VibeCoding]], [[Verifiability]], [[TestDrivenDevelopment]], [[AIPM]], [[ExponentialAIProgress]]
