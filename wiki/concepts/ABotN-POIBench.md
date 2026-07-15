---
title: "ABotN-POIBench"
type: concept
tags: [benchmark, navigation, poi-goal]
sources: [abot-n1-2607-10383]
last_updated: 2026-07-15
---

## Definition
[[ABot-N1]]에서 새로 제안한 POI(Points of Interest)-goal navigation 벤치마크. Street-view 기반으로 POI arrival 성능을 평가하며, monocular depth 기반 지오메트릭 시드 어노테이션에서 distilled VLM(Qwen-3.5-4B)으로 31M→8M 유효 경로 필터링, positive/negative 샘플 쌍合成으로 missing-target 조건에서의 거부 능력을 테스트한다. ABot-N1은 이 벤치마크에서 POI arrival 77.3%(35.0%p 향상)를 달성했다.

## Connections
- [[ABot-N1]] — 벤치마크 개발 및 성능 보고 주체
- [[ABotN-PointBench]] — 함께 제안된 point-goal 벤치마크
- [[Qwen-3.5-4B]] — 데이터 필터링에 사용된 distilled VLM
