## AI/ML Learning Series

### Day 23: Transformer Block Stabilization Components

This section extends the [[Transformer]] architecture foundation from [[2026-05-14-day22-ai-ml-learning-review|Day 22: Transformer Block, Multi-Head Attention, Positional Encoding]] with three critical stabilization components:

#### Residual Connection
- Formula: `y = x + F(x)` — preserves original information through skip path
- Enables deep networks (50+ layers) by providing direct gradient path
- Applied after [[Attention]] and [[PositionWiseFFN]] in each Transformer block

#### LayerNorm
- Normalizes per-token hidden state along feature dimension (not batch)
- Key difference from [[BatchNormalization|BatchNorm]]: independent of batch size and sequence length
- Stabilizes numerical scale across layers; critical for deep Transformer training
- Modern LLMs favor [[PreLN]] over [[PostLN]] for training stability

#### Position-wise FFN
- MLP applied independently to each token: expand → non-linear activation → contract
- Typical dimensions: `d_model=768` → `d_intermediate=3072` → `d_model=768`
- Complements [[Attention]]: mixes information between tokens (attention) vs transforms features per token (FFN)
- Contains majority of Transformer parameters

**Connection to prior days:**
- [[2026-05-13-day21-ai-ml-learning-review|Day 21: QKV, Scaled Attention, Self-Attention]] — attention mechanism
- [[2026-05-14-day22-ai-ml-learning-review|Day 22: Transformer Block, Multi-Head Attention, Positional Encoding]] — full Transformer block architecture

**Next:** Continue with advanced Transformer concepts and training techniques.