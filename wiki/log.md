## [2026-05-02] ingest | 2026-05-02 AI/ML Learning Day 10

Added source. Key claims: introduced [[LinearRegression]] with [[LeastSquares]] objective and [[Residual]]-based fitting, [[LogisticRegression]] as linear-score+[[Sigmoid]] binary decision flow, and [[DecisionBoundary]]/[[LinearSeparability]]/[[Hyperplane]] geometry for classification; linked these to [[CrossEntropy]] for classification optimization and connected them with [[FeatureSpace]] transformation and [[LLM]] intuition.

## [2026-05-01] ingest | 2026-05-01 AI/ML Learning Day 09

Added source. Key claims: 교차검증을 통해 [[CrossValidation]]/[[KFoldCrossValidation]] 기반의 안정적 성능 추정으로 단일 split 편향을 줄였고, 도메인 목표에 맞는 [[EvaluationMetric]] 설계를 위해 [[Precision]], [[Recall]], [[F1Score]], [[AUROC]]를 활용했으며, [[Regression]]과 [[Classification]]의 [[RegressionLoss]]와 [[ClassificationLoss]] 차이를 통해 모델 학습 신호를 정확히 분리했다.

## [2026-04-30] ingest | 2026-04-30 AI/ML Learning Day 08

Added source. Key claims: Day 08 formalizes the connection between [[Overfitting]], [[Underfitting]], [[BiasVarianceTradeoff]], and [[Regularization]], with practice-oriented diagnostic guidance around [[TrainingLoss]]/[[ValidationLoss]] divergence and model complexity control via [[L1Penalty]], [[L2Penalty]], and [[WeightDecay]]. Also added conceptual updates with new pages: [[Underfitting]], [[Bias]], [[BiasVarianceTradeoff]], [[WeightDecay]], [[L1Penalty]], [[L2Penalty]], and updated index/overview entries.

## [2026-04-29] ingest | 2026-04-29 AI/ML Learning Day 07

Added source. Key claims: 모델의 표현력은 [[HypothesisSpace]]와 [[Capacity]]로 정리되며 과소/과대 적합이 trade-off를 만든다. [[TrainSet]], [[ValidationSet]], [[TestSet]] 분리를 통해 일반화 가능성을 진단하고, [[Generalization]]은 [[GeneralizationGap]] 및 [[OutOfSample]] 성능으로 평가해야 한다. capacity 균형, split 규칙 준수, [[DataLeakage]] 회피를 통해 실전 배포 신뢰도를 높인다.

## [2026-04-28] ingest | 2026-04-28 AI/ML Learning Day 06

Added source. Key claims: [[SGD]]/[[MiniBatch]]는 전체 데이터 gradient의 대체 추정치로 계산 효율을 높여 반복 학습을 가능케 하며, [[LearningRate]]가 수렴 안정성의 핵심 변수로 [[Convergence]], [[Oscillation]], [[Divergence]]를 좌우한다. [[Momentum]]과 [[Adam]]은 각각 누적 방향 정보와 1차/2차 모멘트 정보를 이용해 [[AdaptiveLearningRate]]와 함께 업데이트 안정성을 향상시키는 optimizer 전략이다.

## [2026-04-27] ingest | 2026-04-27 AI/ML Learning Day 05

Added source. Key claims: 학습을 [[Optimization]] 문제로 재정의해 [[Objective]], [[LossFunction]], [[EmpiricalRisk]], [[EmpiricalRiskMinimization]], [[GradientDescent]]의 연결고리를 정리했고, [[Objective]]와 [[Argmin]], [[LossFunction]]와 [[EmpiricalRisk]], 그리고 [[Gradient]]와 [[StepSize]]의 역할 구분을 추가했다.

## [2026-04-26] ingest | 2026-04-26 AI/ML Learning Day 04 — Derivatives, Gradients, and Backpropagation

