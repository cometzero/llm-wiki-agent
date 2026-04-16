---
title: "📌 KernelSBOM은 무엇을 하는 프로젝트인가?"
type: source
tags: [lpc2025]
date: 2026-04-16
source_file: raw/LPC2025/KernelSBOM_ Reconstructing Linux Kernel Builds into Trusted SPDX Bills of Materi... Maximilian Huber.md
---

## Summary
kernelsbom은 리눅스 커널 빌드를 재구성하여 신뢰할 수 있는 spdx 소프트웨어 자재 명세서(SBOM)를 생성하는 파이썬 기반 도구입니다. 성공적인 커널 빌드로부터 bzImage나 커널 모듈 파일 같은 최종 배포 아티팩트를 역추적하여, cmd 파일과 추가적인 휴리스틱(예: .s 파일 내 incbin 구문, 하드코딩된 메이크파일 의존성)을 분석해 빌드 과정을 재구성합니다.

## Key Claims
- 이 프로젝트의 핵심 임무는 Linux 커널 빌드를 위한 SBOM(Software Bill of Materials)을 생성하는 것이다.
- 생성된 SBOM은 현재 GitHub URL에 위치하며, SPDX 재단 저장소로 이동하거나 프로젝트 이름이 변경될 수 있으며, 현재 활발히 개발 중이다.
- KernelSBOM은 성공적인 커널 빌드(소스 디렉터리와 출력 디렉터리로 구성됨)가 주어졌을 때, 빌드가 완료된 후에 실제로 무슨 일이 일어났는지 재구성하는 Python 도구이다.
- 목표는 최종 배포 아티팩트(예: BZ 이미지 또는 커널 모듈 파일)와 같은 루트(Roots)에서 시작하여 해당 아티팩트들이 어떻게 생성되었는지 또는 어떤 요소들이 포함되었는지를 파악하는 것이다.

## Key Quotes
> "1. 이 프로젝트의 핵심 임무는 Linux 커널 빌드를 위한 SBOM(Software Bill of Materials)을 생성하는 것이다." — extracted from the source narrative.

## Connections
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[LinuxFoundation]] — directly referenced in or strongly associated with this source.
- [[Git]] — directly referenced in or strongly associated with this source.
- [[SPDX]] — directly referenced in or strongly associated with this source.
- [[KernelSBOM]] — one of the main technical themes discussed by this source.
- [[SPDXSBOM]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
