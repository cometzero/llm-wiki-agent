---
title: "Kernel Function Signatures"
type: concept
tags: [linux, bpf, btf, types]
sources: [lwn-weekly-edition-2026-06-04-1074950]
last_updated: 2026-06-12
---

## Summary
[[KernelFunctionSignatures]]는 커널 내부 함수의 실제 인자·반환 타입을 BTF/kfunc 같은 메타데이터로 정확히 표현하는 문제를 가리킨다. [[BPF]] 프로그램과 검증기가 커널 함수를 안전하게 호출하려면 타입 정보가 C 구현과 일치해야 하며, 이는 관찰 가능성과 확장성의 기반이 된다.

## Connections
- [[BPF]] — kfunc 호출과 verifier 타입 검사에 필요하다.
- [[LinuxKernel]] — 내부 API를 도구가 이해 가능한 형태로 노출하는 커널 인프라.
