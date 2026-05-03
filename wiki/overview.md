# Overview

This wiki synthesizes knowledge from multiple sources about AI, machine learning, hardware, autonomous systems, and their societal impacts.

## Core AI/ML Foundations

The wiki covers a structured 30-day learning path. Key mathematical foundations include:

- **Linear Algebra** (2026-04-29-ai-ml-learning-review): [[VectorSpace]], [[Basis]], [[LinearMap]], [[Rank]], [[DotProduct]], [[Norm]], [[CosineSimilarity]] — underpinning [[Embedding]], [[Attention]], and basic [[Gradient]] operations.
- **Probability & Statistics** (2026-04-24-ai-ml-learning-review): [[RandomVariable]], [[ProbabilityDistribution]], [[Probability]], [[PMF]], [[PDF]], [[CDF]], and moment/dependence notions like [[Expectation]], [[Variance]], [[Correlation]]. Also covers [[ConditionalProbability]] and [[BayesTheorem]] through [[Prior]], [[Likelihood]], [[Posterior]] as a core update mechanism.
- **Machine Learning as Function Approximation** (2026-04-25-ai-ml-learning-review): [[FunctionApproximation]], [[HypothesisSpace]], [[LossFunction]], [[FeatureMatrix]], [[CurseOfDimensionality]].
- **Optimization via Calculus** (2026-04-26-ai-ml-learning-review, [[2026-04-27-ai-ml-learning-review]], [[2026-04-28-ai-ml-learning-review]]): [[Derivative]], [[PartialDerivative]], [[Gradient]], [[DirectionalDerivative]], [[ChainRule]], [[Jacobian]], [[ComputationalGraph]], [[ForwardPass]], [[BackwardPass]], [[Backpropagation]], [[Autograd]], [[GradientDescent]], [[LearningRate]], [[VanishingGradient]], [[ExplodingGradient]], [[MiniBatch]], [[Variance]], [[Momentum]], and [[Adam]], and the practical implications for [[Convergence]], [[Divergence]], and Oscillation.

## Core Learning Flow Added by Day 05

AI/ML learning starts from setting an [[Objective]], evaluating [[LossFunction]] through [[EmpiricalRisk]], then iterating [[GradientDescent]] with an [[UpdateRule]]. Learning stability is dominated by the [[LearningRate]] and regularization controls such as [[Constraint]], [[Regularization]].

## Core Learning Flow Added by Day 06

[[MiniBatch]] provides a practical gradient estimator tradeoff between compute and variance, enabling faster practical convergence but requiring careful noise-aware optimization control.

## Core Learning Flow Added by Day 07

[[HypothesisSpace]], [[Capacity]], and [[Overfitting]] are the key structural trio: bigger capacity improves fit but increases risk without sound validation design.

## Core Learning Flow Added by Day 08

Generalization is managed through the balance of [[BiasVarianceTradeoff]], with regularization and data split discipline reducing the risk of brittle memorization.

## Core Learning Flow Added by Day 09

Evaluation requires a utility-driven lens: not all metrics are equal for all decisions; [[CrossValidation]], [[Precision]], [[Recall]], and [[F1Score]] are used by failure-cost context.

## Core Learning Flow Added by Day 10

[[LinearRegression]], [[LogisticRegression]], and [[DecisionBoundary]] framing connect geometric separation to practical classification logic.

## Core Learning Flow Added by Day 11

SVM/SNN/DecisionTree triad frames the robustness of margins, local neighborhoods, and recursive splits as complementary paths to generalization.

## GPU, Memory, and CUDA Execution

A new source adds a lower-level systems perspective on [[GPU]] design and why it matters for deep learning:

- [[GPU]]s are framed as throughput-first processors, while [[CPU]]s remain latency-optimized.
- [[DRAM]] and [[SRAM]] explain the tradeoff between capacity and access speed in [[GlobalMemory]], [[SharedMemory]], and [[Registers]].
- [[CUDA]] programming is mapped to kernels, blocks, and warps, with [[SIMT]] execution explaining how a warp shares instructions across threads.
- [[WarpDivergence]] and memory alignment issues are highlighted as practical performance hazards.
- [[TensorCores]] are presented as the specialized compute path that makes modern deep learning practical at scale.

This complements the wiki's broader AI hardware arc, which already covers [[NVIDIA]] Tensor Core evolution, [[Hopper]], [[Blackwell]], and inference-centric system design. The new material grounds those later-generation architectures in the foundational constraints of memory hierarchy and warp-level execution.

### Deep Learning as Matrix-Multiply Workload

The source reinforces a recurring theme across the wiki: deep learning changes architectures, but the computational core remains dominated by large matrix multiplications.

