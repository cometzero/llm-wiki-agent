---
title: "no_new_privs와 System-wide Privilege Boundaries"
type: concept
tags: [linux, security, privilege]
sources: [lwn-weekly-edition-2026-10-22-1100612]
last_updated: 2026-10-30
---

## Overview

`no_new_privs`는 실행 파일의 setuid/setgid 및 file capabilities를 통해 `execve()` 시 새 권한을 획득하는 것을 제한하는 process 속성이다. 자식 process와 후속 실행으로 상속된다. 이미 권한을 가진 service의 모든 작업을 막는 만능 sandbox는 아니다.

## System-wide deployment

SUSE의 2026년 실험은 PID 1에서 제약을 물려주고 account-utils의 작은 client가 제한된 privileged service와 IPC로 통신하게 하는 방식을 다룬다. `run0`·polkit와 PAM 연동, sudoers 이관, rootless/distribution container·FUSE·SELinux 호환성은 별도 과제다. 설정 한 줄을 켰다고 기존 권한 정책까지 자동 보존되는 것은 아니다.

## Verification implications

실행 제약 상속, service 허용 목록, 인증 UI, 비대화형 script, 권한 저하와 상승 경로를 분리해 시험해야 한다. 원문 실험 결과를 모든 배포판의 권장 기본 설정으로 일반화하지 않는다.

## Connections

- [[LinuxKernel]] — process 실행·상속과 credential transition.
- [[lwn-weekly-edition-2026-10-22-1100612]] — SUSE 실험 및 미해결 호환성 항목.
