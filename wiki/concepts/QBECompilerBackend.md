---
title: "QBE Compiler Backend"
type: concept
tags: [compiler, backend, llvm-alternative]
sources: [lwn-weekly-edition-2026-07-16-1081915]
last_updated: 2026-07-24
---

## Definition
[[QBECompilerBackend|QBE]](Quick Backend Engine)는 [[LLVM]], [[GCC]] 같은大型 컴파일러 백엔드의 경량 대안으로 설계된 소형 컴파일러 백엔드다.

## Overview
Quentin Carbonneaux가 개발한 QBE는 단일 개발자도 이해할 수 있을 만큼 작게 설계되었으며, MIT 라이선스로 공개된다.

### 1.3 릴리스 주요 변경사항
1. **성능 최적화**: GVN, GCM, targeted loop optimization, if-elimination 도입
2. **메타프로그래밍**: OCaml 기반 mgen 도구로 instruction selection 단순화
3. **플랫폼 지원**: Windows x64 ABI 백엔드, ELF 시스템에서 PIC/shared object 지원

### 성능 수치
- CoreMark: 수정 없이 63% (타겟 70%)
- Hare 언어 테스트: 런타임 성능 33% 개선
- 컴파일 속도 우선으로 인한 제한 유지

### 한계
- DWARF/PDB 소스 수준 디버깅 정보 생성 미지원
- self-hosting 불가 (C 프론트엔드 필요)
- minimalist C 구현으로 학습 곡선 가파름

## Connections
- [[QuentinCarbonneaux|Quentin Carbonneaux]] — 개발자
- [[Hare]] — 주요 사용자
- [[cproc]] — QBE 사용자
- [[LLVM]] — 대체 대상
- [[mgen]] — 메타프로그래밍 도구
