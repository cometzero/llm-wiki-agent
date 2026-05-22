---
title: "Andrew Morton"
type: entity
tags: [kernel-maintainer, memory-management]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# Andrew Morton

Andrew Morton은 Linux 커널 메모리 관리(mm) 하위시스템의 오랫동안 핵심 유지관리자였다. 2026년 4월, 그는 유지관리 역할에서 점진적 은퇴를 시작할 것임을 밝혔다.

## Key Contributions
- `-mm` 트리와 메모리 관리 패치 흐름의 중심 역할
- 방어 계층 시스템(-mm 트리, 메인라인 테스트, stable 백포트, 배포판 검증) 설계
- 빠른 개발 속도를 가능하게 하는 다층 검증 체계

## Transition
- **Successor**: David Hildenbrand가 통합 트리 관리를 인수
- **Challenge**: `mm` 디렉터리의 164개 C 파일이 강하게 얽혀 있어 분할이 어려움
- **Concern**: 리뷰 부담이 소수에게 집중되는 현상

## Related Pages
- [[DavidHildenbrand]]
- [[MemoryManagement]]
