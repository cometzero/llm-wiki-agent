---
title: "MonteCarloTreeSearch"
type: concept
tags: [Planning, Search, Autonomy]
sources:
  - tesla-s-shift-to-end-to-end-deep-learning-full-breakdown
last_updated: 2026-05-10
---

## Definition
[[MonteCarloTreeSearch]]는 상태-행동 후보를 트리 기반으로 샘플링·확장·평가해 최적 경로를 탐색하는 방법으로, 큰 분기 수를 확률적으로 정밀 탐색한다.

## In Tesla Context
2022년 [[Tesla]] 초기 설계에서는 [[Planning]]에 신경망 점수와 결합해 사용되었으며, 후보 궤적의 상대적 우위를 계산하는 데 쓰였다.

## Limitation
기존 규칙/휴리스틱 손실과 결합될 경우, 전체 파이프라인의 글로벌 최적화 관점에서 불연속이 발생할 수 있으므로 [[EndToEndDeepLearning]] 전환에서는 통합 학습 구조로 점차 대체 또는 축소되는 경향이 있다.
