---
title: "GroqChip"
type: entity
tags:
  - chip
  - microarchitecture
  - nlp
  - llm
last_updated: 2026-05-03
sources:
  - hotchips34-groq-abts-final-pdf
---

## 개요
[[GroqChip]]은 [[Groq]]의 TSP 계열에서 사용되는 소프트웨어 정의/결정론형 칩 블록 집합으로, 대규모 병렬 연산과 정적 제어 가능한 데이터 흐름을 기반으로 동작한다.

## 구조 요약
- [[VXM]] 유닛, [[MXM]] 유닛, [[SXM]], [[MEM]], [[ICU]]를 분리 배치.
- 스트림 기반 데이터 플로우와 수평 데이터 흐름, 수직 명령어 처리의 조합을 강조.
- 대역폭 중심으로 온칩 메모리와 제어 버퍼를 노출해 컴파일러가 정확한 타이밍/위치 제어를 수행.

## 핵심 의의
- 단일 칩 최적화뿐 아니라 멀티칩·멀티노드 운영에서도 성능 예측성을 보장하기 위한 [[SoftwareDefinedHardware]]의 하드웨어 실체로 볼 수 있다.
- [[BERT]], [[GEMM]], [[Cholesky]], [[AllReduce]] 성능 분석의 시험대가 되는 아키텍처다.

## 연결
- [[StreamingTensorProcessor]]
- [[RealScale]]
- [[VLIW]]
- [[ISA]]
- [[Reliability]]