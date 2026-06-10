---
title: "WorldActionModel"
type: concept
tags: [autonomous-driving, policy, world-model, architecture]
sources: [nvidia-omnidreams-2606-03159, nvidia-omnidreams-2606-03159-learning]
last_updated: 2026-06-10
---

## Overview
World-Action Model (WAM)은 world dynamics representation과 action을 함께 다루는 policy model architecture로, [[VLA]]와 대비된다.

## Details
- **핵심 차이점**: VLA가 language reasoning에 중점을 두는 반면, WAM은 dynamics-aware representation에 집중
- **driving 분야 함의**: language reasoning보다 world dynamics prediction이 action quality에 더 직접적일 수 있음
- [[Alpamayo]]가 WAM architecture를 따르는 policy model

## WAM vs VLA 비교

| Aspect | [[VLA]] | [[WorldActionModel]] |
|--------|---------|----------------------|
| Focus | Language reasoning | World dynamics |
| Representation | Semantic, linguistic | Geometric, physical |
| Application | General robot control | Driving-specific |
| Latency | Higher (CoT overhead) | Lower (direct dynamics) |

## Connections
- [[VLA]]와 대비되는 autonomous driving policy architecture
- [[OmniDreams]]의 deployment에서 [[Alpamayo]] policy로 사용
- [[AlpaSim]] closed-loop simulation의 핵심 구성 요소
