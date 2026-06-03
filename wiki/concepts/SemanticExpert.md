---
title: "Semantic Expert"
type: concept
tags: [VLA, dual-system, semantics]
sources: [robosemanticbench-2606-02277-ko]
last_updated: 2026-06-03
---

## Definition

Semantic Expert는 [[Pi0]] 계열 [[VLA]] 모델에서 instruction과 observation을 해석하여 semantic decision을 생성하는 구성 요소이다. Dual-system 아키텍처에서 low-frequency System-2 모듈로 동작한다.

## Action Expert와의 관계

| Expert | Role | Frequency |
|--------|------|-----------|
| [[SemanticExpert]] | 해석, semantic decision 생성 | Low (System-2) |
| [[ActionExpert]] | 실제 행동 실행 | High (System-1) |

## The Gap Problem

[[RoboSemanticBench]] 연구에 따르면:
1. Imitation learning loss는 semantic decision을 action module에 안정적으로 전달하도록 강제하지 않음
2. Policy는 색상, 위치 등 shortcut으로 task success를 얻을 수 있음
3. 결과적으로 Semantic Expert의 출력이 Action Expert에 반영되지 않음

## Solution Direction

강력한 [[VLM]]을 action expert에 붙이는 것만으로는 충분하지 않으며, selected semantic target을 action module에 보존·노출하는 training objective/interface가 필요하다.

## Related Concepts

- [[SemanticGrounding]] — semantic expert의 핵심 기능
- [[Pi0]] — dual-system 아키텍처
- [[VLA]] — semantic/action expert 통합 체계
