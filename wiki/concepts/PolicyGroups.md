---
title: "Policy Groups"
type: concept
tags: [kernel, memory-management, cgroups]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[PolicyGroups]]는 [[Chris Li]]가 제안한 [[ControlGroups]] 대안으로, 자원 관리보다 정책 관리에 초점을 맞추며 통합 계층 구조에 강제되지 않는다. [[SwapTiers]] 같은 계층적이지 않은 정책 표현에 사용될 수 있다.

## Use Cases
- 서비스 수준 목표 (자식 그룹이 부모보다 빠를 수 있음)
- 서로 다른 속도의 스왑 장치 접근 제어
- Android 포그라운드/백그라운드 작업 구분
- 파일시스템 할당 제어
- 네트워크 제어 정책

## Implementation Options Discussed
- [[ControlGroups]]에 연결
- [[ExtendedAttributes]] 사용
- [[BPF]] LSM 활용
- 별도 가상 파일시스템 (계층 없는 flat 뷰)
- 프로세스에 직접 연결

## Related
- [[ControlGroups]]
- [[SwapTiers]]
- [[MemoryManagement]]
- [[LSFMM+BPF Summit]]