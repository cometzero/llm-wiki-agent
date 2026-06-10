---
title: "CUDA Kernel"
type: entity
tags:
  - CUDA
  - GPU
  - Kernel
  - ParallelProgramming
  - ComputeCapability
  - MemoryHierarchy
  - ThreadHierarchy
  - CUDAProgrammingModel
sources:
  - cuda-refresher-the-cuda-programming-model-nvidia-technical-blog.md
---

# CUDA Kernel

A **CUDA Kernel** is a function authored in CUDA C/C++ (or another CUDA‑enabled language) that is executed concurrently by a large number of threads on an NVIDIA GPU. Declared with the `__global__` qualifier, a kernel is not called like a regular function from the host; instead it is *launched* from the CPU (the *host*) using a kernel‑launch syntax that specifies the execution configuration—how many thread blocks (grid) and how many threads per block (block dimensions). When the kernel is launched, the GPU hardware schedules the resulting threads across its many cores, exposing massive data‑parallelism.  

The kernel operates within the GPU’s **memory hierarchy**: it can read from and write to global memory, make use of fast on‑chip shared memory, allocate registers for per‑thread data, and manage local memory when resources are constrained. The kernel’s behavior is further governed by the GPU’s **compute capability**, which defines the set of hardware features and instructions available (e.g., support for certain atomic operations, DP4A, or tensor cores).  

Key actions and responsibilities associated with a CUDA Kernel include:

1. **Authoring the kernel code** – writing the parallel computation that each thread will perform.  
2. **Specifying the launch configuration** – determining grid size, block size, and optional shared‑memory allocation via `<<<gridDim, blockDim, shmem, stream>>>` (or the runtime API equivalents).  
3. **Data movement** – transferring input data from host to device and results back using `cudaMemcpy` or unified memory.  
4. **Synchronization** – using `__syncthreads()` within a block and optional stream/events synchronization to coordinate work.  
5. **Performance tuning** – applying techniques such as memory coalescing, bank‑conflict avoidance, occupancy maximization, and warp‑level primitives to exploit the hardware’s capabilities.  

Because a kernel runs entirely on the GPU, it can accelerate workloads that exhibit fine‑grained parallelism—such as matrix operations, image processing, neural‑network inference, scientific simulations, and Monte‑Carlo methods—orders of magnitude faster than a CPU‑only implementation. In the Personal LLM Wiki, the **CUDA Kernel** entity captures its definition, the semantics of kernel launches, its relationship to the **Thread Hierarchy** (grids, blocks, threads) and **Memory Hierarchy**, and the influence of **Compute Capability** on kernel behavior. Related concepts include **CUDA Kernel Launch**, **Thread Hierarchy**, **Memory Hierarchy**, and the broader **CUDA Programming Model**.