# Wiki Overview

## 2026-W28 Hugging Face VLA deployment/update
- [[Embodied-cpp]] extends the VLA/WAM corpus toward deployment infrastructure: multi-rate execution, latency-first batch-1 inference, and five-layer C++ runtime abstraction for heterogeneous robots and edge devices.
- [[VLACorrector]] extends the action-chunking corpus toward adaptive closed-loop execution: [[LatentSpaceVisionMonitor]] detects stale chunks and [[OnlineGradientGuidance]] guides recovery replans.
- Together these papers emphasize that VLA progress depends not only on action generation quality, but also on runtime scheduling, monitoring, invalidation, and recovery under real closed-loop constraints.

## LWN Weekly Linux/Open Source Tracking
- The July 2, 2026 LWN translation adds [[DebianProtestware]], [[Git255]], [[RhombusMetaprogramming]], [[KernelHardening]], [[KernelWriteback]], [[BPFLocalStorage]], [[SecureBootCertificateExpiration]], and [[ObjectStorageAlternatives]] to the recurring Linux/open-source operations corpus.
- Across the May–July LWN sources, the wiki now tracks a continuous thread from package and publishing trust ([[SupplyChainSecurity]], [[AURSupplyChainAttack]], [[TrustedPublishing]]) to kernel release flow ([[LinuxKernel72]], [[BPF]], [[KernelHardening]]) and operational infrastructure ([[OSPM2026]], [[RMRBRMR]], [[ObjectStorageAlternatives]]).
