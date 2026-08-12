---
title: "Trajectory Anchoring Bias"
type: concept
tags: [failure-mode, reasoning, safety, autonomous-driving]
sources: ["deft-rlvr-2608-01755-analysis"]
last_updated: 2026-08-12
---

## Definition
**Trajectory Anchoring Bias**는 GT trajectory나 미래 경로 정보가 모델 추론 초기에 노출되면서, 최종 답변이 장면 근거보다 정답에 맞는 텍스트 정합으로 편향되는 failure mode를 뜻한다.

## 발생 양상
- 모델이 실제 추론 없이 정답 형태의 설명을 생성
- decision은 trajectory 후보 선택과 정합되지 않아도 설명만 그럴듯함
- 사람 평가에서 환각이 상승하거나 근거-결정 정합이 떨어질 수 있음

## 완화 방법
- 후보 노출 지연([[DEFT]])
- 후보 기반 검증(예: [[AD-MCQ]])
- rubric 기반 reward로 explanation-anchored selection 교차 검증

## 영향
- 특히 Vision-Language-Action 시스템에서 안전성 관련 의사결정의 신뢰도를 직접 위협함.

## Related
- [[DEFT]]
- [[DEFT-RLVR]]
- [[AD-MCQ]]
- [[RLVR]]
