---
title: "📌 멀티커널 아키텍처는 무엇이며, 어떤 핵심적인 이점을 제공하는가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/Multikernel Architecture_ Kernel-to-Kernel Isolation and Resource Management - Cong Wang.md
---

## Summary
멀티커널 아키텍처는 가상화나 하이퍼바이저 없이 하나의 머신에서 여러 Linux 커널을 동시에 실행하여 커널 간 격리와 탄력적인 리소스 관리를 제공하는 새로운 접근 방식입니다. 리눅스 커널의 고전적인 '단일 커널' 모델에 도전하여, 하이퍼바이저나 가상화 없이 단일 머신에서 여러 리눅스 커널을 동시 실행하는 멀티커널(Multikernel) 아키텍처를 소개합니다. 이 콘텐츠를 통해 독자들은 커널 수준의 강력한 격리(Isolation)와 동적 자원 관리를 실현하는 혁신적인 접근법을 이해하고, 기존 컨테이너 및 VM의 한계를 넘어 노이즈 이웃 문제 제거 및 공격 표면 축소를 달성하는 방법을 배울 수 있습니다. 특히, kexec, Device Tree Overlay와 같은 기존 리눅스 요소를 재활용하여 무중단 라이브 커널 업데이트나 커널 크래시 자동 복구를 구현하는 구체적인 청사진과 실질적인 코드를 확인할 수 있어 시스템 엔지니어와 개발자에게 깊은 통찰을 제공합니다.

## Key Claims
- 발표자는 Tong Wang이며, 리눅스 커널 개발자이자 마이크로넬 테크놀로지(Micronel Technology)의 창업자 겸 CEO이다.
- 발표 주제는 멀티커널 아키텍처이며, 이 아키텍처는 커널 간 격리(kernel-to-kernel isolation)와 탄력적 자원 관리(elastic resource management)를 제공한다.
- 오랫동안 하나의 머신에서는 하나의 리눅스 커널만 실행될 수 있다는 가정이 존재했다.
- 여러 커널을 실행하려면 KVM이나 Xen과 같은 가상화(Virtualization) 기술 또는 AM과 같은 특정 하드웨어가 필요하다는 가정이 지배적이었다.

## Key Quotes
> "멀티커널 아키텍처는 가상화나 하이퍼바이저 없이 하나의 머신에서 여러 Linux 커널을 동시에 실행하여 커널 간 격리와 탄력적인 리소스 관리를 제공하는 새로운 접근 방식입니다." — extracted from the source narrative.

## Connections
- [[CongWang]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Xen]] — directly referenced in or strongly associated with this source.
- [[CongWang]] — directly referenced in or strongly associated with this source.
- [[HypervisorVirtualization]] — one of the main technical themes discussed by this source.
- [[MultikernelArchitecture]] — one of the main technical themes discussed by this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