Added source. Key claims: Day 04 formalized optimization intuition from [[Derivative]] and [[PartialDerivative]] to [[Gradient]], and linked [[ChainRule]] + [[ComputationalGraph]] to practical [[Backpropagation]]/[[Autograd]] workflows. It also emphasized [[DirectionalDerivative]], [[ForwardPass]]/[[BackwardPass]], and [[LearningRate]] tradeoffs in avoiding unstable updates.

## [2026-04-26] ingest | 2026-04-25 AI/ML Learning Day 03

Added source. Key claims: 머신러닝을 [[FunctionApproximation]] 관점에서 정리하고, [[HypothesisSpace]]와 [[LossFunction]]의 역할을 분리했으며, [[FeatureMatrix]]와 [[TensorShape]] 중심의 데이터 표현을 정리했다. 또한 고차원에서 발생하는 [[CurseOfDimensionality]]를 경고하고 [[Regularization]], [[DimensionalityReduction]], [[RepresentationLearning]]의 중요성을 추가 연결했다.

## [2026-04-26] ingest | 2026-04-24 AI/ML Learning Day 02

Added source. Key claims: Day 02 documents [[Probability]] foundations for AI/ML through [[RandomVariable]] and [[ProbabilityDistribution]], distinguishes [[PMF]], [[PDF]], and [[CDF]] for discrete/continuous modeling, and connects summary statistics ([[Expectation]], [[Variance]], [[Covariance]], [[Correlation]]) with [[ConditionalProbability]] and [[BayesTheorem]] via [[Prior]], [[Likelihood]], and [[Posterior]] for practical [[Classification]] intuition.

## [2026-04-26] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: 벡터·기저 의존 좌표 개념을 정리했고, 행렬을 [[LinearMap]] 관점으로 해석했으며, [[DotProduct]], [[Norm]], [[CosineSimilarity]]를 [[Embedding]], [[Attention]], [[Gradient]] 연산과 연결했다.

## [2026-04-26] ingest | 2026-04-26 AI/ML Learning Day 04 — Derivatives, Gradients, and Backpropagation

Added source covering derivative, partial derivative, gradient, chain rule, computational graph, and backpropagation. Created concept pages for Derivative, PartialDerivative, Gradient, ChainRule, ComputationalGraph, Backpropagation, GradientDescent, Autograd, VanishingGradient, ExplodingGradient.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source: AI/ML 30일 학습 Day 01 — 수按月기초 복습. Key claims: (1) [[VectorSpace]]에서 좌표는 [[Basis]]-dependent하며 벡터 자체는 불변이다. (2) [[Matrix]]는 [[LinearMap]]의 계산 표현이며 [[Rank]]는 보존되는 독립 정보 차원 수다. (3) [[DotProduct]]는 방향+크기 결합 측정으로 [[Attention]] scoring에, [[CosineSimilarity]]는 방향만 측정해 [[Embedding]] retrieval에 쓰인다. (4) [[Norm]]은 [[Gradient]] clipping과 regularization의 기초다. Created/updated concept pages: [[VectorSpace]], [[Basis]], [[LinearMap]], [[Rank]], [[DotProduct]], [[Norm]], [[CosineSimilarity]]. Updated overview with AI/ML Mathematical Foundations section.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: [[VectorSpace]] defines the abstract space for vector representations; coordinates are [[Basis]]-dependent, not intrinsic to the vector. [[Matrix]] is the computational form of a [[LinearMap]], and [[Rank]] measures preserved information dimensionality. [[DotProduct]], [[Norm]], and [[CosineSimilarity]] quantify vector relationships—used respectively in [[Attention]] scoring, [[Regularization]]/[[GradientNormClipping]], and [[Embedding]] retrieval. Created concept pages: VectorSpace, Basis, LinearMap, Rank, DotProduct, Norm, CosineSimilarity, LoRA, LowRankApproximation, GradientNormClipping. No contradictions with existing wiki content.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: 벡터공간은 표현의 대상, 행렬은 선형변환, dot product·norm·거리는 표현 간 관계를 수치화. [[VectorSpace]], [[LinearMap]], [[DotProduct]], [[Norm]], [[CosineSimilarity]] 개념 페이지 생성.

