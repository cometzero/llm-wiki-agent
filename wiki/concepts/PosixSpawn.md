---
title: "posix_spawn"
type: concept
tags: [placeholder, unix, process, runtime]
sources: [lwn-weekly-edition-2026-06-11-1076254]
last_updated: 2026-06-19
---

## Summary
`posix_spawn()`은 새 프로세스를 생성하고 프로그램을 실행하는 POSIX API로, 전통적인 `fork()+exec()` 조합의 비용과 멀티스레드 안전성 문제를 줄이려는 용도로 쓰인다. LWN 2026-06-11호에서는 더 표현력 있는 spawn template 논의와 연결된다.

## Connections
- [[SpawnTemplate]] — `fork()+exec()` 이후의 프로세스 생성 API 설계 논의.
- [[lwn-weekly-edition-2026-06-11-1076254]] — 프로세스 생성 기사.
