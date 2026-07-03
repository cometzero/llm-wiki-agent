---
title: "BPF Coroutines"
type: concept
tags: [bpf, coroutine, kernel]
sources: [lwn-weekly-edition-2026-06-25-1078380]
last_updated: 2026-07-03
---

BPFCoroutines는 BPF program을 suspend/resume 가능한 stackless coroutine 형태로 표현하려는 제안이다. 핵심은 verifier가 resume/destroy 경로, 잠금 상태, 안전한 상태 전환을 검증하면서도 긴 계산과 사용자 공간 상호작용을 BPF 모델에 맞게 다루는 데 있다.

## Connections
- [[BPF]]