## [2026-04-25] ingest | 2026-04-25 AI/ML Learning Day 03

Added source. Key claims: ML as [[FunctionApproximation]], [[HypothesisSpace]]/[[LossFunction]] as model selection axes, and high-dimensional sparsity as the main driver for [[RepresentationLearning]], [[Regularization]], and [[DimensionalityReduction]].

## [2026-04-25] ingest | 2026-04-24 AI/ML Learning Day 02

Added source. Key claims: [[RandomVariable]]는 불확실성의 수치 매핑이며 [[PMF]]/[[PDF]]/[[CDF]]로 분포를 다룬다; [[Expectation]], [[Variance]], [[Covariance]], [[Correlation]]은 분포 요약 통계량 축을 이룬다; [[BayesTheorem]]은 [[Prior]], [[Likelihood]], [[Posterior]]로 조건부 갱신을 정식화한다.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: 수학 기초를 벡터공간 기반으로 정리해 coordinate의 basis-dependent 성격을 명확화했고, [[Matrix]]를 [[LinearMap]]로 재해석해 LLM의 [[Embedding]]·[[Attention]] 연산과 연결했으며, [[DotProduct]], [[Norm]], [[CosineSimilarity]]의 측정 목적 차이를 학습-복습 질문으로 정리했다.

## [2026-04-25] ingest | 2026-04-25 AI/ML Learning Day 03

Added source. Key claims: ML을 function approximation으로 보는 관점, hypothesis space와 loss function의 역할, feature matrix의 구조, curse of dimensionality와 대응 전략.

## [2026-04-25] ingest | 2026-04-25 AI/ML Learning Day 03

Added source. Key claims: ML can be framed as function approximation over a hypothesis space optimized by a loss function; feature matrices and tensor shapes encode data structure; high-dimensional sparsity creates the curse of dimensionality and motivates representation learning, regularization, and dimensionality reduction.

## [2026-04-25] ingest | 2026-04-24 AI/ML Learning Day 02

Added source. Key claims: 확률변수/분포의 기본 구분과 PMF/PDF/CDF의 사용 구간, 기댓값·분산·공분산·상관의 관계, 조건부확률과 베이즈 정리를 통해 분류에서 prior·likelihood·posterior가 어떻게 결합되는지 정리했다.

## [2026-04-25] ingest | 2026-04-23 AI/ML Learning Day 01

Added source. Key claims: 벡터는 고정 대상이지만 [[Coordinate]]는 [[Basis]]에 따라 변하고, [[Matrix]]를 [[LinearMap]] 관점으로 해석해 [[DenseLayer]]·[[Attention]]을 이해할 수 있으며, [[DotProduct]], [[L2Norm]], [[CosineSimilarity]]가 각각 [[LLM]]의 [[Attention]], [[Regularization]], [[EmbeddingSearch]]에서 다른 목적의 유사도/거리 측도로 사용된다는 점을 정리했다.

## [2026-04-21] ingest | \"인간지능 시대는 끝났다\" 인공지능이 가져올 인류 절멸의 위기, 이재명 대통령이 차지호의원에게 내린 숙제 (차지호 의원) 1부

Added source. Key claims: [[UN]] 다자기구 AI 기능을 한국 공동 캠퍼스로 이전해 [[GlobalAIHub]]를 만든다는 제안, [[Polycrisis]](동시복합위기) 조건에서 [[HumanIntelligenceSystem]]의 한계를 보완하기 위한 [[ConnectedIntelligence]] 중심 전환 필요성, AI 시대 노동시장·안보 질서의 급격한 재편 가능성, 과도기 고용 및 소득안전장치로서 [[UniversalBasicIncome]]의 제한적 후보 제시.

## [2026-04-21] ingest | Understanding the RISC-V Extensions for AI - John Simpson, SiFive

