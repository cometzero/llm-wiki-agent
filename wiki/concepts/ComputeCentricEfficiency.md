---
title: "Compute-Centric Efficiency"
type: concept
tags: [VLA, efficiency, optimization]
sources: [policytrim-2606-22540]
last_updated: 2026-06-24
---

## Definition
Compute-centric efficiency는 VLA deployment 속도를 빠르게 하기 위한 전통적 접근법으로, model pruning, token reduction, quantization, hardware optimization 등으로 **per-step inference latency를 줄이는 데 집중**한다.

## 한계
Compute-centric efficiency만으로는 VLA deployment의 실제 병목(반복적 재계산, 불필요한 micro-action)을 해결할 수 없다. PolicyTrim은 이를 보완하는 **intrinsic policy efficiency** 관점을 제시한다.

## 연결
- [[IntrinsicPolicyEfficiency]] — compute-centric efficiency와 구분되는 새로운 패러다임
- [[PolicyTrim]] — compute-centric efficiency가 아닌 policy efficiency 최적화
- [[VLA]] — 효율화 대상
