---
title: "📌 Linux에서 게임 경험을 향상시키기 위한 Sched_ext의 역할은 무엇인가?"
type: source
tags: [oss2025-japan, safety, inference]
date: 2026-04-16
source_file: raw/OSS2025_Japan/Enhancing Your Gaming Experience on Linux With Sched_ext - Changwoo Min, Igalia.md
---

## Summary
Sched_ext는 Linux 커널 6.12에 공식 병합된 BPF 기반 확장 가능한 스케줄러 프레임워크로, 사용자 지정 스케줄러를 구현하여 게임 워크로드의 지연 시간 및 에너지 소비를 최적화함으로써 전반적인 게임 경험을 향상시키는 데 기여합니다. LAD 스케줄러는 지연 시간에 민감한 작업을 우선 처리하여 1% 낮은 FPS를 개선하고, 하이브리드 CPU를 효율적으로 사용하여 에너지 소비를 줄임으로써 성능과 에너지 효율을 동시에 향상시키는 것을 목표로 합니다.

## Key Claims
- 발표자는 Igalia 소속의 Chang Min이며, Sched\_ext 스케줄러 프레임워크를 활용하여 리눅스 기반 게임 경험을 향상시키는 방법을 논한다.
- Sched\_ext는 사용자가 맞춤형 스케줄러(custom scheduler)를 작성할 수 있도록 지원하는 스케줄러 프레임워크이다.
- 과거 리눅스 게이밍은 환상처럼 여겨졌으나, 실제로는 그렇지 않다.
- Steam Deck과 Steam OS가 대표적인 예시이며, Steam Deck을 통해 리눅스에서 윈도우 게임을 플레이할 수 있다.

## Key Quotes
> "LAD 스케줄러는 지연 시간에 민감한 작업을 우선 처리하여 1% 낮은 FPS를 개선하고, 하이브리드 CPU를 효율적으로 사용하여 에너지 소비를 줄임으로써 성능과 에너지 효율을 동시에 향상시키는 것을 목표로 합니다." — extracted from the source narrative.

## Connections
- [[ChangwooMin]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Qualcomm]] — directly referenced in or strongly associated with this source.
- [[Igalia]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[SchedExt]] — one of the main technical themes discussed by this source.
- [[InteractiveInference]] — one of the main technical themes discussed by this source.
- [[DeadlineSchedulerVerification]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
