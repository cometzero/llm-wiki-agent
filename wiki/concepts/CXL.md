---
title: "CXL (Compute Express Link)"
type: concept
tags: [hardware, memory, interconnect, pcie]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[CXL]]은 PCIe 버스를 통해 CPU 근처에 공유 메모리 노드를 제공하는 데이터센터 기술이다. 커널 지원이 진행 중이지만 [[MemoryManagement]] 복잡성을 높이고 있다.

## Current Challenges
- [[RemoteNUMA]] 메모리보다 지연 시간이 나쁜 경우 존재
- 구성 가능성이 높아 커널-펌웨어 충돌 가능성
- 핫플러그 특성: 메모리 사라지면 시스템 RAM도 사라질 수 있음
- 표준과 하드웨어 구현의 빠른 진화

## Development Areas
- 오류 처리 개선
- [[Accelerator]] 지원 (상대적으로 단순)
- [[vfio-cxl]] — VM으로 CXL 가속기 내보내기
- [[DynamicCapacity]] — [[DeviceDAX]] 연동
- [[GuestMemfd]] 통합

## Not Yet Addressed
- 오류 격리 (CXL 호스트 브리지 장애 시 전체 시스템 영향)
- Peer-to-peer 동작
- CXL 암호화 지원

## Related
- [[DeviceDAX]]
- [[GuestMemfd]]
- [[vfio-cxl]]
- [[MemoryManagement]]
- [[LSFMM+BPF Summit]]