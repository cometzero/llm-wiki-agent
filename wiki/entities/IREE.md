---
title: "IREE"
type: entity
tags:
  - MLIR
  - LLVM
  - Compiler
  - AMD
  - Runtime
  - HAL
last_updated: 2026-05-10
sources:
  - unveiling-the-inner-workings-of-iree-an-mlir-based-compiler-for-diverse-h-w
---

## 핵심 개요

[[IREE]](Intermediate Representation Execution Environment)는 ML 모델 배포를 위해 [[MLIR]] 기반으로 설계된 컴파일러/실행 스택이다.

## 핵심 정체성

- 목표: 한정된 모델 코드베이스를 CPU, [[GPU]], [[NPU]] 등으로 확장 가능한 방식으로 배포.
- 핵심 방식: [[Host-Device Programming Model]] 기반 스케줄링.
- 장점: 아키텍처 불가지론성, 오픈소스 확장성, 디버깅 가능한 단계별 변환.

## 주요 구성 요소

- 입력: [[PyTorch]], [[TensorFlow]], [[TOSA]], [[ONNX]] 같은 상위 표현.
- 변환: [[MLIR]] 다이얼렉트 기반 하향(Progressive Lowering).
- 실행: [[HAL]] 통해 디바이스 바인딩.
- 아티팩트: [[VMFB]](VM File) 생성 후 런타임 해석.

## 역사 및 운영

- 시작은 [[Google]] 기반 오픈소스 기획에서 출발해 [[Nod.ai]] 기여를 거쳐 [[AMD]] 계열에서 이식/최적화가 진행되었다는 기술 문맥이 반복적으로 등장한다.
- 오픈 소스 공개 진행: [[GitHub]] 커뮤니티와 공개 PR/리뷰/토론을 통한 공개 개발.

## 성능 및 제한

- 대부분의 모델에서 시작 가능한 성능 기반을 제공.
- 최고 성능은 추가 튜닝(디스패치/휴리스틱/트랜스폼) 단계가 필요한 경우가 있음.

## 실무 메시지

- [[IREE]]는 "최초 동작성 + 가시성 높은 디버깅 + 점진적 최적화"를 중시한 실용형 스택으로 이해한다.