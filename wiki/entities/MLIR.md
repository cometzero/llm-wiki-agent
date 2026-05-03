---
title: "MLIR"
type: entity
tags:
  - compiler
  - IR
  - LLVM
  - accelerator
sources:
  - npu-v0-1-hw-architecture
last_updated: 2026-05-03
---

## 개요
[[MLIR]]은 다단계 변환 가능한 중간표현 계층으로, 본 문서에서는 [[IREE]] 기반의 AOT pipeline에서 NPU kernel ELF 산출의 전단으로 언급된다.

## 이 문서에서의 역할
- NPU 타일용 커널을 컴파일 타임에 구조화
- runtime에서 queue-less launch를 전제로 하는 정적/컴파일러 스케줄링 지원

## 연관 링크
- [[IREE]], [[NPUv01]], [[AOT]], [[Compiler]], [[RVV]]
