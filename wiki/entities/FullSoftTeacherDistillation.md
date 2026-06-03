---
title: "FullSoft Teacher Distillation"
type: entity
tags: [training, distillation, vla]
sources: [visualthink-vla-2605-30011-ko-analysis]
last_updated: 2026-06-03
---

## Overview
FullSoft teacher distillation은 VisualThink-VLA의 training recipe에서 사용되는 knowledge distillation 기법이다. Teacher 모델의 soft probability 분포를 student 모델(VLA)에 전달하여 학습한다.

## Related Concepts
- [[VisualThinkVLA]] — 적용 시스템
- [[RouteSupervision]] — 함께 사용되는 training 기법
- [[CounterfactualUtility]] — dynamic loss 구성 요소
