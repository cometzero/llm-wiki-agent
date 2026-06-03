---
title: "GSR (Grasp Success Rate)"
type: concept
tags: [metric, VLA, robotics, manipulation]
sources: ["robosemanticbench-2606-02277-ko-analysis"]
last_updated: 2026-06-03
---

## Definition
RoboSemanticBench에서 제안된 메트릭으로, VLA 모델의 grasp(집기) 성공률을 측정한다. semantic target selection과 별개로 물리적 조작 능력을 평가한다.

## Connections
- [[RoboSemanticBench]] — 메트릭이 정의된 벤치마크
- [[TSR]] — 함께 사용되는另一位 메트릭
- [[nSG]] — 함께 사용되는另一位 메트릭
- [[VLA]] — 측정 대상 모델
- [[SemanticGrounding]] — TSR/nSG가 측정하는 대상

## Notes
GSR alone은 모델의 semantic understanding을 측정하지 않는다. Semantic target selection은 TSR과 nSG로 별도 측정한다.
