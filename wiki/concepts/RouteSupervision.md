---
title: "Route Supervision"
type: concept
tags: [training, supervision, vla]
sources: [visualthink-vla-2605-30011-ko-analysis]
last_updated: 2026-06-03
---

## Overview
Route supervision은 VisualThink-VLA의 training에서 사용되는 기법으로, selective router가 올바른 evidence를 선택하도록 supervision을 제공하는 것이다. VisualEvidence-Agent와 VisualEvidence-Set을 통해 구현된다.

## Training Recipe Components
1. **FullSoft teacher distillation** — soft probability 전달
2. **Route supervision** — evidence 선택 guidance
3. **Counterfactual utility 기반 dynamic loss** — gradient 조절

## Inference Optimization
- Hard routing으로 비용 절감
- Training에서의 route supervision이 inference efficiency를 지원

## Related Concepts
- [[VisualThinkVLA]] — 적용 시스템
- [[VisualEvidenceAgent]] — 구현 에이전트
- [[CounterfactualUtility]] — 함께 사용되는 loss 기법
