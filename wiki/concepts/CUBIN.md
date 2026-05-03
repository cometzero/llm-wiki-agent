---
title: "CUBIN"
type: concept
tags: [cuda, gpu, binary, compiler]
sources: [understanding-ptx-the-assembly-language-of-cuda-gpu-computing-nvidia-technical-blog]
last_updated: 2026-05-03
---

# CUBIN

CUBIN is the architecture-specific NVIDIA GPU binary produced from [[PTX]] by ptxas or by CUDA driver JIT compilation. A CUBIN targets a specific compute capability family such as `sm_80` or `sm_86`.

## Relationship to PTX
- PTX is portable across a range of future NVIDIA GPUs when JIT compilation is available.
- CUBIN is faster to load for known target GPUs but has narrower binary compatibility.
- CUDA applications often package both CUBIN and PTX variants in a [[Fatbin]].
