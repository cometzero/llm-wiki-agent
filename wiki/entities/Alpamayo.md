---
title: "Alpamayo"
type: entity
tags: [policy, autonomous-driving, NVIDIA, WAM]
sources: [nvidia-omnidreams-2606-03159, nvidia-omnidreams-2606-03159-learning]
last_updated: 2026-06-10
---

## Overview
NVIDIA의 WAM(World-Action Model) 기반 autonomous driving policy로, [[WorldActionModel]] architecture를 따르는 policy model이다.

## Details
- [[WorldActionModel]] backbone을 사용하는 end-to-end autonomous driving policy
- [[AlpaSim]] 환경에서 closed-loop evaluation 가능
- [[OmniDreams]]의 generated observation을 입력으로 받아 action 출력

## Connections
- [[AlpaSim]]과 [[OmniDreams]] 사이의 policy agent로 동작
- [[WorldActionModel]] architecture 기반
- [[VLA]]와 비교하여 world dynamics prediction에 집중