Added source. Key claims: [[RiscV]] AI 확장은 벡터 계열 기반의 점진 확장([[VectorBatchProduct]], [[IntegratedMatrixExtensions]])과 고성능 행렬 상태 확장([[VectorMatrixExtensions]], [[AttachedMatrixExtensions]])로 분기되며, 엣지와 데이터센터 도메인별/[[LLM]] prefill-decode 단계별로 ISA 선택이 달라져야 한다. [[SiFive]]와 [[JohnSimpson]]의 정리에서 [[FP8]]/정밀도 처리와 [[FP64]] 성능 영향이 채택 전략의 핵심 제약으로 나타난다.

## [2026-04-21] ingest | Terafab Keynote | Building AI Chips for Earth & Space

Added source. Key claims: [[Terafab]] 협업( [[Tesla]]·[[SpaceX]]·[[xAI]])을 통해 연간 [[Terawatt]]급 AI 컴퓨팅 확보를 추구하고, 현재 [[20 gigawatt|20GW]] 수준의 제약을 넘어서려면 통합형 반도체 생산과 우주 배치 기반의 [[SpaceBasedAIComputing]]이 필요하다는 점, 그리고 장기적으로 [[ElectromagneticMassDriver]] 기반의 [[Petawatt]] 확장을 제시한다.

## [2026-04-21] ingest | Project Glasswing: Securing critical software for the AI era — Anthropic

Added source. Key claims: ProjectGlasswing은 Anthropic의 [[ClaudeMythosPreview]]로 핵심 소프트웨어 취약점을 대규모로 선제 탐지하고 패치 권고로 연결해 방어 속도를 높이는 협업형 보안 프로그램으로 정리되며, 40개 이상 파트너 확장, 1억 달러 크레딧 지원, 오픈소스 보안 기부, 그리고 90일 내 공개 보고/권고 산출을 핵심 운영 과제로 둔다.

## [2026-04-21] ingest | GTC 2026 – The Inference Kingdom Expands

Added source. Key claims: NVIDIA-Gruq LPU 통합 기반 [[AFD]]로 디코드/어텐션-FFN 분리를 통해 지연·처리량 트레이오드를 재설계했으며, [[CPO]]와 [[CMX]]/[[STX]] 중심의 네트워크-스토리지 확장으로 인퍼런스 랙 아키텍처를 GPU 중심을 넘는 계층형 플랫폼으로 진화시켰다.

## [2026-04-21] ingest | EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

Added source. Key claims: EAGLE-3 removes the feature-prediction bottleneck in favor of direct token prediction, introduces [[TrainingTimeTest]] to simulate inference during training, and adds [[MultiLayerFeatureFusion]] across low/mid/high layers. It reports up to 6.47x speedup in [[Vicuna-13B]]/[[HumanEval]] and shows higher or stable acceptance behavior while proposing a data-dependent scaling law for inference acceleration.

## [2026-04-21] ingest | Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI

Added source. Key claims: [[AndrejKarpathy]] 프레임에서 AI 에이전트의 본질은 코드 작성 대체보다 에이전트 지시·오케스트레이션 역량 강화이며, [[AutoResearch]]는 인간 병목을 줄이는 자율 연구 루프를 구현하는 방식이다. [[OpenClaw]]/지속형 클로 구조와 [[agent-first software]], [[Speciation]] 논의를 통해 소프트웨어 생산성, 사용자 경험, 연구 조직 설계가 동시에 재편되는 흐름을 정리한다.

## [2026-04-20] ingest | Understanding the RISC-V Extensions for AI

Added source. Key claims: RISC-V AI 가속은 [[RiscVExtensionsForAI]]의 네 갈래 접근( [[VectorBatchProduct]], [[IntegratedMatrixExtensions]], [[VectorMatrixExtensions]], [[AttachedMatrixExtensions]])로 분기되며, 엣지/데이터센터 워크로드와 배치-대역폭 특성에 따라 적합한 설계를 선택해야 한다. 소프트웨어-하드웨어 협업 관점에서 [[FP8]], [[Bfloat16]], 그리고 [[KVCache]] 경량화 같은 모델 레벨 조정이 함께 성능-비용 균형을 결정한다.

