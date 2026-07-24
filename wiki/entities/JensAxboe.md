---
title: "Jens Axboe"
type: entity
tags: [kernel, io_uring, storage]
sources: [lwn-weekly-edition-2026-07-16-1081915]
last_updated: 2026-07-24
---

## Overview
[[JensAxboe|Jens Axboe]]는 Linux 커널의 io_uring 하위 시스템을 개발하고 유지보수하는 핵심 인물이다. 2026년 7.2 커널 릴리스를 위해 잠금 없는 MPSC(다중 생산자/단일 소비자) FIFO 대기열 알고리즘을 설계 및 게시했다.

## Key Contributions
- [[io_uring]] 비동기 I/O 인터페이스의 설계 및 유지보수
- Dmitry Vyukov와 협력하여 잠금 없는 MPSC 큐 알고리즘 개발
- io_uring의 성능 최적화를 위한 스핀락 기반 인큐 동작을 원자적 연산으로 대체

## Connections
- [[io_uring]] — 개발하는 주요 커널 하위 시스템
- [[DmitryVyukov|Dmitry Vyukov]] — MPSC 알고리즘 협력자
- [[LinuxKernel|Linux Kernel]] — 주요 기여자
