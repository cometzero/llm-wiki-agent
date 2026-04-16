---
title: "📌 Userspace Assisted Scheduling (UAS) via SKITS는 무엇을 해결하고자 하는가?"
type: source
tags: [lpc2025]
date: 2026-04-16
source_file: raw/LPC2025/Userspace Assisted Scheduling via Sc... John Stultz, Mr Qais Yousef, Steven Rostedt, Vincent Guittot.md
---

## Summary
리눅스 스케줄러가 다양한 하드웨어 및 워크로드 요구사항을 충족하며 상호작용성과 처리량 간의 균형을 맞추기 어려운 문제를 해결하기 위해 사용자 공간에서 스케줄링에 더 많은 정보를 제공하는 방법을 제시합니다. 리눅스 커널의 고질적인 문제인 인터랙티비티와 처리량(Throughput) 간의 불균형을 해소하기 위한 획기적인 사용자 공간 지원 스케줄링(Userspace Assisted Scheduling) 프레임워크 제안입니다. 이 콘텐츠는 기존 커널의 스케줄러가 가지는 서버 중심의 '처리량 편향(throughput bias)'을 극복하고, 안드로이드와 같은 하이브리드 환경에서 레이턴시(Latency)를 보장하며 모든 워크로드를 효과적으로 처리하는 새로운 로드맵을 제시합니다. 특히, Apple의 성공적인 QoS(Quality of Service) 모델을 벤치마킹하여 User Interactive, User Initiated, Utility, Background와 같은 간단한 클래스 기반의 사용자 인터페이스를 도입하고, API 사용 없이 설정 파일 기반으로 QoS 힌트를 제공하는 '제로 API 채택 전략'을 통해 개발 복잡도를 최소화하는 실용적인 통찰을 얻을 수 있습니다.

## Key Claims
- 리눅스는 서버부터 임베디드 시스템, 안드로이드의 하이브리드 시스템까지 다양한 하드웨어와 워크로드를 지원해야 한다.
- 역사적으로 서버 시장이 주요 기여자였기 때문에, 리눅스 커널에는 처리량(throughput) 편향이 존재한다.
- 시간이 지남에 따라 개선되고 있지만, 상호작용성(interactivity)이 중요해지면서 처리량과 상호작용성 간의 균형을 맞추는 것이 매우 어려워지고 있다.
- 애플리케이션들이 구식(archaic) 방식으로 작성되어 마치 자신이 시스템의 유일한 사용자인 것처럼 가정하는 경향이 있다.

## Key Quotes
> "3. 시간이 지남에 따라 개선되고 있지만, 상호작용성(interactivity)이 중요해지면서 처리량과 상호작용성 간의 균형을 맞추는 것이 매우 어려워지고 있다." — extracted from the source narrative.

## Connections
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[UserspaceAssistedScheduling]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
