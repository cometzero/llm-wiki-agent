---
title: "📌 리눅스 NPU 서브시스템이 엣지 AI/LLM 워크로드에서 겪는 핵심적인 문제는 무엇인가?"
type: source
tags: [lpc2025]
date: 2026-04-16
source_file: raw/LPC2025/Demystifying Linux NPU Subsystem_ From Vision to LLM at Edge - Mr Jagan Teki.md
---

## Summary
기존 리눅스 DRM(Direct Rendering Manager) 스택이 LLM과 같이 상태 유지(stateful) 및 장기 실행(long-loop) 워크로드의 메모리 관리, 작업 스케줄링, 전력 처리 등을 효율적으로 지원하지 못하여 한계에 부딪히는 것이 핵심입니다. 벤더들은 강력한 자체 툴체인을 통해 DRM의 일부 기능만 활용하고, 작업 모델, 실행 주기, 전력 및 메모리(SRAM) 할당, 스케줄링 등 핵심 기능을 독자적인 드라이버 단에서 구현하여 LLM 워크로드를 지원하고 있습니다.

## Key Claims
- 발표자는 U-boot 및 리눅스 커뮤니티에서 13~15년간 주요 기여자였으며, 현재는 에지 추론을 위한 NPU 관련 회사를 운영하고 있다.
- 최근 몇 년간 NPU는 과거 GPU처럼 임베디드 및 PCI 노드에서 독립적인 블록이 되었다.
- 그러나 리눅스 관점에서 NPU는 아직 GPU처럼 '1급 컴퓨트 리소스(first-class compute)'로 인정받지 못하고, 특수한 사례로 남아있는 상황이다.
- 본 발표는 NPU가 왜 1급 리소스가 아닌지, 현재까지의 작업 현황, 그리고 Vision 모델부터 LLM 모델까지 에지 워크로드의 문제점을 중점적으로 다룬다.

## Key Quotes
> "기존 리눅스 DRM(Direct Rendering Manager) 스택이 LLM과 같이 상태 유지(stateful) 및 장기 실행(long-loop) 워크로드의 메모리 관리, 작업 스케줄링, 전력 처리 등을 효율적으로 지원하지 못하여 한계에 부딪히는 것이 핵심입니다." — extracted from the source narrative.

## Connections
- [[JaganTeki]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Qualcomm]] — directly referenced in or strongly associated with this source.
- [[JaganTeki]] — directly referenced in or strongly associated with this source.
- [[NPU]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
