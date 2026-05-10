---
title: "Task/Phase Workflow"
type: concept
tags: [workflow-design, AI-agent, task-decomposition]
last_updated: 2026-05-10
sources:
  - 99-가-모르는-하네스-엔지니어링-ai-에이전트-생산성을-10배-올리는-세팅법-바이브마피아-최수민님
---

## 정의

[[TaskPhase]]는 AI 워크플로우에서 하나의 큰 작업을 독립 실행 가능한 여러 단위로 나눈 구조를 뜻한다. 본문에서는 보통 하나의 태스크가 10개 안팎의 페이즈로 분해된다고 설명한다.

## 핵심 구성

- **태스크(Task)**: 전체 목표(예: 기능 구현, 문서 업데이트, 테스트 정비)를 담는 상위 단위.
- **페이즈(Phase)**: 태스크 완료를 위한 하위 단계(요구사항 정합성, 구현, 테스트, 리뷰, 정리).
- **독립 실행성**: 각 페이즈는 하위 세션에서 직렬/병렬로 처리될 수 있어야 한다.
- **복구성**: 실패 시 rollback·재실행이 가능한 상태 정보를 유지한다.

## 기대 효과

- 메인 컨텍스트 오염을 억제하고,
- 작업 재현을 가능하게 하며,
- 자동화된 에이전트 간 협업에서 책임 구분을 선명하게 한다.

## 연관 개념

- [[HarnessEngineering]]
- [[AutonomousAgent]], [[SubAgent]], [[ContextWindow]], [[SessionCompaction]]

## 메모

이 개념은 [[Software engineering]]의 단계적 실행 원리를 AI 오케스트레이션에 맞춘 특수화 버전으로 볼 수 있다.