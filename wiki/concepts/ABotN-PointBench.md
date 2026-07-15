---
title: "ABotN-PointBench"
type: concept
tags: [benchmark, navigation, vlpn, point-goal]
sources: [abot-n1-2607-10383]
last_updated: 2026-07-15
---

## Definition
[[ABot-N1]]에서 새로 제안한 point-goal navigation 전용 벤치마크. LiDAR-inertial SLAM + 3DGS scene modeling으로 고품질 시뮬레이션 환경을 구축하고, traversability-aware query sampling과 ground-truth reference trajectory 생성으로 체계적으로 평가한다. hierarchical distance splits를 지원한다.

## Connections
- [[ABot-N1]] — 벤치마크 개발 주체
- [[ABotN-POIBench]] — 함께 제안된 POI-goal 벤치마크
- [[VLN-CE]] — 기존 연속 환경 VLN 벤치마크
