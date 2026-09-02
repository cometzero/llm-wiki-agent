---
title: "OFT"
type: concept
tags: [VLA, continuous-action]
sources: [vlact-2608-27550-paper-ko, vlact-2608-27550-analysis]
last_updated: 2026-09-02
---

# OFT

OFT는 VLA backbone의 action query token에서 continuous action chunk를 병렬 회귀하는 action head 계열이다. One-shot inference가 가능한 장점이 있으나 multimodal action distribution을 직접 생성하는 flow/diffusion head와는 다른 trade-off를 갖는다. [[VLAct]]는 OFT를 [[PI]], [[GR00T]]와 함께 multi-head supervision에 사용한다.
