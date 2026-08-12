---
title: "DEFT"
type: concept
tags: [reasoning, verifiability, autonomous-driving, vlm]
sources: ["deft-rlvr-2608-01755-analysis"]
last_updated: 2026-08-12
---

## Definition
**DEFT(Deferred Exposure of Future Trajectories)**는 자율주행/의사결정 모델에서 미래 trajectory를 즉시 노출하지 않고, 장면 근거 기반 추론을 먼저 수행한 뒤 후보 집합을 노출해 선택을 수행하게 하는 설계 패턴이다.

## 핵심 아이디어
- reasoning 단계에서는 모델이 GT future에 맞춰 결과를 변명하지 않도록 `candidate-blind` 상태를 유지한다.
- decision 단계에서만 후보를 제시해 selection을 정합적으로 평가한다.
- 장점: CoT의 유창성이나 길이가 아니라, reasoning-결정 간 인과 정합으로 평가가 이동한다.

## 주요 구성요소
- scene reasoning
- evidence/risk/rule rationale 생성
- candidate-grounded decision
- verifier + reward 정합

## 장점
- [[TrajectoryAnchoringBias]] 완화
- text-only 설명의 사후합리화 리스크 감소
- selection 정확도와 해석 가능성의 분리 평가

## 한계
- 후보집합 품질에 의존한다.
- 다변량 continuous 제어는 후보 이산화로 표현력이 제한될 수 있다.

## Links
- [[DEFT-RLVR]]
- [[AD-MCQ]]
- [[TrajectoryAnchoringBias]]
- [[RLVR]]
