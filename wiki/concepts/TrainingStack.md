---
title: "Training Stack"
type: concept
tags: [ai-ml, system-design, training]
sources: [2026-05-23-day30-ai-ml-learning-review, 2026-05-22-day30-ai-ml-learning-review]
last_updated: 2026-05-23
---

## Definition
Training stack은 모델 학습에 필요한 코드, GPU, optimizer, loss, checkpoint, 실험 관리 도구의 묶음이다. 모델 구조, loss function, optimizer, gradient 계산, GPU 학습, checkpoint 저장, validation 평가를 포함한다.

## Components
1. **모델 구조**: neural network 아키텍처 정의
2. **Loss Function**: 예측과 정답의 차이를 측정
3. **Optimizer**: gradient를 이용해 loss가 줄어드는 방향으로 weight 업데이트
4. **GPU 학습**: 대규모 행렬 연산 병렬 처리
5. **Checkpoint**: 학습 중 모델 상태 저장
6. **Validation**: 학습 진행 상황 모니터링

## Basic Flow
```
model(x) = y
loss = difference(y_pred, y_true)
new_weight = old_weight - learning_rate × gradient
```

## Connections
- [[DataPipeline]] — 학습 데이터의 공급원
- [[InferenceStack]] — 학습된 모델이 배포되는 곳
- [[FeedbackLoop]] — 학습 결과가 feedback으로 개선됨
- [[Evaluation]] — 학습된 모델의 성능 측정
