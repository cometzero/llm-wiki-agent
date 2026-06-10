---
title: "RTC (Real-Time Chunking)"
type: concept
tags: [real-time, control, vla, latency]
sources: [tbd-vla-2606-07895, tbd-vla-2606-07895-learning]
last_updated: 2026-06-10
---

## Definition

RTC(Real-Time Chunking)는 [[VLA]] inference에서 실행 중인 action chunk 이후의 미래 chunk를 실시간으로 갱신하는 메커니즘이다. Control loop에서 필요한 action prefix만 실행하고 나머지는 계속 업데이트한다.

## How It Works

1. 현재 block의 action prefix를 실행
2. 환경 피드백 수신
3. 나머지 block들을 환경 변화에 맞게 갱신
4. 다음 block으로 진행

## Key Benefits

- **낮은 latency**: 필요한 action만 즉시 실행
- **적응성**: 환경 변화에 실시간 대응
- **효율성**: [[BlockDiffusion]]과 결합하여 병렬 처리 유지

## Implementation Notes

- Prefix KV cache 활용으로 반복 계산 감소
- Block size 결정이 RTC 성능에 영향
- Expectation sampling이 argmax보다 안정적

## Related Concepts

- [[BlockDiffusion]] — 병렬 디노이징 기반
- [[TemporalAR]] — 순차 블록 생성 구조
- [[ClosedLoopLatency]] — 실시간 제어 latency
- [[ActionTokenization]] — action의 token 변환

## Connections

- [[TBDVLA]] — RTC를 지원하는 VLA framework
- [[FastDVLA]] — 저지연 inference 연구
- [[ReflectDrive-2]] — 자율주행 실시간 planning

## Applications

- [[RoboticControl]] — 로봇의 실시간 동작 제어
- [[AutonomousDriving]] — 차량의 실시간 trajectory 생성
