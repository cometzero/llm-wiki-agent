---
title: "Autorubric"
type: concept
tags: [rubric, evaluation, llm-assessment]
last_updated: 2026-08-12
source: [deft-rlvr-2608-01755-references]
---

## Summary
[[Autorubric]]는 비검증 가능한 과제에서의 LLM 응답을 rubric 기반으로 다층적으로 평가하려는 구조적 framework다.

## Key idea
- 단순 정답/정답률이 아니라 근거, 규칙 정합, 품질 축을 분리해 정량화한다.
- DEFT-RLVR류는 scene/risk/rule 기반 rubric을 RLVR과 결합해 decision alignment를 강화한다.

## Connections
- RubricBasedEvaluation
- [[DEFT-RLVR]]
- [[RLVR]]
- [[Verifiability]]

## Key Claims
- 긴 텍스트 생성 자체보다 rubric에서 높은 정합 점수를 얻는 reasoning trace가 실제 행동 선택 정합과 더 잘 맞는다.

## Contradictions
- 없음.
