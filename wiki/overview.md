## AI/ML Learning Series

### Day 24: Causal Mask and Attention Extensions
- Covers [[AttentionMasking]], [[CausalMask]], [[PaddingMask]], [[EncoderDecoderAttention]], and [[TransformerParallelism]].
- Introduced masking as an information-access control mechanism and explained why self-attention has quadratic cost in sequence length.

### Day 25: LLM 기본 파이프라인 — next-token prediction, tokenization, pretraining
- Adds the full foundational loop for LLMs: input text is segmented by [[Tokenization]], converted via [[Embedding]], and trained with [[NextTokenPrediction]] under [[CausalLanguageModel]] framing.
- Shows how [[SelfSupervisedLearning]] creates objectives from raw text and why [[Objective]], [[Loss]], and [[Optimizer]] define learning behavior.
- Connects tokenizer design ([[Subword]], [[BytePairEncoding]], [[Vocabulary]], [[SpecialToken]]) to quality, context efficiency, and inference cost.
- Clarifies why [[CausalLanguageModel]] and [[MaskedLanguageModel]] are better choices for generation vs understanding-style tasks.

### Linkage
- **Day 24 → Day 25:** Masking concepts from token attention set the training condition that next-token generation must respect.
- **Day 25 → Day 26 (next):** Next-step will cover sampling controls (temperature/top-k/top-p), decoding stability, and decoding-time trade-offs.