---
title: "Model-Predictive Control"
type: concept
tags: [control-theory, planning, world-model]
sources: [world-action-models-survey-2606-20781]
last_updated: 2026-06-24
---

## Summary
MPC(Model-Predictive Control)는 여러 candidate action을 rollout하고 future utility를 비교하는 classic planning 기법이다. WAM survey에서 action-scoring rollout 방식으로 인용되며, [[WorldActionModel]]은 learned predictive substrate를 사용해 이 과정을 vision-language foundation model 시대에 재해석한다.

## Key Relationship with WAM
- **Classic MPC**: analytical model 기반 candidate action 평가
- **WAM 기반**: learned predictive model(vision/language-conditioned) 기반 action scoring
- 핵심 연결: future prediction → candidate action utility 비교 → optimal action 선택

## Connections
- [[WorldActionModel]] — learned predictive substrate for action scoring
- [[Vision-Language-Action Models]] — VLA와 MPC의 결합 가능성
- [[Autonomous Driving]] — trajectory planning에서의 MPC 응용
