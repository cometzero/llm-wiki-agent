---
title: "📌 EROFS는 컨테이너 환경에서 어떤 이점을 제공하는가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/EROFS and containers - Xiang Gao (Alibaba Cloud).md
---

## Summary
EROFS는 컨테이너 OS의 시작 속도를 높이고 이미지 크기를 줄이며, OCI 이미지 풀링을 가속화하고, 루트 파일 시스템의 무결성을 보장하여 전반적인 컨테이너 운영 효율성을 크게 향상시킵니다. - 블록 기반의 불변(immutable) 파일 시스템 - 고정 파일 시스템 블록 크기를 사용한 데이터 정렬 - 내장된 청크 기반 중복 제거 및 투명 압축 기능

## Key Claims
- 블록 기반의 불변(immutable) 파일 시스템
- 고정 파일 시스템 블록 크기를 사용한 데이터 정렬
- 내장된 청크 기반 중복 제거 및 투명 압축 기능
- EROFS의 정의 및 역사: EROFS는 'Enhanced Read-Only File System'의 약자로, 2017년 말에 시작되어 리눅스 커널 5.4 버전부터 사용 가능한 블록 기반의 불변(immutable) 파일 시스템이다.

## Key Quotes
> "2. 핵심 설계 특징: EROFS는 고정된 파일 시스템 블록 크기를 사용하며, 디스크 내 데이터가 파일 시스템 블록 내에서 엄격하게 정렬(aligned)된다." — extracted from the source narrative.

## Connections
- [[XiangGao]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[AlibabaCloud]] — directly referenced in or strongly associated with this source.
- [[QEMU]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[EROFS]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
