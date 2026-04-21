---
title: "EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test"
type: source
tags:
  - llm
  - inference
  - inference-acceleration
  - scaling-laws
date: 2026-04-21
source_file: raw/AI/LilysAI/eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-time-test.md
last_updated: 2026-04-21
sources:
  - eagle-3-scaling-up-inference-acceleration-of-large-language-models-via-training-time-test
---

## Summary
[[EAGLE3]]는 [[LLM]] 추론 속도 개선을 위해 기존 특징 예측 위주 방식의 한계를 넘어, 추론 대상 토큰을 직접 예측하는 방식으로 변경했고 동시에 [[TrainingTimeTest]]를 통해 학습 과정에서 추론 동작을 모사하도록 만든다. 이로 인해 데이터 규모 증가가 추론 가속 성능 개선으로 이어지는 새로운 스케일링 관계가 관측된다.

다층 표현을 통합적으로 쓰는 [[MultiLayerFeatureFusion]] 설계가 기존의 최상단 특징 단일 사용 방식보다 풍부한 의미 정합성을 제공해 수용률 저하를 완화한다. 실험에서 [[Vicuna-13B]], [[LLaMA-3.1-8B]], [[LLaMA-3.3-70B]] 기준으로 높은 추론 가속률을 기록하며, [[InferenceOptimization]]의 비용-품질-품질안정성 균형을 동시에 끌어올리는 방향성을 제시한다.

## Key Claims
- [[EAGLE3]]는 기존 [[EAGLE]] 계열의 특징 예측 한계를 넘어 **직접 토큰 예측** 경로를 채택한다.
- [[TrainingTimeTest]]는 학습 중 추론 과정을 시뮬레이션해 추론 성능을 강화하는 핵심 기법이다.
- [[MultiLayerFeatureFusion]]은 저/중/고 레이어 특징을 결합해 한 층의 특징만 의존할 때보다 더 풍부한 신호를 제공한다.
- 실험 결과, [[Vicuna-13B]]/[[HumanEval]]에서 최대 6.47x 가속(약 6.5x), [[LLaMA-3.1-8B]]/[[MT-bench]]에서 4.40x, [[LLaMA-3.3-70B]]/[[GSM8K]]에서 4.34x 가속을 보고한다.
- 평균 수용률은 단계 증가에 따라 급락하지 않고 안정적으로 유지된 것으로 정리된다.
- 추론 데이터 확장의 장점을 추론 가속 영역으로 직접 이전해, 훈련 데이터 증가 시 성능이 비례해 개선되는 스케일링 법칙을 보인다.

## Key Quotes
> "기존 EAGLE은 다음 단계의 특징(Feature)을 예측하는 데 집중했으나, 이는 모델의 표현력을 제한했습니다. EAGLE-3는 이를 제거하고 직접 토큰을 예측합니다."

> "다층 특징을 결합하여 더 풍부한 의미 정보를 활용합니다."

> "최대 6.5배 속도 향상: 기존 EAGLE-2 대비 약 1.4배 더 빠른 성능을 기록했습니다."

> "훈련 데이터가 늘어날수록 추론 속도가 비례하여 빨라지는 스케일링 법칙을 최초로 발견했다는 점이 핵심입니다."

## Connections
- [[EAGLE3]] — 본문의 핵심 기술 패밀리.
- [[LLM]] 추론 가속의 대표적인 실험 기반 사례로 [[InferenceOptimization]]과 연결된다.
- [[TrainingTimeTest]]는 추론 품질 안정성과 속도를 동시에 다루는 핵심 기법이다.
- [[MultiLayerFeatureFusion]]은 고정된 단일 레이어 특징 기반 설계의 한계를 완화한다.
- [[Vicuna-13B]], [[LLaMA-3.1-8B]], [[LLaMA-3.3-70B]]는 벤치마크 모델로, 각기 [[HumanEval]], [[MT-bench]], [[GSM8K]]에서 성능 효과를 보여준다.
- [[이벤트 루프 추론 비용]], [[인터랙티브 추론]], [[동시성 추론 파이프라인]]과 연결되는 비용 절감형 아키텍처 전환으로 읽을 수 있다.

## Contradictions
- No explicit contradiction with existing wiki content was identified during this ingest pass.