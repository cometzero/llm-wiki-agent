---
title: "Flash-Friendly Swap"
type: concept
tags: [kernel, swap, flash, embedded]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[FlashFriendlySwap]]은 [[Youngjun Park]]이 제안한 임베디드 장치용 스왑 최적화로, [[SSD]] 수명을 연장하기 위해 [[EraseBlock]] 정렬 순차 쓰기와 [[Deduplication]]을 적용한다.

## Key Techniques
- Erase block 정렬 순차 쓰기
- 중복 제거(de-duplication) — 최대 절전 라운드 페이지再利用
- [[zram]]과 유사한 압축 기반 RAM 스왑
- Shrinker 스레드를 통한 영구 저장장치 flush

## Benefits
- [[WriteAmplification]] 감소
- Flash [[WearLeveling]] 부담 경감
- 임베디드 장치寿命 연장

## Related
- [[SwapSubsystem]]
- [[zram]]
- [[Deduplication]]
- [[LSFMM+BPF Summit]]