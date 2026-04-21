---
title: "Model Speciation"
type: concept
tags: [model-design, efficiency, llm]
last_updated: 2026-04-21
sources: [andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai]
---

## Definition
[[Speciation]]은 단일 범용 모델로 모든 작업을 처리하려는 접근 대신, 작업별로 특화된 모델군을 운영해 성능/지연/비용 효율을 맞추려는 전략이다.

## Motivation
- 검증 가능한 작업에서 성능이 좋더라도 주관적/맥락적 작업에서는 일관성 부족 가능.
- 리소스 제한 환경에서 경량 특화 모델이 효율적일 수 있음.

## In This Source
- [[AndrejKarpathy]]는 동물 뇌의 기능 분화 유비로 모델 분화를 제시하고, 미세조정 능력의 미성숙을 이유로 연구가 초기 단계임을 지적한다.

## Related
- [[LLMAgents]]
- [[AutoResearch]]
- [[ClaudeOpus46]]
