---
title: "VLAct"
type: entity
tags: [vision-language-action, robotics, pretraining, cross-embodiment]
last_updated: 2026-09-02
---

## 개요

[[VLAct]]는 [[VisionLanguageAction]]의 성능 향상을 위해 continued pretraining 단계에서 backbone 표현을 유지하면서 행동(decoding) 쪽으로만 안정적으로 적응하는 레시피를 제시하는 연구 계열이다.

## 핵심 아이디어

- pretrained [[VisionLanguageModel|VLM]]에서 visual-language prior를 유지한다.
- robot trajectory 데이터와 caption 데이터를 섞어 학습해 action-only fine-tuning으로 인한 [[CatastrophicForgetting|표현 붕괴]]를 줄인다.
- 다수의 continuous action head ([[OFT]], [[PI]], [[GR00T]])로 [[DecoderLockIn]]을 완화한다.
- embodiment 간엔 전체 좌표를 통일하지 않고 [[ActionSpaceAlignment]] 가능한 부분(예: gripper)만 공유한다.

## 연결

- 관련 벤치마크: [[LIBERO-Plus]], [[RoboTwin 2.0]], [[VLA-Arena]], [[RoboDojo]], [[RoboCasa]], [[DOMINO]]
- 관련 개념: [[RepresentationLearning]], [[CrossEmbodimentLearning]], [[ContinuedPretraining]], [[ActionHead]], [[WrapAwareLoss]]
- 실험 기반: [[Qwen3-VL]] 계열 백본 기반 public robot/caption data 활용

## 비고

학습 노트 기준으로, downstream에서는 task-specific head를 새로 붙여 continued pretraining head에 과도하게 의존하지 않는 구조를 권장한다.