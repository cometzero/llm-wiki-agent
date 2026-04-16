---
title: "📌 안드로이드 부트의 미래를 위한 GBL, DRTM, UKI 기술은 무엇이며 왜 중요한가?"
type: source
tags: [lpc2025, safety]
date: 2026-04-16
source_file: raw/LPC2025/Android Boot, DRTM, UKIs - Dmitrii Merkurev (Google), Leif Lindholm (Qualcomm), Ram Muthiah (Google).md
---

## Summary
안드로이드 부트의 현대적이고 안전한 변화를 이끌기 위해 GBL(Google Bootloader)은 EFI 애플리케이션으로 부트플로우를 표준화하고, DRTM(Dynamic Root of Trust for Measurement)은 초기 펌웨어 손상으로부터 보호하며, UKI(Unified Kernel Image)는 부팅 프로세스를 통합하는 핵심 기술입니다. 안드로이드 부트 시스템의 근본적인 변화를 예고하는 GBL(Generic Bootloader), DRTM, UKIS에 대한 심층적인 논의를 담고 있습니다. 파편화된 안드로이드 부트 환경을 표준화하고 효율성을 높이기 위해 구글이 제안한 EFI 애플리케이션 기반 GBL의 도입 배경과, 향후 보안 강화를 위한 DRTM(Dynamic Root of Trust for Measurement) 통합 방안에 대한 복잡한 기술적 도전을 다룹니다. 특히, 장치별 특성을 유지하면서 어떻게 신뢰 환경을 구축하고 안드로이드 가상화 프레임워크(AVF)를 보호할 수 있을지에 대한 구체적인 해결책(멀티 스테이지 DLM)과, 최종적으로 UKIS(Unified Kernel Image)를 통해 부트 이미지를 통합하는 로드맵까지 파악할 수 있어, 임베디드 시스템 엔지니어와 모바일 보안 개발자에게 미래 안드로이드 플랫폼의 핵심 방향성을 제시합니다.

## Key Claims
- 일반적으로 안드로이드 기기는 파티션 세트를 사용하며, 부트 시 커널, RAM 디스크, 장치 트리(device trees) 같은 최종 부트 아티팩트(artifact)를 제공하는 부트 파티션을 주로 활용한다.
- 파티션 감지: 장치 부트에 필요한 블록 장치와 파티션을 감지한다.
- 모드 및 슬롯 확인: 안드로이드 부트 모드와 활성 슬롯을 확인한다.
- 파티션 포맷 처리: 안드로이드 사용자 지정 파티션 포맷을 로드하고 검증하여 부트 아티팩트를 추출하고 롤백 보호를 처리한다.

## Key Quotes
> "안드로이드 부트의 현대적이고 안전한 변화를 이끌기 위해 GBL(Google Bootloader)은 EFI 애플리케이션으로 부트플로우를 표준화하고, DRTM(Dynamic Root of Trust for Measurement)은 초기 펌웨어 손상으로부터 보호하며, UKI(Unified Kernel Image)는 부팅 프로세스를 통합하는 핵심 기술입니다." — extracted from the source narrative.

## Connections
- [[DmitriiMerkurev]] — directly referenced in or strongly associated with this source.
- [[LeifLindholm]] — directly referenced in or strongly associated with this source.
- [[RamMuthiah]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.
- [[HypervisorVirtualization]] — one of the main technical themes discussed by this source.
- [[AndroidBootSecurity]] — one of the main technical themes discussed by this source.
- [[DRTM]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
