---
title: "ABot-N1: 범용 Visual Language Navigation foundation model을 향하여 — References"
type: source
tags: [references, visual-language-navigation, vln, embodied-ai]
date: 2026-07-15
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W29/abot-n1-visual-language-navigation-2607-10383/references.md
source_hash: 764e5a3d6b3e668b
---

## Summary
ABot-N1(2607.10383) 원문 References 섹션을 기준으로, Visual Language Navigation 연구의 학습에 중요한 reference를 선별한 요약이다. Semantic Scholar references endpoint에서 안정적인 목록을 얻지 못해 원문 직접 확인이 필요했다.

## 읽는 순서 제안
1. **benchmark/metric 논문** — 결과표의 의미를 파악한다
2. **backbone/modeling 논문** — architecture novelty를 분리한다
3. **closed-loop 또는 deployment 관련 논문** — 실제 적용 리스크를 점검한다

## 주요 레퍼런스 분류

### Benchmark/Metric 논문
VLN/VLA 평가 기준을 정의한 핵심 벤치마크 논문群

### Backbone/Modeling 논문
[[ABot-N1]]의 slow-fast VLM→pixel goal→continuous waypoint 구조와 관련된 아키텍처 설계 논문群

### Closed-loop/Deployment 논문
[[VLA]]의 실제 로봇 적용 및 배포 관련 논문群

##Connections
- [[ABot-N1]] — 메인 페이퍼; 본 레퍼런스 요약의 대상
- [[ABot-N0]] — ABot-N1의前身 버전으로 관련 아키텍처 발전 연속성
- [[VLA]] — Vision-Language-Action 통합 모델; VLN 연구와 핵심 관련
- [[VLN]] — Visual Language Navigation; 본 레퍼런스 요약의 대상 분야
- [[WorldActionModel]] — WAM survey 관련; navigation 연구와 연결 가능
- [[Qwen-RobotNav]] — [[Qwen3VL]] 기반 navigation 연구; VLN-CE, NAVSIM 벤치마크 공유
- [[PolicyTrim]] — VLA action efficiency 관련; action chunk utilization 연구와 연결
- [[ObjectCentricResidualRL]] — zero-shot sim-to-real transfer 연구; navigation domain adaptation과 연결
- [[GR00TN1]] — NVIDIA의 VLA 연구; [[VLA]] backbone으로 관련
- [[π0.5]] — Physical Intelligence의 VLA; navigation capability 연구와 연결
- [[OpenVLA]] — open-source VLA; ABot-N1의 foundation model 비교 대상으로 관련

## Contradictions
- 없음
