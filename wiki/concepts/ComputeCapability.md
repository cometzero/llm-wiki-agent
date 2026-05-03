---
title: "Compute Capability"
type: concept
tags:
  - CUDA
  - GPU
  - HardwareVersioning
date: 2026-05-03
sources:
  - cuda-refresher-the-cuda-programming-model-nvidia-technical-blog
---

## 개요
[[Compute Capability]]는 [[GPU]] 하드웨어의 기능 계층 정보를 나타내는 버전 신호로, 지원 명령어/기능, 컴파일 타깃 선택, 실행 특성 판단의 기준이 된다.

## 형식
- 일반적으로 X.Y 형식
  - X: 주 개정
  - Y: 부 개정(점진적 개선)

## 적용
- 런타임에서 어떤 기능이 사용 가능한지 판단
- 기능 미지원 이슈 회피, 성능 특성 반영

## 실무적 의미
동일한 커널 코드라도 [[Compute Capability]]가 다르면 최적화 전략이나 사용 가능한 경로가 달라질 수 있어, 배포·호환성 검토에서 필수 점검 항목이다.