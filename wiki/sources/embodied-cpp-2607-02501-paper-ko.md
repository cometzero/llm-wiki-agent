---
title: "Embodied.cpp: 이기종 로봇을 위한 Embodied AI 모델의 휴대형 추론 런타임"
type: source
tags: [huggingface-weekly, vla, robotics]
date: 2026-07-08
source_file: raw/Robotics/HuggingFaceWeeklyPapers/2026-W28/embodied-cpp-portable-inference-runtime-2607-02501/paper-ko.md
source_hash: 81ad485627a82ec11fe5331b0b1dcf0a2f619abb9b7bfac5373b37b48724052e
---

## Summary
Embodied.cpp 논문의 한국어 기술 번역이다. VLA/WAM deployment를 위한 multi-rate execution, latency-first batch-1 inference, extensible embodied I/O, five-layer C++ runtime architecture를 설명하고 HY-VLA/π0.5/WAM block 평가 결과를 보존한다.

## Key Claims
- Embodied deployment는 일반 LLM/VLM serving과 다른 runtime contract를 요구한다.
- VLA와 WAM은 공통 backbone path를 공유하지만 head, prediction branch, deployment adapter가 달라 plug-in boundary가 필요하다.
- HY-VLA 100.0%, π0.5 91.0% success rate와 LingBot-VA block memory 312.2→88.1 MiB 결과를 제시한다.

## Key Quotes
> "Embodied AI 모델은 이제 Vision-Language-Action(VLA) 모델과 World-Action Model(WAM)까지 확장되었지만, 실제 배포는 모델별 Python stack, backend 가정, 로봇 측 glue code에 파편화되어 있다." — Abstract 번역
> "Embodied.cpp는 이러한 요구를 직접 겨냥한 portable C++ inference runtime이다." — Introduction 번역

## Connections
- [[Embodied-cpp]] — VLA/WAM용 portable C++ inference runtime
- [[WAM]] — World-Action Model 계열 deployment target
- [[MultiRateExecution]] — perception/backbone/action head refresh rate 분리
- [[LatencyFirstBatch1]] — robot closed-loop batch-1 inference 최적화

## Contradictions
- 없음.
