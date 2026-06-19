---
title: "Spawn Template"
type: concept
tags: [kernel, process, optimization]
sources: [lwn-weekly-edition-2026-06-11-1076254]
last_updated: 2026-06-19
---

## Overview
Linux 커널에 제안된 프로세스 생성 최적화 API. 동일한 실행 파일을 반복 실행하는 애플리케이션의 fork()/exec() 패턴을 가속화한다.

## Background
fork()는 전체 프로세스 상태(메모리 포함)를 복사해야 하는 비용이 많이 드는 시스템 호출이다. fork()+exec() 패턴은 복사 후 즉시 모든 것을 삭제하므로 비효율적이다.

## Proposed API
- spawn_template_create() — 실행 파일 템플릿 생성
- spawn_template_spawn() — 템플릿을 사용한 프로세스 생성

벤치마크 결과: 약 2% 성능 개선

## Developer Discussions
- Mateusz Guzik: fork()+exec() 패턴을 완전히 폐기해야 한다고 주장
- Christian Brauner: pidfd 기반으로 새로운 posix_spawn() 구현을 선호
- Linus Torvalds: 조심스러운 찬성

## Connections
- [[LinuxKernel]] — 적용 분야
- [[PosixSpawn]] — 관련 API
- [[LiChen]] — 제안자
