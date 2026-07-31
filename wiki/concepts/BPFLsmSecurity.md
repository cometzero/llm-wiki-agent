---
title: "BPF LSM Security"
type: concept
tags: [linux, kernel, bpf, security]
sources: [lwn-weekly-edition-2026-07-23-1083123]
last_updated: 2026-07-31
---

## Summary
BPF LSM policy가 공격자나 misconfiguration에 의해 우회·변조되지 않도록 보호하는 Linux security topic이다.

## Notes
BPF LSM은 security hook에 programmable policy를 넣을 수 있게 하지만, policy attachment나 map/program state가 tamper되면 방어 체계 자체가 공격 표면이 된다. LWN 2026-07-23은 BPF LSM을 runtime security boundary로 사용할 때 integrity guard가 필요함을 보여 준다.

## Connections
- [[BPF]] — programmable security and tracing substrate
- [[KernelHardening]] — broader Linux hardening context
- [[lwn-weekly-edition-2026-07-23-1083123]] — BPF LSM tamper-resistance source
