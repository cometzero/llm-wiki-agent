---
title: "Mshare"
type: concept
tags: [kernel, memory-sharing, system-call]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# Mshare

mshare는 여러 프로세스가 공유 메모리 영역뿐 아니라 해당 페이지 테이블도 함께 사용할 수 있게 하려는 Linux 커널 제안이다.

## 목적
수천 개의 프로세스가 동일한 메모리 영역을 공유할 때, 각 프로세스의 페이지 테이블 총 크기가 공유 메모리 자체를 넘어설 수 있다. 이를 해결하기 위해 페이지 테이블도 공유한다.

## 2026 API 변경 (Anthony Yznaga)

파일시스템 기반 `msharefs` 대신 시스템 호출 API로 돌아감:
- `mshare_create()` — 공유 영역 생성, 파일 디스크립터 반환
- `mshare_attach()` — 프로세스 주소 공간에 매핑
- `mshare_map()` — 백킹 스토어 설정

### 소유권 모델
생성 프로세스가 종료하거나 fd를 닫으면 영역과 모든 매핑이 제거된다.

## 과제
- 페이지 테이블 순회와 잠금 처리
- RSS 통계 올바르게 노출
- 소유권 이전 메커니즘
- TLB 플러시 처리

## 사용 사례
- HPC 프로세스 간 리소스 공유
- Android Zygote 모델과의 통합 가능성

## Related Pages
- [[MemoryManagement]]
- [[HugeTLBFS]]
