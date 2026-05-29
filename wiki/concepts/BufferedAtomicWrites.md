---
title: "Buffered Atomic Writes"
type: concept
tags: [kernel, storage, io, atomicity]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[BufferedAtomicWrites]]는 [[PostgreSQL]]과 같은 [[BufferedIO]]를 사용하는 데이터베이스를 위한 8KB 원자적 쓰기 보장 기능이다. 기존 [[O_DIRECT]] 원자적 쓰기는 클라우드 스토리지에서 가능했지만, 페이지 캐시를 우회하지 않는 [[BufferedIO]]에서는 찢긴 쓰기(torn writes)가 발생했다.

## Key Details
- [[PostgreSQL]]은 [[FullPageWrites]]와 [[WAL]]으로 찢긴 쓰기를 방지하나 성능 비용이 큼
- 8KB 원자적 쓰기 가능 시 TPS 1.7배 증가, TPS 변동성 14배 감소
- [[RWF_WRITETHROUGH]] 플래그: 페이지 캐시에 복사 후 즉시 [[DirectIO]] 발행
- 동일 파일 내 동시 쓰기 시 [[inode]] 잠금 경합으로 최대 65% 성능 저하 가능

## Related
- [[WriteThrough]]
- [[RWF_WRITETHROUGH]]
- [[PostgreSQL]]
- [[WAL]]
- [[DirectIO]]
- [[io_uring]]