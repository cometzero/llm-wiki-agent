---
title: "Decoder Lock-In"
type: concept
tags: [modeling, action-decoding, transfer-learning]
last_updated: 2026-09-02
---

## 정의

[[DecoderLockIn]]은 [[VisionLanguageAction]] 또는 유사한 다중 모달 정책에서, 단일 action head가 latent 표현을 과도하게 독점적으로 최적화해 다른 action 표현 방식으로의 일반화가 약해지는 현상이다.

## 동작 메커니즘

동일한 latent $z$에 대해 head가 하나만 강하게 맞춰질 때 다른 head가 같은 표현 공간을 활용하기 어렵고, 결국 특정 parameterization에 대한 의존성이 생긴다.

## VLAct 문맥에서의 완화

[[VLAct]]은 [[OFT]], [[PI]], [[GR00T]] 같은 다중 continuous action head를 함께 학습해 단일 head 집중을 완화한다.

## 관련 연결

- [[ActionHead]]
- [[ActionSpaceAlignment]]
- [[RepresentationLearning]]
- [[ContinuedPretraining]]
