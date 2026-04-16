---
title: "📌 Linux 커널의 안전성 강화를 위한 Address Space Isolation(주소 공간 격리)은 무엇인가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/Address Space Isolation for Enhanced Safety of the Linux Kernel - Igor Stoppa, NVIDIA.md
---

## Summary
Linux 커널 내부에서 발생하는 자체 간섭으로부터 커널을 보호하기 위해 MMU(메모리 관리 장치)를 활용하여 커널 내부에 여러 컨텍스트(safe, core, qm)를 정의하고 각 컨텍스트의 메모리 접근을 제한하는 기술입니다. 커널 내부에서 발생할 수 있는 오류의 확산을 방지하여 시스템의 복원력을 높이고, 안전성 분석을 단순화하며, 궁극적으로는 완전한 시스템 이중화 없이도 안전한 시스템 구축을 가능하게 하는 것입니다.

## Key Claims
- 리눅스 커널의 안전성(Safety) 문제에 대한 해결책을 모색하는 실험을 공유하는 것이 목표이다.
- 이 실험은 커널이 자기 간섭(Self-interference)으로부터 스스로를 보호하는 방안에 중점을 둔다.
- 청중이 이 발표를 통해 간섭에 대처하는 아이디어와 하드웨어 개선 요청 방안을 얻기를 희망한다.
- 리눅스는 모놀리식 커널 구조로 인해 안전성 확보에 최적의 선택이 아니다.

## Key Quotes
> "커널 내부에서 발생할 수 있는 오류의 확산을 방지하여 시스템의 복원력을 높이고, 안전성 분석을 단순화하며, 궁극적으로는 완전한 시스템 이중화 없이도 안전한 시스템 구축을 가능하게 하는 것입니다." — extracted from the source narrative.

## Connections
- [[IgorStoppa]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[NVIDIA]] — directly referenced in or strongly associated with this source.
- [[ELISA]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[AddressSpaceIsolation]] — one of the main technical themes discussed by this source.
- [[DevicetreeAndFwnodes]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
