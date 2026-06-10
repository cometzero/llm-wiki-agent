---
title: "Real-Time Chunking (RTC)"
type: concept
tags: [real-time, chunking, closed-loop, vla, control]
sources: [tbd-vla-2606-07895-analysis]
last_updated: 2026-06-10
---

## Overview
Real-Time Chunking(RTC)은 VLA가 이미 실행 중인 action prefix 이후의 미래 action block을 temporal in-painting 방식으로 갱신할 수 있는 메커니즘이다. 이는 closed-loop robot manipulation에서 환경 변화에 실시간으로 대응하는 데 핵심적이다.

## Key Properties
1. **Temporal In-painting**: 실행 완료된 block을 조건으로 미래 block 갱신
2. **Closed-loop Support**: 환경 피드백 기반 action 수정
3. **Latency Benefit**: 전체 trajectory 재생성이 아닌 부분 갱신으로 효율성

## Evaluation Impact
- **Without RTC**: 60.0% success rate
- **With RTC**: 67.1% success rate
- **Improvement**: +7.1% (11.8% relative improvement)

## How It Works
1. 현재까지 실행 완료된 action block을 prefix로 저장
2. 새 observation을 기반으로 미래 block 생성
3. 이전 prediction과 temporal consistency 유지하면서 갱신
4. 부분 재실행으로 부드러운 trajectory 전환

## Related Concepts
- [[TBDVLA]] — RTC를 지원하는 VLA framework
- [[TemporalBlockDiffusion]] — block-level temporal modeling
- [[ClosedLoopControl]] — 피드백 기반 제어
- [[BlockDiscreteDiffusion]] — 병렬 block generation

## Applications
- Robot manipulation with dynamic obstacles
- Real-time trajectory adaptation
- Closed-loop autonomous driving (future extension)
