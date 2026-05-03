---
title: "Neural Network Quantization & Number Formats From First Principles"
type: source
tags: [Quantization, NumberFormats, INT8, FP16, FP8, BF16, NVIDIA, Hardware]
date: 2026-05-03
source_file: raw/Technology/LilysAI/neural-network-quantization-number-formats-from-first-principles.md
sources:
  - neural-network-quantization-number-formats-from-first-principles
last_updated: 2026-05-03
---

## Summary
이 문서는 [[NeuralNetworkQuantization|신경망 양자화]]와 [[NumberFormat|숫자 형식]]을 첫 원리에서 설명한다. 핵심 주장은 정확도를 유지하면서 에너지와 면적 효율을 높이려면, [[INT8]]/[[FP16]]/[[BF16]]/[[FP8]] 같은 형식의 범위-정밀도-회로 비용 트레이드오프를 함께 설계해야 한다는 것이다.

또한 대규모 [[LLM]]과 [[Transformer]] 워크로드에서는 행렬 곱셈과 [[FMA]]가 계산의 중심이므로, 저장 형식뿐 아니라 누산 형식과 데이터 이동 경로까지 포함해 양자화를 봐야 한다고 정리한다. 마지막으로 [[PostTrainingQuantization]], [[QuantizationAwareTraining]], [[BlockNumberFormats]], [[LogNumberSystems]] 같은 기법과 [[NVIDIA]]/[[AMD]]/[[Intel]]/[[Google]]/[[Microsoft]] 등의 하드웨어 벤더 동향을 묶어, 양자화가 단순한 비트 축소가 아니라 시스템 설계 문제임을 강조한다.

## Key Claims
- 신경망 양자화의 핵심 목표는 정확도를 크게 잃지 않으면서 에너지 효율성과 메모리 효율성을 높이는 것이다.
- 현대 [[LLM]] 연산의 대부분은 행렬 곱셈과 [[FMA]]로 구성되며, 숫자 형식 선택이 전체 시스템 비용을 좌우한다.
- 저비트 형식은 메모리 병목을 줄이지만, 값 분포를 충분히 잘 근사하지 못하면 정확도 손실이 발생한다.
- [[INT8]]은 추론 칩에서 매우 중요하지만, 누산과 정렬 비용 때문에 [[FloatingPoint|부동 소수점]] 형식이 더 유리한 구간도 있다.
- [[FixedPoint|고정 소수점]]은 단순하고 구현이 쉬우나 동적 범위가 큰 값을 다루기 어렵다.
- [[FloatingPoint|부동 소수점]]은 지수와 가수를 사용해 넓은 동적 범위를 다루며, [[IEEE754]] 계열 표준이 이를 뒷받침한다.
- [[FP32]]는 범위와 정밀도가 넉넉하지만 비트 비용이 크고, [[FP16]]과 [[BF16]]은 범위와 정밀도 사이의 절충안이다.
- [[FP8]]은 추론과 훈련에서 더 낮은 비용을 제공하지만, 누산과 반올림 오차를 더 신중히 관리해야 한다.
- [[BlockNumberFormats|블록 숫자 형식]]은 텐서의 인접 요소들이 비슷한 크기를 가진다는 관찰을 활용해 여러 값이 지수를 공유하도록 만든다.
- [[PostTrainingQuantization|PTQ]]는 비교적 가볍게 적용할 수 있지만, 실제로는 수정된 훈련이나 대리 목적함수에 의존하는 경우가 많다.
- [[QuantizationAwareTraining|QAT]]는 정확도 손실을 줄이기 위해 양자화된 정밀도에 모델을 적응시키는 더 비싼 접근법이다.
- [[NVIDIA]]는 [[Hopper]]와 [[Blackwell]]에서 저정밀도와 텐서 메모리 경로를 적극적으로 밀고 있으며, [[FP8]]/[[FP4]]/[[FP6]]과 같은 형식이 중요한 설계축이 되었다.
- [[BlockNumberFormats]], [[LogNumberSystems]], [[NF4]], [[AF4]], [[PAL]] 같은 대안 형식은 더 나은 표현 효율을 주장하지만, 하드웨어 구현 비용과 일반성에서 제약이 있다.
- 벤더들의 공통 과제는 미래 모델 분포가 달라져도 유효한 형식과 회로를 설계하는 것이다.

## Key Quotes
> "정확도를 유지하면서 에너지 효율성을 높이는 것입니다"

> "모든 최신 ML 모델의 대부분은 행렬 곱셈으로 구성된다"

> "저비트 부동 소수점에서는 곱셈은 저렴하지만 누적은 비싸다"

## Connections
- [[NeuralNetworkQuantization]] — 문서의 중심 주제.
- [[NumberFormat]] — 비트 표현, 범위, 정밀도 논의의 상위 개념.
- [[FixedPoint]] — 스케일 팩터로 숫자 범위를 바꾸는 단순한 형식.
- [[FloatingPoint]] — 지수와 가수를 사용하는 넓은 동적 범위 형식.
- [[IEEE754]] — 부동 소수점 표준의 근간.
- [[INT8]] — 전용 추론 하드웨어에서 중요한 저정밀도 정수 형식.
- [[FP16]] — 범위와 정밀도의 중간 지점.
- [[BF16]] — 넓은 지수 범위를 유지하는 16비트 부동 소수점.
- [[FP8]] — 저비트 훈련/추론의 핵심 형식.
- [[PostTrainingQuantization]] — 훈련 후 적용하는 양자화 기법.
- [[QuantizationAwareTraining]] — 양자화에 맞춰 다시 훈련하는 기법.
- [[BlockNumberFormats]] — 여러 값이 지수를 공유하는 형식.
- [[LogNumberSystems]] — 로그 기반 수치 표현의 대안.
- [[NF4]] — 정규 분포 가정 기반 4비트 형식.
- [[AF4]] — 정규 분포 가정 기반 4비트 형식.
- [[PAL]] — 대안 숫자 형식 계열.
- [[NVIDIA]] — 양자화와 텐서 메모리/저정밀도 형식의 선도 벤더.
- [[Hopper]] — FP8 훈련 레시피와 텐서 코어 기반 저정밀도 확산과 연결.
- [[Blackwell]] — FP4/FP6, TMEM, 저정밀도 경로가 강조되는 다음 세대.
- [[LLM]] — 양자화의 주요 적용 대상.
- [[Transformer]] — 대규모 행렬 곱셈 중심 연산의 대표 아키텍처.
- [[FMA]] — 양자화된 숫자 형식 비용을 이해하는 기본 계산 단위.

## Contradictions
- 기존 [[NVIDIA]], [[Hopper]], [[Blackwell]] 관련 서사와 충돌하지 않는다. 다만 본 문서는 세대별 GPU 기능보다 숫자 형식과 양자화 원리에 초점을 둔다.
- 일부 수치와 형식 비교는 설명용 일반화이므로, 실제 하드웨어와 커널 구현에서는 형식별 성능/정확도가 다를 수 있다.
