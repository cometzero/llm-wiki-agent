---
title: "📌 RV와 데드라인 스케줄러를 사용하여 런타임에 서브시스템을 검증하는 방법은 무엇인가요?"
type: source
tags: [lpc2025]
date: 2026-04-16
source_file: raw/LPC2025/RV and the deadline scheduler_ how to verify your subsystem at runti... Gabriele Monaco & Juri Lelli.md
---

## Summary
커널에 런타임 검증(RV) 메커니즘을 적용하여 데드라인 스케줄러의 동작이 이론적 모델과 일치하는지 확인하고, 오류 발생 시 디버깅하는 과정을 통해 이를 수행합니다. 이벤트와 상태 전이에 시간 제약(클록)을 추가한 Timed Automata(시간 자동자)를 사용하여 모델을 구성하며, 커널 트레이스 포인트를 통해 이벤트를 수집하고, Per Object Monitor를 활용해 데드라인 엔티티별로 동작을 모니터링합니다.

## Key Claims
- 발표자들은 데드라인 스케줄러(deadline scheduler)와 데드라인 서버(deadline servers)의 특정 명세(specification)를 런타임 검증기(Runtime Verifier, RV)를 사용하여 검증하려는 작업을 소개한다.
- 이 작업은 커널 개발자가 머릿속에 가지고 있는 스케줄러의 이상적인 동작 모델(mental model)을 구현된 코드가 제대로 따르고 있는지 확인하는 것을 목표로 한다.
- RV를 통해 구현체가 멘탈 모델을 준수하는지 확인하고, 이를 위해 위키피디아 등에서 조사하여 런타임 검증이라는 방법을 발견하게 되었다.
- 리눅스 커널에는 이미 런타임 검증 메커니즘이 구현되어 있었으며, 이 메커니즘이 개발자가 생각했던 것과 유사하다고 판단했다.

## Key Quotes
> "2. 이 작업은 커널 개발자가 머릿속에 가지고 있는 스케줄러의 이상적인 동작 모델(mental model)을 구현된 코드가 제대로 따르고 있는지 확인하는 것을 목표로 한다." — extracted from the source narrative.

## Connections
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[DeadlineSchedulerVerification]] — one of the main technical themes discussed by this source.
- [[DeterministicExecution]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
