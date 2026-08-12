---
title: "Structured Chain of Thought"
type: concept
tags: [reasoning, chain-of-thought, verifiability]
last_updated: 2026-08-12
source: [deft-rlvr-2608-01755-references]
---

## Summary
[[StructuredChainOfThought]]는 자유 텍스트 CoT 생성을 단순히 길이로 평가하지 않고, 장면 근거·규칙 정합·후보 선택 정합을 명시적으로 반영하도록 설계한 추론 형태다.

## Key idea
- Candidate가 먼저 공개되는 환경에서는 explanation이 정답에 맞춘 사후 합리화로 흐르기 쉬우므로, DEFT 계열은 candidate exposure를 지연해 reasoning의 독립성을 지키려 한다.
- AD/도메인 VLA에서는 텍스트의 유창성보다 decision-grounding의 일관성이 더 중요하다.

## Connections
- [[DEFT]]
- [[DEFT-RLVR]]
- [[AD-MCQ]]
- TrajecoryAnchoringBias
- RubricBasedEvaluation

## Key Claims
- 구조화된 reasoning은 텍스트 품질 자체보다 근거 정합성과 후보 일치도를 더 중요하게 본다.

## Contradictions
- 없음.
