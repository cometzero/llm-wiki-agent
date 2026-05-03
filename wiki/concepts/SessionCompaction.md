---
title: "SessionCompaction"
type: concept
tags:
  - agentic-workflow
  - llm-ops
  - context-management
sources:
  - vibe-coding-in-prod
last_updated: 2026-05-03
---

## 개요
[[SessionCompaction]]은 장시간 AI 협업 세션에서 누적된 맥락을 압축해 토큰/인지 비용을 줄이고, 작업 연속성과 재개 효율을 유지하는 운영 기술이다.

## 목적
- 세션이 과열되거나 휴식 시점에 컨텍스트 관리 비용을 줄인다.
- 장시간 협업에서 일관성 손실 없이 진행 상태를 문서화해 이어받을 수 있게 한다.
- [[ClaudeCode]] 같은 도구를 장시간 사용할 때 생산성 저하를 예방한다.

## 방식
- 맥락 요약: 변경 계획, 영향도, 다음 액션을 문서로 정리한다.
- 경계 구분: 고위험 도메인은 사람이 인수 인계한 뒤 compaction 한다.
- 재개 절차: 요약 기반으로 세션을 다시 확장한다.

## 연결
- [[ExponentialAIProgress]], [[VibeCoding]], [[ClaudeCode]], [[AIPM]], [[Verifiability]]
