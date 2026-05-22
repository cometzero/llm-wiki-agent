---
title: "DAMON"
type: entity
tags: [kernel-subsystem, memory-management, monitoring]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# DAMON (Data Access MONitor)

DAMON은 Linux 커널의 메모리 접근 모니터링 서브시스템으로, 5.15 커널에 처음 병합되었으며 현재 대부분의 배포판 커널에서 활성화되어 있다.

## Core Functionality
- 5ms마다 메모리 접근 샘플링 (가벼운 오버헤드, 일반적 시스템에서 0.1% 미만)
- 100ms마다 사용자 공간에 접근 정보 반환
- DAMOS를 통한 메모리 관리 동작(회수, 마이그레이션 등)

## 2026 Updates (SeongJae Park)

### 계층화 (Tiering)
- `damos_migrate` — RAM과 CXL 메모리 간 페이지 이동
- TPP-DAMON → NUMA-TPP-DAMON으로 확장
- 동적 인터리빙(dynamic interleaving) — 메모리 대역폭 활용 극대화

### 데이터 속성 모니터링
- 페이지 수준 속성(유형, cgroup, 유휴성) 샘플링
- DAMOS 필터로 동작하는 프로브 시스템

### DAMON-X
- 여러 DAMON 모듈이 공통 모니터링 매개변수 공유
- "그냥 동작하는 DAMON(DAMON that just works)" 지향

### THP 연동
- `damos_hugepage` — 접근 패턴 기반 THP collapse/split
- 벤치마크에서 메모리 팽창의 80% 제거, 성능 향상의 46% 보존

## Related Concepts
- [[CXL]] — 메모리 계층화 대상
- [[TransparentHugePage]]
- [[MemoryTiering]]
