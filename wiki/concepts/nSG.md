---
title: "nSG (normalized Success of Grasp)"
type: concept
tags: [metric, VLA, robotics, semantic-grounding]
sources: ["robosemanticbench-2606-02277-ko-analysis"]
last_updated: 2026-06-03
---

## Definition
RoboSemanticBench에서 제안된 메트릭으로, [[TSR]]과 [[GSR]]을 결합하여 semantic target selection 후 grasp가 성공하는 비율을 정규화하여 측정한다. Semantic reasoning이 실제 행동으로 올바르게 이어지는지 종단간 평가한다.

## Connections
- [[RoboSemanticBench]] — 메트릭이 정의된 벤치마크
- [[GSR]] — 구성 요소 메트릭
- [[TSR]] — 구성 요소 메트릭
- [[VLA]] — 측정 대상 모델
- [[SemanticGrounding]] — 측정 대상 능력

## Notes
nSG는 "올바른 대상을 선택하고 그 대상을 성공적으로 집는" 전체 파이프라인의 성공률을 측정하여, semantic-to-action 연결의 종단간 효과를 평가한다.
