---
title: "Shared Scratchpad Memory"
type: concept
tags:
  - memory
  - accelerator
  - architecture
sources:
  - npu-v0-1-hw-architecture
last_updated: 2026-05-03
---

## 정의
[[SharedScratchpadMemory]]는 cache가 아닌 compiler-managed local memory로, tile 내부의 harts/IME가 공유해 사용한다. v0.1에서는 2 MB/16-bank(128 KB per bank), 256-bit width, ECC(SECDED) 구성을 채택한다.

## 운영 규칙
- compiler-managed 주소 체계 사용
- bank group coloring으로 activation/weight/output/temp 분리 배치
- arbitration은 안전장치로 동작하되 primary 성능은 정적 배치에 의존

## 왜 중요한가
- predictability 중심 워크로드에서 메모리 액세스 패턴의 안정적 분할을 가능하게 하고, cache 충돌 불확실성을 줄인다.

## 연관 링크
- [[NPUv01]], [[TileBasedNPU]], [[Banking]], [[VectorRegisterFile]], [[BarrierSynchronization]]
