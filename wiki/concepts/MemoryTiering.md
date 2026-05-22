---
title: "MemoryTiering"
type: concept
tags: [linux, kernel, memory]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

## Summary
Memory tiering은 DRAM, CXL 메모리, NVM 등 지연시간과 대역폭이 다른 메모리 계층 사이에서 페이지를 배치·이동하는 기법이다. DAMON 같은 접근 패턴 관측 도구는 어떤 데이터를 빠른 계층에 둘지 결정하는 데 활용될 수 있다.

## Connections
- [[lwn-weekly-edition-2026-05-14-1071535]] — 이 개념/엔티티가 소개되거나 중요 맥락으로 연결된 LWN 주간 번역 소스.
