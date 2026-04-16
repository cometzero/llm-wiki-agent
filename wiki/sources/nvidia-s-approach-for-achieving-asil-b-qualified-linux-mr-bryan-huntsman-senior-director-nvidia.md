---
title: "📌 NVIDIA가 리눅스 커널을 ASIL B 인증받기 위해 어떤 접근 방식을 취하는가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/NVIDIA's Approach for Achieving ASIL B Qualified Linux - Mr Bryan Huntsman (Senior Director, NVIDIA).md
---

## Summary
NVIDIA는 리눅스 커널 전체를 인증하는 대신, MMU 기반의 메모리 분리 및 페이지 테이블 스위칭을 통해 안전 필수 코드를 비안전 코드로부터 보호하는 방식으로 접근합니다. 커널의 비안전 관련 부분에 대한 광범위한 변경이나 인증 노력을 줄여, 전통적인 방법 대비 비용과 노력을 크게 절감하면서도 ASIL B 수준의 안전 목표를 달성할 수 있습니다.

## Key Claims
- 본 발표는 리눅스 커널의 안전성 확보에 대한 NVIDIA의 아이디어를 다루며, 원래는 Automotive Linux Summit에서 발표되었고, 리눅스 플러머스(Plumbers) 컨퍼런스에 늦게 추가되었다.
- 발표 내용은 주로 자동차 용어에 초점을 맞추고 있으나, 일반적으로 모든 안전 산업에 적용될 수 있다.
- 이 개념이 나오게 된 '💡깨달음의 순간(light bulb moment)'은 수년 전 주소 공간 격리(Address Space Isolation)에 대한 강연에서 비롯되었다.
- 리눅스에서 안전성을 확보하기 어려운 문제 공간(problem space)에 대한 논의는 OSS Europe (8월)에서 진행되었고, 본 강연은 이 논의의 연장선상에 있다.

## Key Quotes
> "NVIDIA는 리눅스 커널 전체를 인증하는 대신, MMU 기반의 메모리 분리 및 페이지 테이블 스위칭을 통해 안전 필수 코드를 비안전 코드로부터 보호하는 방식으로 접근합니다." — extracted from the source narrative.

## Connections
- [[BryanHuntsmanSeniorDirector]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[NVIDIA]] — directly referenced in or strongly associated with this source.
- [[AutomotiveGradeLinux]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[ASILBQualifiedLinux]] — one of the main technical themes discussed by this source.
- [[AddressSpaceIsolation]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
