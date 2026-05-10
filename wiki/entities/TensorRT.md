---
title: "TensorRT"
type: entity
tags: [AI, Inference, Compiler, Runtime]
last_updated: 2026-05-10
sources: [hc2022-google-pienaar-v1-pdf]
---

## 개요
[[TensorRT]]는 NVIDIA 계열 추론 최적화 런타임/컴파일러 계열의 대표 사례로, 모델 변환과 런타임 최적화가 분리된 도메인별 스택의 전형이다.

## MLIR과의 연결
- 본 소스에서 도메인 특화 IR의 장단점을 논의할 때 [[TensorRT]]와 같은 전용 스택이 반복적으로 갖는 중복 구현 비용의 맥락이 언급된다.
- [[MLIR]]은 서로 다른 계층의 연산/타깃 최적화 경계를 통합해 비슷한 문제를 하나의 구조로 다루는 대안으로 제시된다.

## 관련 링크
- [[MLIR]]
- [[NVIDIA]]
- [[Compiler]]
- [[Optimization]]
- [[Pass]]