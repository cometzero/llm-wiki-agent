---
title: "Software 3.0"
type: concept
tags: [software-paradigm, AI, prompting, systems-design]
sources: [andrej-karpathy-from-vibe-coding-to-agentic-engineering]
last_updated: 2026-05-10
---

## Definition

[[Software 3.0]]은 소프트웨어를 작성하는 방식이 코드 작성(명시적 규칙)에서 학습 가중치 및 자동 추론(데이터 기반)으로, 다시 [[Prompting]] 중심 제어로 이동한 단계를 가리킨다.

## Three-Stage View

- **Software 1.0**: 개발자가 직접 규칙(코드)으로 동작을 명세.
- **Software 2.0**: 데이터셋/학습으로 모델 가중치를 통해 동작을 학습.
- **Software 3.0**: [[LLM]]을 컨텍스트 해석기(인터프리터)로 활용해 텍스트, 이미지, 에이전트 실행 지시로 문제를 해결.

## Practical Effects

- 문제 해결의 시작점이 "코드를 어떻게 짜는가"가 아니라 "에이전트에 무엇을 복사/붙여넣기하고 어떤 제약으로 실행할지"로 바뀐다.
- 배포/운영은 구현보다도 제약 정의와 검증 루프의 품질이 성패를 가른다.

## Related Concepts

- [[Prompting]]
- [[AgenticEngineering]]
- [[Verifiability]]
- [[AI에이전트]]
- [[LLM]]
- [[AIAutomation]]