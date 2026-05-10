---
title: "Host-Device Programming Model"
type: concept
tags:
  - Runtime
  - Scheduler
  - Compiler
  - MLIR
  - IREE
last_updated: 2026-05-10
sources:
  - unveiling-the-inner-workings-of-iree-an-mlir-based-compiler-for-diverse-h-w
---

## 정의

[[Host-Device Programming Model]]은 컴퓨팅 파이프라인을 호스트가 큰 단위의 스케줄링/의존성 조정 역할을 수행하고, 디바이스는 전달받은 명령 흐름을 연속 실행하는 구조로 분해하는 실행 모델이다.

## 동작 방식

- 컴파일러는 텐서 연산을 디스패치 단위로 분할한다.
- 디스패치 간 의존성 그래프를 구성한다.
- 호스트는 이를 바탕으로 실행 순서와 명령 버퍼를 계획한다.
- 디바이스는 명령 버퍼를 받아 커널을 실행한다.

## IREE 맥락

[[IREE]]는 이 모델을 텐서 워크로드 배포의 핵심으로 사용한다. 호스트는 실행 순서를 조정하고, 디바이스는 연속성 높은 배치 실행을 유지한다.

## 장점

- 하드웨어 간 이식성 향상
- 실행 오버헤드 예측성 증가
- 디버깅 가능한 의존성 경로 확보

## 비교

GPU 중심의 기존 모델과 달리 CPU를 디바이스처럼 취급해 통합 처리할 수 있다는 점에서 [[MLIR]] 기반 컴파일 스택 확장성에 유리하다.