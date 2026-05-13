---
title: "AutoEdit"
type: concept
tags: [self-correction, trajectory-editing, RL]
sources: [reflectdrive-2-2605-04647-analysis]
last_updated: 2026-05-13
---

## Overview
AutoEdit는 draft trajectory tokens를 입력으로 받아 token-to-token rewrite를 수행하는 self-correcting 모듈이다.

## Mechanism
- Draft trajectory의 각 token을 조건으로 다음 token 예측
- Longitudinal/lateral perturbation을 이용한 structure-aware supervision 적용
- Drivable-area field regularization 포함
- RL fine-tuning 후 gain이 증가하는 것이 관찰됨

## Safety Features
- Drivable area constraint enforcement
- Structure-aware correction (longitudinal/lateral axis)
- Multi-agent interaction failure(yield timing, cut-in response)는 추가 연구 필요

## Connections
- [[ReflectDrive2]] — integrated in
- [[DecisionDraftReflectPipeline]] — reflection stage
- [[ClosedLoopReward]] — training signal
