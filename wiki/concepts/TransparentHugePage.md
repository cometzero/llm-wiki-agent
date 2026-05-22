---
title: "Transparent Huge Page (THP)"
type: concept
tags: [memory-management, performance, kernel]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# Transparent Huge Page (THP)

THP는 커널이 자동으로 거대 페이지(일반적으로 2MB)를 프로세스에 투명하게 제공하는 메커니즘이다.

## 1GB THP 확장 (2026 논의)

Usama Arif가 LSFMM+BPF 2026에서 PMD 수준(2MB)을 넘어 PUD 수준(1GB) THP 확장을 제안했다.

### 목적
- 테라바이트급 메모리 시스템에서 페이지 테이블 관리 비용 감소
- TLB 압박 완화

### 과제
- 1GB 연속 물리 메모리 할당 어려움
- CMA(Contiguous Memory Allocator) 필요성
- 페이지 분할 시 페이지 테이블 예치 비용 (약 2MB)
- Migration과 memory hotplug 처리
- 공유 메모리로 제한해야 한다는 제안

## DAMON 연동
`damos_hugepage`를 통해 접근 패턴 기반 THP collapse/split 가능:
- THP 메모리 팽창의 80% 제거
- 성능 향상의 46% 보존

## Related Pages
- [[HugeTLB]]
- [[DAMON]]
- [[MemoryManagement]]
- [[CMA]]
