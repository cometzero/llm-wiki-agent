---
title: "Action Grounding"
type: concept
tags: [VLA, Robotics, Reasoning]
sources: [visualthink-vla-2605-30011, visualthink-vla-2605-30011-ko-analysis, visualthink-vla-2605-30011-learning, robosemanticbench-2606-02277, robosemanticbench-2606-02277-ko-analysis]
last_updated: 2026-06-03
---

## Definition
Action grounding은 언어/시각 reasoning 결과( semantic decision)가 실제 waypoint, trajectory, gripper action 등 executable physical action으로 변환되는 과정을 의미한다.

## Core Problem
VLA 모델이 VQA(Vision Question Answering) 태스크에서 높은 성능을 보이더라도, semantic answer가 action pathway에 전달되지 않으면 의미 없는 [[ShortcutBehavior]]가 발생할 수 있다.

## Key Requirements
1. **Semantic Decision Identification**: 어떤 것을 semantic decision으로 볼지 정의
2. **Interface Definition**: decision이 physical target/action으로 변환되는 명확한 interface 설계
3. **Metric Separation**: motor execution과 semantic selection의 메트릭 분리
4. **Latency Consideration**: latency와 safety-critical failure mode 동시 고려

## VisualThink-VLA Approach
Visual intermediate reasoning으로 textual CoT 대신 visual evidence states를 사용:
- Candidate visual evidence bank → selective router → visual state composer → VLA action decoder
- Teacher-student distillation으로 sparse interface가 dense teacher 성능 보존

## Related Concepts
- [[VisualReasoning]] — textual CoT 대비 효율적
- [[SelectiveRouting]] — instruction 기반 evidence 선택
- [[ShortcutBehavior]] — grounding 실패의 증상
- [[ClosedLoop]] — 실시간 환경에서 실행

## Connections
- [[RoboSemanticBench]] — semantic grounding 진단 benchmark
- [[OpenVLA]] — VLA baselines 중 하나
- [[π0.5]] — VLA action prediction 연구