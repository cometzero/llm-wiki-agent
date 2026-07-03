---
title: "KASAN for JIT-compiled BPF"
type: concept
tags: [bpf, kasan, memory-safety]
sources: [lwn-weekly-edition-2026-06-25-1078380]
last_updated: 2026-07-03
---

BPFKASAN은 JIT-compiled BPF code에서도 Kernel Address Sanitizer (KASAN)가 메모리 오류를 탐지할 수 있게 하려는 작업이다. 이번 호는 BPF JIT의 load/store instrumentation, register save/restore overhead, sanitizer와 verifier/JIT 경계의 실무 문제를 다룬다.

## Connections
- [[BPF]]
