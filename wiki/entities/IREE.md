---
title: "IREE"
type: entity
tags:
  - compiler
  - ML
  - accelerator
  - MLIR
sources:
  - npu-v0-1-hw-architecture
last_updated: 2026-05-03
---

## 개요
[[IREE]]는 [[AOT]] 방식으로 커널 실행 이미지를 생성하는 컴파일 체계로, 이 문서에서 [[NPUv01]]의 kernel code 전달 경로로 언급된다.

## 이 문서에서의 역할
- source model: [[MLIR]] 기반 오프라인 컴파일 아티팩트(`ELF kernel`) 생성
- execution model: host에서 doorbell launch로 kernel dispatch

## 연관 링크
- [[MLIR]], [[NPUv01]], [[IngestionFlow]], [[AOT]], [[RVV]]
