---
title: "MPSC FIFO Queue"
type: concept
tags: [kernel, io-uring, concurrency, lockless]
sources: [lwn-weekly-edition-2026-07-16-1081915]
last_updated: 2026-07-24
---

## Definition
MPSC(Multi-Producer, Single-Consumer) FIFO Queue는 여러 생산자가 동시에 enqueue하고 하나의 소비자가 dequeue하는 잠금 없는 자료구조다.

## Overview
[[io_uring]] 7.2는 커널의 표준 연결 목록 기본 요소를 대체하는 새로운 잠금 없는 MPSC 대기열을 도입했다. 이 설계는 스핀락 기반 인큐 동작을 원자적 연산으로 대체하여 고도로 동시적인 비동기 I/O 작업에서 경합을 줄인다.

### 기존 방식의 단점
- 단일 연결 목록은 본질적으로 스택이어서 FIFO 순서 유지를 위해 역순 처리 필요
- 재시도 루프로 인해 경쟁 상황에서 캐시 라인 바운싱 발생

### 새로운 설계
- Jens Axboe가 게시하고 Dmitry Vyukov가 제공한 알고리즘 사용
- xchg() 원자 연산으로 꼬리 포인터 업데이트 직렬화
- 별도 헤드 포인터로 생산자/소비자 간 캐시 경합 방지

## Performance Impact
- 오버헤드 감소로 성능 크게 향상
- 더 많은 작업이 더 빠르게 수행
- 커널에서 실행하는 데 소요되는 시간 감소

## Connections
- [[io_uring]] — 적용되는 커널 하위 시스템
- [[JensAxboe|Jens Axboe]] — 설계자
- [[DmitryVyukov|Dmitry Vyukov]] — 알고리즘 제공자
