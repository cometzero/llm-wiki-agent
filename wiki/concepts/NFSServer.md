---
title: "Linux NFS Server"
type: concept
tags: [linux, filesystem, networking]
sources: [lwn-weekly-edition-2026-10-22-1100612]
last_updated: 2026-10-30
---

## Overview

Linux NFS server는 network filesystem 요청을 처리하며 local filesystem·RPC·cache·접근 제어 사이의 경계를 연결한다. 2026-10-22 LWN 보도는 LOCALIO, remote copy, cache 제어, delegation, 서명된 file handle과 netlink 관리의 변화를 정리한다.

## Boundaries

- LOCALIO는 같은 host의 client/server 사이에서 경로를 줄이는 최적화이며 모든 원격 요청에 적용되는 것은 아니다.
- Delegation은 client cache를 허용하는 protocol 상태다. 충돌 시 회수·갱신 알림과 metadata 관측이 정확성의 일부다.
- File-handle 서명과 TLS는 각각 위조·추측과 전송 중 노출이라는 서로 다른 위험을 다룬다.
- 관리 API 전환과 Rust/XDR 코드 생성 계획은 이미 배포된 기본 동작과 구분해야 한다.

## Connections

- [[LinuxKernel]] — VFS, RPC, filesystem 및 kernel 관리 인터페이스.
- [[Rust]] — protocol parsing의 향후 안전성 개선 방향.
- [[lwn-weekly-edition-2026-10-22-1100612]] — 구현 현황과 향후 계획의 근거.
