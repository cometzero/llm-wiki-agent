---
title: "Kiryl Shutsemau"
type: entity
tags: [kernel, memory-management, virtualization]
sources: [lwn-weekly-edition-2026-07-09-1080835]
last_updated: 2026-07-17
---

## Profile
커널 메모리 관리 및 가상화 개발자. 2008년 2.6.25 커널에 첫 커밋. [[ClaudeOpus]] LLM을 활용한 패치 세트 개발.

## Key Contributions
- [[Userfaultfd]] 확장: VM 게스트 메모리에 대한 작업 세트 추적 기능 추가
- 동기/비동기 두 가지 모드의 페이지 액세스 추적
- VM 관리자가 게스트 메모리 사용 패턴 파악 가능

## LLM Workflow
8~10 라운드의 리뷰를 통해 코드 품질 확보. LLM은 아이디어 검증과 코드 생성 보조 도구로 활용.

## Connections
- [[LSFMMbpfSummit2026]] — VM 게스트 메모리 작업 세트 추적 세션
- [[Userfaultfd]] — 사용자 공간 페이지 폴트 처리
- [[MemoryManagement]] — 메모리 관리 하위 시스템
- [[Hypervisor]] — VM 관리자 통합
