---
title: "Grace Hopper Superchip"
type: entity
tags:
  - NVIDIA
  - Grace
  - Hopper
  - CPU-GPU
sources:
  - nvidia-hopper-아키텍처-심층-분석하기-nvidia-technical-blog
last_updated: 2026-05-03
---

## Definition
[[GraceHopperSuperchip]]는 CPU+GPU 결합형 아키텍처로, [[H100]] 계열의 대규모 AI/HPC 처리에서 링크 대역폭과 워크로드 확장성을 높이기 위한 플랫폼 요소이다.

## 핵심 포인트
- [[H100]]와 NVIDIA Grace CPU 결합을 통해 대규모 데이터 이동 대역폭을 확장한다.
- 텍스트에서 총 900GB/s급 연결 성능(및 기존 대비 높은 배수 향상)이 제시되어, 테라바이트급 응용에 유리하다는 점을 시사한다.
- [[PCIeGen5]] 대비 빠른 동기화/인터커넥트 경로를 강조한다.

## 관계
- [[NVIDIA]] 데이터센터 AI 전략에서 연산뿐 아니라 시스템 인터커넥트 효율을 함께 다루는 구조로 해석된다.
- 추론 성능의 ‘처리량 + 대역폭 + 지연 안정성’ 트라이디 균형 측면에서 중요한 축이다.
