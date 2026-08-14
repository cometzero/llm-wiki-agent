---
title: "Process Builder API"
type: concept
tags: [linux, unix, process, api-design]
sources: [lwn-weekly-edition-2026-08-06-1086134]
last_updated: 2026-08-14
---

## Summary
[[ProcessBuilderAPI]]는 child process를 만들 때 전통적인 `fork()` 후 setup, `exec()` 순서를 그대로 노출하는 대신, file descriptor·environment·working directory·credentials 같은 configuration을 명시적 builder contract로 조립하려는 UNIX process-creation API 방향이다. `fork()`의 광범위한 호환성과 async-signal-safety 제약 사이에서 안전하고 예측 가능한 process launch를 제공하는 것이 목표다.

## Connections
- [[lwn-weekly-edition-2026-08-06-1086134]] — proof-of-concept과 API 범위 논의
- [[LinuxKernel72]] — Linux system-call/API evolution의 인접 맥락
