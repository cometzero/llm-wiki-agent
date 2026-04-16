---
title: "📌 PREEMPT_RT 커널에서의 핵심적인 개선 사항은 무엇인가?"
type: source
tags: [lpc2025]
date: 2026-04-16
source_file: raw/LPC2025/News from PREEMPT_RT - Sebastian Siewior.md
---

## Summary
PREEMPT_RT 커널에서 발생하던 락(lock) 경쟁 문제를 해결하기 위해 명시적인 잠금 메커니즘을 도입하고, futex 및 lazy preempt 동작을 개선하여 시스템 성능과 안정성을 향상시킨 것이 핵심입니다. 리눅스 커널의 PREEMPT_RT 패치와 관련된 최신 핵심 업데이트를 심층 분석하는 세션입니다. 독자는 이 발표를 통해 고성능 컴퓨팅 및 실시간 시스템의 성능을 저해했던 주요 문제점(Bottom Half 락 경합, Futex 해시 충돌 지연, 부적절한 워크큐 스케줄링)이 어떻게 해결되었는지 기술적 배경과 구체적인 구현 변경점을 파악할 수 있습니다. 특히 lock_nested_BH 도입을 통한 네트워킹 드라이버 최적화, Futex의 해시 버킷 스케일링을 통한 성능 개선, 그리고 lazy preempt를 기반으로 한 사용자 공간 스핀락 지연 기능의 개발 현황 등 실시간 성능을 극대화하기 위한 커널 내부의 가장 중요한 변화와 그 효과를 명확히 이해하고 자신의 시스템에 적용할 수 있는 통찰을 얻게 될 것입니다.

## Key Claims
- 발표 주제: 발표자(Sebastian Siewior)와 다른 개발자들이 지난 1년간 작업한 PREEMPT_RT(Real-Time Preemption) 관련 핵심 업데이트와 그 효과를 소개한다.
- 주요 내용: 주로 성능을 저해했던 기술적 문제점들의 해결책과 구체적인 구현 변경점들을 다룬다.
- PREEMPT_RT(RT) 환경에서는 컨텍스트 스위치가 가능하도록 BH가 선점 가능하게 구현된다.
- 일반적인 Non-RT 환경에서는 모든 핸들러가 하드 IRQ 이후에 처리되지만, RT에서는 인터럽트 핸들러와 소프트 인터럽트(Soft IRQ)가 스레드화된다.

## Key Quotes
> "PREEMPT_RT 커널에서 발생하던 락(lock) 경쟁 문제를 해결하기 위해 명시적인 잠금 메커니즘을 도입하고, futex 및 lazy preempt 동작을 개선하여 시스템 성능과 안정성을 향상시킨 것이 핵심입니다." — extracted from the source narrative.

## Connections
- [[SebastianSiewior]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[SebastianSiewior]] — directly referenced in or strongly associated with this source.
- [[PREEMPTRT]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
