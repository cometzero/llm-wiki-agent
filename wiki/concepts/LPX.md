---
title: "LPX"
type: concept
tags: [inference-architecture, workload-separation, die-efficiency]
sources: [트렌드포스-sk하이닉스-때문에-엔비디아-루빈-생산량이-대폭하향-되었다]
last_updated: 2026-04-20
---

## Definition
[[LPX]]는 [[CPX]] 이후 단계에서 디코드 연산을 추가로 분리해 처리 효율을 높이는 전략으로, 결과적으로 루빈 다이 사용량 자체를 더 줄이는 방향으로 작동한다.

## Key Claims in Source
- CPX에서 시작한 분리 전략을 확장해 일부 연산을 더 세분화.
- 같은 성능을 더 적은 루빈 다이로 달성 가능한 구조로 설명됨.
- 루빈 다이의 잉여분은 차세대 [[VeraRubinPlatform]] 라인(예: [[루빈 울트라]])로 전환 가능성 제기.

## Relationship
- [[CPX]], [[VeraRubinPlatform]], [[HBM4]], [[GDDR]]
- [[SKHynix]]와 [[SamsungElectronics]] 물량 배치 재설계와의 연동

## Implication
루빈 다이 공급량 전망을 과거와 동일 선상으로 단순 추정할 경우, LPX 적용으로 인해 발생한 수요 재편을 간과할 수 있다.