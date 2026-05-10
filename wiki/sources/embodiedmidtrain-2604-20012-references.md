---
title: "EmbodiedMidtrain references and related work notes"
type: source
tags: [VLM, VLA, EmbodiedAI, DataSelection, DistributionShift, MidTraining, ProximityEstimator, RepresentationAlignment, RobotManipulation]
date: 2026-05-10
sources:
  - embodiedmidtrain-2604-20012-references
last_updated: 2026-05-10
source_file: raw/Robotics/HuggingFaceWeeklyPapers/embodiedmidtrain-2604.20012/embodiedmidtrain-2604.20012-references.md
source_hash: 2b8f55324d046874
---

## Summary
[[EmbodiedMidtrain]]는 [[VLM|vision-language model]]을 바로 [[VLA|vision-language-action]]로 전이하기 전에, 미리 학습된 VLM 분포에서 목표 과업에 정합되는 샘플만 골라 [[MidTraining]]하는 접근이 핵심 성능 병목을 줄인다는 점을 정리한다. 핵심 메시지는 "더 큰 VLM = 더 좋은 VLA"가 아니라 “표현 정렬이 좋은 VLM 샘플”이 더 중요하다는 것이다.

저자 관점에서 [[DistributionShift]]는 VLM 사전학습 분포와 로보틱스 조작 분포의 간극이며, 이 간극을 줄이기 위한 핵심은 데이터 양 증대가 아니라 [[DataSelection|샘플 단위 정렬]]이다. 이를 위해 VLM feature 위에서 학습한 [[ProximityEstimator]]로 VLA 적합도 점수를 매기고 상위 샘플로 mid-training을 수행한다. 실험 축은 주로 로봇 조작 벤치마크(예: [[Calvin]], [[LIBERO]], [[SimplerEnv]])이며, 모델 확장보다 데이터 적합성 편향이 효과를 지배한다.

## Key Claims
- [[VLM]] 백본(예: [[InternVL3.5|InternVL3.5]], [[Qwen3VL|Qwen3-VL]])를 그대로 [[Fine-tuning]]했을 때보다, [[VLA]] 타깃에 가까운 샘플 위주의 [[MidTraining|미드트레이닝]]이 전반 성능을 크게 개선한다.
- [[VLA]] 성능은 단순한 백본 크기/프리트레이닝 양의 함수가 아니라, VLM 내부에서의 표현 정렬도와 목표 도메인 정합도에 크게 의존한다.
- [[ProximityEstimator]]를 통한 sample-level 점수화는 무작위/거리 기반/퍼플렉시티 기반 baseline 대비 일관되게 우수했다.
- learned proximity 기반 샘플은 [[InternVL3.5|InternVL3.5-1B]]에서 선별되어 [[Qwen3VL|Qwen3-VL]] 같은 다른 백본에도 이식 가능성이 확인된다.
- [[DistributionShift|분포 이동]] 문제를 줄이면, down-stream loss가 유사해도 [[RobotManipulation]] 성능이 달라질 수 있다는 점이 분명해진다.
- 기존 아키텍처 변경 없이도, 입력 데이터의 target-centric 정렬이 [[OpenVLA|OpenVLA]], [[Pi0|π0]], [[GR00T]]류 대비 실용적 성능 개선 경로로 작동한다.
- [[EmbSpatial-Bench]], [[RefSpatial]], [[Robo2VLM]], [[RoboPoint]], [[RoboRefer]]와 같은 embodied/spatial VLM 데이터는 로봇 조작 정합성에서 가치를 가진다.

## Key Quotes
> "VLA 성능은 단순히 VLM 크기나 pretraining 양으로만 결정되지 않는다."

> "VLM 내부에도 VLA와 가까운 샘플과 먼 샘플이 혼재해 있으므로 sample-level selection이 필요하다."

> "학습 loss가 비슷해도 downstream 성능은 크게 달라질 수 있어 representation alignment의 품질이 중요하다."

## Connections
- [[EmbodiedMidtrain]] — 본 출처의 중심 파이프라인.
- [[VLM]] — 백본 후보군을 구성하는 입력 언어·시각 모델군.
- [[VLA]] — 대상 과업군(vision-language-action).
- [[MidTraining]] — 본 논문식 전환 단계의 핵심 절차.
- [[DataSelection]] — 샘플 단위 정렬 기반의 성능 개선 전략.
- [[RepresentationAlignment]] — VLM 표현공간에서 VLA 적합 샘플을 탐색하는 기준.
- [[DistributionShift]] — VLM 학습 분포와 로봇 과업 분포 간 간극.
- [[ProximityEstimator]] — VLA-정합 점수를 산출하는 분류기식 모듈.
- [[MMD]] — 분포 거리 비교의 통계적 배경.
- [[RobotManipulation]], [[Calvin]], [[SimplerEnv]], [[LIBERO]] — 성능 검증 과제군.
- [[OpenVLA]], [[Pi0]], [[GR00T]], [[VLM4VLA]] — 로보틱스-파운데이션 계열 비교 프레임.
- [[RefSpatial]], [[EmbSpatial-Bench]], [[Robo2VLM]], [[RoboPoint]], [[RoboRefer]], [[InternVL3.5]], [[Qwen3VL]], [[Qwen2.5VL]], [[PaliGemma]], [[Kosmos-2]], [[Qwen-VL]], BLADE? — sample 대상 및 후보 모델/백본 맥락.

## Bibliography Notes
- 핵심 비교군: [[VLM4VLA]], [[InternVL3.5]], [[Qwen3VL]], [[Qwen2.5VL]], [[Qwen-VL]], [[PaliGemma]], [[Kosmos-2]].
- 대표 벤치마크/데이터: [[RefSpatial]], [[EmbSpatial-Bench]], [[Robo2VLM]], [[RoboPoint]], [[Calvin]], [[SimplerEnv]], [[LIBERO]], [[RoboRefer]].
- 통계 근거: [[Gretton et al.]], [[MMD]].
- 비교 프레임 모델: [[OpenVLA]], [[Pi0]], [[GR00T]].

## Contradictions
- 기존 소스에서 반복적으로 강조되던 "더 큰 모델 확장이 곧 성능 개선" 정합성 가설과 충돌한다기보다, 본 자료는 모델 확장 이전 단계의 데이터 적합도가 결정적임을 추가적으로 보여주는 반증 가능성이 높은 보완 근거로 해석된다.