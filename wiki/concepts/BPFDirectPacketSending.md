---
title: "BPF Direct Packet Sending"
type: concept
tags: [kernel, bpf, networking]
sources: [lwn-weekly-edition-2026-07-16-1081915]
last_updated: 2026-07-24
---

## Definition
BPF 직접 패킷 전송(BPF Direct Packet Sending)은 [[BPF]] 프로그램이 나가는 네트워크 패킷을 직접 생성할 수 있게 하는 커널 기능이다.

## Overview
[[Tetragon]]과 같은 BPF 기반 보안 모니터링 도구는 user-space agent와 ring buffer를 통해 통신한다. BPF 프로그램이 remote server와 직접 통신할 수 있다면 훨씬 효율적이다.

### 구현 접근법
- [[Netpoll]] 인프라 활용: 어떤 컨텍스트에서든 커널 코드가 패킷 전송 가능
- bpf_netpoll_create()로 netpoll 컨텍스트 생성
- bpf_netpoll_send_udp()로 UDP 패킷 전송
- 커널의 기존 cryptography API와 결합하여 암호화 가능

### 논쟁
- **UDP vs TCP**: UDP는 "evil"이라는 피드백, TCP는 네트워킹 담당자가 더 선호
- **netpoll 우회**: 일반 네트워킹 스택을 우회하므로 대역폭 관리 제한
- Alexei Starovoitov: "netpoll이 이미 커널에서 쓰이고 있으므로 TCP를 선호할 이유 없음"

### 이후 발전
2026년 7월 6일, Tardy 등은 netpoll 대신 UDP 커널 소켓을 생성하고 사용하는 새 패치 세트 발표

## Connections
- [[BPF]] — 기술 기반
- [[Tetragon]] — 주요 사용 사례
- [[Netpoll]] — 백엔드 인프라
- [[SongLiu|Song Liu]], [[MaheTardy|Mahé Tardy]], [[LiamWiseheart|Liam Wiseheart]] — 개발자
