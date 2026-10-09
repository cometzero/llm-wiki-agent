---
title: "C Undefined Behavior"
type: concept
tags: [c, compiler, memory-safety]
sources: [lwn-weekly-edition-2026-10-01-1096293]
last_updated: 2026-10-09
---

## Summary

C는 abstract machine의 observable behavior를 기준으로 compiler의 최적화를 제한한다. Undefined behavior(UB)는 표준이 실행 결과를 규정하지 않는 영역이며, 개발자가 기대하는 검사·실행 순서와 compiler의 가정이 충돌할 수 있다.

## Operational Implications

C23의 time-travel 제한과 C2y draft 개선은 UB 축소를 지향하지만 C를 즉시 memory-safe language로 만들지는 않는다. Warning·static analysis·sanitizer·bounds checking·하드웨어 지원은 각각 서로 다른 오류를 다룬다. 특히 temporal memory safety는 별도의 검증과 비용이 필요하다. Compiler option, ABI/POSIX contract, test coverage를 명시하고 우연한 최적화 결과에 의존하지 않는 설계가 중요하다.

## Connections

- [[Compiler]] — observable behavior와 optimization contract.
- [[LinuxKernel]] — C 기반 system software의 안전성·성능 경계.
- [[lwn-weekly-edition-2026-10-01-1096293]] — Martin Uecker의 Kernel Recipes 발표를 다룬 특집.
