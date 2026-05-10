---
title: "EmbodiedMidtrain: VLM과 VLA 사이의 간극을 Mid-training으로 잇기"
type: source
tags:
  - VLA
  - VLM
  - EmbodiedAI
  - Robotics
  - DataSelection
  - DistributionShift
  - MidTraining
  - SampleSelection
  - MMD
  - Calibration
date: 2026-05-10
sources:
  - embodiedmidtrain-2604-20012-ko-analysis
last_updated: 2026-05-10
source_file: raw/Robotics/HuggingFaceWeeklyPapers/embodiedmidtrain-2604.20012/embodiedmidtrain-2604.20012-ko-analysis.md
source_hash: 06fcef563db732cd
---

## Summary
이 논문 [[EmbodiedMidtrain]]는 [[VLM]]을 그대로 fine-tuning하는 방식으로는 [[VLA]] 성능이 충분히 살아나지 않는다는 점을 분포 관점에서 설명한다. 저자들은 [[VLM]] 학습 분포와 [[VLA]] 학습 분포 간 간극이 크며, 특히 [[DistributionShift|분포 이동]]이 존재한다는 점을 먼저 정량화한다. 그다음, VLM 후보군에서 [[VLA]]에 가까운 샘플만 선별해 mid-training corpus를 구성하고 이 데이터를 이용해 VLA downstream 적응 능력을 높인다는 점에서 핵심 기여가 있다.

실험은 [[RobotManipulation]] 벤치마크에서의 성능 향상으로 정합성이 검증되며, 데이터량 증가보다 분포 정렬이 중요하다는 메시지를 강화한다. 특히 [[InternVL3.5|InternVL3.5-1B]]과 [[Qwen3VL|Qwen3VL-2B]]의 실험에서, 비교적 작은 모델도 적절한 mid-training 데이터로 더 큰 모델 대비 동등한 경쟁력을 보이는 결과가 제시되었다.

## Key Claims
- [[VLA]]은 [[VLM]]을 backbone으로 쓰되, [[VLM]] pretraining 분포가 robot manipulation 분포와 다르기 때문에 단순 pretraining 규모 확대만으로는 한계가 있다.
- [[VLM]]과 [[VLA]] 데이터셋은 representation space에서 집합 분포 차이가 크며, 특히 VLA 데이터는 상대적으로 compact하고 분리된 군집 구조를 보인다.
- [[VLM]] 내부에도 VLA에 가까운 샘플이 일부 존재하므로, 데이터 전부를 fine-tuning하거나 random으로 고르면 효과가 떨어진다.
- 저자들은 frozen된 [[VLM]] feature 위에 lightweight [[BinaryClassification|binary classifier]]를 두고, VLA-정합 점수를 학습하는 
  [[ProximityEstimator|proximity estimator]]를 구성한다.
- 이 score를 바탕으로 top-K 샘플을 뽑아 mid-training을 수행하면 세 가지 로보틱스 benchmark에서 일관된 성능 향상이 보고된다.
- 성능 개선은 pretraining 예산만 늘렸을 때 대비, 데이터의 분포 정렬 정도가 더 중요함을 보여준다.
- best-performing estimator가 random/거리 기반/퍼플렉서티 기반 대비 우수해, sample-level 선택이 모델 성능에 핵심적임을 입증한다.
- learned proximity 기반 샘플은 다른 backbone(예: [[InternVL3.5|InternVL3.5-1B]]에서 뽑은 데이터가 [[Qwen3VL|Qwen3VL-2B]]에 이식 가능)에도 효과가 있어, 데이터셋 자체의 도메인 신호를 잡아낼 수 있음이 시사된다.
- 학습 loss는 비슷해도 downstream task 성능은 달라질 수 있어, [[TrainingDynamics|초기화 품질]]은 task-specific proxy보다 [[RepresentationAlignment|표현 정렬]]이 더 중요할 수 있다.

## Key Quotes
> "VLA 성능은 단순히 VLM 크기나 pretraining 양만으로 결정되지 않는다."

> "VLM 데이터 내부에서도 VLA와 가까운 샘플과 먼 샘플이 섞여 있으므로 sample-level data selection이 필요하다."

> "학습 loss가 비슷해도 downstream 성능은 크게 달라질 수 있어, representation alignment의 품질이 더 중요하다."

## Connections
- [[EmbodiedMidtrain]] — 본 논문의 중심 파이프라인.
- [[VLA]] — Vision-Language-Action 모델 계열의 target adaptation 대상.
- [[VLM]] — backbone source 모델 집합.
- [[EmbodiedAI]] — spatial grounding 및 물리적 조작 맥락의 목표 domain.
- [[DataSelection]] — sample-level 데이터 선별의 핵심 전략.
- [[DistributionShift]] — VLM pretraining 분포와 VLA target 분포의 간극 개념.
- [[MMD]] — 분포 간 거리 측정에 쓰인 핵심 지표.
- [[RobotManipulation]] — 성능 검증 벤치마크가 적용되는 과업군.
- [[Calvin|Calvin ABC-D]], [[SimplerEnv|SimplerEnv-Bridge]], [[LIBERO|LIBERO-10]] — 대표 benchmark.
- [[InternVL3.5|InternVL3.5-1B]] — main backbone 후보.
- [[Qwen3VL|Qwen3VL-2B]] — cross-backbone 전이 성능 실증.
- [[EdgeAI]] — 작은 모델의 현장 배포 관점에서 데이터 적응 접근이 갖는 실무적 의미.

## Contradictions
- 기존 로보틱스 소스들 일부는 구조/아키텍처 통합(예: [[EndToEndDeepLearning]])을 중심으로 성능 개선을 설명하는 반면, 본 논문은 아키텍처 변경 없이 "데이터 분포 정렬"만으로도 상당한 개선을 보인다는 실무적 반증을 제시한다. 이는 모순이 아니라 성능 개선의 상보적 경로로 해석된다.