---
title: "AI/ML Learning Review Day 15 (2026-05-07)"
type: source
tags: [ai-ml-learning, review]
date: 2026-05-07
last_updated: 2026-05-07
source_file: raw/ai_ml_learning/2026-05-07-day15-ai-ml-learning-review.md
source_hash: 958aa8f6e5237341
---

## Summary
Day 15 continued the [[DeepLearning]] training journey with three core topics: [[RepresentationLearning]], initialization, and [[VanishingGradient]] / [[ExplodingGradient]].

The lesson reframed deep learning as building useful internal numeric representations in multiple layers, and explained that stable learning requires good starting parameters and stable gradient flow. The follow-up answers reinforced intuition with concrete examples and quiz-style prompts.

## Key Claims
- Deep neural networks should learn useful feature-like structure from raw input via [[FeatureExtraction]], producing layered [[RepresentationLearning]] that becomes progressively more abstract.
- Good [[Initialization]] is required so that signals and gradients neither vanish nor explode through layer depth.
- [[XavierInitialization]] and [[HeInitialization]] target scale control based on layer fan dimensions, with [[HeInitialization]] generally matched to [[ReLU]].
- Symmetry must be broken in [[Weights]] at startup so neurons can specialize instead of learning identical functions.
- [[VanishingGradient]] is repeated contraction of gradient factors; [[ExplodingGradient]] is repeated expansion; both hinder learning. Techniques like [[ResidualConnection]], [[LayerNorm]], proper initialization, and [[GradientClipping]] stabilize learning.

## Key Claims (with examples)
- [[RepresentationLearning]] is stronger than handcrafted features in image/text because manually engineering all useful cues is hard.
- If all [[Weights]] in a layer start equal, neurons compute identical outputs and remain redundant through training.
- If gradients repeatedly multiply values like 0.5, they collapse to near-zero across many layers.
- If gradients repeatedly multiply values like 2, they can grow rapidly and cause unstable jumps in updates.

## Key Quotes
> "좋은 representation을 만들면 뒤의 작업이 쉬워진다" — core intuition for deep learning. 

> "초기화는 학습 시작점에서 중요한데, 값의 scale이 너무 크면 activation이 폭발하고 너무 작으면 신호가 죽는다." — initialization stability principle.

> "0.5를 계속 곱하면 vanishing, 2를 계속 곱하면 exploding" — intuitive chain-rule behavior in backprop.

## Connections
- [[RepresentationLearning]] — 핵심 주제, 특히 입력에서 추상적 표현으로 가는 흐름.
- [[LatentRepresentation]] — 사람이 직접 라벨링하지 못해도 유용하게 정렬되는 내부 표현.
- [[Embedding]] — 텍스트 입력을 수치로 바꾸는 예시.
- [[HiddenState]] — [[Transformer]]와 [[LLM]]에서 문맥 기반 의미를 담는 내부 상태.
- [[Initialization]] — 학습 안정성의 시작점.
- [[XavierInitialization]] / [[HeInitialization]] — layer 입력 차원 기반 scale 설정 규칙.
- [[SymmetryBreaking]] — 서로 다른 뉴런이 다른 역할을 갖도록 출발 조건을 다르게 설정.
- [[VanishingGradient]], [[ExplodingGradient]] — 깊은 네트워크 학습 실패의 핵심 패턴.
- [[ChainRule]] — backward에서의 gradient 곱셈 효과를 이해하는 수학적 기초.
- [[GradientClipping]] — [[ExplodingGradient]] 완화 장치.
- [[ResidualConnection]], [[LayerNorm]], [[Optimizer]], [[LearningRate]] — 실전에서의 안정화 장치 조합.
- [[ForwardPass]], [[BackwardPass]], [[GradientFlow]] — 학습 신호의 전체 흐름과 연동.
- [[Transformer]], [[LLM]], [[CNN]], [[RNN]], [[TransferLearning]] — day15 내용이 적용되는 주요 모델군.

## Today's 3 concepts
1. [[RepresentationLearning]]와 [[LatentRepresentation]]
2. [[Initialization]]와 [[TrainingStability]]
3. [[VanishingGradient]]와 [[ExplodingGradient]]

## Today’s one-line summary
딥러닝은 층을 따라 좋은 내부 표현을 만들고, 이를 학습시키기 위해 [[Initialization]]과 [[Gradient]] 흐름 안정성이 필수적이다.

## Follow-up Review Questions

### Q1. Why is [[RepresentationLearning]] better than hand-crafting features for image/text?
A. Raw image/text spaces are high-dimensional and context-dependent, so handcrafted rules often miss robust, reusable structure.

### Q2. Why is all-zero (or identical) initialization problematic?
A. It causes neurons to be symmetric; they receive the same updates and fail to specialize.

### Q3. Explain vanishing/exploding gradient via repeated multiplication examples.
A. Repeatedly multiplying by 0.5 drives gradient toward 0 (vanish), while repeatedly multiplying by 2 drives it to very large values (explode).
