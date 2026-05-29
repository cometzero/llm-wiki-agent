---
title: "Kairui Song"
type: entity
tags: [kernel, memory-management, developer]
sources: [lwn-weekly-edition-2026-05-21-1072730]
last_updated: 2026-05-29
---

## Overview
[[Kairui Song]]은 Linux 커널 [[SwapSubsystem]] 개발자로, [[SwapTable]] 도입으로 스왑 서브시스템의 오버헤드를 크게 줄였다. 2026년 [[LSFMM+BPF Summit]]에서 스왑 개선 로드맵과 [[MGLRU]] 통합에 기여했다.

## Key Contributions
- [[SwapTable]] 구현 및 최적화
- folio 기반 스왑 코드 정리
- [[MGLRU]] 개선 패치 세트 개발
- 가상 스왑 계층(virtual swap layer) 제안

## Related
- [[SwapTable]]
- [[MGLRU]]
- [[LSFMM+BPF Summit]]
- [[MemoryManagement]]