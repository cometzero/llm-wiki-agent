---
title: "Tensor Memory Accelerator"
type: concept
tags:
  - Blackwell
  - GPU
  - AsyncCopy
  - SharedMemory
  - Performance
last_updated: 2026-05-03
sources:
  - modular-matrix-multiplication-on-blackwell-part-2-using-hardware-features-to-optimize-matmul
---

## 정의
[[TensorMemoryAccelerator]](TMA)는 GMEM↔SMEM 간 데이터를 비동기적으로 이동시키는 하드웨어 유닛/경로로, GPU 메모리 계층 접근의 대기 시간을 줄이고 커널 단계 동기화를 명시적으로 설계하게 한다.

## 핵심 역할
- 타일 기반 입력 로딩과 저장을 별도 경로로 오버랩 가능하게 만든다.
- 동시 실행에서 필요한 경우 `mbar`/배리어 단계 동기화로 코어-쓰레드 진행을 제어한다.
- Blackwell 최적화 맥락에서 [[Tcgen05MMA]] 파이프라인 시작 전/후 데이터 가용성을 보장한다.

## 실무 포인트
- 블록당 타일 크기(BMxBK, BNxBK)와 바이트 수를 정확히 추정해 `expect_bytes` 형태로 배리어를 초기화해야 한다.
- 실제 진행 제어는 `tma_phase` 같은 단계 토글과 병렬 반복 스케줄과 결합될 때 효과가 크다.
- TMA store는 `fence`와 `commit_group`/`wait_group`로 후속 저장 흐름을 제어한다.

## 연결
- [[Blackwell]]
- [[SharedMemory]]
- [[Swizzling]]
- [[Tcgen05MMA]]
- [[TMEM]]
