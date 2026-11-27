---
title: "Dynamic Linker Hardening"
type: concept
tags: [lwn, linux, security]
sources: [lwn-weekly-edition-2026-11-12-1105460]
last_updated: 2026-11-27
---

## Summary

Dynamic linker는 공유 라이브러리와 ELF executable을 memory에 배치한다. 이 호의 glibc tunable 제안은 position-dependent executable, executable stack 및 fixed mapping 같은 위험한 실행 조건을 제한하려는 접근을 다룬다.

## Operational Boundary

PIE/ASLR 보완은 일반적인 악성 코드 차단 보증이 아니다. 배포판 기본 binary뿐 아니라 외부 배포 executable·runtime/JIT·legacy 프로그램에 대한 regression test가 필요하며 article 시점 제안을 현재 기본값으로 가정하지 않는다.

## Connections

- [[lwn-weekly-edition-2026-11-12-1105460]] — 2026-11-12 보도와 한국어 번역·해설.
- [[LinuxKernel]] — 관련 기술·당사자 맥락.
