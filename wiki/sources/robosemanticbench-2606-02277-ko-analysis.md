---
title: "RoboSemanticBench: VLA 모델의 Action Prediction에서 Semantic Grounding 진단하기 — analysis"
type: source
tags: [VLA, semantic-grounding, benchmark, robotics, embodied-AI]
date: 2026-06-03
sources: ["robosemanticbench-2606-02277-ko"]
last_updated: 2026-06-03
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W23/robosemanticbench-2606-02277/analysis.md
source_hash: f207698441d8af1a
---

## Summary
RoboSemanticBench(RSB)는 [[VLA]] 모델의 언어/상식 이해와 실제 행동 선택 간의 격차를 진단하는 embodied benchmark로, 수학·상식 문제를 물리적 블록 선택 과제로 변환하여 측정한다. GSR/TSR/nSG 메트릭으로 grasp 능력과 semantic target selection을 분리 분석하며, OpenVLA/π 계열/GR00T 계열 등의 near-random 수준 semantic grounding 실패를 실증한다.

## Key Claims
- 현재 [[VLA]] benchmark는 manipulation success와 semantic understanding을 분리하기 어렵다
- RSB benchmark는 [[SemanticGrounding]] 격차를 embodied answer-selection task로 측정한다
- 수학·hard math·일반지식 문제를 [[RSB-Math]], [[RSB-HardMath]], [[RSB-General]]로 분류한다
- 4-choice/10-choice 형태의 선택 과제로 변환하여 평가한다
- [[GSR]]/[[TSR]]/[[nSG]] 메트릭으로 grasp 능력과 semantic target selection을 분리 측정한다
- OpenVLA, [[Pi0]], [[GR00T-N1]] 등 대표 VLA에서 semantic grounding gap이 존재함을 실증한다
- [[ReasoningVLA]], VLA cotrain 등 개선 방향을 탐색한다
- 평가 방식은 단순 VQA/open-loop reasoning score가 아니라 simulation 또는 real-robot execution 기반이다
- 자율주행 [[VLA]]에도 동일한 semantic grounding 위험이 존재한다

## Key Quotes
> "VLA가 '말을 이해한다'는 주장과 실제 action prediction이 의미를 따라 움직이는지는 다르며, RoboSemanticBench는 이 간극을 수학/상식 질문→물리적 블록 선택 과제로 드러낸다"

## Connections
- [[SemanticGrounding]] — RSB가 진단하는 핵심 병목 현상
- [[VLA]] — 진단 대상 모델类别
- [[OpenVLA]] — 평가 대상 중 하나
- [[GR00T]] — 평가 대상 중 하나 (NVIDIA 계열)
- [[ReasoningVLA]] — 개선 방향으로 언급
- [[GSR]] — Grasp Success Rate 메트릭
- [[TSR]] — Target Selection Rate 메트릭
- [[nSG]] — normalized Success of Grasp 메트릭
- [[RSB-Math]] — 벤치마크 하위 데이터셋
- [[RSB-HardMath]] — 벤치마크 하위 데이터셋
- [[RSB-General]] — 벤치마크 하위 데이터셋
- [[AutonomousDriving]] — 동일한 semantic grounding 위험이 적용되는 도메인
- [[EndToEndAutonomy]] — 자율주행 VLA의 semantic decision→action grounding 필요성

## Contradictions
- 기존 [[VLA]] benchmark가 manipulation success로 semantic understanding을 암묵적으로 측정하던 방식과 달리, RSB는 이를 명시적으로 분리 측정한다

## Implications
RSB의 발견은 [[FoundationModel]] 기반 robotics 연구에 중요한 시사점을 제공한다:
1. [[VLM]] backbone의 언어/상식 능력이 실제 action target selection에 반영되지 않을 수 있다
2. Semantic reasoning trace가 실제 행동을 causally guide하는지 검증이 필요하다
3. 자율주행에서도 route instruction이나 traffic-rule semantics "이해"와 실제 waypoint/trajectory 선택 간 격차가 존재할 수 있다
