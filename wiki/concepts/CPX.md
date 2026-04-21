---
title: "CPX"
type: concept
tags: [inference-architecture, workload-separation, memory-systems]
sources: [트렌드포스-sk하이닉스-때문에-엔비디아-루빈-생산량이-대폭하향-되었다]
last_updated: 2026-04-20
---

## Definition
[[CPX]]는 NVIDIA 추론 스택에서 디코드/프리필 등 연산 경로를 분리해 처리 효율과 비용 구조를 바꾸는 방법론으로 정의된다. 본문에서는 HBM 대역폭 병목을 완화하기 위해 프리필에 [[GDDR]] 사용 여지를 넓히는 방식이 핵심으로 묘사된다.

## Key Mechanics
- 연산 경로 분해로 메모리 요구의 성격을 재분류
- 과거 단일 다이 의존형 설계 대비 자원 분할 활용
- 비용 효율 중심의 워크로드 배치 전환

## Relationship
- [[LPX]]은 CPX의 뒤를 이어 디코드 경로를 더 세분화한 확장 개념으로 연결된다.
- [[VeraRubinPlatform]] 및 [[HBM]] 수요 추정에 직접적인 영향을 준다.
- [[SKHynix]], [[SamsungElectronics]]와 같은 공급사 다이 배치 전략을 바꾼다.

## Notes
- 본 소스에서는 CPX가 루빈 다이 조정 배경의 초기 축으로 제시된다.