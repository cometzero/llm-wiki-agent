---
title: "LSFMM+BPF 2026 Summit"
type: entity
tags: [linux-kernel, conference, memory-management]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit

2026년 5월 크로아티아 자그레브에서 열린 커널 개발자 핵심 Summit으로, 스토리지, 파일시스템, 메모리 관리, BPF 하위시스템 개발자들이 핵심 개발 현안을 논의했다.

## Key Tracks

### Memory Management Track
- Andrew Morton 유지관리 transition
- DAMON 업데이트 — 계층화, 데이터 속성 모니터링, THP 연동
- 1GB 투명 대형 페이지(THP) 확장
- mshare 재검토 — 페이지 테이블 공유
- 직접 매핑(direct map) 바깥 메모리 관리
- 64KB 기본 페이지 크기 지원

### BPF Track
- GCC 16 BPF 지원

### Joint Sessions
- DMA-buf를 통한 읽기/쓰기 API
- 플래시 친화적 스왑
- 버퍼드 원자적 쓰기

## Related Pages
- [[MemoryManagement]]
- [[DAMON]]
- [[TransparentHugePage]]
- [[DMAbuf]]
