---
title: "DriveDreamer-Policy"
type: entity
tags:
  - geometry
  - world-action-model
  - unified-planning
sources:
  - simwam-2608-07468-references
last_updated: 2026-08-12
---

## 개요
[[DriveDreamer-Policy]]는 geometry-grounded 생성과 planning을 통합하는 WAM형 접근으로 언급되는 연구군이다.

## 핵심 연결
- [[SimWAM]] 대비, 추론 시 video 출력을 남기는 통합 방식과의 대비군으로 중요.
- unified generation/planning 강점과 deployment 비용의 trade-off 분석 포인트를 제공한다.

## 관계
- [[SimWAM]]: 학습/배포 분리 대비의 반대 편향으로, 통합 전략의 강점과 비용 구조를 비교.
- [[WorldActionModel]], WorldActionModels are Zero-shot Policies 주변 연구군과 인접.

## 관련 개념
- [[InferenceTimeActionOnlyDeployment]]
- [[FlowMatching]]
- GeometryGrounding
