---
title: "Context Rot: How Increasing Input Tokens Impacts LLM Performance"
type: source
tags: ["ai", "research", "long-context"]
date: 2026-04-16
source_file: "raw/AI/Context Rot_ How Increasing Input Tokens Impacts LLM Performance _ Chroma Research.md"
---

## Summary
Chroma Research의 문맥 길이 연구를 정리한 문서로, 입력 토큰 수가 늘어날수록 성능이 균일하게 유지되지 않고 비선형적으로 저하되는 현상을 Context Rot로 설명한다. 단순 NIAH 테스트를 넘어 방해 요소, 유사성, 구조 변화가 긴 컨텍스트 활용 능력에 얼마나 큰 영향을 주는지 보여준다.

## Key Claims
- 긴 컨텍스트 벤치마크의 고득점은 실제 긴 문서 작업 성능을 충분히 보장하지 않는다.
- 입력 길이만 늘려도 모델 성능은 일관성 없이 저하될 수 있으며 이를 [[ContextRot]]로 볼 수 있다.
- 실무형 평가에서는 검색뿐 아니라 구조화, 추론, 방해 요소 내성이 함께 중요하다.

## Key Quotes
> 입력 길이만을 변화시켜, 입력 길이의 영향만을 직접 측정한다.

## Connections
- [[ContextRot]] — 이 자료가 정의하고 검증하는 핵심 현상
- [[LongContext]] — 긴 입력 처리 능력 평가와 직결
- [[Chroma]] — 연구를 발표한 조직
- [[LLMAgents]] — 긴 컨텍스트 의존형 에이전트 설계 시 주의점 제공

## Contradictions
- No direct contradiction identified in this first ingest pass.
