---
title: "Continued Pretraining"
type: concept
tags: [pretraining, continual-learning, transfer-learning]
last_updated: 2026-09-02
---

## 정의

[[ContinuedPretraining]]는 과도한 task-specific fine-tuning 이전에, 이미 학습된 대규모 기본 모델을 도메인 특화 신호(여기선 robot data + caption data)로 추가 학습해 표현을 확장하는 단계다.

## VLAct에서의 핵심

- lower layers(vision encoder/LLM 하위)를 보호하고 upper layer를 task 관련 신호로 조정
- caption signal로 [[VisionLanguageModel]]의 broad prior를 유지
- downstream에서는 신규 head를 얇게 붙여 transfer를 평가

## 장점

representation을 유지한 채 action-specific 성능을 끌어올릴 수 있어, 단순 데이터 증대만으로 생기는 drift 리스크를 줄인다.
