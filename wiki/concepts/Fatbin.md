---
title: "Fatbin"
type: concept
tags: [cuda, gpu, binary, compatibility]
sources: [understanding-ptx-the-assembly-language-of-cuda-gpu-computing-nvidia-technical-blog]
last_updated: 2026-05-03
---

# Fatbin

A CUDA fatbin is a container that can bundle multiple GPU-code variants, including architecture-specific [[CUBIN]] binaries and portable [[PTX]].

## Compatibility role
Fatbins let a CUDA application load precompiled CUBIN for known GPU compute capabilities while retaining PTX for driver-side JIT compilation on newer compatible GPUs. This balances startup performance with forward compatibility.
