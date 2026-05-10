---
title: "Tesla's Occupancy Networks: A look at How They Work"
type: source
tags: [Tesla, AutonomousVehicle, OccupancyNetwork, OccupancyGrid, NeRF, Robotics]
date: 2026-05-10
sources:
  - tesla-s-occupancy-networks-a-look-at-how-they-work
last_updated: 2026-05-10
source_file: raw/Robotics/LilysAI/tesla-s-occupancy-networks-a-look-at-how-they-work.md
source_hash: 2e2af3812ffcced3
---

## Summary
이 문서는 테슬라의 자율주행 스택에 도입된 [[OccupancyNetwork]]의 핵심 의도를 정리한다. 기존 2D 기반 객체 기반 처리의 한계를 줄이고, 차량 주변 3D 공간을 작은 [[Voxel]] 셀 단위로 나눈 뒤 각 셀의 점유 여부만 판단함으로써 더 연속적이고 강건한 주행 판단을 만들려는 구조이다.

특히 [[Tesla]]는 기존 점검의 병목인 고정 크기 박스 기반 객체 탐지, 데이터셋 제한, 사각지대 대응 한계를 줄이기 위해 공간 점유 예측을 우선으로 두고, 이를 [[OccupancyFlow]]와 결합해 동적 예측 및 장면 재구성을 강화한다. 또한 [[NeuralRadianceField|NeRF]] 기반의 오프라인 정합성 검증을 통해 재구성 품질을 점검한다.

## Key Claims
- 기존 [[2D]]/박스 기반 인식은 깊이 불일치, 가려짐, 복합 모양 객체 표현 실패처럼 드문 케이스에서 취약점이 크다. 예: 캥거루처럼 [[Ontology]]에 없는 객체는 기존 검출 기반 파이프라인에서 놓치기 쉽다.
- [[OccupancyNetwork]]는 3D 공간을 여러 [[Voxel]]로 분할해 각 복셀의 점유 상태(비어있음/점유됨)를 예측한다.
- 핵심 전환은 객체 분류 중심이 아니라 공간 존재성 판별인 "Occupancy over Detection"이다.
- [[Tesla]]는 고정 직사각형([[FixedRectangles]])을 대체해 형태가 비정형인 장애물(예: 돌출 트렁크, 트레일러)도 voxel 점유 형상으로 모델링한다.
- 기존 조감도(BEV 기반의 객체 박스 표현)에 비해, [[OccupancyVolume]]은 고도(z)까지 반영한 체적 표현으로 조향/제동 의사결정을 더 안정화한다.
- 점유 예측 속도는 100 FPS 이상으로, 카메라 입력 처리 속도보다 빠른 추론 여유를 가진다.
- 아키텍처는 8개 카메라 입력 -> [[RegNet]] 및 [[BiFPN]] 기반 특징 추출 -> 어텐션 모듈 -> 시간 정렬된 [[OccupancyGrid]] 융합 -> [[Deconvolution]] 디코딩으로 [[OccupancyVolume]]과 [[OccupancyFlow]]를 생성한다.
- [[OccupancyFlow]]는 각 복셀의 이동 방향/속도 정보를 제공해 예측, 가려진 영역 추론, 경로 계획에 도움을 준다.
- [[NeuralRadianceField]]는 여러 시점 영상의 장면 재구성을 통해 생성된 볼륨을 sanity check하고, [[FleetAverage|fleet averaging]]와 디스크립터 기반 정합으로 오염(안개/흐림/저품질 영상) 영향을 완화한다.

## Key Quotes
> "테슬라의 문제 인식은 객체를 어디에 두는지가 아니라, 공간이 어디가 채워져 있는지 예측하는 것이다." — source summary interpretation

> "고정된 직사각형은 차량의 비정형 실루엣을 담지 못한다. 복셀 점유는 모양과 형태를 더 직접적으로 보존한다." — source summary interpretation

> "점유 유출은 데이터셋 오타고지식에 덜 의존해, 기존 학습 집합에 없는 객체도 '점유 셀'로는 반응할 수 있다." — source summary interpretation

## Connections
- [[Tesla]] — 본 소스의 기술 적용 주체.
- [[AutonomousVehicle]] — [[OccupancyNetwork]]가 실시간 제어 신뢰도를 강화하는 목표 도메인.
- [[EndToEndAutonomy]] — 점유 기반 표현이 통합 제어 스택의 감지·판단 품질을 개선하는 방식과 정합.
- [[OccupancyNetwork]] — 본 소스의 중심 개념.
- [[OccupancyGrid]] — 3D 복셀 점유 표현을 위한 공간 분할 구조.
- [[OccupancyFlow]] — 각 점유 복셀의 시간별 이동 추적.
- [[NeuralRadianceField]] — 장면 재구성 기반 정합 확인용 보조 모듈.
- [[VisionTransformer]] — 일부 기존 인식 프레임의 2D 처리 관점을 보완한다는 대비 맥락.
- [[Bayes risk?]] — not currently a direct source mention; omitted intentionally.
- [[SensorFusion]] — [[Tesla]] 멀티카메라 기반 점유 융합의 기반 축.

## Contradictions
- 본 소스는 기존 객체 검출·BEV 직사각형 중심 패러다임의 한계를 강하게 지적한다. 기존 [[Tesla]] 관련 소스 일부가 모듈형/분해형 파이프라인의 디버깅 편의성을 강조한 것과 완전 충돌이라기보다 설계 우선순위의 차이(표현 정밀도와 장면 연속성 대 모듈별 책임 분리)로 정리된다.