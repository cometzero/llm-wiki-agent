---
title: "Prompting"
type: concept
tags: [LLM, interaction-design, software-interfaces]
sources: [andrej-karpathy-from-vibe-coding-to-agentic-engineering]
last_updated: 2026-05-10
---

## Definition

[[Prompting]]은 [[LLM]]의 컨텍스트 윈도우를 제어해 의도, 제약, 기대 출력, 검증 기준을 전달하는 행위이며, [[Software 3.0]]에서 핵심 인터페이스로 간주된다.

## Operational Meaning

- 단순 질문이 아니라 `실행 의도 + 환경 조건 + 검증 조건`을 함께 담는 명세 형태가 된다.
- 잘못된 [[Prompting]]은 오히려 비효율·오류·보안/품질 리스크로 이어질 수 있다.
- 좋은 [[Prompting]]은 [[AI에이전트]] 자동화의 정확도를 높이고, [[Verifiability]] 작업을 쉽게 만든다.

## Related Concepts

- [[Software 3.0]]
- [[LLM]]
- [[AgenticEngineering]]
- [[Verifiability]]
- [[HumanIntelligenceSystem]]