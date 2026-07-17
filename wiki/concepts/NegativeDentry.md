---
title: "Negative Dentry"
type: concept
tags: [kernel, filesystem, vfs, caching]
sources: [lwn-weekly-edition-2026-07-09-1080835]
last_updated: 2026-07-17
---

## Definition
존재하지 않는 파일을 나타내는 [[DentryCache]] 항목. 경로명 조회 단락(short-circuit) 최적화.

## 문제점
- 수백만 개의 negative dentry가 디렉토리에 축적 가능
- `fsnotify_set_children_dentry_flags()` 호출 시 soft-lock 발생
- 참조 횟수 오버플로 (d_lockref 카운트 필드)
- 해시 체인 과도한 길어짐

## 해결 방안 논의
1. Negative dentry를 `d_children` 목록 끝으로 이동
2. `cond_resched()` 호출 추가
3. `dentry-negative` sysfs knob 활용
4. 디렉터리당 경험적 제한 (提案: 1,000개)

## 사용자 공간 해결
[[ChristianBrauner]]: "사용자 공간이 관리를 담당해야 한다"

## Connections
- [[DentryCache]] — 상위 캐시 시스템
- [[VFS]] — 가상 파일시스템
- [[PathnameLookup]] — 경로명 조회
- [[LSFMMbpfSummit2026]] — 문제 제기 장소
