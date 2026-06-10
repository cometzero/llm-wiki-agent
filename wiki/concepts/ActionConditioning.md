---
title: "Action-Conditioned Generation"
type: concept
tags: [generation, conditioning, policy]
sources: [nvidia-omnidreams-2606-03159]
last_updated: 2026-06-10
---

# Action-Conditioned Generation

Policy action에 조건화된 sensor observation 생성 기법.

## OmniDreams에서의 조건화 입력
1. **World-scenario map**: HD map 정보 (lane, boundary, dynamic agents)
2. **Text prompt**: weather, lighting, time-of-day
3. **Memory cache**: KV cache로 유지되는 visual history
4. **Policy action**: immediate driving actions (braking, steering 등)

## 핵심 특성
- Policy action이 simulator state를 바꾸고, 그 state가 다음 observation 생성에 직접 영향
- Reactive environment: 갑작스러운 action 변화에 즉각 반응

## 왜 중요한가?
Closed-loop evaluation에서 policy의 작은 action error가 장기적으로 어떻게 누적되는지 검증 가능

## Connections
- [[OmniDreams]] — 구현체
- [[ClosedLoopSimulation]] — 핵심 사용 사례
- [[WorldModel]] — 상위 개념
