---
title: "Training Stack"
type: concept
tags: [ai-ml, training, mlops, system-design]
sources: [2026-05-24-day30-ai-ml-learning-review]
last_updated: 2026-05-24
---

## Definition

[[TrainingStack]]은 모델을 학습시키는 코드, 데이터 로더, GPU, loss function, gradient, optimizer, checkpoint 관리 등을 포함하는 전체 인프라이다. 모델을 "배우게" 하는 핵심 구성 요소들이다.

## Key Concepts

### Core Components
1. **Model**: 입력 tensor를 받아 예측 생성
2. **Loss function**: 예측과 정답의 차이를 숫자로 표현
3. **Gradient**: loss를 줄이려면 weight를 어느 방향으로 바꿀지 알려주는 값
4. **Optimizer**: gradient를 사용해 모델 파라미터를 업데이트 (SGD, Adam 등)
5. **Data loader**: 학습 데이터 batch 공급
6. **GPU infrastructure**: 대규모 병렬 계산
7. **Checkpoint management**: 학습 중간 저장/복원

### Training vs Inference
- Training: gradient 계산 + 파라미터 업데이트 (weight 변경)
- Inference: 현재 weight로 예측만 수행 (업데이트 없음)

## Connections
- [[DataPipeline]] — 학습 데이터 공급
- [[InferenceStack]] — 학습된 모델 사용
- [[FeedbackLoop]] — 실패 사례 기반 재학습 데이터
- [[Evaluation]] — 학습 진행 상황 측정

## Practical Notes

[[TrainingStack]]은 모델을 배우게 하는 곳이다. 학습에서는 [[DataPipeline]]의 품질이 곧 모델 품질의 상한선을 결정한다.
