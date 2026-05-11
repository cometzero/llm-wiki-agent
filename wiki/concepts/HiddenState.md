---
title: "HiddenState"
type: concept
tags: [rnn, sequence-model, memory]
sources: [2026-05-11-day19-ai-ml-learning-review]
last_updated: 2026-05-11
---

The hidden state in an [[RNN]] is a vector that serves as the model's internal memory, summarizing information seen so far in the sequence. It is updated at each time step by combining the current input with the previous hidden state.

## Key Properties

- **Learned**: The hidden state is not hand-designed; it emerges from training to minimize loss.
- **Fixed-size**: The dimensionality is a hyperparameter (e.g., 5, 768, 4096).
- **Sequential**: Each hidden state depends on all previous inputs via the recurrence.
- **Compression**: All past information must be compressed into this fixed-size vector, which is a bottleneck for long sequences.

## Role in Sequence Tasks

- **Classification**: The final hidden state can be used as a sequence representation for classification.
- **Generation**: The hidden state is passed to a decoder to generate the next token.
- **Encoder-Decoder**: The encoder's final hidden state initializes the decoder.

## Limitations

- Information from early time steps can be overwritten or diluted as the hidden state is updated.
- Fixed capacity limits the amount of information that can be retained.
- This bottleneck motivates [[Attention]], which allows direct access to all past hidden states.

## Related
- [[RNN]]
- [[LSTM]]
- [[GRU]]
- [[Attention]]
- [[SequenceModel]]