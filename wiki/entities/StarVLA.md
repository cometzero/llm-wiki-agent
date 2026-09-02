---
title: "StarVLA"
type: entity
tags: [robotics, vla, foundation-model]
last_updated: 2026-09-02
---

## 개요

[[StarVLA]]는 LEGO-like codebase 계열의 VLA 백본 실험 플랫폼으로, 지속 사전학습에서 모델 구조 자체보다 학습 레시피와 action supervision 설계가 성능 이동에 미치는 영향을 분석하는 기준점이다.

## 핵심

- [[VLAct]]의 reference chain에서 주요 초기 계보로 등장한다.
- multi-branch action recipe나 action-space 정렬 실험에서 baseline 설계 비교군으로 활용된다.
- 실험에서 데이터 스케일보다 representation drift 억제가 중요할 때 출발점이 되는 VLA 베이스라인 성격이 강하다.

## 연결

- [[StarVLA-Alpha]]
- [[VLAct]]
- [[VisionLanguageAction]]
- [[Qwen3VL]]
- [[ActionSpaceAlignment]]