---
title: "Half Precision"
type: concept
tags:
  - FloatingPoint
  - Precision
  - CUDA
  - TensorCore
sources:
  - introduction-to-tensor-cores-programming
last_updated: 2026-05-03
---

## Summary
[[HalfPrecision]]는 보통 16-bit 부동소수점 정밀도로, 메모리 점유를 크게 줄이고 처리량을 높이는 장점을 가진다. 비용이 큰 AI 연산에서는 성능 향상을 위해 널리 사용되며, 텐서 코어와 결합 시 유효성이 크다.

## Key Claims
- 입력 정밀도를 줄이면 메모리 대역폭과 저장 부담이 낮아진다.
- 오차 축적으로 인한 수치 안정성 한계가 있으므로 누산/출력 단계의 정밀도 조합이 중요하다.
- 텐서 코어 워크플로우에서 [[FP16]] 입력 + [[SinglePrecision]] 누산 조합이 실무적으로 많이 사용된다.

## Connections
- [[SinglePrecision]] — 입력 대비 정밀도 보완 포인트.
- [[TensorCores]] — [[FP16]] 입력에서 활용도가 높음.
- [[WMMA]] — 구현 시 텐서 정밀도 지정 항목으로 필수.

## Notes
[[HalfPrecision]]은 속도와 정확도의 절충점이므로 데이터 분포와 연산 안정성 기준을 함께 고려해야 한다.