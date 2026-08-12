---
title: "RLVR"
type: concept
tags: [reinforcement-learning, verification, reward, alignment]
sources: [deft-rlvr-2608-01755-learning, deft-rlvr-2608-01755-analysis, deft-rlvr-2608-01755-paper-ko]
last_updated: 2026-08-12
---

RLVR은 outcome을 기계적으로 검증할 수 있는 reward를 사용해 policy를 후학습하는 방식이다. DEFT-RLVR 문맥에서는 [[AD-MCQ]] 선택 정답성과 structured rubric 신호를 함께 사용해, reasoning 품질과 decision 정합성을 동시에 높이는 학습 프레임으로 쓰인다.

## 핵심 포인트
- 검증 가능한 목표에 reward를 직접 연결한다.
- 단순 텍스트 유창성보다 정답성과 정합성을 우선시한다.
- rubric reward를 결합하면 reasoning trace의 질까지 다룰 수 있다.

## Connections
- [[DEFT-RLVR]]
- [[DEFT]]
- [[AD-MCQ]]
- [[TrajectoryAnchoringBias]]
