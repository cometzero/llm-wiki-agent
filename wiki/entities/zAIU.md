---
title: "zAIU"
type: entity
tags: [ibm, accelerator, onnx, inference]
sources: ["le-onnx-pdf"]
last_updated: 2026-04-20
---

## Summary
[[zAIU]](IBM zAIU, 또는 IBM Mainframe AI Unit)는 IBM Z 기반 메인프레임용 온칩 AI 가속기로, [[ONNX-MLIR]]에서 고성능 추론 경로로 지원되는 대상 하드웨어다.

## Key Facts
- [[IBM]] [[Telum]] 계열 메인프레임에 탑재되어 고속 실시간 추론을 목표로 한다.
- [[zDNN]] API에 정렬된 연산 인터페이스를 통해 매트릭스 연산 기반 워크로드를 처리한다.
- [[ONNX-MLIR]]은 zAIU를 위해 [[zHigh]]/[[zLow]] 다이얼렉트 계열과 [[zTensor]] 표현을 사용해 메모리·레이아웃을 반영한 하향 경로를 제공한다.

## Connections
- [[ONNX-MLIR]], [[IBM]], [[Telum]], [[zDNN]], [[IBMZ]], [[ONNX]], [[MLIR]]