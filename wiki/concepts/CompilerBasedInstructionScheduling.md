---
title: "Compiler-Based Instruction Scheduling"
type: concept
tags:
  - compiler
  - scheduling
  - inference
  - deterministic
last_updated: 2026-05-03
sources:
  - hotchips34-groq-abts-final-pdf
---

## 개요
Compiler-Based Instruction Scheduling은 실행 성능을 런타임 예측성에 맞춰 하드웨어가 아닌 컴파일러가 명령어 발행 시퀀스를 정밀 제어하는 방식이다.

## TSP 관점 핵심
- [[ICU]] 단위로 사이클 단위 명령어 발행.
- 기능 유닛별 고정 실행 지연을 가정해 타이밍 예측을 강화.
- [[SYNC]]·[[NOTIFY]]·트래픽 패턴 기반 라우팅을 통해 결정론적 통신을 유지.

## 의미
- 동적 적응형 라우터 의존도를 줄이고 처리 경로의 분기성을 낮춰 지연 편차 감소.
- 추론 워크로드에서 특히 배치-1 응답의 분산을 줄이는 데 유리.

## 연결
- [[DeterministicExecution]]
- [[SoftwareDefinedHardware]]
- [[PacketlessRouting]]
- [[DragonflyTopology]]