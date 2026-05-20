---
title: "VLA Policy (Vision-Language-Action Policy)"
type: concept
tags: [robotics, vla, foundation-model, embodied-ai]
sources: [physbrain-1-0-2605-15298-references]
last_updated: 2026-05-20
---

## Overview
VLA(Vision-Language-Action) Policy는 비전, 언어, 행동 생성을 통합하는 로보틱스 정책 학습 패러다임. VLM(Vision-Language Model)의 사전 지식을 로봇 제어에 전이하여, generic visual understanding과 reasoning 능력을 활용한 generalist robotic policy를 구축한다.

## Key Characteristics
- Vision encoder + Language model + Action head의 통합 구조
- Pretrained VLM의 zero-shot 또는 fine-tuned transfer
- Physical commonsense prior 주입으로 out-of-domain robustness 향상 가능

## Representative Models
- [[OpenVLA]] — VLM 기반 robot policy 대표 baseline
- [[Pi0]] — [[PhysicalIntelligence]]의 generalist action generation
- [[GR00T-N1]] — [[NVIDIA]]의 robotics foundation model

## Evaluation Benchmarks
- [[SimplerEnv]] — CoRL 2024, out-of-domain generalization 평가
- [[LIBERO]] — NeurIPS 2023, long-horizon manipulation 평가
- [[RoboCasa]] — RSS 2024, household manipulation 평가

## Connections
- [[physbrain-1-0-2605-15298]] — VLA policy에 physical commonsense supervision을 주입하는 연구
- [[OpenVLA]], [[Pi0]], [[GR00T-N1]] — 주요 VLA policy baseline들
- [[SimplerEnv]], [[LIBERO]], [[RoboCasa]] — 평가 벤치마크