---
title: "BPF Tracepoints"
type: concept
tags: [linux, kernel, bpf, observability]
sources: [lwn-weekly-edition-2026-07-23-1083123]
last_updated: 2026-07-31
---

## Summary
[[BPF]] program을 kernel tracepoint에 붙여 production observability와 debugging을 수행하는 커널 확장 메커니즘이다.

## Notes
여러 tracepoint에 program을 붙이는 기능은 tracing boilerplate와 overhead를 줄이고, system behavior를 더 넓게 관찰할 수 있게 한다. verifier, attachment lifetime, permissions가 맞물려 있어 production debugging과 security tooling 모두에 영향을 준다.

## Connections
- [[BPF]] — programmable kernel extension base
- [[lwn-weekly-edition-2026-07-23-1083123]] — multiple tracepoint attachment discussion
