---
title: "RoboSemanticBench: VLA 모델의 Action Prediction에서 Semantic Grounding 진단하기"
type: source
tags: [robotics, VLA, benchmark, semantic-grounding, embodied-AI]
date: 2026-06-03
sources: []
last_updated: 2026-06-03
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W23/robosemanticbench-2606-02277/paper-ko.md
source_hash: f7ae4d6f4aab51be
---

## Summary

RoboSemanticBench(RSB)는 [[VLA]] 모델이 [[SemanticGrounding]]을 통해 instruction semantics를 행동 예측에 올바르게 연결하는지 진단하는 embodied benchmark이다. 물리적 블록 선택 과제를 통해 기존 [[VLA]] 모델들의 "semantic expert와 action expert 간 격차(semantic gap)"를 정량화한다.

## Key Claims

- [[VLA]] 모델은 pretrained VLM backbone에서 semantic competence를 가지지만, 이것이 robot action prediction으로 안정적으로 전달되지 않는다
- Imitation learning loss는 task success 분포 매칭에 최적화되어, semantic decision → action mapping을 강제하지 않는다
- 대표 [[VLA]] 모델들은 block grasp는 성공하지만, target selection은 near-random 또는 below-random 수준이다
- Semantic grounding gap은 harder semantic domain과 10-choice suite에서 더 커진다
- 실패 원인은 motor control이 아니라 instruction semantics가 action pathway에 통합되지 않는 데 있다

## Key Quotes

> "grasp success를 통제하면 semantically correct block 선택은 random 또는 below-random에 가깝게 나타나 backbone-level semantic competence와 action prediction 사이의 persistent gap을 보여준다"

> "강한 VLM을 action expert에 붙이는 것만으로는 semantically grounded policy가 되지 않으며, selected semantic target을 action module에 보존·노출하는 training objective/interface가 필요함을 시사한다"

## Task Construction

RSB는 세 가지 task type으로 구성된다:

| Task Type | Description | 예시 |
|-----------|-------------|------|
| RSB-Math | 두 자리 덧셈/뺄셈, 한 자리×두 자리 곱셈 | 47 + 38 = ? |
| RSB-HardMath | GSM8K식 grade-school word problem | "지갑에 $15가 있고..." |
| RSB-General | commonsense/factual knowledge | 물의 어는점은? |

## Metrics

| Metric | 의미 | 이상적 값 |
|--------|------|-----------|
| GSR (Grasp Success Rate) | 후보 블록 집기 성공률 | 높을수록 |
| TSR (Task Success Rate) | 정답 블록 answer zone 이동 성공률 | 높을수록 |
| nSG (normalized Semantic Grounding) | grasp 성공 시 정답 선택률 | 1.0 (perfect) |

high GSR + low TSR = "무엇인지는 모르겠지만 일단 잡는다"

## Choice Suite Design

- **4-choice**: A/B/C/D
- **10-choice**: A/B/D/E/F/G/H/I/K (J 제외) — color/position shortcut 방지를 위해 same-color letter blocks 사용

## Implementation

- Embodiment: Aloha-AgileX dual-arm
- Environment: tabletop simulator (MPLib motion planning)
- Sensors: multi-view RGB, wrist cameras, proprioception
- Expert: scripted policy로 ground-truth answer → block 매핑

## Connections

- [[VLA]] — 대상 기술
- [[Pi0]] — dual-system (semantic/action expert) 설명 참조
- [[GR00T-N1]] — 관련 VLA 모델
- [[OpenVLA]] — 관련 VLA 모델
- [[SemanticGrounding]] — 핵심 진단 대상 개념
- [[EmbodiedBenchmark]] — benchmark 카테고리
- [[ActionPrediction]] — 예측 대상 태스크

## Contradictions

없음 — 신규 벤치마크로 기존 wiki 내용과 명시적 모순 없음
