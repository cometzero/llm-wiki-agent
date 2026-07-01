---
title: "On-Device Inference (VLA/Navigation)"
type: concept
tags: [edge, deployment, latency, quantization]
sources: [qwen-robotnav-2606-18112]
last_updated: 2026-07-01
---

## Summary
On-device inference for VLA navigation models involves deploying large vision-language models on edge hardware (e.g., NVIDIA Jetson Thor) with quantization and acceleration. Qwen-RobotNav evaluates both cloud and edge deployment, using FP8 quantization and TensorRT optimization on Jetson Thor.

## Key Techniques
- **FP8 Quantization**: Reduces memory and compute footprint
- **TensorRT Acceleration**: GPU inference optimization
- **Hardware**: NVIDIA Jetson Thor (automotive edge platform)

## Why It Matters
- Autonomous driving and robot navigation require low-latency, real-time responses
- On-device inference avoids cloud round-trip latency
- Safety-critical applications need deterministic latency guarantees

## Connections
- [[Qwen-RobotNav]] — evaluates on-device deployment
- [[AgenticNavigation]] — fast trajectory module benefits from edge inference
- [[Benchmark]] — NAVSIM closed-loop evaluation requires real-time inference
