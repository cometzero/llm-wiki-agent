---
title: "TypeInfo"
type: concept
tags:
  - QOM
  - QEMU
  - 장치 모델링
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

`TypeInfo`는 [[QEMU]] 장치/클래스 객체를 등록할 때 사용되는 메타 정보 구조다.

## 핵심 항목

- name
- parent
- instance_size
- class_init
- instance_init
- interfaces

## 실무

- QEMU에서 새로운 장치 등록 시 `type_register`와 함께 사용.
- 하드웨어 모델의 객체 구조와 계층 관계를 선언.

## 연결

- [[QOM]]
- [[TypeImpl]]
- [[ObjectClass]]
- [[InterfaceClass]]
- [[QEMU]]