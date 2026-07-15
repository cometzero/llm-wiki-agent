---
title: "WOSAC"
type: entity
tags: [benchmark, traffic-simulation, evaluation]
sources: [flow-erd-2607-06957]
last_updated: 2026-07-15
---

# WOSAC

## Overview
WOSAC은 traffic simulation의 realism과 diversity를 동시에 평가하는 benchmark로, Flow-ERD에서 realism metric으로 사용된다. Realism-diversity Pareto frontier 측정의 기준점이 된다.

## Key Characteristics
- **Realism metrics**: 생성된 traffic behavior의 물리적/시맨틱 사실성 평가
- **Log-free diversity**: likelihood-free한 다양성 측정 방식으로 실제 분포 가정 없음
- **Pareto frontier analysis**: realism-diversity trade-off를 frontier 곡선으로 시각화

## Connections
- [[FlowERD]] — WOSAC benchmark의 realism/diversity metrics 사용
- [[VLA]] evaluation — VLA policy의 closed-loop robustness 평가에 활용 가능
