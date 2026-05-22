---
title: "Memory Management"
type: concept
tags: [kernel, memory, subsystem]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# Memory Management (Linux Kernel)

Linux 커널의 메모리 관리 하위시스템(mm)은 페이지 할당, 회수, 매핑, NUMA 밸런싱을 담당한다.

## 2026 주요 화제

### 유지관리 Transition
- Andrew Morton의 점진적 은퇴
- David Hildenbrand의 통합 트리 인수
- 리뷰 부담 집중 문제와 LLM 도구 활용 논쟁

### DMA-buf 읽기/쓰기 API
- io_uring 통합으로 설정 비용 amortize
- IOMMU 사전 매핑으로 최대 8.8배 성능 향상

### 직접 매핑 보안
- Brendan Jackman의 `__GFP_UNMAPPED` 플래그
- "mermap" — CPU 로컬 임시 커널 매핑
- migration type → freetype으로의 확장

### Huge Page 확장
- 1GB THP (Usama Arif)
- 64KB 기본 페이지 크기 지원 (Ryan Roberts, Kiryl Shutsemau)

### mshare 재검토
- Anthony Yznaga의 시스템 호출 API 제안
- 페이지 테이블 공유를 통한 메모리 효율화

## Related Pages
- [[AndrewMorton]]
- [[DavidHildenbrand]]
- [[TransparentHugePage]]
- [[DMAbuf]]
