---
title: "ReflectDrive"
type: entity
tags: [autonomous-driving, VLA, diffusion, RL]
sources: [world-action-models-survey-2606-20781-analysis, reflectdrive-2-2605-04647]
last_updated: 2026-06-24
---

# ReflectDrive

이산 diffusion 기반 자율주행 trajectory planning 연구. Decision-Draft-Reflect 파이프라인으로 NAVSIM 91.0 PDMS 달성, NVIDIA Thor에서 ~30ms latency 구현. WAM 서베이에서 autonomous driving VLA planner 비교 기준으로 언급된다.

## 연결
- [[WorldActionModel]] — WAM 서베이의 비교 기준축 제공
- [[AutonomousDriving]] — 주요 적용 도메인
- [[VLAPlanner]] — autonomous driving VLA planning 연구
