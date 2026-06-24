---
title: "Vision-Language-Action Models"
type: concept
tags: [vla, multimodal, robotics, autonomous-driving]
sources: [world-action-models-survey-2606-20781]
last_updated: 2026-06-24
---

## Summary
VLA(Vision-Language-Action Models)는 vision과 language context를 executable action으로 직접 변환하는 multimodal model이다. WAM survey는 VLA를 "현재에서 바로 action을 예측하는 policy"로 정의하고, [[WorldActionModel]]은 그 사이에 action-facing future를 삽입하는 계열로 구분한다.

## Key Distinctions
- **VLA**: vision/language context → executable action (현재 상태에서 직접 예측)
- **WAM**: vision/language context → action-facing future prediction → action (future 예측을 사이에 둠)
- 핵심 질문: simple visual prediction benchmark는 control utility를 보장하는가?

## Related Concepts
- [[WorldActionModel]] — VLA와 대비되는 action-facing predictive model
- [[VideoWorldModels|Video World Models]] — realistic future를 생성하지만 action path 연결 필요
- [[SemanticGrounding]] — VLA의 언어적 타겟 선택 능력 문제
- [[VisualReasoning]] — VLA의 visual intermediate reasoning
- [[Latent World Models]] — pixel rendering 생략으로 latency 감소
- [[Model-Predictive Control]] — candidate action rollout과 future utility 비교

## Connections to Entities
- [[VisualThink-VLA]], [[TBD-VLA]], [[ReflectDrive]] — 다양한 VLA action generation 방식
- [[OpenVLA]], [[GR00T]] — 주요 VLA 백본
- [[VLA4AD]] — VLA taxonomy survey
