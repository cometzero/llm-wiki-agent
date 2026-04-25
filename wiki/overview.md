# Wiki Overview

Living synthesis across all sources. Last updated: 2026-04-25.

## AI/ML Foundations

머신러닝은 [[FunctionApproximation]] 문제로 이해할 수 있다. [[HypothesisSpace]]는 모델이 탐색할 함수 집합, [[LossFunction]]은 오차 측정 기준이다. 데이터는 [[FeatureMatrix]] (sample × feature)로 표현되며, [[DeepLearning]]에서는 [[Tensor]] shape 이해가 필수적이다. 고차원 공간에서는 [[CurseOfDimensionality]]가 발생하여 거리 개념이 약화되고 overfitting 위험이 커지므로, [[RepresentationLearning]], [[Regularization]], [[DimensionalityReduction]]이 중요해진다.

Day 03에서는 이 관점이 더 직접적으로 정리된다. 머신러닝은 입력을 출력으로 대응시키는 함수를 학습하는 문제이며, [[HypothesisSpace]]는 후보 함수를 제한하는 탐색 공간, [[LossFunction]]은 그 후보의 성능을 재는 기준이다. 분류, 회귀, sequence modeling, next-token prediction은 같은 함수 근사 틀 안에서 이해할 수 있고, [[FeatureMatrix]]와 [[Tensor]]는 이러한 함수를 실제 데이터 구조 위에 구현하기 위한 표현 언어다.

또한 고차원 공간에서는 데이터가 희소하게 퍼지면서 거리 기반 방법의 신뢰성이 떨어지고, [[NearestNeighbor]], [[DensityEstimation]], nonparametric method가 불안정해진다. 따라서 [[RepresentationLearning]]으로 더 좋은 좌표계를 학습하고, [[Regularization]]으로 과적합을 줄이며, [[DimensionalityReduction]]으로 문제를 다루기 쉬운 차원으로 압축하는 전략이 중요해진다.

또한 [[VectorSpace]] 기반 시각에서 벡터는 고정 실체가 아니라 표현 대상이며, [[Coordinate]]는 [[Basis]]에 따라 달라진다. 이 관점은 [[Matrix]]를 단순 배열이 아닌 [[LinearMap]]로 해석하게 하고, [[Attention]]의 점수 계산, [[EmbeddingRetrieval]], [[Gradient]] 처리에서 [[DotProduct]], [[Norm]], [[CosineSimilarity]]가 중심이 되는 이유를 설명한다.

Day 02에서는 여기에 [[Probability]]와 [[Statistics]] 기초가 덧붙는다. [[RandomVariable]]와 [[ProbabilityDistribution]], 이산/연속 표현인 [[PMF]], [[PDF]], [[CDF]], 그리고 [[Expectation]], [[Variance]], [[Covariance]], [[Correlation]]을 통해 불확실성과 분산 구조를 정리하고, [[ConditionalProbability]]/[[BayesTheorem]]에서 [[Prior]], [[Likelihood]], [[Posterior]]로 정보가 갱신되는 프레임을 통해 분류·진단·의사결정 문제와 연결한다.

## AI Infrastructure & Hardware

[[NVIDIA]]의 [[GPU]]-[[LPU]] 이원 구조, [[RiscV]]의 AI 확장, [[Terafab]]의 우주 기반 컴퓨팅 등 하드웨어 계층에서도 AI 추론 효율을 극대화하기 위한 다양한 접근이 진행 중이다. [[EAGLE3]]는 [[TrainingTimeTest]]를 통해 추론 가속 스케일링을 보여준다.

## AI Safety & Governance

[[Anthropic]]의 [[ProjectGlasswing]]은 AI를 활용한 취약점 탐지 협력 모델을, [[차지호]]의 프레임은 [[UN]] 기반 AI 거버넌스와 [[ConnectedIntelligence]]를 제시한다. [[AndrejKarpathy]]는 [[AutoResearch]]와 [[ModelSpeciation]]을 통해 AI 에이전트의 자율성과 조직 최적화를 논의한다.

## Market & Economics

[[H100]] 렌탈 가격, [[DRAM]] 현물가, [[HBM]] 수급, [[SpaceX]] 상장 등 AI 인프라 수요와 반도체 시장의 구조적 변화가 관찰된다. [[ClaudeCode]]는 에이전트형 코딩의 변곡점으로 평가된다.