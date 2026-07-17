---
title: "Rik van Riel"
type: entity
tags: [kernel, memory-management]
sources: [lwn-weekly-edition-2026-07-09-1080835]
last_updated: 2026-07-17
---

## Profile
오래된 커널 메모리 관리 개발자로, 1998년부터 Linux 메모리 조각화 방지에 기여. 40개 패치로 구성된 시리즈로 1GB HugePage 안정적 할당 시도.

## Key Contributions
- [[ZonedMemoryAllocator]] 제안 (이후 커널에 통합)
- [[SuperPageBlock]] 개념으로 1GB PUD 수준 HugePage 할당 안정화
- 이동 가능/이동 불가능 페이지 블록 분리 정책
- [[ClaudeOpus]] LLM 보조로 패치 생성 (Assisted-by 태그)

## Current Work
1GB HugePage 안정적 할당을 위해 [[Hugetlbfs]] 예약 없이 런타임 할당 가능하도록 하는 패치 세트 개발.

## Connections
- [[LSFMMbpfSummit2026]] — 1GB HugePage 패치 세트 발표
- [[MemoryManagement]] — 메모리 할당자 하위 시스템
- [[LorenzoStoakes]] — 패치 세트에 대한 강한 비판 제기
- [[HugeTLB]] — 대용량 페이지 서브시스템
