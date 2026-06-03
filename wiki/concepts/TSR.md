---
title: "TSR (Target Selection Rate)"
type: concept
tags: [metric, VLA, robotics, semantic-grounding]
sources: ["robosemanticbench-2606-02277-ko-analysis"]
last_updated: 2026-06-03
---

## Definition
RoboSemanticBench에서 제안된 메트릭으로, VLA 모델이 올바른 semantic target(의미적 목표)를 선택하는 비율을 측정한다. 물리적 grasp能力和无关하게 언어/상식 이해에 따른 행동 선택 능력을 평가한다.

## Connections
- [[RoboSemanticBench]] — 메트릭이 정의된 벤치마크
- [[GSR]] — 함께 사용되는另一位 메트릭
- [[nSG]] — 함께 사용되는另一位 메트릭
- [[VLA]] — 측정 대상 모델
- [[SemanticGrounding]] — 이 메트릭이 직접 측정하는 대상

## Notes
TSR은 모델이 "무엇을 집어야 하는지"를 올바르게 결정하는 능력을 측정하며, [[GSR]]과 결합하여 semantic grounding vs manipulation capability를 분리 분석할 수 있다.
