---
title: "RealScale"
type: entity
tags:
  - interconnect
  - chip-to-chip
  - networking
  - ai-infrastructure
last_updated: 2026-05-03
sources:
  - hotchips34-groq-abts-final-pdf
---

## 개요
[[RealScale]]는 [[Groq]]에서 제시한 칩-투-칩(C2C) 및 시스템 확장 흐름의 통합명을 가리키며, 분산 환경에서 TSP 간 통신을 단순화하고 흐름 제어를 소프트웨어/ISA로 정합시키는 접근이다.

## 주요 포인트
- 기존 RDMA 대비 구조 단순화를 지향하고, 전역 SRAM 접근 모델을 논리적으로 공유해 통신 경로를 정리.
- 분산 DRAM 배치와 직접 C2C 링크를 통해 멀티 TSP 확장성을 높이고, 동기화 비용을 제어.
- 결정론 유지 관점에서 흐름 제어와 링크 지연 추정 정보를 실행 제어로 반영.

## 연결
- [[C2C]]
- [[SoftwareDefinedNetworking]]
- [[PacketlessRouting]]
- [[DeterministicExecution]]
- [[DragonflyTopology]]