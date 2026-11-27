---
title: "User Namespace and File Capabilities"
type: concept
tags: [lwn, linux, security]
sources: [lwn-weekly-edition-2026-11-12-1105460]
last_updated: 2026-11-27
---

## Summary

User namespace 안의 root는 host root와 다르지만 ID mapping 및 file capability가 결합하면 namespace 바깥의 권한에 영향을 줄 수 있다. 이 호는 file capability가 예상한 namespace 경계를 넘어 적용되지 않도록 제한하는 kernel patch series를 다룬다.

## Operational Boundary

제안의 존재를 모든 배포판에 적용된 수정으로 해석하지 않는다. 실제 보안 평가는 kernel 버전·backport·UID/GID mapping·파일 소유권과 capability metadata를 함께 확인해야 한다.

## Connections

- [[lwn-weekly-edition-2026-11-12-1105460]] — 2026-11-12 보도와 한국어 번역·해설.
- [[LinuxKernel]] — 관련 기술·당사자 맥락.
