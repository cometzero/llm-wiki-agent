---
title: "ExploreVLA"
type: entity
tags:
  - autonomous-driving
  - world-modeling
  - planning
sources:
  - simwam-2608-07468-references
last_updated: 2026-08-12
---

## 개요
[[ExploreVLA]]는 dense world modeling과 탐색을 결합한 end-to-end 자율주행 맥락의 VLA 계열로 정리되는 연구군이다.

## 핵심 연결
- [[SimWAM]]과 대비해 planning 경로에 world modeling을 어떻게 끼워넣는지를 보여주는 비교군.
- 언어 중심 VLA와 달리 numerical trajectory policy 중심으로 읽히며, deployment latency 관점에서 차별점이 크다.

## 관계
- [[SimWAM]]: world modeling 결합 정도와 inference 비용의 trade-off 비교군.
- [[ClosedLoopPlanning]], [[AutonomousDrivingVLA]] 비교 대상.

## 관련 개념
- [[WorldActionModel]]
- [[InferenceTimeActionOnlyDeployment]]
- [[FlowMatching]]
