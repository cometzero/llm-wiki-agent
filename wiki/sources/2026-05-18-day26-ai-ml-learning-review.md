---
title: "AI/ML Learning Review — Day 26 (2026-05-18): Scaling Laws, Instruction Tuning, RLHF"
type: source
tags: [diary, ai-ml-learning, llm-training]
date: 2026-05-18
source_file: raw/ai_ml_learning/2026-05-18-day26-ai-ml-learning-review.md
source_hash: 4bfad581548a1432
---

## Summary
Day 26 of the AI/ML Fundamentals Daily Learning program covers three core concepts in LLM training pipelines: scaling laws, instruction tuning with SFT, and RLHF with preference optimization. The lesson explains how modern LLMs are designed using scaling laws, trained to follow instructions via supervised fine-tuning, and aligned to human preferences through reinforcement learning.

## Today\'s Three Concepts
1. [[ScalingLaw]]와 모델 크기 (Scaling Laws and Model Size)
2. [[InstructionTuning]]과 [[SupervisedFineTuning]]
3. [[RLHF]]와 [[PreferenceOptimization]]

## Concept 1: 스케일링 법칙과 모델 크기

### 한 줄 직관
LLM은 보통 **모델을 더 크게 만들고, 데이터를 더 많이 보여 주고, 계산을 더 많이 쓰면 성능이 예측 가능한 방식으로 좋아지는 경향**이 있는데, 이 관계를 정리한 것이 scaling law입니다.

### 개념 정의
[[ScalingLaw]]는 모델의 성능, 특히 language model의 loss가 **모델 크기(parameter count), 학습 데이터 양(data scaling), 계산량(compute budget)**에 따라 어떻게 변하는지 관찰하고 수식으로 정리한 경험 법칙입니다.

### 핵심 포인트
- **[[ParameterCount]]**: 모델 안의 학습 가능한 숫자 개수입니다. 실제 LLM은 수십억, 수천억 개까지 갑니다.
- **[[DataScaling]]**: 학습에 사용한 token 수와 데이터 다양성입니다.
- **[[ComputeBudget]]**: GPU 시간, 연산량, 비용의 총량입니다.
- 핵심은 "무조건 크게"가 아니라 **균형 있게 크게**입니다.

### 수학 예시
- 모델 A: parameter 1백만 개, 데이터 1억 token
- 모델 B: parameter 1천만 개, 데이터 1억 token
- 모델 C: parameter 1천만 개, 데이터 10억 token

C처럼 데이터도 함께 늘어야 큰 모델의 장점이 제대로 살아납니다.

## Concept 2: Instruction Tuning과 SFT

### 한 줄 직관
Pretraining이 "언어를 넓게 읽고 배우는 단계"라면, instruction tuning과 SFT는 모델에게 **사람의 지시를 어떻게 따라야 하는지 예시로 가르치는 단계**입니다.

### 개념 정의
- **[[InstructionTuning]]**: LLM이 질문, 요청, 명령 같은 instruction을 보고 적절한 답변을 하도록 학습시키는 과정입니다.
- **[[SupervisedFineTuning]]**: 정답 예시가 붙어 있는 데이터로 모델을 추가 학습시키는 방법입니다.

### 데이터 구조
1. **instruction**: 사용자가 원하는 작업
2. **input/context**: 작업에 필요한 자료
3. **response/answer**: 모델이 따라 배워야 할 좋은 답변

### 핵심 포인트
- 데이터 품질이 매우 중요합니다. 나쁜 답변을 정답으로 주면 모델도 나쁜 스타일을 배웁니다.
- 다양한 instruction이 필요합니다.
- SFT는 모델에게 "무엇을 아는가"보다 "어떻게 답할 것인가"를 강하게 가르칩니다.

## Concept 3: RLHF와 Preference Optimization

### 한 줄 직관
SFT가 "좋은 답변 예시를 따라 하게 만드는 학습"이라면, RLHF와 preference optimization은 **여러 답변 중 사람이 더 좋아하는 답변을 더 자주 만들도록 조정하는 학습**입니다.

### 개념 정의
- **[[RLHF]]**: 사람의 피드백을 이용해 모델의 답변 정책(policy)을 개선하는 방법입니다.
- **[[PreferenceOptimization]]**: 사람이 선호한 답변과 덜 선호한 답변의 차이를 이용해 모델을 개선하는 방법입니다.
- **[[DPO]]**: Direct Preference Optimization. reward model을 별도로 두지 않는 방법입니다.

### RLHF 흐름
1. SFT model 준비
2. **[[PreferenceData]]** 수집: 같은 prompt에 대해 여러 답변을 만들고 사람이 더 좋은 답변을 고름
3. **[[RewardModel]]** 학습: prompt와 답변을 입력하면 "사람이 좋아할 점수"를 예측
4. **[[PolicyOptimization]]**: LLM이 더 높은 reward를 받는 답변을 만들도록 조정

### 핵심 포인트
- "정답 하나를 외우는 것"이 아니라 "선호의 방향을 배우는 것"
- KL penalty 등으로 기존 언어 능력을 유지해야 함

## 배워야 할 용어
- [[ScalingLaw]], [[ParameterCount]], [[ComputeBudget]], [[DataScaling]], [[Loss]]
- [[InstructionTuning]], [[SupervisedFineTuning]], [[InstructionFollowing]], [[FineTuning]]
- [[RLHF]], [[RewardModel]], [[PreferenceData]], [[PolicyOptimization]], [[DPO]]

## Connections
- [[ScalingLaw]] — defines the relationship between model size, data, and compute
- [[InstructionTuning]] — teaches the model to follow human instructions
- [[SupervisedFineTuning]] — the practical implementation method for instruction tuning
- [[RLHF]] — aligns model outputs with human preferences
- [[RewardModel]] — predicts human preference scores
- [[PreferenceOptimization]] — broader category including DPO and PPO-based methods
- [[ParameterCount]] — number of learnable parameters in a model
- [[ComputeBudget]] — total GPU time and computational resources for training
- [[DataScaling]] — scaling the amount and diversity of training data

## Contradictions
- None identified with existing wiki content. This lesson builds on previous days covering transformer architecture and pretraining fundamentals.
