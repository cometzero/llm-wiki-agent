---
title: "Lorenzo Stoakes"
type: entity
tags: [kernel, memory-management, developer]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[Lorenzo Stoakes]]는 Linux 커널 [[MemoryManagement]] 개발자로, 익명 페이지 역매핑(anonymous reverse mapping)의 복잡성 문제를 해결하기 위해 [[COWContext]] 대안안을 제안했다.

## Key Contributions
- [[COWContext]] 구조 제안 — [[VMA]] 단위 추적 대신 [[mm_struct]] 단위 익명 매핑 추적
- [[RCU]] 기반 빠른 조회 지원
- 기존 [[ReverseMapping]] 코드의 "매우 망가진 추상화" 비판

## Related
- [[COWContext]]
- [[ReverseMapping]]
- [[MemoryManagement]]
- [[LSFMM+BPF Summit]]