---
title: "Packetless Routing"
type: concept
tags:
  - networking
  - inference
  - routing
  - performance
last_updated: 2026-05-03
sources:
  - hotchips34-groq-abts-final-pdf
---

## 개요
Packetless Routing은 텐서 단위를 라우트 대상으로 취급해 전통적인 패킷 헤더 중심 통신보다 낮은 제어 오버헤드와 결정론적 처리 경로를 노리는 네트워크 스케줄링 방식이다.

## 특성
- 고정 텐서 단위(예: 320B) 교환을 전제로 헤더/테일 오버헤드를 축소.
- 하드웨어 흐름 제어 플래그를 최소화해 성능 변동을 낮춤.
- 소프트웨어 제어 트래픽 패턴 기반으로 경로 분산을 관리.

## TSP 연계
본 소스에서 [[RealScale]]/C2C 구성은 패킷 중심이 아닌 텐서 중심 라우팅으로 부하 분산·지연 편차를 개선한다.

## 연결
- [[SoftwareDefinedNetworking]]
- [[C2C]]
- [[DragonflyTopology]]
- [[DeterministicExecution]]