## [2026-04-20] ingest | Terafab Keynote | Building AI Chips for Earth & Space

Added source. Key claims: [[Terafab]] projects a partnership-led plan by [[Tesla]], [[SpaceX]], and [[xAI]] to build terawatt-scale AI computing, emphasizing integrated fab capabilities, orbital deployment economics, and long-horizon expansion toward [[Petawatt]]-scale systems.

## [2026-04-20] ingest | Project Glasswing: Securing critical software for the AI era — Anthropic

Added source. Key claims: [[Anthropic]]가 [[ProjectGlasswing]]를 통해 [[ClaudeMythosPreview]] 기반으로 [[ZeroDayVulnerability]]를 고속 탐지·공유·패치하는 방식의 [[AIForCybersecurity]] 협업 모델을 추진하며, 파트너십 확장·규제 협력·안전 가드를 함께 병행해야 함을 정리한다.

## [2026-04-20] ingest | GTC 2026 – The Inference Kingdom Expands

Added source. Key claims: [[NVIDIA]]는 [[Groq]]의 [[LPU]]를 추론 스택에 흡수해 [[GPU]]와의 이종 협업으로 프리필/디코드 분업을 강화했다. [[AFD]]와 [[Speculative Decoding]]은 디코드 지연 개선의 핵심 기법으로 등장하며, [[CPO]]·[[LPX]]·[[VeraETL256]]·[[CMX]]/[[STX]]는 대규모 AI 인프라에서 네트워크, CPU, 스토리지 병목을 함께 다루는 연계 전략으로 정리되었다.

## [2026-04-20] ingest | EAGLE-3: Scaling up Inference Acceleration of Large Language Models via Training-Time Test

Added source. Key claims: [[EAGLE3]] removes direct [[Feature Prediction]] bottlenecks, adopts [[TrainingTimeTest]] plus [[MultiLayerFeatureFusion]] for data-aware scaling, and reports strong speedups (6.47x/4.40x/4.34x) with stronger acceptance stability across [[HumanEval]], [[MT-bench]], and [[GSM8K]].

## [2026-04-20] ingest | Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI

Added source. Key claims: [[AndrejKarpathy]]가 [[LLMAgents]]의 병렬 협업형 전환, [[AutoResearch]]의 자율 루프, [[ModelSpeciation]] 필요성, 그리고 [[agent-first software]]와 [[OpenClaw]] 사례를 통해 인간의 병목이 오케스트레이션으로 이동함을 강조했고, 연구 조직은 [[MetaOptimization]]으로 재구성될 수 있음을 제시했다.

## [2026-04-20] ingest | 메모리 현물가 하락, 사이클 꺾인 게 아닌 '과열 해소' | 김장열 유니스토리자산운용 본부장 [집중 오늘의 주식]

Added source. Key claims: 현물가 하락을 사이클 종료가 아닌 과열 해소로 보았고, 장기계약 최저가(Floor) 구조로 중기 가격 안정성이 강화될 수 있다고 정리했다. 또한 [[TurboQuant]]는 단기 효율화와 병목 이동을 동시에 낳을 수 있으며, [[ASMR]]·[[OnDeviceAI]]는 장기 메모리 수요 확대 가능성에 대한 상반축 시나리오를 제공한다.

## [2026-04-20] ingest | Dissecting Nvidia Blackwell - Tensor Cores, PTX Instructions, SASS, Floorsweep, Yield

Added source. Key claims: 소스 본문이 비어 있어 실질적 기술 주장 없음. 문서 제목 기반으로 [[NVIDIA]] [[Blackwell]] 및 [[Tensor Cores]], [[PTX]], [[SASS]], [[Floorsweep]], [[ChipYield]] 키워드만 확인됨.

## [2026-04-20] ingest | Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI

