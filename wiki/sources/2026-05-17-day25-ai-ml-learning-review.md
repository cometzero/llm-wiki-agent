---
title: "AI/ML Learning Review — Day 25 (2026-05-17): LLM Baseline Learning Pipeline"
type: source
tags: [ai-ml-learning, llm, language-model, tokenization, pretraining]
date: 2026-05-17
last_updated: 2026-05-17
source_file: raw/ai_ml_learning/2026-05-17-day25-ai-ml-learning-review.md
source_hash: 0d937180ee2ca39c
---

## Summary
Day 25 introduces the foundational LLM learning pipeline: text is first transformed by [[Tokenization]] into discrete [[Token]] sequences, then modeled with [[NextTokenPrediction]] in a [[CausalLanguageModel|causal language model]] setup using a self-supervised [[Pretraining]] loop that minimizes [[CrossEntropyLoss]]. The lesson connects objective choice ([[CausalLanguageModel]], [[MaskedLanguageModel]]) with what a model can learn, how inference is generated token-by-token, and why tokenizer design (especially [[Subword]], [[BytePairEncoding]]) directly affects both quality and cost.

## Key Claims
- [[LanguageModel]]s are sequence probability engines that estimate next-token distributions over [[Vocabulary]], not one-shot answer mappers.
- LLM pretraining is usually [[SelfSupervisedLearning]]: the raw text itself supplies supervised targets.
- [[NextTokenPrediction]] for GPT-family models uses left-to-right [[Autoregressive]] generation and requires [[CausalMask]] during training/inference compatibility.
- [[Tokenization]] is a non-neural pre-processing boundary with large impact on input length, OOV handling, and inference cost.
- [[Subword]] tokenization balances dictionary coverage and sequence length; it reduces unknown-word failure while increasing token counts in some cases.
- In pretraining, [[Objective]] defines the learning problem and [[Loss]] guides parameter updates via [[Gradient]] + [[Optimizer]].

## Key Quotes
> "Language model은 지금까지 나온 token들을 보고 다음 token의 확률분포를 예측하는 모델이다."

> "다음 token은 앞에서부터 이어지며 생성된다. 즉 언어모델은 '토큰 하나씩' 확률적으로 이어붙인다."

> "토크나이저가 모델의 입구다. 같은 문장도 tokenizer가 다르면 token 수, id, embedding lookup 결과가 달라진다."

## Connections
- [[LanguageModel]] — probability over token sequences
- [[NextTokenPrediction]] — fundamental training and inference framing
- [[Autoregressive]] — one token at a time generation
- [[CausalMask]] — prevents looking at future tokens
- [[Tokenization]] — text-to-id conversion stage
- [[Subword]] / [[BytePairEncoding]] — segmentation methods for robust vocabulary use
- [[Embedding]] — token-id to vector lookup
- [[Vocabulary]] / [[Token]] / [[Token id]] — core token-level representations
- [[CausalLanguageModel]] and [[MaskedLanguageModel]] — two major objective families
- [[Pretraining]] / [[SelfSupervisedLearning]] — how large-scale LLMs bootstrap
- [[Optimizer]] / [[CrossEntropyLoss]] / [[HiddenState]] — optimization loop and representations

## Core Content

### 오늘의 3개 개념
1. 언어모델과 next-token prediction
2. 토큰화와 subword 분해
3. 사전학습 objective

### 핵심 정리
- GPT류의 기본은 다음 token 예측이다. 모델이 문장 시작부터 끝까지 확률 분포를 계속 확장한다.
- 모델이 이해한다고 보이는 행동은 사실, 각 단계에서 가장 가능성 높은 토큰을 누적 생성하는 과정을 반복한 결과다.
- Tokenization은 모델 성능 뿐 아니라 비용/속도까지 좌우한다.
- Pretraining objective가 다르면 모델이 학습에 쓰는 정보와 생성 스타일이 달라진다.

### 요약 수식
언어모델 목표 확률:

`P(x_t | x_1, x_2, ..., x_{t-1})`

문장 확률 분해:

`P(x_1, x_2, x_3) = P(x_1) P(x_2 | x_1) P(x_3 | x_1, x_2)`

cross-entropy 최적화:

`L = -\sum_t \log P_\theta(x_t | x_{<t})`

### 결론
LLM의 기본은 단순해 보이지만, [[Context]] 기반 확률 모델링, token-level representation, 그리고 objective/loss 설계가 합쳐져서 장기적으로는 문맥 추론, 지식 반영, 코드 스타일 학습까지 이끈다.

## Review Questions (source)
1. Language model이 단어 빈도만으로는 충분하지 않고 문맥을 이해해야 하는 이유는?
2. Subword tokenization은 OOV 문제를 줄이되 어떤 비용을 늘릴 수 있는가?
3. Causal LM과 masked LM의 문맥 접근 차이는 무엇이며, 어떤 task에 자연스럽게 맞는가?

## Follow-up Review Answers
### 1) 왜 단순 빈도만으로는 부족할까?
[[NextTokenPrediction]]은 문맥(좌우 의존성, 세계 지식, 문법, 대화 흐름)을 반영해 token 분포를 다르게 만들기 때문에, 빈도만 외우면 "나는 물을"에서 "마셨다"처럼 문맥에 맞는 예측이 어렵다.

### 2) Subword는 모르는 단어를 어떻게 완화하나?
미등록 단어를 조각으로 분해해 의미 단위의 유사한 패턴을 통해 처리한다. 대신 토큰 분해가 촘촘해져 [[SequenceLength]]가 늘고 [[Attention]] 비용이 증가한다.

### 3) Causal LM vs masked LM
- [[CausalLanguageModel]]: 왼쪽 문맥만 사용, 생성형 대화/요약/코드생성에 자연스러움.
- [[MaskedLanguageModel]]: 양쪽 문맥으로 빈칸 복원, 문장 이해/분류/문장 판단 등에서 유리.

## Contradictions
- None identified versus existing entries.

## 오늘의 한 줄 요약
LLM은 텍스트를 [[Tokenization]]해 [[NextTokenPrediction]]으로 사전학습하고, 자기 자신이 생성한 정답 위치(자동 라벨)에서 [[CrossEntropyLoss]]를 줄이며 [[Autoregressive]] 생성에서 token 단위로 반응한다.