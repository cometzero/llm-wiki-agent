---
title: "RMR and BRMR Block Replication"
type: concept
tags: [storage, rdma, block-device]
sources: [lwn-weekly-edition-2026-06-25-1078380]
last_updated: 2026-07-03
---

RMRBRMR는 Reliable Multicast-like RDMA transport와 block replication layer를 결합해 compute host를 우회하는 single-hop durable block replication을 제공하려는 커널 모듈 설계다. Cloud provider가 낮은 overhead로 durable block device를 노출하는 방법과 DRBD류 접근과의 trade-off를 설명한다.

## Connections
- [[LinuxKernel]]
