---
title: "Swap Table"
type: concept
tags: [kernel, memory-management, swap]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[SwapTable]]은 [[Kairui Song]]이 도입한 스왑 서브시스템 최적화로, 페이지당 오버헤드를 3~11바이트에서 2~10바이트로 줄였다. 장기 목표는 3바이트까지 감소이다.

## Key Improvements
- 스왑 서브시스템 복잡성 제거
- folio 기반 코드 정리
- [[SwapCache]] 활용 개선
- [[Readahead]] 최적화

## Future Work
- 가상 스왑 계층(virtual swap layer) 추가
- 스왑 장치 제거/조각 모음 개선
- [[THP]] 스와핑 효율화
- 스왑 영역 크기 동적 조정

## Related
- [[SwapSubsystem]]
- [[SwapCache]]
- [[folio]]
- [[Kairui Song]]
- [[LSFMM+BPF Summit]]