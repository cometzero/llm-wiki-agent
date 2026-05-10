---
title: "AIG Shark"
type: entity
tags:
  - AMD
  - ML
  - Compiler
  - Deployment
  - Runtime
last_updated: 2026-05-10
sources:
  - unveiling-the-inner-workings-of-iree-an-mlir-based-compiler-for-diverse-h-w
---

## 핵심 개요

[[AIG Shark]]는 [[AMD]] 생태계에서 모델 배포를 위해 제시된 소프트웨어 스택명으로, [[Shark Tank]], [[Shark Turbine]], [[IREE]], [[Shark Runtime]], [[Shark Studio]]로 구성되는 실용형 파이프라인 계열로 설명된다.

## 구성

- [[Shark Tank]]: PyTorch 등 모델 그래프를 컴파일러 적합 형태로 정규화.
- [[Shark Turbine]]: 변환/컴파일 흐름의 상위 계층 오케스트레이션.
- [[Shark Runtime]] (Shortfin): 아티팩트 실행 및 캐시/배치/배포 운영.
- [[Shark Studio]]: 워크플로우 패키징과 사용자 배포 입출력 레이어.

## 역할

- ML 모델을 엔드투엔드로 추론 가능한 형태로 전환하기 위한 운영형 연계 계층.
- [[IREE]] 컴파일 결과물의 배포 실무를 가속화하는 소프트웨어 번들.
