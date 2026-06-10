---
title: "WorldScenarioMap"
type: concept
tags: [simulation, condition, structured-representation]
sources: [nvidia-omnidreams-2606-03159, nvidia-omnidreams-2606-03159-learning]
last_updated: 2026-06-10
---

## Overview
World-scenario map은 lane, traffic light, actor box, ego/action state를 rendering한 structured condition으로, photorealistic generation과 controllable simulation을 연결한다.

## 구성 요소
- **HD map**: lane geometry, road structure
- **3D actor boxes**: dynamic objects (vehicles, pedestrians)
- **Ego trajectory/action**: 자체 차량의 위치와 행동
- **Text prompt**: VLM caption으로 생성된 weather/time/traffic condition

## 수학적 표현

```text
world condition = HD map + dynamic actor boxes + ego trajectory/action + text prompt
```

## 중요성
- **geometry/action condition**: scene structure를 제어
- **text prompt**: weather/lighting/time 등 appearance factor를 제어
- world-scenario map이 부정확하면 generated observation이 그럴듯해도 policy evaluation은 왜곡됨

## Connections
- [[OmniDreams]]의 condition branch 입력으로 사용
- [[WorldActionModel]]과 결합하여 simulator state/action에 반응하는 generation 가능
- [[AlpaSim]]과 [[OmniDreams]] 사이의 인터페이스 역할
