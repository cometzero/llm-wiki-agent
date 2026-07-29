---
title: "ALOHA"
type: entity
tags: [dataset, manipulation, teleoperation, robotics, embodiment]
sources: ["data-pyramid-for-embodied-manipulation-2607-24744"]
last_updated: 2026-07-29
---

## Summary

[[ALOHA]]는 로봇 조작 데이터 수집에서 leader-follower teleoperation 방식으로 고품질 trajectory를 얻기 위한 대표 데이터셋/데이터 수집 계열이며, [[UMI]] 기반 수집과 함께 실로봇 조작 학습의 핵심 레퍼런스 축으로 쓰인다.

## Connections

- [[RealRobotData]] — 실세계 action grounding의 높은 정렬 신호를 제공하는 축
- [[UMI]] — 저비용/고규모 수집 파이프라인의 보완 축
- [[Xiaomi-Robotics-1]] — trajectory-scale 학습의 정렬 대상 데이터 계열
- [[CrossEmbodimentLearning]] — embodiment 간 전이 시 정렬 난이도를 가늠하는 사례

## Notes

- 본 소스에서 [[ALOHA]]는 [[DROID]]와 함께 고비용 real-robot 데이터의 분포 확대 및 정렬 기준을 설명하는 참고 레퍼런스로 언급됨.
