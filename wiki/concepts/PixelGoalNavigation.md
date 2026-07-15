---
title: "Pixel Goal Navigation"
type: concept
tags: [navigation, pixel-goal, embodied-ai]
sources: [abot-n1-2607-10383]
last_updated: 2026-07-15
---

## Definition
Pixel goal navigation은 목표 위치를 이미지 공간의 픽셀 좌표로 지정하는 navigation paradigm이다. [[ABot-N1]]에서 slow vision-language reasoner가 생성한 pixel goal을 fast action expert가 소비하여 continuous waypoint를 출력한다. Point-goal navigation을 이미지로 표현하여 VLN-CE와 같은 continuous 환경에서의 ground-truth 좌표 어긋남 문제를 완화한다.

## Connections
- [[ABot-N1]] — Pixel goal navigation의 핵심 구현
- [[ABotN-PointBench]] — Pixel goal navigation 전용 벤치마크
- [[ABot-N0]] — 선행 pixel goal 관련 연구
- [[PointGoalNavigation]] — 기하학적 좌표 기반 point-goal과 대비
