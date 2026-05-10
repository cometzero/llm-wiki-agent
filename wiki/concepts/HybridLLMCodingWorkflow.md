---
title: "Hybrid LLM Coding Workflow"
type: concept
tags: [AI에이전트, 코딩, 멀티모델, 자동화]
last_updated: 2026-05-10
sources: [the-coding-assistant-breakdown-more-tokens-please]
---

## Definition

[[Hybrid LLM Coding Workflow]]는 코딩 과제를 단일 모델로 처리하지 않고, 작업 유형별로 적합한 모델을 분기해 쓰는 운영 패턴이다.

## Typical Pattern

- 초기 탐색/요구 정렬/스캐폴딩: 사용자 의도 추론이 강한 모델 선호(예: [[Claude Opus 4.7]], [[ClaudeCode]]).
- 구조적 분석/긴 추론이 필요한 본 구현, 테스트 보정, 정밀 수정: 추론 강한 모델 선호(예: [[GPT-5.5]], [[Codex]]).
- 회귀·리뷰·배포 단계: 하네스 검증, 문서화, [[ToolUse]] 정책을 갖춘 엔지니어링 규칙 적용.

## Operational Benefit

- 모델 편향(빠른 생성 vs 과도한 보수성)을 상쇄.
- 토큰 비용·지연·품질의 균형을 조정하기 쉬움.
- [[TokenEconomy]]에서 실제 워크로드당 비용을 낮추면서 품질 리스크를 제한.

## Failure Modes

- 모델 간 handoff 기준이 없으면 일관성 붕괴.
- 자동 라우팅이 너무 공격적이면 컨텍스트 누수, 비용 급등, 리젝션 루프 발생.
- 버그 검증이 약화되면 "정답률"과 상관없는 신뢰도 위험 발생.

## Example in this Source

해당 소스는 "새 애플리케이션/POC는 [[Claude]] 계열로 시작, 실제 문제 해결과 버그 수정은 [[Codex]]로 전환" 같은 단계 분리를 제안한다.

## Related Links

- [[ClaudeCode]]
- [[Codex]]
- [[GPT-5.5]]
- [[CodingLLMBenchmarks]]
- [[HarnessEngineering]]
- [[ToolUse]]