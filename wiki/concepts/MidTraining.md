---
title: "MidTraining"
type: concept
tags:
  - VLM
  - VLA
  - TransferLearning
sources:
  - embodiedmidtrain-2604-20012-ko-analysis
last_updated: 2026-05-10
---

## 개념

[[MidTraining]]은 pretraining과 최종 fine-tuning 사이에서 도메인 정렬 목적의 추가 학습 단계로, 기존 모델 구조를 바꾸지 않고 데이터 분포를 맞추는 작업에 초점을 둔다.

## EmbodiedMidtrain 적용

- frozen [[VLM]] backbone을 유지한 채,
- VLA에 가까운 샘플을 선별해 추가 학습,
- 그 뒤 VLA fine-tuning을 수행한다.

## 특징

- 아키텍처 변경 없이 데이터 분포를 맞춘다.
- 학습 budget은 증가시킬 수 있지만, 목적은 domain shift 완화이다.
- downstream task(특히 [[RobotManipulation]])에서 초기화 품질 향상으로 성능 곡선 상단을 끌어올린다.

## 관련 항목

- [[VLA]]
- [[VLM]]
- [[DataSelection]]
- [[EmbodiedAI]]