Added source. Key claims: AI 에이전트의 병렬 오케스트레이션이 직접 코딩 비중을 낮추고 지시·검증 역량을 핵심 능력으로 전환시키며, [[AutoResearch]]로 연구 병목(인간 프롬프트 병목)을 줄이자는 흐름을 제시한다. OpenClaw, Claw, Dobby the Elf Claw 사례로 에이전트형 소프트웨어 경험(특히 [[agent-first software]])의 전환이 가시화되었고, 장기적으로는 [[ModelSpeciation]]과 [[OpenSource]]/프론티어 균형이 핵심 구조로 부상한다.

## [2026-04-20] ingest | The Great GPU Shortage – Rental Capacity – Launching our H100 1 Year Rental Price Index

Added source. Key claims: (1) H100 1-year rental contracts rose sharply (about 40% from 2025년 10월 to 2026년 3월), indicating persistent GPU scarcity-driven pricing power. (2) Supply constraints are now mostly a contract-structure and long-horizon capital allocation issue rather than a short-lived spot-market fluctuation. (3) Multi-agent, high-token workloads and memory/server inflation are reinforcing demand, so AI compute scarcity is treated as a durable macro-structural condition.

## [2026-04-20] ingest | 환율 1500원 시대 시작되나? 전쟁 끝나도 못 내려오는 이유 | 변정규 다이와증권코리아 본부장 [신과대화]

Added source. Key claims: 전쟁 종료 이후에도 [[한미금리차]]와 지속적 [[달러 강세]], 그리고 [[QuantitativeTightening]]이 맞물리면 [[환율]]은 빠르게 하락하지 않고 1,500원대 고착이 지속될 수 있다는 점을 정리했다. 정책 도구로 제시된 [[WGBI]]와 [[KoreaAccount]]는 즉각적 해결이 아니라 점진적 완충 수단으로 작동하며, 고환율은 물가·채권·기업조달비용 및 특히 중소기업 부담으로 이어질 수 있음을 덧붙였다.

## [2026-04-20] ingest | 트렌드포스 "SK하이닉스 때문에 엔비디아 루빈 생산량이 대폭하향 되었다"

Added source. Key claims: 엔비디아 루빈 생산량 하향은 SK하이닉스의 공정 문제 단일 원인 해석보다 CPX/LPX 기반 워크로드 분리와 루빈 다이 필요량 감소가 핵심 원인이라는 점, 그리고 수급 배분은 [[JenHuang]]의 통제 하에서 [[SKHynix]]/[[SamsungElectronics]] 간 역할 재편으로 확장되는 점을 추가했다.

## [2026-04-20] ingest | 제2의 테슬라? 3천조 괴물 상륙! 스페이스X 상장, 약일까 독일까? | 정의훈 유진투자증권 연구원

Added source. Key claims: [[SpaceX]] 상장 이슈가 우주산업의 밸류에이션 허브로 해석되며, 유통물량·수급 민감도와 모멘텀형 자금 이동이 핵심이다. [[위성통신]]과 [[아르테미스]]는 개별 자산군보다 산업 구조/기술 패권 축으로 정리되었고, [[네이버]], [[카카오]], 게임주의 사례는 국내 주식 수급의 실적 대비 성장성 함의와 결합되어 기록됨.

## [2026-04-20] ingest | 인간의 가치는 오직 의지만 남을 겁니다 - 노정석 대표(비팩토리)

Added source. Key claims: [[비팩토리]]의 AI 도입은 [[AI에이전트]] 기반으로 반복 노동을 축소하고 부가가치 활동으로 재편한다는 조직 운영 사례를 제공한다; AI 전환은 인력 간 적응 속도 차이를 키워 [[AI인재양극화]]를 가속시킬 수 있으며, AI 시대 인간의 핵심 가치는 지식량보다 실행 의지로 이동한다.

## [2026-04-20] ingest | "인간지능 시대는 끝났다" 인공지능이 가져올 인류 절멸의 위기, 이재명 대통령이 차지호의원에게 내린 숙제 (차지호 의원) 1부

