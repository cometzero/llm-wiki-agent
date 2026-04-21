---
title: "Model Speciation"
type: concept
tags: [model-design, specialization, llm-architecture]
last_updated: 2026-04-20
sources: [andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai]
---

## Definition
[[ModelSpeciation]]은 작업 유형별로 특화된 모델을 분화시켜, 단일 범용 모델의 들쭉날쭉한 성능 문제를 완화하고 비용·성능을 최적화하는 접근이다.

## Core Claim
단일 모델은 일부 영역에서 매우 강력해도 주관성/문맥해석 같은 영역에서 오차가 커질 수 있다. 특화 모델은 그 반대의 균형을 맞추고 운영 비용을 낮출 수 있다.

## Mechanism
- 도메인별 성능 기준 정립
- 특정 작업군에 맞는 미세 조정
- 지연/처리량/정확도 요구에 맞춘 모델 라우팅

## Risks
- 미성숙한 미세조정 기술로 인해 과도한 특화가 오히려 역효과를 낼 수 있음.
- 과도한 스플릿은 통합/운영 복잡도 증가로 이어질 수 있음.

## Connections
- [[AndrejKarpathy]] — 단일 모델 접근의 위험을 제시하고 특화 필요성을 강조.
- [[LLMAgents]] — 특화형 에이전트가 병렬 배치되기 위한 이론적 기반.
- [[AIpsychosis]] — 모델의 jaggedness를 설명하는 보완 개념.
- [[AutoResearch]] — 실험 루프에서 작업군별 모델 선택의 기반이 될 수 있음.

## Related Source
- [[andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai]]