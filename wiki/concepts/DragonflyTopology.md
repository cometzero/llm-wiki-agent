---
title: "Dragonfly Topology"
type: concept
tags:
  - networking
  - topology
  - ai-infrastructure
  - scalability
last_updated: 2026-05-03
sources:
  - hotchips34-groq-abts-final-pdf
---

## 개요
Dragonfly Topology는 적은 홉 수와 높은 경로 다양성을 동시에 제공하도록 설계된 확장형 네트워크 토폴로지 패턴이다.

## TSP 적용 포인트
- [[Groq]]의 시스템 스케일 구성에서 그룹 단위 라우팅과 비최소 경로 라우팅을 활용해 다중 경로 대역폭을 확보.
- 네트워크 직경 저하를 통해 통신 지연을 줄이고 결정론적 스케줄링을 지원.
- 소프트웨어 스케줄링 네트워크와 결합될 때 하드웨어 동적 중재 비의존 동작에 유리.

## 연결
- [[PacketlessRouting]]
- [[SoftwareDefinedNetworking]]
- [[RealScale]]
- [[DeterministicExecution]]
- [[Groq]]