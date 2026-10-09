---
title: "Rust Native GPU Target"
type: concept
tags: [rust, gpu, runtime, experimental]
sources: [lwn-weekly-edition-2026-10-01-1096293]
last_updated: 2026-10-09
---

## Summary

Christian Legnitto의 RustConf 2026 구상은 GPU API를 Rust wrapper로 노출하기보다 Rust의 기존 semantics를 유지하면서 GPU를 일반 compile target으로 만드는 것이다. GPU가 지원하지 않는 작업은 host CPU에 위임하고, GPU kernel launch·warp·lane을 각각 process·thread·SIMD와 연결한다.

## Trade-offs

- 기존 library의 재사용과 점진적인 concurrency 도입을 목표로 한다.
- 초기 busy waiting, host delegation, 큰 binary, 하드웨어 특화 최적화의 제약이 생길 수 있다.
- 공개 준비 중인 prototype 단계의 제안이며 수작업 CUDA 수준 성능은 실측 결론이 아니다. CPU/GPU execution·memory·latency contract를 따로 검증해야 한다.

## Connections

- [[Rust]] — language semantics를 hardware 실행 모델에 매핑.
- [[lwn-weekly-edition-2026-10-01-1096293]] — native GPU 지원 특집의 번역과 해설.
