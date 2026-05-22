---
title: "Kernel Killswitch"
type: concept
tags: [security, kernel, emergency-mitigation]
sources: [lwn-weekly-edition-2026-05-14-1071535]
last_updated: 2026-05-22
---

# Kernel Killswitch

커널 killswitch는 Sasha Levin이 제안한 실행 중인 커널에서 특정 기능을 즉시 비활성화할 수 있는 응급 완화 메커니즘이다.

## 목적
수정이 준비되기 전에 취약점 공개가 이어지는 상황에서, 패치를 설치할 때까지 취약한 경로를 차단한다.

## 사용 예시
```
"이 소켓 패밀리가 하루 동안 작동하지 않는다"는 비용
vs
"알려진 취약 커널을 계속 실행하는" 비용
```

## 적용场景
네트워크 프로토콜, 파일 시스템, ioctl 경로처럼 공격 표면이 명확한 경우에 유용하다.

## Related Pages
- [[VulnerabilityDisclosure]]
- [[DirtyFrag]]
- [[SecurityMitigation]]
