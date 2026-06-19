---
title: "BPF Loop Verification via Scalar Evolution"
type: concept
tags: [bpf, verification, kernel]
sources: [lwn-weekly-edition-2026-06-11-1076254]
last_updated: 2026-06-19
---

## Overview
BPF 검증자의 루프 처리를 개선하기 위한 기술. 스칼라 진화(scalar evolution)를 사용하여 루프 변수의 값 범위를 계산하고 검증자를 단일 패스로 처리 가능하게 한다.

## Background
기존 BPF 검증자는 루프를 만나면 종료 조건까지 반복하여 평가. 이로 인해 명령 수 제한에 도달할 수 있음.

## Technique
1. 뒤로 점프를 찾아 루프 식별
2. 도미네이터 트리를 사용하여 루프 구조(헤더, 뒤쪽 가장자리, 래치, 출구) 분석
3. 스칼라 진화로 루프 변수의 값 범위 계산
4. 해당 범위의 값으로 루프 본문 안전성 검증

## Challenges
- 환원 불가능한 루프 처리
- 중첩 루프의 바깥쪽 변수 변경
- 스택으로 유출/복원되는 레지스터

## Connections
- [[BPF]] — 적용 기술
- [[EduardZingerman]] — 개발자
- [[LSFMMBPFSummit]] — 발표 행사