- [[AlexNet]] is treated as the historical proof point that enough data plus enough compute can unlock much better feature learning than hand-engineered pipelines.
- [[ImageNet]] remains the canonical benchmark for that breakthrough.
- Later model families such as [[CNN]], [[RNN]], [[Transformer]], and [[SSM]] differ structurally, but all still depend heavily on dense linear algebra.

### Practical Implications for Inference

The source also connects directly to inference optimization:

- minimize global memory access when possible,
- use [[SharedMemory]] and [[Registers]] efficiently,
- understand that [[GPU]]s hide latency by switching work rather than eliminating latency,
- and keep execution fed with enough data to sustain occupancy.

That aligns with the wiki's existing [[InferenceOptimization]], [[InteractiveInference]], and [[AIInfrastructure]] themes, where bandwidth, memory staging, and scheduling decisions often matter more than peak FLOPS alone.

## Neural Network Quantization and Number Formats

A new source adds a dedicated systems and numerics perspective on [[NeuralNetworkQuantization]]:

- [[INT8]], [[FP16]], [[BF16]], and [[FP8]] are framed as practical points on a range between range, precision, and hardware cost.
- [[FixedPoint]] and [[FloatingPoint]] are contrasted as simple scaling-based versus exponent-based representations.
- [[IEEE754]]-style floating point is shown to trade complexity for dynamic range, while low-bit formats shift the burden onto calibration, scaling, and accumulation.
- [[PostTrainingQuantization]] and [[QuantizationAwareTraining]] represent the two main adaptation paths from full precision to reduced precision.
- [[BlockNumberFormats]], [[LogNumberSystems]], [[NF4]], [[AF4]], and [[PAL]] show that quantization research is not only about fewer bits, but about matching value distributions more cleverly.
- The source reinforces a recurring hardware theme in the wiki: the best numeric format depends on the workload, the distribution of values, and the data movement path, not just the raw bit width.

This also complements the wiki's existing [[NVIDIA]] [[Hopper]] and [[Blackwell]] materials, where low-precision training and inference formats are tied to tensor-core design, memory traffic, and energy efficiency rather than being treated as isolated model tricks.

## Blackwell Microarchitecture and Data Path Rework

A new Blackwell-focused source adds a more detailed systems view of how modern AI accelerators are changing:

- [[Blackwell]] B200 combines a dual-die package, unified memory addressability, and much larger on-chip resources to behave as a single logical device.
- [[TensorMemory|TMEM]] is the main architectural break from Hopper: tensor compute no longer relies only on registers and shared memory.
- [[tcgen05.mma]] and related [[PTX]] instructions shift tensor execution toward finer-grained, thread-level dispatch and lower single-instruction latency.
- The [[DecompressionEngine|DE]] offloads common compression formats so compressed model weights and datasets can stay resident in memory while being transparently decompressed on demand.
- Low-precision formats such as [[FP4]] and [[FP6]] are now first-class tuning knobs for [[LLM]] inference, not just research curiosities.

This strengthens the wiki's existing [[Blackwell]] and [[Hopper]] materials by showing that the next frontier is not only more tensor throughput, but also more explicit control over memory movement, compression, and operand staging.

## Autonomous Driving VLA Study

A new source introduces a dedicated weekly study corpus for [[VisionLanguageActionForAutonomousDriving]]. It centers the question of whether language meaningfully improves [[ActionGrounding]] and driving safety, or whether it remains a thin explanatory layer on top of behavior.

- The study process is weekly, structured, and time-boxed around [[Asia/Seoul]] scheduling.
- The analysis frame is explicitly closed-loop and safety-oriented rather than purely offline benchmark-driven.
- The documentation style emphasizes tables, diagrams, and evaluation matrices, which suggests a preference for comparing action fidelity, language role, and long-tail robustness across papers.
- The corpus also includes a reusable note template that standardizes translation, architecture analysis, evaluation comparison, and critique for each weekly paper.
- This adds an autonomous-driving-specific strand to the wiki's existing [[VLA]], [[ClosedLoopEvaluation]], and [[Safety]] themes.

### VLA for Autonomous Driving Taxonomy

The newest weekly study note expands this strand into a more detailed taxonomy. It distinguishes [[VisionAction|VA]] from [[VisionLanguageActionForAutonomousDriving|VLA]], then further splits VLA into [[EndToEndVLA]] and [[DualSystemVLA]]. Within that map, the key question is not whether a model can talk about the scene, but whether language actually grounds into executable action at the waypoint, trajectory, or control level.

- [[ActionGrounding]] is the primary test for whether a model deserves to be treated as driving policy rather than explanation layer.
- [[ClosedLoopEvaluation]] and safety monitors matter more than text-only metrics.
- [[LongTailGeneralization]] is framed as a safety requirement, not just a benchmark claim.
- The weekly study notes are therefore evolving into a reusable evaluation language for future VLA papers.
