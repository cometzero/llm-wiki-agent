---
title: "fanotify Updates"
type: concept
tags: [kernel, filesystem, monitoring]
sources: [lwn-weekly-edition-2026-06-11-1076254]
last_updated: 2026-06-19
---

## Overview
파일 시스템 이벤트 모니터링을 위한 Linux 커널 API. Hierarchical Storage Management(HSM) 시스템에서 활용됨.

## Recent Updates (2026)
- FAN_PRE_ACCESS 이벤트 통합 (2025년 초)
- 마운트 트리 이벤트 감시 (Linux 6.15)
- 사용자 네임스페이스 내 마운트 감시 (Linux 6.16)
- 정지된 권한 이벤트 감시 개선
- Watched inode 관리 최적화

## Upcoming Features
- 재시작 가능한 권한 이벤트 (2개 fd: 제어 + 큐)
- 네임스페이스 트리 감시 (listns() 연동)
- 제어 그룹(cgroup) 감시 지원

## HSM Issues
사전 콘텐츠 이벤트와 파일 시스템 동결 사이의 교착 상태 문제. 매핑된 범위에 페이지 폴트 발생 시 HSM 데몬이 채우려 할 때 발생.

## Connections
- [[LinuxKernel]] — 적용 분야
- [[AmirGoldstein]] — 주요 개발자
- [[ChristianBrauner]] — namespace 감시 논의
