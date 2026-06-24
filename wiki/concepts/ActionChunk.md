---
title: "Action Chunk"
type: concept
tags: [VLA, robot-control, action-prediction, inference-efficiency]
sources: [tbd-vla-2606-07895-learning, policytrim-2606-22540-analysis, policytrim-2606-22540-learning]
last_updated: 2026-06-24
---

## Definition

한 번의 inference(forward pass)로 예측하는 **여러 step의 action sequence**. VLA가 환경과 한 번交互할 때마다 여러 시간 step의 행동을 미리 예측하여 저장하고, 이를 순차적으로 실행한다.

## Role in Deployment Efficiency

```text
Deployment speed ∝ fewer inference calls × longer reliable chunks
                     (fewer physical steps / longer action chunk)
```

- [[ActionChunk]] 길이 ↑ → inference call 수 ↓ → deployment 속도 ↑
- 단, [[TailDegradation]]으로 인해 무한히 늘릴 수 없음 → [[PolicyTrim]]으로 reliable horizon 탐색

## Key Properties

| Property | 설명 |
|---|---|
| Chunk horizon | 한 inference에서 예측하는 step 수 |
| Reliable horizon | 성공적으로 실행 가능한 최대 chunk 길이 |
| Tail degradation | chunk 뒤쪽으로 갈수록 신뢰도 하락 |

## Connections
- [[PolicyTrim]] — action chunk utilization을 3배 향상시키는 방법
- [[TailDegradation]] — chunk 길이 제한 요인
- [[PhysicalSteps]] — deployment efficiency 계산의 분모
- [[TBDVLA]] — temporal block discrete diffusion 기반 VLA (action chunk 사용)
- [[ActionTokenization]] — action chunk를 discrete token 시퀀스로 인코딩하는 기법
