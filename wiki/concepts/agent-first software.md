---
title: "agent-first software"
type: concept
tags: [software-architecture, llm]
last_updated: 2026-04-21
sources: [andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai]
---

## Definition
[[agent-first software]]는 인간이 직접 조작하는 UI 중심 설계가 아니라, 에이전트가 API를 호출하고 조율하도록 설계된 소프트웨어 아키텍처를 의미한다.

## Properties
- 개별 앱 통합 대신 API/서비스 계층으로의 이동
- 사용자에게는 간단한 인터페이스, 에이전트에게는 깊은 상태·메모리·도구 노출
- 장기적으론 에이전트 간 협업 및 지속성에 맞춘 제어면 강화

## In This Source
- [[DobbyTheElfClaw]] 사례가 앱 다중화 문제를 API 기반 하나의 제어면으로 대체할 수 있음을 보여줌.
- [[OpenClaw]] 같은 지속형 클로가 이 방향의 실행 플랫폼이 될 수 있음을 시사.

## Risks
- 주관적 판단이 필요한 업무에서 과신 통제가 필요.
- 지표만으로 평가되지 않는 도메인에서 실패 사례가 누적될 수 있음.
