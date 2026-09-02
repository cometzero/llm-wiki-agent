---
title: "Wrap-Aware Loss"
type: concept
tags: [loss-function, robot-control, angles]
last_updated: 2026-09-02
---

## 정의

[[WrapAwareLoss]]는 주기적 변수(예: joint angle)의 예측 오차를 $[-\pi,\pi]$ 주기 범위로 정규화한 후 계산하는 손실이다.

## 수식

$$\operatorname{wrap}(x)=((x+\pi)\bmod 2\pi)-\pi,$$
$$\mathcal L_{wrap}=\|\operatorname{wrap}(\hat a-a)\|_1.$$

## 필요성

조인트 각도처럼 경계가 있는 신호에서 일반 L1 loss를 쓰면 $+\pi$와 $-\pi$ 근처에서 큰 오차로 학습이 불안정해질 수 있다.

## 사용 위치

연속적 action regression(특히 다중 embodiment의 제어 신호)에서 angle periodicity를 반영해야 할 때 유용.
