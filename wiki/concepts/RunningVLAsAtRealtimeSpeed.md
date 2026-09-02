---
title: "Running VLAs at Real-time Speed"
type: concept
tags: [VLA, serving, latency]
sources: [ponderpounce-2608-24115-references]
last_updated: 2026-09-02
---

# Running VLAs at Real-time Speed

실시간 VLA serving은 model-call p50만이 아니라 sensor-to-actuator deadline, p95/p99 jitter, action chunk horizon, concurrent throughput, memory, power 및 fallback behavior를 함께 측정해야 한다. [[PonderPounce]]의 cache/fused-kernel profile도 이 전체 system metric으로 해석해야 한다.
