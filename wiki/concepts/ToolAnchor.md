---
title: "ToolAnchor"
type: concept
tags: [agentic-tools, context-anchoring, counterfactuals]
last_updated: 2026-08-12
source: [deft-rlvr-2608-01755-references]
---

## Summary
[[ToolAnchor]]는 tool 사용 시 counterfactual/context anchor를 결합해 에이전트가 shortcut으로 특정 경로를 반복하지 않도록 유도하는 연구 축이다.

## Key idea
- 컨텍스트 앵커는 반대로 모델을 shortcut으로 이끄는 경향을 키울 수도 있어, DEFT 계열의 후보 노출 조절과 비교 실험에 유용하다.
- AD 추론에서 tool-like trace와 scene decision이 상호작용할 때 context-anchoring의 방향성은 중요한 편향 요인이다.

## Connections
- [[DEFT]]
- [[DEFT-RLVR]]
- [[TrajectoryAnchoringBias]]

## Key Claims
- 앵커링은 성능 향상을 가져올 수 있으나, 경우에 따라 overfitting shortcut을 강화할 수 있다.

## Contradictions
- 없음.
