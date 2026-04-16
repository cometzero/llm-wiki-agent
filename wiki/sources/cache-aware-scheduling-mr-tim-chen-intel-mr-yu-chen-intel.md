---
title: "📌 캐시 인식 스케줄링이란 무엇이며, 어떤 문제를 해결하는가?"
type: source
tags: [lpc2025]
date: 2026-04-16
source_file: raw/LPC2025/Cache Aware Scheduling - Mr Tim Chen (Intel), Mr Yu Chen (Intel).md
---

## Summary
캐시 인식 스케줄링은 numa 노드 내 여러 캐시(ARC) 간의 데이터 공유 문제를 해결하여, 프로세스의 스레드들을 가장 활발한 ARC에 모으는 전략입니다. 기존 노드 밸런서가 작업을 CPU에 고르게 분산시키려 하여 캐시 간 데이터 전송 비용이 증가하고 성능이 저하되는 문제를 해결하기 위함입니다.

## Key Claims
- 문제의 배경: 일부 플랫폼에서는 하나의 NUMA 노드(Non-Uniform Memory Access Node)에 다중 L3 캐시(LLC, Last Level Cache)가 존재한다.
- 비용 발생: 이러한 ARC(Affinity Region) 간의 캐시 일관성(Cache Coherence)을 유지하는 데에는 많은 비용이 발생한다.
- 최악의 시나리오: 데이터 리더(Reader)와 라이터(Writer)가 서로 다른 ARC에 있을 때, ARC 간의 캐시 재생성(refitting the cache)은 매우 비싸다.
- 노드 밸런서의 한계: 이러한 토폴로지(구조)에서 노드 밸런서(Node Balancer)에 문제가 발생할 수 있다.

## Key Quotes
> "1. 목표: 노드 밸런서가 캐시에 민감한 작업(cache-sensitive tasks)을 인식하도록 만드는 것이다." — extracted from the source narrative.

## Connections
- [[TimChen]] — directly referenced in or strongly associated with this source.
- [[YuChen]] — directly referenced in or strongly associated with this source.
- [[Intel]] — directly referenced in or strongly associated with this source.
- [[TimChen]] — directly referenced in or strongly associated with this source.
- [[CacheAwareScheduling]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
