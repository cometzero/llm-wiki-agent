---
title: "LPX"
type: entity
tags: [inference-hardware, rack-system, nvidia]
last_updated: 2026-04-21
sources:
  - gtc-2026-the-inference-kingdom-expands
---

## Summary
[[LPX]]는 [[NVIDIA]]가 발표한 LPU 기반 랙 시스템명으로, 32개의 1U LPU 컴퓨트 트레이와 스케일업/스케일아웃 네트워크를 결합해 디코드 중심의 저지연 추론 가속을 실서비스 환경으로 확장하기 위한 플랫폼이다.

## Key Architecture
- 각 랙은 여러 LPU 트레이와 스펙트럼형 스위치 계열을 결합.
- FPGA가 C2C↔이더넷/PCIe 변환과 제어 타이밍을 맡아 네트워크 적응력을 제공.
- 일부 구성은 전체 디코드 처리를 LPX 안에서 수행할 수 있도록 시스템 DRAM(KV 캐시 용) 확장을 고려.

## Connections
- [[LPU]], [[Speculative Decoding]], [[AFD]], [[CPO]], [[SpectrumX]], [[BlueField]] — LPX 설계에서의 연동 핵심 요소.
- [[Groq]] — LPU 계보와 NVIDIA 통합 맥락의 기술 기원 축.

## Contradictions
- No explicit contradiction identified.