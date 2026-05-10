---
title: "Agentic Engineering"
type: concept
tags: [AI-engineering, automation, software-development, verification]
sources: [andrej-karpathy-from-vibe-coding-to-agentic-engineering]
last_updated: 2026-05-10
---

## Definition

[[AgenticEngineering]]은 [[LLM]] 기반 [[AI에이전트]]를 단순 코드 생성기처럼 쓰지 않고, 명확한 목표·제약·검증 규칙 아래에서 운영하는 소프트웨어 엔지니어링 방식이다.

## Core Principles

- **목표 중심 설계**: 사람은 What/Why/Constraints를 정의하고, 에이전트는 How를 반복 실행한다.
- **검증 중심 반복**: [[Verifiability]]가 높은 작업을 우선 자동화하고, 모호한 작업은 재검토 루프로 돌린다.
- **인간 감독 유지**: [[AI 시대의 인간 가치]]의 핵심(판단, 이해, 미학, 책임)을 유지한다.
- **실패 분해**: [[DistributionShift]], [[JaggedIntelligence]] 같은 비정상 응답 구간을 전처리 규칙으로 차단한다.

## Why It Matters

기존의 [[VibeCoding]]이 진입 장벽을 낮추는 데 강점을 보이는 반면, [[AgenticEngineering]]은 품질과 일관성, 팀 운영에서의 추적 가능성까지 확보하는 데 초점을 둔다.

## Related Concepts

- [[LLMAgents]]
- [[VibeCoding]]
- [[Verifiability]]
- [[ClosedLoopEvaluation]]
- [[Software 3.0]]
- [[Prompting]]
- [[AI 시대의 인간 가치]]