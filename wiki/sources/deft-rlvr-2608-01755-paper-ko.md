---
title: "DEFT-RLVR: 자율주행 VLM에서 검증 가능한 추론을 위한 미래 trajectory 지연 노출"
type: source
tags: [autonomous-driving, vlm, vlma, rlvr, ad-mcq, trajectory-anchoring-bias, korean-technical-translation]
date: 2026-08-12
source_url: https://arxiv.org/abs/2608.01755
hf_url: https://huggingface.co/papers/2608.01755
arxiv_id: "2608.01755"
selected_reason: "후보 중 최상위 점수(47)·141 upvote이며, 자율주행 VLM의 CoT 신뢰성·trajectory planning·RLVR을 직접 다룸"
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W32/deft-rlvr-verifiable-ad-vlms-2608-01755/paper-ko.md
source_hash: 89f3e4b76bbda909
---

## Summary
본 논문은 자율주행 Vision-Language-Action 시스템에서 GT 미래 trajectory를 조기 노출할 때 생기는 Trajectory Anchoring Bias를 줄이고, 대신 [[AD-MCQ]] 후보 선택 기반의 검증 가능한 추론을 제안한다. 핵심 아이디어는 **DEFT(Deferred Exposure of Future Trajectories)**로, 장면 이해/추론을 먼저 만들고 후보 trajectory를 나중에 공개해 선택하게 하는 방식이다. 결과적으로 “장면 근거”와 “후보 선택 정답성”을 분리해 평가할 수 있게 하며, [[DEFT-RLVR]]에서는 여기에 [[RLVR]] 보상과 구조화된 rubric을 결합해 추론 정합성과 데이터 효율을 동시에 개선한다.

요지는 다음 두 단계로 정리된다:
1. 후보 trajectory를 숨긴 상태에서 장면 기반 위험/규칙 인지를 먼저 설명하게 하여 causal grounding을 유지
2. 후보를 노출해 explanation과 후보 간 일치도를 점검하고 정답을 선택

실험은 AD-MCQ와 OOD 설정에서 추론 정확도 개선을 보고하며, 일반 시각 능력 저하를 상대적으로 억제하는 편익도 제시한다. [[Qwen3VL]] 기반 베이스라인을 바탕으로 nuScenes(500 scene) 기반 분석, 기본 VLM 비교, 그리고 후보 품질-난이도 설정 변화를 다룬다.

## Key Claims
- GT 미래 trajectory를 모델 입력에서 미리 노출하면 post-hoc 합리화가 증가하고 hallucination이 악화될 수 있으며, 실험적으로 GT 노출 조건의 심한 환각 비율이 50.0%로, 노출하지 않은 조건(29.0%)보다 높다.
- 사람이 평가한 정량 비교에서, GT 비노출 condition의 선호도가 GT 노출보다 더 높았다(예: 60.5% 대 24.0%).
- 저자들은 이런 문제를 **trajectory anchoring bias**로 해석하고, GT를 설명 타깃으로 쓰는 annotation이 GT를 근거처럼 재구성하는 짧은 shortcut 방향을 강화한다고 주장한다.
- [[AD-MCQ]]는 다수의 scene별 후보 trajectory를 구성해 candidate set에서 정답 선택을 명시적으로 판정하게 하여, reasoning과 action 선택을 분리된 기준으로 검증한다.
- 코드북 크기/클러스터링 타협점으로 K=8192를 제시하며, reconstruction fidelity와 downstream 활용성을 균형 있게 확보했다고 보고한다.
- DEFT-RLVR은 2단계 추론(선행 reasoning, 후행 candidate grounding)을 RLVR 기반으로 통합 최적화하고, structured rubric reward(장면 증거, 위험/규칙 정합, decision logic)를 사용해 무의미한 장문 추론을 억제한다.
- 실험에서 AD-MCQ in-domain, OOD(nuScenes 500 scene), 그리고 baseline general visual benchmarks의 성능이 개선 경향을 보였고, AD reasoning 특화 성능과 일반 visual capability 보존 사이의 trade-off를 완화한 것으로 보고된다.
- 후보 노출 지연은 shortcut 최적화(특히 답-사후 정합형 reasoning 유도)를 감소시키고, rubrics 탐색 비용/탐색 폭을 안정화한다.

## Key Quotes
> "trajectory를 사전 노출하면 grounding보다 post-hoc rationalization이 강화될 수 있다."

> "DEFT는 reasoning을 먼저 만들고 candidate를 나중에 노출하는 순서를 통해, causal scene grounding을 훼손하지 않은 상태로 후보 선택을 검증 가능하게 만든다."

> "후보 노출 지연이 커질수록 shortcut 최적화가 줄고, rubric supervision이 탐색 비용을 불필요하게 증가시키는 경향을 억제한다."

## Connections
- Trajectory Anchoring Bias — GT 결과에 과도하게 정렬되는 CoT 유도 현상
- [[DEFT]] — future trajectory 지연 노출의 핵심 설계
- [[DEFT-RLVR]] — DEFT + RLVR 결합으로 선택 정밀도와 신뢰성 동시 개선
- [[AD-MCQ]] — candidate-based, 정답 판별 가능한 AD benchmark 형태
- [[RLVR]] — selection과 reasoning 경로를 통합 최적화하는 보상 학습 프레임
- [[Qwen3VL]] — 베이스라인 모델로 사용된 backbone
- [[AutonomousDrivingVLA]] — 본 논문의 적용 도메인 축
- [[ClosedLoopPlanning]] — trajectory 후보와 closed-loop 평가의 연결 지점
- [[Hallucination]] — GT-conditioned CoT 유도에서의 위험 신호

## Contradictions
- 없음: 기존 출처에서 제시된 일반적인 추론 기반 접근(특히 이유 설명이 성능을 보장한다는 가정)과 충돌하지는 않으나, 본 논문은 **추론-근거 텍스트 자체의 존재가 곧 grounding 보장을 뜻하지 않는다**는 점을 반례 기반으로 강화한다.