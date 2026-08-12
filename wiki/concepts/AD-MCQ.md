---
title: "AD-MCQ"
type: concept
tags: [autonomous-driving, mcq, verifiable-reasoning, selection]
last_updated: 2026-08-12
source: [deft-rlvr-2608-01755-references]
---

## Summary
[[AD-MCQ]]는 자율주행 장면에서 scene-specific 후보를 구성해 후보군 기반으로 정답 선택을 판별 가능한 형식으로 만드는 framework다.

## Key idea
- 모델이 직접 결과를 생성하기보다 후보 집합에서 선택하게 함으로써, 설명 텍스트와 실제 의사결정 정합성을 더 직접적으로 점검한다.
- DEFT-RLVR의 후보-노출 지연 설계와 결합할 때, decision 오류의 원인을 후보 품질, 근거 정합, 정당성 추론 경로로 분해하기 쉽다.

## Connections
- [[DEFT-RLVR]]
- [[DEFT]]
- [[RLVR]]
- [[TrajectoryAnchoringBias]]
- [[ClosedLoopPlanning]]

## Key Claims
- 선택형 판단은 자유 서술형 CoT만으로는 드러나지 않는 shortcut failure를 진단하기 쉽다.

## Contradictions
- 없음.
