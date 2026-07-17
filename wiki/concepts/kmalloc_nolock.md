---
title: "kmalloc_nolock"
type: concept
tags: [kernel, memory, bpf, allocation]
sources: [lwn-weekly-edition-2026-07-09-1080835]
last_updated: 2026-07-17
---

## Definition
모든 커널 컨텍스트에서 lock 없이 메모리 할당 가능한 함수. [[Bpf]] 맵에서 사전 할당 없이 사용 가능.

## 설계 목표
- Sleepable/non-sleepable BPF 프로그램 모두 지원
- [[RCU]] 중요 섹션 내부 접근 가능
- Typesafety-by-RCU 메커니즘 활용

## 기존 문제
- 과거 BPF 맵은 사전 메모리 할당 필요
- 할당 실패 시 메모리 낭비
- BPF 할당자는 다른 곳에서 사용 불가

## 성능 특성
- "거의 모든 작업에서 성공"
- 경우에 따라 buddy allocator로 폴백
- 즉시 해제/재활용 지원

## Connections
- [[Bpf]] — 주요 사용처
- [[RCU]] — 메모리 안전성 보장
- [[MemoryAllocation]] — 상위 개념
- [[LocklessProgramming]] — 구현 방식