Added source. Key claims: UN 기능 이전을 통해 한국형 AI 공동 캠퍼스를 구축하려는 국가 전략 제안, 다중 위기(Polycrisis)에서 [[AI]]의 거버넌스·안보·노동 재설계 필요성, [[ConnectedIntelligence]] 중심의 과도기 운영 모델, 인류적 리스크를 줄이기 위한 제도적 AI 전환 우선순위, 청년/고령층 생산성 및 국가 간 군사력 격차 재편에 대한 경고.

## [2026-04-20] ingest | Understanding the RISC-V Extensions for AI

Added source. Key claims: [[RiscV]]의 AI 확장(특히 행렬 가속 경로)은 벡터 기반 경량 제안과 상태 기반 대형 제안으로 나뉘며 엣지와 데이터센터 워크로드 성격에 따라 선택되어야 한다고 정리된다. [[RiscVExtensionsForAI]]는 배치 크기, 정밀도(FP8/Bfloat16/FP64), 하드웨어 대역폭 조건을 함께 고려한 확장 프레임워크로 통합되었고, 이를 통해 정밀도와 처리량·대역폭 간의 실무적 트레이드오프가 명확히 드러났다.

## [2026-04-20] ingest | Project Glasswing: Securing critical software for the AI era — Anthropic

Added source. Key claims: [[Anthropic]] launched [[ProjectGlasswing]] to use [[ClaudeMythosPreview]] for defensive vulnerability discovery across critical software. The source reports thousands of serious findings including [[ZeroDayVulnerability]] cases and emphasizes that AI deployment must be paired with strict safety controls. It also introduces a new collaboration and governance thread in this wiki linking security, AI capability, and public-private coordination.

## [2026-04-20] ingest | 반도체 업황 살아났나? 밸류 재평가의 진짜 조건ㅣ김장열 유니스토리자산운용 본부장

Added source. Key claims: 반도체 밸류 재평가의 핵심은 빅테크 CAPEX 가이던스와 AI 가격 정책, 재고 및 선구매 계약 신호의 동시 변화이며, 현재는 부정적 시그널이 뚜렷하지 않아 펀더멘탈이 상대적으로 안정적이라는 판단이다. SK하이닉스의 180만 원대 목표주가 논리는 실적성장 지속 가정에 의존하며, 삼성전기의 실리콘 커패시터/ABF 포지션과 SoC 패키징 경쟁력, 삼성/하이닉스/마이크론 차별화가 종목 밸류 분기 포인트로 제시되었다.

## [2026-04-20] ingest | HBM 다음은 HBF, 엔비디아·MS를 영원히 가두는 삼성·하이닉스의 30년 가두리 전략

Added source. Key claims: HBF를 HBM 다음 단계의 AI 메모리 전략으로 제시, 빅테크를 묶는 가격·공급·표준화 동학을 주장, HBM/HBF 로드맵(HBM4/8, HBF5) 및 장기 계약 전략을 통해 시장 종속 구조 강화 가능성을 강조.

## [2026-04-20] ingest | ONNX와 ONNX Runtime

Added source. Key claims: ONNX는 프레임워크 간 상호운용 표준으로서 그래프 기반 모델 포맷을 제공하고, [[ONNXRuntime]]는 그래프 최적화·실행 공급자 파티셔닝·경량 API/학습 지원을 통해 다양한 하드웨어에서 고성능 추론을 수행한다. 또한 [[Microsoft]]의 실제 운영 사례에서 ONNX Runtime 성능 향상 수치가 제시되며, 모델 획득은 변환/ONNXZoo/Azure Custom Vision/직접 학습 경로로 정리되었다.

## [2026-04-20] ingest | ONNX-MLIR 기반 추론 컴파일 파이프라인

