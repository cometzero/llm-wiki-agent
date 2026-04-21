---
title: "RiscV"
type: concept
tags: [architecture, ISA, open-source, ai]
sources: [understanding-the-risc-v-extensions-for-ai-john-simpson-sifive]
last_updated: 2026-04-20
---

## Definition
[[RiscV]]는 오픈 ISA 계열로, AI 워크로드 대응을 위해 매트릭스 가속, 데이터 타입 확장, 벡터/행렬 결합 경로를 확장하려는 제안이 활발하다.

## Key points from source
- AI의 급성장으로 행렬 연산이 병목이 되면서 ISA 수준의 경량 확장이 아닌, 워크로드 특성별 다층 확장이 필요해졌다.
- [[RiscVVector]]의 기본성은 유지되며, layer norm/softmax 같은 비행렬 연산을 소화해야 하므로 완전 대체가 아니라 보완 관계가 성립한다.
- 엣지와 데이터센터는 하드웨어 크기·배치 크기·대역폭 특성이 달라 서로 다른 확장 방식이 더 적합할 수 있다.
- 컴파일러 체인(LLVM/GCC) 연동은 실제 도입 가능성과 생태계 확산의 핵심 실무 조건이다.

## Related pages
- [[RiscVExtensionsForAI]]
- [[RiscVExtensionsForAI#VectorBatchProduct]]
- [[FP8]]
- [[RiscVVector]]
- [[SiFive]]
