---
title: "HugeTLB"
type: concept
tags: [kernel, memory, huge-pages]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[HugeTLB]]는 [[hugetlbfs]] 서브시스템이 제공하는 대형 페이지 메모리로, [[VM]] 실행에 효율적이지만 [[LiveUpdate]] 중 보존이 어렵다.

## Live Update Preservation
[[Pratyush Yadav]]의 제안:
1. 보존할 huge page 동결 (address-space 플래그 또는 inode 플래그)
2. 크기/위치 메타데이터 기록
3. 새 커널에서 [[hugetlbfs-backed-memfd]]로 복원
4. [[cgroup]] 과금 및 페이지 캐시 편입

## Current Limitations
- [[CMA]] (Contiguous Memory Allocator)와의 상호작용 미해결
- Live update 활성화 시 CMA+hugetlbfs 병용 비활성화

## Related
- [[hugetlbfs]]
- [[LiveUpdate]]
- [[KexecHandover]]
- [[CMA]]
- [[LSFMM+BPF Summit]]