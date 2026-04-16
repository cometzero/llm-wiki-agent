---
title: "📌 NVIDIA가 리눅스에서 ASIL B 수준의 안전성을 달성하기 위한 접근 방식은 무엇인가?"
type: source
tags: [oss2025-japan, safety]
date: 2026-04-16
source_file: raw/OSS2025_Japan/NVIDIA's Approach for Achieving ASIL B Qualified Linux - Bryan Huntsman US, NVIDIA.md
---

## Summary
NVIDIA는 리눅스 커널 내에 안전 관련 코드와 비안전 관련 코드를 물리적으로 분리하는 ‘컨텍스트(Context)’ 개념을 도입하여 커널 공간 간의 공간적 간섭 문제를 해결함으로써 ASIL B 인증이 가능하다고 보고 있습니다. 대부분의 리눅스 커널 코드는 안전성 고려 없이 개발 과정을 그대로 유지할 수 있으며, 안전 필수 코드 영역은 알려지지 않은 오류로부터 보호되어 전체 시스템의 안전성 분석 노력과 비용을 크게 줄일 수 있습니다.

## Key Claims
- 발표자(Bryan Huntsman)는 안전 전문가(Safety Expert)가 아니며, 이 컨셉을 직접 개발한 사람은 아님
- 이 컨셉은 공동으로 개발되었으며, 주로 자동차 용어(automotive terminology)를 사용하지만, 자동차 외 분야에도 동일하게 적용되는 개념이다
- 이 아이디어의 기원은 몇 년 전 Open Source Summit 유럽 더블린에서 발표된 주소 공간 격리(address space isolation) 관련 논의에서 비롯되었다
- 3개월 전(8월), 동료 Igor가 이 문제에 대해 더 상세한 개요를 발표한 바 있다

## Key Quotes
> "NVIDIA는 리눅스 커널 내에 안전 관련 코드와 비안전 관련 코드를 물리적으로 분리하는 ‘컨텍스트(Context)’ 개념을 도입하여 커널 공간 간의 공간적 간섭 문제를 해결함으로써 ASIL B 인증이 가능하다고 보고 있습니다." — extracted from the source narrative.

## Connections
- [[BryanHuntsmanUs]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[NVIDIA]] — directly referenced in or strongly associated with this source.
- [[BryanHuntsmanUs]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[ASILBQualifiedLinux]] — one of the main technical themes discussed by this source.
- [[AddressSpaceIsolation]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
