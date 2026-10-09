---
title: "PostgreSQL"
type: concept
tags: [database, linux, performance]
sources: [lwn-weekly-edition-2026-05-21-1072730, lwn-weekly-edition-2026-10-01-1096293]
last_updated: 2026-10-09
---

## Summary

PostgreSQL은 관계형 데이터베이스 시스템이며 Linux의 I/O·memory management·scheduling 변화가 correctness와 performance에 직접 영향을 주는 application 사례다. 2026-05-21 LWN corpus에서 처음 연결되었으며 2026-10-01 특집에서 Andres Freund의 kernel 협업 경험으로 문맥이 확장되었다.

## Kernel Interface and Regression Testing

2026-10-01 특집은 process에서 thread 중심 구조로의 점진적 이동, asynchronous I/O와 향후 direct I/O, buffered atomic writes의 필요성을 설명한다. cpuidle 상호작용에 따른 scaling plateau, code huge pages, futex 상태 공간·wakeup, cgroup memory overcommit, fallocate와 CoW, large-folio contention 등이 실제 workload의 병목으로 제시된다. 단일 microbenchmark 개선을 database durability·tail latency·동시 실행 workload의 전체 개선으로 간주하지 말고 회귀 테스트해야 한다.

## Connections

- [[lwn-weekly-edition-2026-05-21-1072730]] — 이전 corpus의 연결을 보존.
- [[lwn-weekly-edition-2026-10-01-1096293]] — Kernel Recipes의 application 관점.
- [[LinuxKernel]] — I/O·memory·scheduler 계약.
