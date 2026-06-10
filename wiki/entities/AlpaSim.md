---
title: "AlpaSim"
type: entity
tags: [simulator, autonomous-driving, NVIDIA]
sources: [nvidia-omnidreams-2606-03159, nvidia-omnidreams-2606-03159-learning]
last_updated: 2026-06-10
---

## Overview
NVIDIA의 autonomous driving simulator로, OmniDreams의 deployment 환경으로 활용된다.

## Details
- closed-loop evaluation을 위한 sensor simulation 플랫폼
- [[OmniDreams]]의 generated observation을 받아 policy action을 생성하는 루프
- policy-induced future scenario 생성이 가능

## Connections
- [[OmniDreams]]-generated observation → [[Alpamayo]] policy → AlpaSim → 다음 observation
- [[WorldActionModel]] 기반 policy evaluation 환경
