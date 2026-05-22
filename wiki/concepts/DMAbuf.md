---
title: "DMA-buf"
type: concept
tags: [kernel, io, memory-sharing]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# DMA-buf

dma-buf는 Linux 커널의 버퍼 공유 메커니즘으로, 드라이버들이 메모리 버퍼를 복사 없이 공유할 수 있게 한다.

## io_uring 통합 (2026)

Pavel Begunkov가 Keith Busch의 2022년 작업을 확장하여 dma-buf를 `io_uring`에 등록해 설정 비용을 여러 I/O 작업에 분산시키는 패치 시리즈를 논의했다.

### 목표
- 네트워킹과 스토리지 서브시스템에서 dma-buf 일관된 사용
- IOMMU 사전 매핑(pre-mapping)으로 최대 8.8배 성능 향상

### 새로운 구조
- `io_dmabuf_token` — 드라이버와 io_uring 인터페이스
- `io_dmabuf_map` — I/O 요청 추적, iomap 서브시스템 활용

### 과제
- scatterlist 의존성
- IOMMU 슬롯 자원 고갈 가능성 (권한/capability 필요)
- 파일시스템 지원 방식 미정

## Related Pages
- [[IOUring]]
- [[IOMMU]]
