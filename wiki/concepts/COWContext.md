---
title: "COW Context"
type: concept
tags: [kernel, memory-management, reverse-mapping]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[COWContext]]는 [[Lorenzo Stoakes]]가 제안한 익명 역매핑 대안으로, [[mm_struct]] 단위에서 [[CopyOnWrite]] 관계를 추적한다. 기존 [[ReverseMapping]] 코드의 복잡성과 확장성 문제를 해결하려는 시도이다.

## Key Design
- [[VMA]] 단위 추적 → [[mm_struct]] 단위 추적으로 객체 수 감소
- 프로세스 계층을 따라 공유 COW 관계 추적
- [[RCU]] 기반 잠금 없는 조회 가능 (동기화는 별도 처리 필요)
- 페이지 폴딩 시 [[GracePeriod]] 지연 필요성

## Related
- [[ReverseMapping]]
- [[CopyOnWrite]]
- [[mm_struct]]
- [[MemoryManagement]]
- [[RCU]]