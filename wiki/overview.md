## Embodied AI / VLA

### 데이터 중심 접근
- [[HumanNet]]: 100만 시간 인간 중심 비디오로 [[VLA]] 데이터 부족 문제 해결 — robot data 대신 human video + motion annotation 사용
- [[EmbodiedMidtrain]]: [[VLM]] 샘플의 분포 정렬 기반 [[DataSelection]]으로 [[VLA]] 성능 향상
- [[Tesla]] [[EndToEndAutonomy]]: 차량-로봇 공통 파운데이션 모델, 시뮬레이션 기반 검증
- [[NVIDIA]] [[NVIDIAGR00T]], [[Google]] [[GeminiRobotics]], [[PhysicalIntelligencePi]]: VLA 모델 3대장 비교

### Scaling과 데이터 전략
- HumanNet: 데이터 소스 확장으로 [[VLA]] scaling bottleneck 공략
- [[ARKInvest]] [[BigIdeas2026]]: AI/Robotics 가속화 예측
- [[AndrejKapassi]]의 AI 교육/프로그래밍 방향
- [[Cosmos-Reason1]]: Physical common sense에서 embodied reasoning으로

> [!tip]
> HumanNet은 robot data 부족 → human video + motion annotation + retargeting + VLA post-training이라는 scalable route를 제시하며, 자율주행의 driving video 활용에도 힌트를 제공.

## 관련 기술 동향

- [[VLA]] (Vision-Language-Action) — 인간 시맨틱 이해 + 로봇 행동 생성 통합 모델
- [[Embodied AI]] — 물리적 환경에서 학습하는 AI 패러다임
- [[EndToEndDeepLearning]] — 모듈식에서 End-to-End 통합으로 전환 (Tesla FSD v12 참조)
- [[OccupancyNetwork]] — Tesla의 3D 공간 점유 표현
- [[WorldSimulator]] — 시뮬레이션 기반 검증 (Tesla FSDDemo 참조)