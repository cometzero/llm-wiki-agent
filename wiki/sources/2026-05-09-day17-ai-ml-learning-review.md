---
title: "AI/ML Learning Review — Day 17 (2026-05-09)"
type: source
tags: [ai-ml, deep-learning, cnn, learning-curves]
date: 2026-05-09
source_file: raw/ai_ml_learning/2026-05-09-day17-ai-ml-learning-review.md
source_hash: 75c15a175b4d959b
---

## Summary
Day 17 of an AI/ML learning series covers three core deep learning topics: interpreting learning curves to detect overfitting/underfitting, the local connectivity of [[ConvolutionalNeuralNetworks]] (CNNs) via local receptive fields, and the convolution operation itself (kernel, stride, padding). The source includes lesson material and follow-up review answers reinforcing these concepts.

## Key Claims
- Learning curves (train loss vs. validation loss) are essential for diagnosing model training: both high → underfitting; low train + high validation → overfitting; validation loss plateauing or rising → early stopping point.
- CNNs exploit spatial locality by using local receptive fields, parameter sharing, and hierarchical feature learning, making them far more parameter-efficient than fully connected layers for image data.
- Convolution is a sliding dot-product between a kernel and input patches; stride controls output resolution, padding preserves edge information and output size.
- Early stopping is a strategy to select the model with the best validation performance, not "giving up early."

## Key Quotes
> "train loss 하나만 보면 안 된다는 것입니다. train loss는 모델이 '공부한 문제집'에서 얻은 점수입니다. validation loss는 '새 시험지'에서 얻은 점수입니다." — Learning curve interpretation

> "CNN의 지역 연결성(local receptive field)은 이미지를 한 번에 통째로 보지 않고, 가까운 픽셀끼리 먼저 작은 패턴을 찾는 방식입니다." — CNN local connectivity

> "convolution은 kernel이라는 작은 숫자 표를 입력 위에 올려놓고, 겹치는 숫자끼리 곱한 뒤 모두 더하는 연산입니다." — Convolution operation

## Connections
- [[LearningCurves]] — core concept for monitoring training dynamics
- [[ConvolutionalNeuralNetworks]] — architecture built on local connectivity and convolution
- [[Convolution]] — the fundamental operation in CNNs
- [[EarlyStopping]] — technique derived from learning curve analysis
- [[Overfitting]] — diagnosed via learning curves
- [[Underfitting]] — diagnosed via learning curves
- [[Backpropagation]] — used to train CNN kernels
- [[BatchNormalization]] — mentioned as a regularization technique (from Day 16)
- [[Dropout]] — mentioned as a regularization technique (from Day 16)
- [[VisionTransformer]] — noted as an alternative to CNNs that still uses patch-based local processing

## Contradictions
- None identified with existing wiki content.