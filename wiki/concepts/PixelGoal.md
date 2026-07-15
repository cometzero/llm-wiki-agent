---
title: "Pixel Goal"
type: concept
tags: [visual-navigation, intermediate-representation, action-grounding]
sources: [abot-n1-2607-10383-learning]
last_updated: 2026-07-15
---

## Definition
이미지 공간에서 다음 이동 목표를 지정하는 anchor point. VLM이 직접 action을 출력하는 대신 pixel coordinate로 목표 위치를 지정한다.

## Key Properties
- **Task-agnostic**: 여러 navigation task(point/object/POI/instruction/person-following)를 통합
- **Compact interface**: fast controller가 높은 주기로 실행 가능한 waypoint 생성
- **Action grounding bridge**: [[SlowFastArchitecture]]의 slow→fast 변환 매개체

## Related Concepts
- [[WaypointNavigation]]: pixel goal에서 생성되는 연속 공간의 중간 목표
- [[ActionGrounding]]: pixel goal이 해결하는 핵심 문제
- [[ABot-N1]]: pixel goal을 intermediate representation으로 사용
- [[LMDrive]]: similar waypoint-based navigation approach

## Connections to Existing Concepts
- [[VisualThink-VLA]]: visual intermediate reasoning과 유사한 philosophy
- [[RoboSemanticBench]]: semantic grounding 문제와 관련
