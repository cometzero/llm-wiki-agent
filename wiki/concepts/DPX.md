---
title: "DPX"
type: concept
tags:
  - Hopper
  - InstructionSet
  - DynamicProgramming
  - GPU
sources:
  - nvidia-hopper-아키텍처-심층-분석하기-nvidia-technical-blog
last_updated: 2026-05-03
---

## Definition
[[DPX]]는 동적 프로그래밍 계열 커널을 가속하기 위한 Hopper 계열의 특수 명령어/명령 집합 경향으로 설명된다.

## 의미
- 기존 명령어 대비 특정 DP 루프(예: 스미스-워터맨 등)에서 반복적 하위 문제 결합 구조를 빠르게 처리한다.
- 본 소스에서는 최대 7배 수준의 가속 여지를 제시하며 알고리즘 중심 가속의 예시를 제시한다.

## 활용 예시
- 유전체학, 단백질 염기서열 처리
- 로보틱스 경로 탐색(예: 플로이드-워셜류)
- 대량 그래프/최적화 클래스의 반복 계산

## 관계
- [[H100]]의 산술 유닛 확장과 조합되어 AI 외 특수 워크로드에도 파급 효과를 가진다.
- [[AsynchronousExecution]]/메모리 스케줄링과 함께 병렬 커널 설계에 녹아든다.
