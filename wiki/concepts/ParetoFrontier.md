---
title: "Pareto Frontier"
type: concept
tags: [optimization, multi-objective]
sources: [flow-erd-2607-06957]
last_updated: 2026-07-15
---

## Overview
Pareto frontier는 multiple objectives(Realism vs Diversity)를 동시에 최적화할 때, 한 objective를 희생하지 않고 다른 objective를 개선할 수 없는 점들의 집합입니다.

## Realism-Diversity Trade-off
- 기존 방법들은 realism과 diversity 중 하나만 최적화
- Flow-ERD는 AFM + ERD로 Pareto frontier를 개선(지배)
- "Low-diversity rollouts concentrate on a dominant behavior, whereas low-realism rollouts deviate from plausible traffic motion"

## Connections
- [[FlowERD]] — Pareto frontier 개선 달성
- [[MultiAgentSimulation]] — 핵심 trade-off
