---
title: "QOM"
type: concept
tags:
  - 객체지향
  - 장치 모델링
  - QEMU
sources:
  - qemu-에뮬레이터-내부-구조-tcg-메모리-디바이스-모델링-및-디버깅
last_updated: 2026-05-10
---

## 정의

QOM(QEMU Object Model)은 [[QEMU]]의 객체 기반 장치/클래스/인스턴스 모델링 체계다.

## 핵심 구성

- TypeInfo
- TypeImpl
- ObjectClass
- Object
- module_init/type_init
- properties/class_init/instance_init

## 동작 원리

타입 등록 → 초기화 → 객체 생성 → 시스템 등록(`qdev_realize`)의 일련의 수명주기를 가진다.

## 연결

- [[TypeInfo]]
- [[TypeImpl]]
- [[ObjectClass]]
- [[Object]]
- [[DeviceModeling]]
- [[QEMU]]