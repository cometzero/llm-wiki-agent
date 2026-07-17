---
title: "LSFMM+BPF Summit 2026"
type: entity
tags: [kernel, storage, filesystem, memory-management, bpf, conference]
sources: [lwn-weekly-edition-2026-07-09-1080835]
last_updated: 2026-07-17
---

## Overview
Linux Storage, Filesystem, Memory-Management, and BPF Summit 2026. 이 호에서 다룬 주요 세션:

### 세션 목록
1. **Negative Dentries** — [[MiklosSzeredi]] 주도, 수백만 개의 negative dentry로 인한 soft-lock 문제
2. **Faster RCUs** — [[PuranjayMohan]]의 RCU expedited grace period 개선
3. **Lockless Memory Allocation** — [[HarryYu]]의 [[kmalloc_nolock]] 함수
4. **1GB HugePage** — [[RikVanRiel]]의 패치 세트 검토
5. **VM Guest Memory Tracking** — [[KirylShutsemau]]의 userfaultfd 확장

## Connections
- [[MemoryManagement]] — 주요 논의 주제
- [[RCU]] — 동시성 최적화
- [[Bpf]] — BPF 관련 세션
- [[Filesystem]] — 스토리지/파일시스템 세션
