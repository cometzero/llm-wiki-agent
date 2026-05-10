---
title: "VMFB"
type: concept
tags:
  - IREE
  - VM
  - Runtime
  - BinaryArtifact
  - Deployment
last_updated: 2026-05-10
sources:
  - unveiling-the-inner-workings-of-iree-an-mlir-based-compiler-for-diverse-h-w
---

## 정의

[[VMFB]](VM File)는 [[IREE]]가 생성하는 최종 배포 아티팩트로, 디바이스별 실행 가능한 바이너리 조합이 VM 관점에서 링크된 형태다.

## 구성

- 디스패치 대상 코드를 각 장치 형식으로 번역한 바이너리 또는 중간 표현.
- [[VM]] 실행 경로에서 로딩될 수 있도록 패키징된 형태.

## 장점

- 런타임 배포가 간편하고 환경 의존성이 낮다.
- 동일 모델 배포가 CPU/GPU/NPU 경로로 반복 재사용되기 수월하다.

## 제한

- 아웃-오브-박스 성능은 타깃별 고도로 최적화된 전용 커널 대비 추가 조정이 필요할 수 있다.
