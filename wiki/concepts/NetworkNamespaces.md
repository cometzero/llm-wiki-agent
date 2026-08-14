---
title: "Network Namespaces"
type: concept
tags: [linux, networking, containers, isolation]
sources: [lwn-weekly-edition-2026-08-06-1086134]
last_updated: 2026-08-14
---

## Summary
[[NetworkNamespaces]]는 Linux namespace mechanism으로 network devices, routing tables, firewall rules, sockets 등을 process group별로 격리한다. Container와 multi-tenant system의 기본 isolation boundary이며, 다른 namespace를 관찰하거나 BPF program을 적용하는 작업은 capability, target namespace context, verifier 및 LSM policy를 명확히 다뤄야 한다.

## Connections
- [[lwn-weekly-edition-2026-08-06-1086134]] — BPF를 이용한 cross-namespace observation
- [[BPF]] — programmable observability와 networking hook
- [[BPFDirectPacketSending]] — BPF networking data path의 인접 주제
