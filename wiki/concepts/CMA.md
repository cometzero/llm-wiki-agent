---
title: "CMA"
type: concept
tags: [linux, kernel, memory]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

## Summary
Contiguous Memory Allocator(CMA)는 장치 DMA 등에 필요한 물리적으로 연속된 메모리 영역을 Linux에서 확보하기 위한 메커니즘이다. 대형 페이지, DMA, direct map 정책은 모두 연속 메모리 확보와 단편화 사이의 균형에 영향을 준다.

## Connections
- [[lwn-weekly-edition-2026-05-14-1071535]] — 이 개념/엔티티가 소개되거나 중요 맥락으로 연결된 LWN 주간 번역 소스.
