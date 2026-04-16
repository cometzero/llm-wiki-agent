---
title: "📌 TinyML 워크로드를 Zephyr RTOS에 배포하고 최적화하는 방법은 무엇인가?"
type: source
tags: [oss2025-japan, safety]
date: 2026-04-16
source_file: raw/OSS2025_Japan/TinyML at the Edge_ Deploying and Optimizing AI Workloads on Zephyr RTOS - Amandeep Singh, Welzin.md
---

## Summary
TinyML 워크로드를 Zephyr RTOS에 배포하고 최적화하기 위해 다양한 추론 엔진(TensorFlow Lite Micro, MicroTVM, MLAN 등)을 활용하고, AutoML, LLE(Linkable Loadable Extensions)를 통해 모델을 동적으로 업데이트하며, Zephyr RTOS의 빌드 시스템, 보안, 테스트 프레임워크 기능을 이용하는 것이 핵심입니다. TinyML은 센서 데이터를 클라우드로 전송하지 않고 저비용 임베디드 장치(마이크로컨트롤러)에서 경량 AI 모델을 직접 실행하여 실시간 추론을 수행하는 분야입니다. Zephyr RTOS는 낮은 전력 소비, 확장된 통신 프로토콜 지원, 모듈성, 보안 기능 덕분에 TinyML 구현에 최적화된 OS입니다.

## Key Claims
- 본 발표는 Zephyr RTOS 환경에서 TinyML 워크로드를 운영하고 관리하는 실용적인 엔드투-엔드 경로를 제시한다.
- 사용 사례에 따라 최적의 런타임(추론 엔진)을 선택하는 방법
- 이러한 런타임을 AutoML 흐름과 통합하는 방법
- LL ext(Linkable Loadable Extensions)를 사용하여 런타임에 모델을 업데이트하는 방법

## Key Quotes
> "TinyML 워크로드를 Zephyr RTOS에 배포하고 최적화하기 위해 다양한 추론 엔진(TensorFlow Lite Micro, MicroTVM, MLAN 등)을 활용하고, AutoML, LLE(Linkable Loadable Extensions)를 통해 모델을 동적으로 업데이트하며, Zephyr RTOS의 빌드 시스템, 보안, 테스트 프레임워크 기능을 이용하는 것이 핵심입니다." — extracted from the source narrative.

## Connections
- [[AmandeepSingh]] — directly referenced in or strongly associated with this source.
- [[LinuxKernel]] — directly referenced in or strongly associated with this source.
- [[Zephyr]] — directly referenced in or strongly associated with this source.
- [[AmandeepSingh]] — directly referenced in or strongly associated with this source.
- [[TinyML]] — one of the main technical themes discussed by this source.
- [[FunctionalSafety]] — one of the main technical themes discussed by this source.

## Contradictions
- No explicit contradiction with existing wiki pages was identified during this first ingest pass.
