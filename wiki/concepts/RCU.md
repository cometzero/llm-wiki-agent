---
title: "RCU"
type: concept
tags: [kernel, concurrency, synchronization]
sources: [lwn-weekly-edition-2026-05-21-1072730, lwn-weekly-edition-2026-07-09-1080835]
last_updated: 2026-07-17
---

## Definition
Linux 커널의 핵심 lockless 동기화 메커니즘. 읽기 작업은 잠금 없이 수행되고, 쓰기는 복사본 생성 후 원자적으로 포인터 교체.

## Grace Period
RCU로 보호되는 리소스 해제 전 모든 읽기 완료 대기. 두 가지 유형:
- `synchronize_rcu()` — 정지 상태 대기 (수십 ms)
- `synchronize_rcu_expedited()` — IPI로 빠른 대기

## 최신 개선
[[PuranjayMohan]]의 패치:
- Expedited grace period 종료 시 즉시 콜백 실행
- 메모리 사용 33%-41% 감소
- `synchronize_rcu()` 레이턴시 감소

## Connections
- [[LocklessProgramming]] — 상위 개념
- [[KernelConcurrency]] — 동시성Primitive
- [[MemoryReclamation]] — 메모리 회수
- [[Bpf]] — BPF 맵과 통합
