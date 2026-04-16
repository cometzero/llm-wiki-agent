---
title: "📌 SDV(소프트웨어 정의 차량) 시대의 차세대 차량 진단 기술 SOVD(Service-Oriented Vehicle Diagnostics)는 무엇인가?"
type: source
tags: [oss2025-japan, sdv]
date: 2026-04-16
source_file: raw/OSS2025_Japan/SDV-Oriented Use Cases Leveraging Next-Generation Vehicle Diagnostics(SOVD) and Vir... Masanori Itoh.md
---

## Summary
SOVD는 SDV 시대에 필요한 유연하고 동적인 차량 데이터 교환을 위해 기존 이진 기반 진단 프로토콜을 대체하여 HTTP REST 프로토콜로 정의된 차세대 차량 진단 인터페이스입니다. SDV(소프트웨어 정의 차량) 시대를 맞아 차량 진단의 패러다임을 바꿀 SOVD(Service-Oriented Vehicle Diagnostics)의 핵심과 실질적인 활용 방안을 도요타 엔지니어의 시각에서 소개합니다. 기존의 복잡하고 비표준화된 바이너리 기반 진단 방식(UDS/DoIP)이 아닌, HTTP REST API를 기반으로 유연성과 확장성을 극대화한 SOVD를 통해 소프트웨어 및 하드웨어 구성 요소를 동적으로 진단하고 원격에서 관리하는 방법을 구체적인 POC 시스템 구성과 데모를 통해 배울 수 있습니다. 특히, 차량의 사설 IP 문제로 인한 외부 접근의 어려움을 해소하기 위해 Proxy Agent를 활용하여 실시간 원격 진단 시나리오를 구현하는 기술적 통찰을 얻고, ACC(Automotive Edge Computing Consortium)에서의 협력 사례를 통해 차세대 차량 데이터 활용의 방향성을 명확히 파악할 수 있습니다.

## Key Claims
- 본 세션의 주제는 SDV(소프트웨어 정의 차량) 중심 사용 사례이며, 차세대 차량 진단 기술인 SOVD(Service-Oriented Vehicle Diagnostics)와 가상 피드(Virtual Read) 활용에 초점을 맞추고 있다.
- 다만, 발표자는 시간 부족으로 가상 피드 데모 시스템 구축을 완료하지 못하여, 현재는 차량 1대 관련 내용만 다룬다.
- 발표의 주된 내용은 SDV 시대를 대비하는 관점에서 차세대 차량 진단 기술에 중점을 둘 것이며, 작은 데모를 통해 이를 보여줄 예정이다.
- 발표자는 토요타(Toyota)에서 커넥티드 차량 시스템 R&D를 담당하며, 주요 기술 분야는 엔드 투 엔드(end-to-end) 관측성(observability), 표준화, 차량 진단이다.

## Key Quotes
> "2. SDV 시대의 핵심은 차량 측에서 생성되는 데이터를 유연하게 활용하는 것과 차량과의 연결성(Connectivity)을 확보하는 것이다." — extracted from the source narrative.

## Connections
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[AutomotiveGradeLinux]] — directly referenced in or strongly associated with this source.
- [[LinuxFoundation]] — directly referenced in or strongly associated with this source.
- [[SoftwareDefinedVehicle]] — one of the main technical themes discussed by this source.
- [[SOVD]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
