---
title: "IOUring"
type: concept
tags: [linux, kernel, io]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

## Summary
io_uring은 Linux의 고성능 비동기 I/O 인터페이스로, 시스템 호출 오버헤드와 이벤트 처리 비용을 줄이기 위해 제출/완료 큐를 사용한다. DMA-buf를 읽기/쓰기 경로에 활용하는 논의와 함께 zero-copy 및 버퍼 수명 관리 문제와 연결된다.

## Connections
- [[lwn-weekly-edition-2026-05-14-1071535]] — 이 개념/엔티티가 소개되거나 중요 맥락으로 연결된 LWN 주간 번역 소스.
