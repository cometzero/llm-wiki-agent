---
title: "XLA"
type: entity
tags: [AI, Compiler, TensorFlow, Accelerator]
last_updated: 2026-05-10
sources: [hc2022-google-pienaar-v1-pdf]
---

## 개요
[[XLA]]는 [[TensorFlow]] 계열의 도메인 특화 컴파일러/최적화 프레임워크로, 모델 그래프를 하드웨어 친화 형태로 변환하는 데 초점을 둔다.

## MLIR과의 연결
- 본 소스는 [[XLA]]가 기존의 도메인 특화 IR 패턴의 한 예시로, 타 생태계에서도 반복되는 재구현 비용 문제의 대상이 될 수 있음을 암시한다.
- [[MLIR]]의 도입은 [[XLA]]와 같은 스택에서 공통 분석/변환 인프라를 재사용하는 방향의 후보로 제시된다.

## 관련 링크
- [[MLIR]]
- [[TensorFlow]]
- [[TensorRT]]
- [[LLVM]]
- [[Dialect]]