Added source. Key claims: ONNX 모델은 [[ONNX-MLIR]] 파이프라인에서 [[ONNX]]→[[MLIR]](Krnl/Affine/Std)→[[LLVM]] 흐름으로 최적화되어 추론 실행 산출물로 변환되며, IBM 메인프레임의 [[zAIU]]/[[zDNN]] 경로를 포함하고, 버퍼링·상수 처리·컴파일 시간 최적화가 성능 개선 포인트로 제시되었다.

## [2026-04-20] ingest | Vibe coding in prod

Added source. Key claims: [[VibeCoding]] is defined as a production-safe workflow centered on 
3-part execution: ([[AI의 PM 역할]], [[LeafNode]]-first changes, and explicit [[TestDrivenDevelopment]]-backed verification). The source emphasizes that trust must be restored through checkable outputs rather than exhaustive code reading, and extends the existing [[ClaudeCode]]/[[Anthropic]] narrative with concrete risk-aware guidance.

## [2026-04-19] ingest | Vibe coding in prod

Added source. Key claims: 정의적으로는 AI가 코드를 생성하는 것이 아니라 제품 중심·검증 중심으로 운영하는 방법을 제시하며, AI의 PM 역할 강화와 [[LeafNode]] 중심의 변경 전략을 중심 축으로 삼는다; Anthropic/[[ClaudeCode]] 사례를 통해 프로덕션 적용 시 기술 부채 통제와 보안 구간 분리가 중요함을 강조한다; [[TestDrivenDevelopment]]와 스트레스 테스트 기반의 체크포인트를 통해 구현 상세를 모두 읽지 않아도 신뢰를 축적하는 운영 모델이 제시된다.

## [2026-04-16] ingest | Bulk corpus sync

- Rebuilt `wiki/index.md` and `wiki/overview.md` after confirming all raw markdown sources are represented in `wiki/sources/`.
- Corpus status: 64 sources, 91 entities, 65 concepts.

# Wiki Log

Append-only chronological record of all operations.

Format: `## [YYYY-MM-DD] <operation> | <title>`

Parse recent entries: `grep "^## \[" wiki/log.md | tail -10`

---

## [2026-04-18] graph | Knowledge graph rebuilt

221 nodes, 1880 edges (1117 extracted, 763 inferred).

## [2026-04-19] graph | Knowledge graph rebuilt

227 nodes, 1920 edges (1140 extracted, 780 inferred).

## [2026-04-20] graph | Knowledge graph rebuilt

228 nodes, 1932 edges (1147 extracted, 785 inferred).

## [2026-04-21] graph | Knowledge graph rebuilt

393 nodes, 3307 edges (1792 extracted, 1515 inferred).

## [2026-04-25] graph | Knowledge graph rebuilt

426 nodes, 1900 edges (1900 extracted, 0 inferred).

## [2026-04-25] graph | Knowledge graph rebuilt

432 nodes, 1931 edges (1931 extracted, 0 inferred).

## [2026-04-25] graph | Knowledge graph rebuilt

458 nodes, 2122 edges (2122 extracted, 0 inferred).

## [2026-04-26] graph | Knowledge graph rebuilt

468 nodes, 2140 edges (2140 extracted, 0 inferred).

## [2026-04-26] graph | Knowledge graph rebuilt

473 nodes, 2218 edges (2218 extracted, 0 inferred).

## [2026-04-27] graph | Knowledge graph rebuilt

494 nodes, 2351 edges (2351 extracted, 0 inferred).

## [2026-04-28] graph | Knowledge graph rebuilt

498 nodes, 2400 edges (2400 extracted, 0 inferred).

## [2026-04-29] graph | Knowledge graph rebuilt

513 nodes, 2497 edges (2497 extracted, 0 inferred).

## [2026-04-30] graph | Knowledge graph rebuilt

530 nodes, 2589 edges (2589 extracted, 0 inferred).

## [2026-05-01] graph | Knowledge graph rebuilt

542 nodes, 2668 edges (2668 extracted, 0 inferred).

## [2026-05-02] graph | Knowledge graph rebuilt

554 nodes, 2740 edges (2740 extracted, 0 inferred).
