---
title: "Streaming Tensor Processor"
type: concept
tags:
  - architecture
  - hardware
  - llm
  - inference
  - compiler
last_updated: 2026-05-03
sources:
  - hotchips34-groq-abts-final-pdf
---

## 개요
Streaming Tensor Processor([[StreamingTensorProcessor]])는 텐서 연산을 스트리밍 데이터 경로로 처리하면서, 소프트웨어가 하드웨어 자원 배치·명령어 발행·동기화를 직접 통제하는 결정론적 AI 추론 아키텍처 패턴이다.

## 핵심 속성
- **소프트웨어 정의 하드웨어**: 명령어 발행·메모리 할당·라우팅을 소프트웨어 제어.
- **결정론 우선 설계**: 메모리 재정렬/동적 중재를 줄여 실행 예측성을 높임.
- **기능 분할**: [[ICU]], [[MXM]], [[VXM]], [[SXM]], [[MEM]]의 전문화된 역할 분리.
- **ISA/컴파일러 결합**: [[MLIR]] 및 정적 스케줄링 기반으로 정확한 타이밍 제어.

## 성능·신뢰성 함의
- 배치-1 추론, 짧은 응답 시간, 사용자 체감 지연 개선에 유리한 설계 철학.
- 멀티칩 규모에서는 소프트웨어 스케줄링, 글로벌 동기화 카운터, C2C 링크 제어가 성능 일관성의 핵심 요인.
- 예측 불가한 적응형 라우팅, 하드웨어 중재를 줄임으로써 오버헤드를 통제.

## 연결
- [[SoftwareDefinedHardware]]
- [[DeterministicExecution]]
- [[CompilerBasedInstructionScheduling]]
- [[SoftwaeDefinedNetworking]]
- [[RealScale]]