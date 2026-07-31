---
title: "GNOME Session Restore"
type: concept
tags: [gnome, desktop, wayland]
sources: [lwn-weekly-edition-2026-07-23-1083123]
last_updated: 2026-07-31
---

## Summary
[[GNOME]] 환경에서 Wayland 세션의 애플리케이션 상태 저장/복원을 제공하려는 데스크톱 기능 축이다.

## Notes
GNOME save/restore는 X11 세션 관리 경험을 Wayland 기반 데스크톱에 맞게 재구성하려는 흐름이다. LWN 2026-07-23 보도는 compositor, toolkit, 애플리케이션 protocol이 모두 참여해야 사용자가 기대하는 “열려 있던 작업 공간으로 돌아가기”가 가능하다는 점을 강조한다.

## Connections
- [[GNOME]] — desktop environment context
- [[lwn-weekly-edition-2026-07-23-1083123]] — LWN 2026-07-23 source coverage
