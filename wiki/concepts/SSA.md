---
title: "SSA"
type: concept
tags:
  - Compiler
sources: []
last_updated: 2026-05-10
---

## Summary
[[SSA]](Static Single Assignment)는 각 값이 정확히 한 번 정의되는 것을 원칙으로 하는 IR 형식이다.

## Key Points
- [[LLVM]]는 SSA 형식을 오랫동안 사용해왔고, [[MLIR]]은 이를 일반화해 영역/타입/속성 모델과 결합했다.
- 조건 분기/제어흐름 처리에서 phi-node와 유사한 표현 전략이 설계 비용과 구현 복잡도에 영향을 준다.
- MLIR의 다른 표현 장치(예: 다중 값 모델)와 LLVM 변환 간 경계에서 설계 판단이 발생한다.

## Connections
- [[LLVM]]
- [[MLIR]]
- [[Phi nodes]]

## Note
- 본 소스는 LLVM의 phi-node 개념이 MLIR의 블록 변환 전략에서 비용 이슈를 유발했을 수 있다고 분석한다.