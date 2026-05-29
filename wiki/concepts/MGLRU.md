---
title: "MGLRU (Multi-Generational LRU)"
type: concept
tags: [kernel, memory-management, reclaim]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[MGLRU]]는 Linux 커널의 다세대 LRU 페이지 회수 구현으로, 2021년 등장 이후 [[Android]]에서 7천만 대 이상 기기에 배포되었다. 기존 [[LRU]]와 공존하며 코드 통합 문제가 논의되고 있다.

## Key Issues
- [[TraditionalLRU]]와 같은 파일(mm/vmscan.c)에 있어 유지보수 부담
- page cache 보호가 약하여 file-backed 워크로드 성능 저하 가능성
- [[ActiveInactive]] 지표 "튀는" 현상
- [[OOM Killer]] 의존도가 높아지는 경향

## Development Status
- [[LSFMM+BPF Summit]] 2026: 코드 분리 또는 통합 합의 도출
- [[Shakeel Butt]] 주도 통합 작업 진행
- [[Kairui Song]]의 개선 패치 세트로 출발점 확보

## Related
- [[LRU]]
- [[Reclaim]]
- [[PageCache]]
- [[MemoryManagement]]
- [[OOMKiller]]
- [[LSFMM+BPF Summit]]