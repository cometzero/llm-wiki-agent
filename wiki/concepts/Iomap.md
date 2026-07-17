---
title: "Iomap"
type: concept
tags: [kernel, filesystem, io]
sources: [lwn-weekly-edition-2026-07-09-1080835]
last_updated: 2026-07-17
---

## Definition
Linux 커널의 파일시스템 I/O 추상화 레이어. 파일 offset을 block device extent로 매핑하여 파일시스템 간 공통 코드 재사용.

## 구조
```
struct iomap {
    u64 addr;       /* 매핑의 디스크 오프셋 */
    loff_t offset;  /* 매핑의 파일 오프셋 */
    u64 length;     /* 매핑 길이 */
    u16 type;       /* 매핑 유형 */
    u16 flags;      /* 매핑 플래그 */
    // ...
};
```

## 매핑 유형
- `IOMAP_MAPPED` — 일반 매핑
- `IOMAP_HOLE` — 할당되지 않은 영역
- `IOMAP_DELALLOC` — 지연 할당
- `IOMAP_UNWRITTEN` — 미작성 영역

## 콜백 구조
- `iomap_begin()` — 파일시스템이 매핑 정보 제공
- `iomap_end()` — 작업 완료 후 정리

## 사용 파일시스템
XFS, ext4, btrfs, exfat, minix 등 변환 진행 중.

## Connections
- [[Filesystem]] — 상위 추상화
- [[PageCache]] — 버퍼드 I/O
- [[DirectIO]] — 직접 I/O
- [[Dax]] — 영구 메모리 접근
- [[FsVerity]] — 무결성 지원 추가됨
