---
title: "On-Device Inference (VLA/Navigation/Embodied AI)"
type: concept
tags: [edge, deployment, latency, quantization, NPU, memory-orchestration, heterogeneous-hardware]
sources: [qwen-robotnav-2606-18112, embodied-cpp-2607-02501-references]
last_updated: 2026-07-08
---

## Overview
On-device inference는 cloud round-trip 없이 edge device(NVIDIA Jetson, mobile robot, automotive platform, NPU/accelerator 등)에서 LLM/VLM/VLA 추론을 실행하는 deployment 방식이다. 기존 [[Qwen-RobotNav]] context에서는 FP8 quantization과 TensorRT 기반 Jetson Thor deployment가 핵심이었고, 2026-W28 [[Embodied-cpp]] update에서는 robot closed-loop runtime, heterogeneous hardware scheduling, model-weight memory bottleneck까지 범위가 확장되었다.

## Key Techniques
- **FP8 / low-bit quantization**: memory와 compute footprint를 줄인다.
- **TensorRT / backend acceleration**: GPU/edge inference 최적화.
- **Hierarchical weight orchestration**: [[H2O]]처럼 model weights가 KV cache보다 bottleneck이 되는 setting에서 memory residency를 줄인다.
- **Zero-copy I/O-compute parallelism**: data movement overhead와 latency를 줄인다.
- **Heterogeneity-aware inference planning**: CPU/GPU/NPU 등 다양한 hardware target에 module을 배치한다.
- **Latency-first scheduling**: robot closed-loop에서는 throughput보다 low latency/low jitter가 중요하다.

## Why It Matters
- 자율주행과 robot navigation은 low-latency real-time response가 필요하다.
- On-device inference는 privacy, network independence, deterministic latency에 유리하다.
- Safety-critical application에서는 average latency뿐 아니라 tail latency와 jitter 보장이 중요하다.
- VLA/WAM deployment에서는 perception, backbone, action head, world prediction branch가 서로 다른 rate/device에서 실행될 수 있다.

## Related Concepts
- [[H2O]] — memory orchestration 관련 연구
- [[NPU]] — target hardware
- [[LatencyFirst]] — 설계 우선순위
- [[HeterogeneousHardware]] — 지원 대상 hardware
- [[MultiRateExecution]] — embodied model module scheduling

## Connections
- [[Qwen-RobotNav]] — edge deployment와 navigation benchmark context
- [[AgenticNavigation]] — fast trajectory module이 edge inference benefit을 받는 navigation architecture
- [[Benchmark]] — NAVSIM 등 closed-loop evaluation은 real-time inference를 요구
- [[Embodied-cpp]] — VLA/WAM용 주요 on-device/heterogeneous deployment runtime
- [[vla.cpp]] — predecessor on-device VLA runtime
- [[Execution-State Capsules]] — on-device physical AI serving 기법
