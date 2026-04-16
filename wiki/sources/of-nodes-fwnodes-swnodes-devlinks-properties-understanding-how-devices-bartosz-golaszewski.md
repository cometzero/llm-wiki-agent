---
title: "📌 Linux 장치 드라이버 모델에서 다양한 소프트웨어 노드 유형을 이해하는 방법은 무엇인가요?"
type: source
tags: [oss2025-japan]
date: 2026-04-16
source_file: raw/OSS2025_Japan/OF-nodes, Fwnodes, Swnodes, Devlinks, Properties - Understanding How Devices... Bartosz Golaszewski.md
---

## Summary
Linux 커널의 장치 드라이버 모델에서 OF-노드, FW-노드, SW-노드, Device Link 및 속성 같은 다양한 소프트웨어 노드 유형과 이들의 역사적 발전, 상호 관계를 이해하는 것이 중요합니다. 장치가 시스템마다 다르게 연결되어 있더라도 동일한 장치 드라이버를 재사용하고 구성하기 위해 펌웨어(장치 트리, acpi)를 통해 장치 설정을 전달해야 하기 때문입니다.

## Key Claims
- 드라이버 모델의 목적: 모든 유형의 장치에서 공통 코드를 공유할 수 있도록 추상화 계층을 제공하는 것이다.
- 세 가지 주요 행위자: 리눅스 드라이버 모델에는 장치(Devices), 드라이버(Drivers), 버스(Buses) 세 가지 주요 구성 요소가 있다.
- struct device로 표현되며, 하드웨어 구성 요소의 소프트웨어적 논리 표현이다.
- 실제 하드웨어 구성 요소 하나가 여러 struct device로 표현될 수도 있고, 하드웨어 없이 논리적으로만 존재하는 struct device도 생성 가능하다.

## Key Quotes
> "Linux 커널의 장치 드라이버 모델에서 OF-노드, FW-노드, SW-노드, Device Link 및 속성 같은 다양한 소프트웨어 노드 유형과 이들의 역사적 발전, 상호 관계를 이해하는 것이 중요합니다." — extracted from the source narrative.

## Connections
- [[UnderstandingHowDevicesBartoszGolaszewski]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[UnderstandingHowDevicesBartoszGolaszewski]] — directly referenced in or strongly associated with this source.
- [[DevicetreeAndFwnodes]] — one of the main technical themes discussed by this source.
- [[PowerManagementUSB]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
