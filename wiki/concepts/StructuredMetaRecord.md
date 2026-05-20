---
title: "Structured Meta-Record"
type: concept
tags: [data-representation, egocentric-video, physical-commonsense]
sources: [physbrain-1-0-2605-15298, physbrain-1-0-2605-15298-learning, physbrain-1-0-2605-15298-analysis]
last_updated: 2026-05-20
---

## Definition
Raw human egocentric video를 JSON-like schema로 변환한 중간 physical record representation.

## Components
1. **scene_elements**: object, material, geometry, state
2. **spatial_dynamics**: initial layout, relation changes, depth ordering
3. **action_execution**: local manipulation, sub-action order, task objective
4. **depth_aware_relations**: depth 기반 공간 관계

## Purpose
- Raw video/caption은 [[PhysicalCommonsense]]와 action order를 충분히 표현하지 못함
- Structured format으로 physical factor를 명시적으로 표현
- [[PhysicalQA]] 생성의 기반이 됨

## Validation Importance
Schema validation 없이 바로 caption-to-QA를 만들면 hallucination이 policy supervision으로 굳을 수 있다.

## Related Concepts
- [[PhysicalCommonsense]] — 추출 대상
- [[PhysicalQA]] — 변환 출력
- [[Ego4D]] — source dataset
