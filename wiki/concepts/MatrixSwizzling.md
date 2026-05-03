---
title: "Swizzling"
type: concept
tags:
  - SharedMemory
  - BankConflict
  - MatrixLayout
  - Performance
  - Blackwell
last_updated: 2026-05-03
sources:
  - modular-matrix-multiplication-on-blackwell-part-2-using-hardware-features-to-optimize-matmul
---

## 정의
[[Swizzling]]는 공유 메모리 인덱스/배치 규칙을 비트 조작(XOR 등)으로 뒤섞어, 동일 워프 내 스레드 접근이 같은 뱅크로 집중되는 현상을 완화하는 레이아웃 변형 기법이다.

## 왜 중요한가
행렬 곱셈에서 코어 행렬이 동일 뱅크에 집중되면 [[SharedMemoryBankConflict|Bank Conflict]]가 발생해 실행이 직렬화된다. 스위즐링은 이러한 충돌을 분산시켜 처리량을 회복한다.

## 실무 예시
- 128B 스위즐 패턴은 8행×16B 폭×8청크의 방식으로 블록 내 요소를 서로 다른 뱅크에 분포시키는 방식으로 설명된다.
- 커널 3에서 성능 향상의 중심 동력으로 제시되며, 나이브 대비 성능을 크게 끌어올리는 데 기여한다.

## 한계
- 완전한 성능 회복은 계산-메모리 오버랩이 완료되지 않으면 여전히 제한될 수 있다.

## 연결
- [[SharedMemory]]
- [[SharedMemoryBankConflict]]
- [[Blackwell]]
- [[Tcgen05MMA]]
- [[MatrixMultiplication]]
