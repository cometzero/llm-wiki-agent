---
title: "Software Defined Hardware"
type: concept
tags:
  - architecture
  - systems
  - compiler
  - ai-inference
last_updated: 2026-05-03
sources:
  - hotchips34-groq-abts-final-pdf
---

## 개요
Software Defined Hardware([[SoftwareDefinedHardware]])는 하드웨어 구현을 고정된 마이크로아키텍처 동작으로 두기보다, 소프트웨어(컴파일러·런타임)가 실행 타이밍, 메모리 노출, 명령어 스케줄, 라우팅 정책을 더 직접적으로 제어하도록 설계한 방식이다.

## 설계 원칙
- 정적 분석 가능성 강화: 실행 전 컴파일러가 자원 상태를 완전 파악.
- 동적 제어 분리: 런타임은 정해진 제약 내에서 동작 스케줄만 수행.
- 메모리 계층의 평면화: 캐시/재정렬 요소를 줄이고 소프트웨어에 주소·레이스/순서를 노출.
- 인터페이스 단순성: 동작 예측에 필요한 신호를 하드웨어보다 소프트웨어가 보완.

## TSP와의 정합성
[[hotchips34-groq-abts-final-pdf]]는 TSP에서 이 모델을 통해 [[DeterministicExecution]]을 구현한다. 특히 [[StreamedRegisterFile|스트림 레지스터 파일]]와 평면 SRAM 모델을 결합해 결정론적 동기화 비용을 낮춘다.

## 연결
- [[StreamingTensorProcessor]]
- [[DeterministicExecution]]
- [[CompilerBasedInstructionScheduling]]
- [[SoftwareControlledMemory]]
- [[AIInfrastructure]]