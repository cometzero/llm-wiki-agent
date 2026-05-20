---
title: "RL Alignment for Diffusion Models"
type: concept
tags: [reinforcement-learning, diffusion, policy-gradient, autonomous-driving]
sources: ["reflectdrive-2-2605-04647"]
last_updated: 2026-05-13
---

# RL Alignment for Diffusion Models

[[RLAlignment]]는 [[ReflectDrive2]]에서 사용하는 기법으로, draft-and-edit rollout 전체에 terminal reward를 부여하여 policy를 최적화한다.

## 핵심 통찰
Supervised perturbation recovery만으로는 self-editing gain이 작다. Editor 자체의 존재보다 reward-coupled rollout이 중요하다.

## 방법론
- 각 scene에서 여러 goal과 draft를 sampling
- 최종 post-edit trajectory에 closed-loop planning score를 terminal reward로 부여
- Group-relative advantage 계산
- Drafting phase의 unmasking transition과 AutoEdit phase의 rewrite transition 모두에 policy-gradient credit 적용

## 기존 연구와의 차이
- [[DDPO]]/[[DPPO]]: continuous diffusion를 multi-step MDP로 보고 policy gradient 적용
- Discrete diffusion 관련 선행 연구들은 step-aware gradient와 group-relative advantage를 다룬다. 대표 키워드는 [[SPG]] 등이다.
- ReflectDrive-2는 단일 diffusion rollout이 아니라 `draft → AutoEdit`로 구성된 composed rollout 전체에 terminal reward 부여

## Connections
- [[ReflectDrive2]] — 적용 대상
- [[PolicyGradient]] — 기본 학습 방법론
- [[GroupRelativeAdvantage]] — Advantage 계산 방식
