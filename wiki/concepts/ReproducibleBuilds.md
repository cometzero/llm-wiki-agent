---
title: "Reproducible Builds"
type: concept
tags: [security, build-system, debian]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# Reproducible Builds

재현 가능한 빌드는 같은 소스와 빌드 입력으로 동일한 바이너리를 만들 수 있음을 보장하는 공급망 보안 기법이다.

## Debian의 결정 (2026)

2026년 5월, Debian은 재현 가능한 패키지를 필수 요건으로 의무화했다:
- 재현 불가능한 새 패키지의 migration 차단
- 기존 패키지의 재현성 회귀 시 migration 차단

### 범위
Debian 빌드 환경 인스턴스 내 빌드 재현으로 제한 — 일반적인 "완벽한" 재현 가능 빌드보다 좁은 기준이나 중요한 진전이다.

## 요구 사항
- 빌드 타임스탬프 처리
- 파일 순서 결정성
- 환경 의존성 제거

## Related Pages
- [[SupplyChainSecurity]]
- [[Debian]]
