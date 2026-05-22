---
title: "IOMMU"
type: concept
tags: [linux, kernel, memory, dma]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

## Summary
IOMMU는 장치 DMA 접근을 가상 주소 변환과 권한 정책으로 제어하는 하드웨어/커널 메커니즘이다. DMA-buf, GPU, 장치 드라이버 보안에서 격리와 주소 변환 비용을 동시에 고려해야 한다.

## Connections
- [[lwn-weekly-edition-2026-05-14-1071535]] — 이 개념/엔티티가 소개되거나 중요 맥락으로 연결된 LWN 주간 번역 소스.
