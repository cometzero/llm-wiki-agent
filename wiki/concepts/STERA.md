---
title: "STERA"
type: concept
tags: [infrastructure, data-processing, VLA]
sources: [mobileego-anywhere-2605-05945]
last_updated: 2026-05-20
---

## Definition
[[mobileego-anywhere-2605-05945]]에서 공개하는 open infrastructure 이름. Raw mobile capture(MCAP format)를 VLA/foundation model 학습 가능한 표준 포맷으로 변환하는 Python processing suite.

## Processing Pipeline
```
MCAP raw log → STERA Python processing
                        ↓
              ├── 3D hand trajectories (world frame)
              ├── Atomic action labels
              └── Hierarchical instruction tree
                        ↓
               VLA / foundation model pretraining
```

## Key Features
- ARKit sensor fusion: RGB-D + IMU + 6-DoF pose timestamp synchronization
- 3D hand trajectory: 2D keypoint를 depth로 unproject → camera pose로 global frame에 정렬
- Hierarchical instruction: atomic span → episode → sub-goal → session 4단계 구조
- Open source + mobile app 공개

## Connections
- [[mobileego-anywhere-2605-05945]] — infrastructure 제안자
- [[VLA]] — 주요 downstream target
- [[WiLoR]] — hand estimation에 사용
- [[ARKit]] — sensor fusion 소스
