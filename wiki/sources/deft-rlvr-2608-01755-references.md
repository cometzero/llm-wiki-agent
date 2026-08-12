---
title: "DEFT-RLVR 참고 레퍼런스"
type: source
tags: [autonomous-driving, refs, deft, rlvr, ad-mcq, verifiable-reasoning]
date: 2026-08-12
source_url: https://api.semanticscholar.org/graph/v1/paper/ARXIV:2608.01755/references
week: "2026-W32"
ingested_at_kst: "2026-08-12 09:40:01 KST"
selected_reason: "DEFT-RLVR의 핵심 흐름과 연결되는 AD/Verifiable Reasoning 선행 연구를 한데 모은 참고문헌 정리"
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W32/deft-rlvr-verifiable-ad-vlms-2608-01755/references.md
source_hash: 8ad18040264fe595
---

## Summary
[[DEFT-RLVR]]의 핵심 축은 [[TrajectoryAnchoringBias]]를 줄이기 위해 reasoning 과정을 candidate 선택에서 분리한 [[DEFT]] 설계다. 이 페이지는 DEFT-RLVR와 연결되는 선행 연구를 **구조화된 추론([[StructuredChainOfThought]])**, **candidate 기반 AD 선택([[AD-MCQ]])**, **rubric 보상([[Autorubric]])**, **툴 사용 및 컨텍스트 정렬([[ToolAnchor]])**, **추론 길이 제어([[ReasoningStopCriterion]])**, **영상 추론 스케일링([[VeryBigVideoReasoningSuite]])**, **실시간 정렬형 보상([[RealTimeAlignedReward])** 맥락으로 정리한다.

## Key Claims
- Accelerating Structured CoT in Autonomous Vehicles는 추론을 빠르게 전개하는 동향을 제시하며, DEFT는 오히려 후보-노출 타이밍을 바꿔 shortcut을 줄이는 방향으로 보완한다.
- Rethinking Multiple-Choice Questions for RLVR: Unlocking Potential via Distractor Design는 distractor/선택군 설계가 RLVR 품질을 좌우함을 보여주며, 이는 [[DEFT-RLVR]]의 [[AD-MCQ]] 축과 직접 정합된다.
- Autorubric: A Unifying Framework for Rubric-Based LLM Evaluation on Non-Verifiable Tasks는 비검증 과제에서 rubric 계열 reward 체계를 일반화하고, 본 문맥에서는 [[DEFT-RLVR]]의 structured rubric 설계와 자연스럽게 연결된다.
- ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability는 컨텍스트 앵커링이 에이전틱 tool 사용에 미치는 shortcut 효과를 실증해 DEFT의 후보 노출 제어와 대비 축으로 참고된다.
- Does Your Reasoning Model Implicitly Know When to Stop Thinking?는 추론 길이/중단 시점이 품질·비용 트레이드오프에 영향을 줌을 보여주며 [[ReasoningStopCriterion]]의 중요성을 제시한다.
- A Very Big Video Reasoning Suite는 영상 기반 reasoning 대규모 검증 체계의 breadth를 보여주어 AD 비전 모듈의 일반성 점검 기준으로 유효하다.
- Real-Time Aligned Reward Model beyond Semantics는 실시간 reward/alignment 설계 관점을 제공하고, DEFT 계열의 RubricBasedEvaluation 비용-효율 균형과 대비한다.

## 읽기 순서
1. [[AD-MCQ]] 기반 candidate 설계와 distractor 설계를 통해 후보 선택 신뢰도를 먼저 점검
2. RubricBasedEvaluation 및 [[Autorubric]] 계열로 정합 보상 신호를 정밀화
3. [[StructuredChainOfThought]]/[[ReasoningStopCriterion]]로 추론 경로 품질 및 짧은 shortcut을 제어
4. [[ToolAnchor]]/[[RealTimeAlignedReward]]로 컨텍스트 정렬과 실시간 보상 리스크를 비교
5. [[VeryBigVideoReasoningSuite]]로 일반 비전 reasoning 성능과 [[AutonomousDrivingVLA]] 도메인 신호가 일치하는지 교차 점검

## Key Quotes
> "candidate가 먼저 노출되는 추론은 정답 유추보다 정답 정합 편향으로 흘러가기 쉽다." — 구조화·선별형 선택 접근의 실무적 경고

> "rubric가 있는 RL 보상은 길이가 긴 텍스트 자체보다 선택 정합성, 규칙 정합성, 위험 정당화 정합성을 함께 묶어야 의미가 있다." — 구조적 채점 관점에서의 핵심 정합 조건

## Connections
- [[DEFT-RLVR]] — candidate-blind reasoning + 후보-grounded decision의 계보에 해당 선행군 정렬
- [[DEFT]] — future trajectory 지연 노출 설계의 전단계 이론 기반
- [[AD-MCQ]] — 후보군 기반 선택 정답성 평가의 핵심 연결점
- [[RLVR]] — structured reward 신호 학습과 정합성 결합
- [[StructuredChainOfThought]] — 과도한 사후 합리화 감소를 위한 구성적 추론 설계
- [[Autorubric]] — non-verifiable 과제에서의 rubric reward 프레임
- RubricBasedEvaluation — structured rubric 보상/평가 추상화
- [[ToolAnchor]] — 컨텍스트 앵커링이 tool 사용 편향에 미치는 영향 비교 축
- [[ReasoningStopCriterion]] — 추론 지속 여부 조절이 비용·신뢰도에 미치는 영향
- [[VeryBigVideoReasoningSuite]] — 비전 reasoning 일반화 커버리지 확장
- [[RealTimeAlignedReward]] — 실시간 보상 설계와 AD 도메인 적용 시 latency 고려축

## Contradictions
- 없음. 기존 [[DEFT-RLVR]] 핵심 주장과 충돌하지 않으며, 기존 축을 강화하는 참고문헌 정렬로 이해하면 된다.