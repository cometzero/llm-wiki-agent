---
title: "Closed-Loop Reward"
type: concept
tags: [reinforcement-learning, reward-design, autonomous-driving]
sources: [reflectdrive-2-2605-04647-analysis]
last_updated: 2026-05-13
---

## Overview
Closed-loop reward는 환경과의 상호작용을 통해 산출된 terminal reward를 policy 학습에 사용하는 RL 접근법이다.

## ReflectDrive-2에서의 적용
- Draft/edit composed rollout 전체에 PDMS reward 적용
- Policy-gradient credit assignment로 draft와 edit 모듈 jointly 학습
- Open-loop imitation loss 대비 closed-loop planning score 사용

## Limitations
- Reward는 benchmark proxy (PDMS)
- 실제 도로 safety case와 동일하지 않음
- Real-world safety 보장 불가

## Connections
- [[ReflectDrive2]] — RL fine-tuning 방식
- [[DecisionDraftReflectPipeline]] — pipeline training
- [[NAVSIM]] — benchmark metric source
