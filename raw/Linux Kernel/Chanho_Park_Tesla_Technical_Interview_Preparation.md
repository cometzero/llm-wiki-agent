# Tesla Korea Linux Kernel Engineer 기술면접 준비 자료

**지원자:** Chanho Park  
**면접 유형:** 1시간 기술면접, Portfolio 중심 발표 + 경력/기술 질의  
**기준 자료:** 제출 Resume 및 10-page Portfolio  
**작성 목적:** 발표 스크립트, 예상 질문/답변, 핵심 기술 복습, 당일 체크리스트

> 이 문서의 답변은 제출 자료를 바탕으로 만든 **면접용 초안**입니다. 실제로 직접 수행한 범위와 결과만 말하고, `[실제 사례/수치로 교체]` 표시는 반드시 본인의 경험으로 채우십시오. 회사 내부의 비공개 IP 이름, 주소 맵, 고객별 설정, 성능 수치, 장애 로그는 공개하지 말고 설계 원칙과 문제 해결 방법으로 설명하십시오.

---

## 0. 이번 면접에서 전달할 세 가지 메시지

1. **Kernel depth**  
   Linux kernel/BSP, device tree, bootloader, device driver, PREEMPT_RT, debugging/performance, upstream을 하나의 흐름으로 다룰 수 있다.

2. **Bring-up ownership**  
   초기 SoC architecture 단계부터 FVP/QEMU/QBox/ZeBu 기반 pre-silicon bring-up, 실제 silicon 안정화, build/release architecture까지 연결할 수 있다.

3. **System-level breadth**  
   Automotive, IoT, digital camera, mobile, wearable, TV, HPC에서 hardware, firmware, kernel, platform 팀 사이의 경계를 정의하고 장기 유지 가능한 BSP를 설계해 왔다.

### 면접관이 확인하려는 핵심

| 평가 축 | 제출 자료에서 연결할 근거 | 면접에서 보여줄 것 |
|---|---|---|
| Linux kernel/driver 깊이 | ExynosAuto, ARTIK, Tizen, NX300 | probe, IRQ, clock/reset, DMA, UFS, DT, debugging을 구체적으로 설명 |
| Pre/post-silicon bring-up | Hyundai FVP/QEMU/QBox, Exynos v920 ZeBu | 단계별 bring-up plan, 로그/가설/검증 방식, 모델 한계 설명 |
| Realtime Linux | Exynos v920 PREEMPT_RT bring-up | RT의 구조적 차이, driver audit, latency 측정과 한계 |
| Architecture/maintainability | Yocto layers, multi-OEM/single-binary, GKI | 공통화 경계, variant 관리, 업그레이드/회귀 전략 |
| Performance/debug | perf, ftrace, ARM Streamline | 도구 선택 기준과 실제 debugging funnel |
| Open source | Linux/U-Boot/Tizen upstream | patch 선정, review 대응, upstream-first의 장단점 |
| Communication/ownership | BSP lead, Google/OEM/HW collaboration | 본인의 결정, 타 팀과의 interface, 결과와 교훈 |

---

## 1. 권장 1시간 운영안

면접 시작 시 다음처럼 제안합니다.

> “Portfolio 발표는 약 12분으로 준비했습니다. 먼저 핵심 경력과 대표 프로젝트를 설명드린 뒤, 나머지 시간에는 기술 질문을 중심으로 진행하겠습니다.”

| 시간 | 권장 진행 | 목표 |
|---:|---|---|
| 0-2분 | 인사, 발표 시간 확인, 60-90초 자기소개 | 평가 프레임을 먼저 제시 |
| 2-14분 | Portfolio 발표 | 핵심 사례 3개를 일관된 이야기로 연결 |
| 14-50분 | 기술/경력 심층 질문 | 결론-근거-검증-교훈 구조로 답변 |
| 50-57분 | 면접관에게 질문 | 역할의 실제 문제와 기대 수준 확인 |
| 57-60분 | 20초 요약 및 감사 | 세 가지 메시지를 다시 고정 |

### 발표에서 사용할 대표 사례 3개

- **현재:** Hyundai AD/Gateway SoC software architecture + virtual platform 기반 early development
- **가장 직접적인 직무 적합 사례:** ExynosAuto v9/v920 BSP lead + upstream + ZeBu PREEMPT_RT bring-up
- **넓이와 확장성:** ARTIK/Tizen/HPC에서 boot, distro, architecture, platform enablement

---

# 2. 자기소개

## 2.1 한글 75-90초 버전

안녕하세요. Linux Kernel과 SoC System Software를 중심으로 20년 이상 임베디드 소프트웨어를 개발해 온 박찬호입니다.

제 핵심 강점은 초기 SoC architecture 단계에서 boot chain과 BSP 구조를 설계하고, pre-silicon 환경에서 Linux를 bring-up한 뒤, device driver, Yocto build architecture, debugging, upstream까지 연결해 유지 가능한 플랫폼으로 만드는 것입니다.

삼성 System LSI에서는 ExynosAuto v9과 v920의 BSP Lead로서 Linux kernel maintenance, ExynosAuto v9 mainline contribution, v920의 Synopsys ZeBu 기반 PREEMPT_RT Linux bring-up, Android Automotive GKI, 그리고 multi-OEM single-binary source architecture를 담당했습니다.

현재 현대자동차에서는 ARM64 기반 자율주행 SoC와 RISC-V 기반 vehicle gateway SoC의 system software architecture, FVP/QEMU/QBox 기반 pre-silicon 개발, Yocto 및 Linux kernel source/build architecture를 맡고 있습니다.

또한 IoT, Tizen, digital camera, wearable, HPC를 거치며 Linux kernel, U-Boot, Tizen에 upstream contribution을 해왔습니다. 저는 hardware, firmware, kernel 사이의 interface를 명확히 정의하고 bring-up 리스크를 silicon 이전 단계로 앞당겨 줄이는 데 강점이 있으며, 이 경험을 차세대 AI SoC Linux platform 개발에 기여하고 싶습니다.

## 2.2 한글 30초 버전

안녕하세요. Linux Kernel과 SoC System Software를 20년 이상 개발해 온 박찬호입니다. ExynosAuto BSP Lead로 Linux upstream, ZeBu 기반 PREEMPT_RT bring-up, Android GKI와 multi-OEM BSP architecture를 담당했고, 현재는 ARM64/RISC-V Automotive SoC architecture와 FVP/QEMU/QBox 기반 pre-silicon 개발을 수행하고 있습니다. Kernel 깊이와 system architecture, 그리고 hardware/firmware 팀을 연결하는 bring-up ownership이 저의 강점입니다.

## 2.3 English 75-90 second version

Hello, I’m Chanho Park. I’m a Linux kernel and SoC system software engineer with more than 20 years of experience in embedded systems.

My core strength is taking a platform from early SoC architecture and pre-silicon bring-up to a maintainable, production-quality BSP, including boot firmware, Linux kernel, device tree, device drivers, Yocto build architecture, debugging, and upstream contribution.

At Samsung System LSI, I led Exynos Auto v9 and v920 BSP development. My work included mainline Linux contributions for Exynos Auto v9, PREEMPT_RT-based Linux bring-up on Synopsys ZeBu for v920, Android Automotive GKI, and a multi-OEM single-binary kernel architecture.

At Hyundai, I currently work on ARM64 autonomous-driving SoC and RISC-V vehicle-gateway SoC software architecture, using FVP, QEMU, and QBox-based virtual platforms for pre-silicon development.

I also have broad experience across IoT, Tizen, digital cameras, wearables, and HPC, with upstream contributions to Linux, U-Boot, and Tizen. I believe my value is the combination of deep kernel experience, system-level architecture, and the ability to connect hardware, firmware, and platform teams to de-risk bring-up and deliver robust system software.

## 2.4 English 30 second version

Hello, I’m Chanho Park, a Linux kernel and SoC system software engineer with over 20 years of embedded experience. I led Exynos Auto BSP development, including upstream Linux work, PREEMPT_RT bring-up on ZeBu, Android GKI, and multi-OEM BSP architecture. I currently work on ARM64 and RISC-V automotive SoC architecture and pre-silicon development using FVP, QEMU, and QBox. My strength is combining kernel depth, system architecture, and end-to-end bring-up ownership.

## 2.5 말할 때 주의할 점

- “20년 경력”만 강조하지 말고 **최근에도 hands-on으로 kernel/architecture/debugging을 수행한다**는 점을 바로 연결합니다.
- `Principle Engineer`가 아니라 **Principal Engineer**라고 말합니다.
- “모든 것을 했다”보다 **내가 결정한 부분, 직접 구현한 부분, 팀이 수행한 부분**을 구분합니다.
- 문장을 외우기보다 `Kernel depth -> Bring-up ownership -> Cross-domain breadth` 세 축만 기억합니다.

---

# 3. Portfolio 발표 가이드와 스크립트

## 3.1 전체 시간 배분

| Portfolio page | 주제 | 시간 | 핵심 메시지 |
|---:|---|---:|---|
| 1 | Title | 10초 | Linux Kernel/BSP engineer 정체성 |
| 2-3 | About me / Skills | 1분 20초 | 20년을 분야 나열이 아니라 반복 가능한 역량으로 설명 |
| 4 | Hyundai AD SoC | 2분 | architecture + pre-silicon + Yocto/kernel |
| 5 | Green Supercomputer | 1분 | RISC-V boot architecture와 조사/선행개발 범위 |
| 6 | Exynos Auto v9/v920 | 4분 30초 | 가장 중요한 대표 사례, 질문 유도 |
| 7 | ARTIK | 55초 | 여러 SoC/distro/kernel version을 반복 enable한 경험 |
| 8 | Tizen | 55초 | ARM64 platform enabling, kernel optimization, product breadth |
| 9 | Open Source | 50초 | 검증 가능한 engineering evidence |
| 10 | Contact/Closing | 20초 | 세 가지 강점 재요약 |
| **합계** |  | **약 12분** |  |

## 3.2 Page 1 - Title

**권장 멘트**

> “안녕하세요, 박찬호입니다. 저는 Linux Kernel과 BSP를 중심으로 SoC bring-up, embedded platform architecture, 그리고 upstream을 수행해 온 system software engineer입니다. 오늘은 전체 경력을 나열하기보다 세 가지 대표 프로젝트를 중심으로 설명드리겠습니다.”

## 3.3 Page 2-3 - About me / Skills

**권장 멘트**

> “제 경력은 Automotive, IoT, Consumer, HPC로 넓지만, 반복해서 수행해 온 핵심 문제는 동일합니다. 새로운 SoC에서 boot chain과 kernel/BSP를 세우고, device driver와 build system을 연결하며, 성능과 안정성을 검증하고 장기 유지 가능한 source architecture로 만드는 일입니다. ARM64와 RISC-V, Linux/Yocto/Android/Tizen을 다뤘고, upstream review를 실제 제품 개발 프로세스와 연결해 왔습니다.”

**나올 수 있는 질문**

- 최근 3년간 직접 작성한 코드의 비중은 어느 정도인가?
- architecture 역할과 hands-on implementation의 경계는?
- 본인이 가장 깊다고 생각하는 subsystem은?

## 3.4 Page 4 - Hyundai AD SoC SW Development

**권장 멘트**

> “현재는 차세대 Automotive SoC의 software architecture를 설계하고 있습니다. ARM64 기반 AD compute domain과 RISC-V 기반 system-management 또는 gateway domain을 대상으로 boot firmware, Linux/RTOS, security component, BSP와 build flow의 경계를 정의합니다. 핵심은 silicon이 나오기 전에 FVP, QEMU, QBox/SystemC virtual platform에서 kernel boot, device tree, firmware interface와 platform assumption을 검증해 bring-up risk를 앞당기는 것입니다. 또한 Yocto layer와 kernel source/build architecture를 설계해 여러 target과 향후 silicon revision을 수용할 수 있도록 합니다.”

**깊게 준비할 질문**

- FVP, QEMU, QBox의 역할을 어떻게 나누었나?
- virtual platform에서 무엇을 검증하고 무엇은 검증할 수 없나?
- HW/SW interface specification에는 어떤 항목을 정의하나?
- ARM64 compute domain과 RISC-V management domain의 boot ownership은 어떻게 구분하나?
- 초기 architecture 단계에서 kernel team이 hardware에 요구해야 할 것은 무엇인가?

**말하지 말아야 할 것**

- 공개되지 않은 IP 이름, memory map, interrupt number, secure boot key flow, 성능 목표
- 특정 사내 조직이나 vendor의 결함을 직접 지목하는 설명

## 3.5 Page 5 - Green Supercomputer Project

**권장 멘트**

> “Green Supercomputer 프로젝트에서는 compute-node boot architecture를 조사하고 선행개발했습니다. Linux와 lightweight kernel을 병행하는 multi-kernel 구조를 분석했고, ARM Neoverse N2 FVP boot reference와 RISC-V boot firmware stack을 비교했습니다. VisionFive2를 이용해 U-Boot, EDK2, Oreboot, LinuxBoot의 역할과 전환 지점을 실험했습니다. 이 프로젝트는 production deployment가 아니라 architecture evaluation과 pre-development였다는 범위를 명확히 말씀드리겠습니다.”

**깊게 준비할 질문**

- multi-kernel이 OS noise를 줄이는 원리와 trade-off는?
- RISC-V M-mode/S-mode, SBI, OpenSBI/U-Boot의 관계는?
- Oreboot와 LinuxBoot를 왜 검토했나?
- kexec 기반 다음 단계 boot의 장단점은?

## 3.6 Page 6 - Exynos Auto v9/v920 SoC Project: 핵심 슬라이드

이 슬라이드는 직무 요구사항과 가장 직접적으로 연결됩니다. 발표의 절반 가까이를 사용해도 됩니다.

**권장 멘트**

> “가장 대표적인 경험은 Exynos Auto v9/v920 BSP Lead입니다. 처음에는 console과 timer, interrupt, storage 같은 최소 boot path를 안정화한 뒤 kernel version을 4.14에서 5.4, 5.10, 5.15로 단계적으로 올렸습니다. v9에서는 device tree, clock, watchdog, UFS 등 mainline contribution을 수행해 vendor tree의 장기 유지 비용을 줄였습니다.”
>
> “v920에서는 Synopsys ZeBu에서 EVT0 PREEMPT_RT 기반 Linux kernel bring-up을 리드했습니다. ZeBu에서는 절대적인 worst-case latency 수치를 silicon과 동일하게 평가할 수 없기 때문에, 초기 목표를 boot correctness, RT configuration compatibility, interrupt-threading과 driver context 문제, firmware/kernel interface validation으로 두었습니다. 실제 silicon 단계에서는 latency와 power를 다시 측정해야 한다는 구분이 중요했습니다.”
>
> “또한 여러 OEM과 v9/v920을 지원하기 위해 common kernel layer와 OEM-specific configuration/device-tree layer를 분리하고 single-binary support를 설계했습니다. Android Automotive GKI에서는 core kernel과 vendor module 사이의 KMI/ABI 안정성, module packaging, update flow를 고려했습니다. 이 경험을 통해 bring-up을 단발성 성공이 아니라 upgrade, variant, upstream, customer delivery까지 이어지는 platform engineering 문제로 다뤘습니다.”

**반드시 준비할 증거**

- 직접 맡은 subsystem/patch 2-3개: `[예: DT/clock/watchdog/UFS 중 실제로 가장 자신 있는 항목]`
- ZeBu 첫 console까지 막혔던 대표 문제 1개: `[비공개 내용을 제거한 일반화된 사례]`
- PREEMPT_RT 적용 후 발견한 driver/context 문제 1개: `[실제 사례로 교체]`
- multi-OEM/single-binary에서 해결한 충돌 1개: `[실제 사례로 교체]`
- kernel upgrade에서 가장 큰 regression 1개와 찾은 방법: `[실제 사례로 교체]`

## 3.7 Page 7 - ARTIK IoT Module

**권장 멘트**

> “ARTIK에서는 Exynos와 Nexell 기반 여러 module을 대상으로 U-Boot, Linux kernel 4.1/4.4/4.14, Fedora/Ubuntu rootfs, Yocto image generation을 반복적으로 enable했습니다. 이 경험에서 얻은 강점은 특정 보드 한 장의 bring-up이 아니라, SoC/board/distro 차이를 분리하고 여러 제품에 재사용 가능한 BSP와 build flow를 만드는 것입니다.”

## 3.8 Page 8 - Tizen Platform

**권장 멘트**

> “Tizen에서는 reference kernel maintainer와 ARM64 platform enabler 역할을 수행했습니다. ARM Juno에서 Linux kernel과 toolchain, 800개 이상의 package를 ARM64로 enable했고, perf/ftrace/ARM Streamline을 이용해 memory, filesystem, boot, wearable platform 성능을 분석했습니다. 이 시기 경험이 architecture와 distro 전체를 kernel 관점에서 연결하는 기반이 되었습니다.”

## 3.9 Page 9 - Open Source History

**권장 멘트**

> “Open source contribution은 단순 활동 이력이 아니라, 변경을 작게 분리하고 public interface와 compatibility를 고려하며 review feedback을 반영하는 제 engineering 방식의 증거입니다. Linux kernel에서는 ExynosAuto device tree, clock, watchdog, UFS 관련 변경을, U-Boot에서는 RISC-V/driver-model 관련 변경을 upstream했습니다.”

**발표 전 점검**

- Portfolio의 ARTIK 링크 중복은 발표 중 언급하지 않습니다.
- 브라우저에 Linux kernel, U-Boot contribution page를 미리 열어 둡니다.
- 링크를 클릭하라는 요청이 있을 때만 1-2개 representative patch를 보여줍니다.

## 3.10 Closing

> “정리하면 저는 Linux kernel을 깊게 다루면서도, boot firmware와 hardware interface, Yocto/Android platform, pre-silicon environment까지 연결해 SoC bring-up risk를 줄여 온 engineer입니다. 특히 Exynos Auto의 upstream, PREEMPT_RT ZeBu bring-up, multi-OEM BSP architecture 경험이 이번 역할에 가장 직접적으로 기여할 수 있는 부분입니다.”

---

# 4. 답변 구조: 기술면접용 C-D-I-V-R-L

경력 질문은 STAR만으로는 기술 깊이가 부족해 보일 수 있습니다. 다음 6단계를 권장합니다.

1. **Context** - 제품/SoC 단계와 본인의 역할
2. **Difficulty** - 왜 어려웠는지, 제약과 실패 조건
3. **Investigation/Decision** - 가설, 대안, 선택 기준
4. **Implementation** - kernel/driver/architecture 수준의 구체 내용
5. **Validation/Result** - 무엇으로 검증했고 무엇이 개선됐는지
6. **Lesson/Limit** - 한계, 다음 단계, 재발 방지

### 예: “ZeBu에서 PREEMPT_RT bring-up을 어떻게 했습니까?”

- **결론:** “ZeBu에서는 RT latency 수치 자체보다 PREEMPT_RT kernel의 functional bring-up과 driver-context compatibility를 조기에 검증했습니다.”
- **Context:** EVT0 이전, hardware emulator에서 kernel/firmware/BSP 통합이 필요한 단계.
- **Difficulty:** emulator timing은 silicon과 다르고, RT에서 IRQ/lock context가 non-RT와 달라질 수 있음.
- **Decision:** early console -> timer/GIC -> SMP -> storage/rootfs -> RT config/IRQ thread -> stress/trace 순으로 gate를 나눔.
- **Implementation:** RT config, threaded IRQ behavior, `spinlock_t`/`raw_spinlock_t`, sleep-in-atomic, long IRQ-off section, driver init ordering을 점검.
- **Validation:** boot milestone, ftrace/lockdep, interrupt delivery, scheduler/IRQ thread behavior, 반복 boot/stress로 기능 검증. `[실제 도구와 사례로 교체]`
- **Limit:** absolute worst-case latency와 power/thermal 영향은 silicon에서 `cyclictest`/`rtla timerlat`/`osnoise`와 workload stress로 다시 측정해야 함.

---

# 5. 예상 질문 및 답변

## A. 경력, 역할, 동기

### Q1. 20년 경력을 2분 안에 요약해 주세요.

**권장 답변**  
제 경력의 공통 축은 새로운 SoC에서 Linux platform을 enable하고 장기 유지 가능한 BSP로 만드는 것입니다. 초기에는 digital camera와 Tizen에서 bootloader, kernel, driver, performance를 깊게 다뤘고, ARTIK에서는 여러 SoC와 distro를 지원하는 Linux/Yocto platform을 구축했습니다. 이후 ExynosAuto에서는 BSP lead로 upstream, kernel upgrade, PREEMPT_RT ZeBu bring-up, Android GKI, multi-OEM architecture를 담당했습니다. 최근에는 HPC RISC-V boot architecture와 Automotive ARM64/RISC-V SoC software architecture, virtual platform 기반 pre-silicon 개발로 범위를 넓혔습니다. 따라서 제 강점은 경력의 길이보다 kernel depth, bring-up ownership, platform architecture가 함께 있다는 점입니다.

### Q2. 현재도 hands-on 개발을 합니까?

**권장 답변**  
네. 현재 역할에는 architecture 비중이 커졌지만, architecture를 문서로만 정의하지 않고 boot flow, device tree, kernel configuration, Yocto metadata, virtual platform behavior, low-level log를 직접 확인합니다. 과거 ExynosAuto에서는 kernel patch와 upstream review를 직접 수행했고, 현재도 새로운 interface를 정의할 때 최소 동작 코드나 reference boot path를 검증하는 방식으로 일합니다. 실제 코딩 비중은 프로젝트 단계에 따라 달라지지만, debugging 가능한 수준으로 implementation과 source를 계속 소유하는 것이 제 원칙입니다.

### Q3. 가장 자랑스러운 기술적 성과는 무엇입니까?

**권장 답변**  
ExynosAuto v9/v920 BSP ownership을 꼽겠습니다. 단일 기능 개발이 아니라 초기 bring-up, kernel upgrade, mainline contribution, PREEMPT_RT ZeBu bring-up, Yocto/Android platform, GKI, multi-OEM source architecture를 하나의 lifecycle로 연결했습니다. 특히 upstream과 variant architecture를 함께 설계해 단기 bring-up뿐 아니라 장기 유지 비용을 줄였다는 점이 의미가 있습니다. 결과는 `[실제 고객/릴리스/회귀 감소 사례로 교체]`로 검증했습니다.

### Q4. 실패하거나 예상보다 오래 걸린 문제는 무엇입니까?

**답변 틀**  
- 실패를 숨기지 말고 **초기 가정이 무엇이었고 어떤 evidence로 틀렸음을 알았는지** 설명합니다.
- 예: boot hang을 kernel regression으로 추정했지만 실제로는 model의 interrupt/clock behavior 불일치였던 사례.
- 재발 방지: milestone log, interface contract, model capability matrix, automated smoke test를 추가.

**권장 문장**  
“처음에는 `[가설 A]`로 접근했지만 trace와 register 상태를 비교해 보니 `[원인 B]`였습니다. 이후 software, model, RTL 팀이 같은 checkpoint를 볼 수 있도록 boot milestone과 expected register state를 문서화했고, 동일 유형의 문제를 더 빨리 분류할 수 있었습니다.”

### Q5. Architecture와 implementation 중 어느 쪽이 더 강합니까?

**권장 답변**  
Linux kernel/BSP implementation이 기반이고, 그 경험을 architecture 수준으로 확장해 왔습니다. 저는 두 역할을 분리해서 보지 않습니다. 좋은 SoC software architecture는 실제 driver probe, interrupt, DMA, power, boot dependency를 이해해야 하고, 좋은 implementation은 향후 silicon revision, OEM variant, update를 수용할 구조가 필요합니다. 제 차별점은 architecture decision을 source와 debug evidence로 검증할 수 있다는 점입니다.

### Q6. 왜 이 역할에 지원했습니까?

**권장 답변**  
이 역할은 custom AI SoC의 pre/post-silicon bring-up, Linux driver, realtime kernel, HW/SW interface, performance를 하나의 platform 문제로 다룹니다. 이는 제가 ExynosAuto와 현재 Automotive SoC에서 해 온 일과 가장 밀접합니다. 특히 AI accelerator와 camera/high-speed I/O가 결합된 시스템에서는 kernel이 단순 OS port가 아니라 latency, data movement, fault isolation, power를 결정하는 핵심 계층이라고 생각합니다. 저는 기존 kernel/BSP 경험을 활용하면서 AI platform의 workload-driven system optimization으로 범위를 넓히고 싶습니다.

### Q7. 본인의 역할과 팀의 역할을 구분해 주세요.

**권장 답변 구조**  
- “제가 직접 소유한 것”: architecture decision, critical boot path, patch/review, issue triage, cross-team interface
- “팀과 공동으로 한 것”: subsystem driver, validation matrix, release integration
- “타 팀이 소유한 것”: RTL/model/firmware/customer application

“Lead”라고 말한 뒤에는 반드시 **내가 내린 결정 1개, 직접 해결한 문제 1개, 팀을 움직인 mechanism 1개**를 제시합니다.

### Q8. 새로운 분야를 빠르게 학습하는 방법은?

**권장 답변**  
먼저 boot/data path를 한 장으로 그려 ownership과 interface를 분리합니다. 다음으로 architecture spec, kernel subsystem documentation, upstream driver, reference platform을 비교해 최소 동작 path를 정합니다. 그 뒤 로그와 trace를 얻을 수 있는 observability point를 먼저 만들고, 작은 milestone부터 검증합니다. RISC-V boot firmware나 GKI를 시작할 때도 같은 방식으로 기존 ARM/Linux 경험을 전이했습니다.

---

## B. Linux SoC bring-up 및 pre-silicon

### Q9. Pre-silicon Linux bring-up 절차를 설명해 주세요.

**권장 답변**  
저는 bring-up을 다음 gate로 나눕니다.

1. **Contract 확인:** memory map, reset value, clock/reset/power dependency, interrupt map, DMA/IOMMU, boot ownership
2. **Boot firmware:** CPU mode/EL, DRAM, console, DTB 전달, PSCI/SBI, kernel image placement
3. **Early kernel:** `earlycon`, decompression/entry, MMU/page table, timer, GIC/PLIC, SMP
4. **Core devices:** clock/reset, pinctrl, serial, storage, DMA/IOMMU
5. **Rootfs/userspace:** initramfs 또는 minimal Yocto image
6. **Functional drivers:** accelerator/camera/network/storage 순으로 enable
7. **Stress/negative test:** error injection, reboot, suspend/resume, interrupt/DMA load
8. **Post-silicon handoff:** model assumption과 silicon-only validation item을 분리

각 gate마다 expected log/register state와 owner를 정해 software 문제인지 model/RTL/firmware 문제인지 빨리 분류합니다.

### Q10. Kernel이 console 출력 전 멈췄다면 어떻게 디버깅합니까?

**권장 답변**  
먼저 “kernel에 진입하지 못함”, “진입했지만 early console이 틀림”, “MMU/exception에서 죽음”을 구분합니다.

- firmware에서 kernel entry address와 DTB address 검증
- ARM64라면 x0의 DTB physical address, EL, MMU/cache/interrupt 상태 확인
- image format/relocation/decompression 여부 확인
- UART clock/reset/base address와 `earlycon` parameter 검증
- JTAG/emulator breakpoint 또는 instruction trace로 `primary_entry`, `start_kernel` 도달 확인
- `CONFIG_EARLY_PRINTK`, `CONFIG_DEBUG_LL`, `ignore_loglevel` 등 환경에 맞는 수단 사용
- DT와 model memory map 비교

한 번에 많은 config를 바꾸지 않고, 마지막으로 확인된 milestone을 기준으로 binary search합니다.

### Q11. Console은 나오지만 rootfs mount 전에 멈추면?

**권장 답변**  
로그의 마지막 subsystem을 보는 동시에 root device dependency를 역추적합니다. storage host probe, regulator/clock/reset, PHY, DMA/IOMMU, partition, filesystem, kernel command line을 확인합니다. `initcall_debug`, deferred-probe log, dynamic debug, trace event를 사용하고, 가능하면 initramfs로 boot해 storage와 rootfs 문제를 분리합니다. UFS라면 HCI initialization, PHY/UniPro link startup, power mode transition, command completion IRQ를 단계별로 확인합니다.

### Q12. Device driver가 probe되지 않을 때 체크 순서는?

**권장 답변**  
1. DT node `status`, `compatible`, address/interrupt 확인
2. driver config가 built-in/module로 포함됐는지 확인
3. bus/device population과 modalias 확인
4. supplier dependency(clock/regulator/reset/PHY/IOMMU)와 `-EPROBE_DEFER` 확인
5. probe entry에서 resource acquisition 순서를 log/trace
6. binding YAML과 `dtbs_check` 확인
7. module이면 vermagic, symbol/KMI, signing 확인

`-EPROBE_DEFER`는 실패가 아니라 dependency가 아직 준비되지 않았다는 신호이므로 supplier ordering을 봅니다.

### Q13. Interrupt가 발생하지 않을 때 어떻게 접근합니까?

**권장 답변**  
장치에서 interrupt status가 실제로 set되는지부터 CPU까지 경로를 따라갑니다.

- device interrupt enable/status/clear semantics
- clock/reset/power와 event generation
- interrupt controller routing, SPI/PPI number, trigger type/polarity
- DT interrupt specifier와 affinity
- `request_threaded_irq()` 결과와 `/proc/interrupts`
- mask/ack/eoi 순서, shared IRQ 여부
- PREEMPT_RT에서는 IRQ thread가 생성되고 priority/affinity에 의해 지연되지 않는지
- ftrace `irq:*`, scheduler event로 hardirq와 thread wakeup 확인

### Q14. SMP secondary CPU가 online되지 않는다면?

**권장 답변**  
ARM64에서는 PSCI method/firmware, CPU DT node/MPIDR, secondary entry address, cache coherency, GIC redistributor, timer를 확인합니다. RISC-V에서는 hart DT, SBI HSM 또는 platform-specific hart start, interrupt/timer delivery를 확인합니다. primary와 secondary의 firmware state가 다르지 않은지, spin-table/PSCI/SBI 선택이 일관된지 확인합니다.

### Q15. DMA/IOMMU fault가 발생하면?

**권장 답변**  
먼저 CPU virtual address, physical address, DMA address를 혼동하지 않았는지 확인합니다. DMA API 사용, mapping direction, cache coherency, scatter-gather length, device DMA mask를 점검합니다. IOMMU에서는 stream ID, device-tree `iommus`/`iommu-map`, domain attach, page-table mapping과 fault syndrome를 확인합니다. 장치가 stale descriptor를 읽는다면 memory barrier와 descriptor ownership 전환도 봅니다. register dump, IOMMU fault log, DMA tracepoint를 같은 timestamp로 맞추는 것이 중요합니다.

### Q16. Virtual platform과 실제 silicon의 차이 때문에 생긴 문제를 어떻게 분류합니까?

**권장 답변**  
각 기능을 세 범주로 관리합니다.

- **기능적으로 신뢰 가능:** register programming, boot sequence, interrupt route, basic DMA contract
- **조건부 신뢰:** race, timeout, ordering, cache/coherency 모델
- **silicon에서만 검증:** absolute latency, bandwidth, power, thermal, analog PHY margin, errata

문제가 생기면 같은 software binary/config에서 model trace와 spec/RTL expected behavior를 비교합니다. timeout을 무조건 늘려 숨기지 않고, model이 느린 것인지 protocol state가 잘못된 것인지 구분합니다.

### Q17. Pre-silicon에서 post-silicon으로 무엇을 넘겨야 합니까?

**권장 답변**  
- 검증된 boot image/config와 재현 가능한 build manifest
- boot milestone별 expected log
- model capability/known limitation matrix
- silicon-only validation list
- firmware/kernel interface version
- register/interrupt/DMA test utility
- issue tracker에서 software/model/RTL owner가 분류된 open item
- first-silicon day checklist와 rollback image

### Q18. HW/SW interface specification에 어떤 내용을 넣습니까?

**권장 답변**  
memory map, reset value와 sequence, clock/power domain dependency, interrupt routing/trigger, DMA addressing/coherency, IOMMU stream ID, register access width/order, mailbox/doorbell protocol, shared memory layout, firmware ABI/versioning, error code/recovery, security ownership, low-power state와 wake-up source, observability register를 포함합니다. 가장 중요한 것은 정상 path뿐 아니라 timeout, reset, partial failure 시 ownership을 정의하는 것입니다.

---

## C. PREEMPT_RT / Realtime Linux

### Q19. PREEMPT_RT kernel은 일반 kernel과 무엇이 다릅니까?

**권장 답변**  
핵심 목표는 kernel 내부의 non-preemptible section을 줄여 높은 우선순위 task의 scheduling latency를 예측 가능하게 만드는 것입니다. 대표적으로 대부분의 interrupt handler가 threaded context로 이동하고, 일반 `spinlock_t`가 RT에서는 priority inheritance 가능한 sleeping lock semantics를 갖습니다. 반면 아주 낮은 수준에서 hard non-preemptible semantics가 필요한 코드는 `raw_spinlock_t`를 사용합니다. softirq, timer, per-CPU data protection도 RT에서 context와 locking assumption이 달라질 수 있어 driver audit가 필요합니다.

### Q20. Threaded IRQ는 어떻게 동작하며 왜 중요합니까?

**권장 답변**  
최소한의 hard IRQ top half가 interrupt를 acknowledge하고 IRQ thread를 깨운 뒤, 대부분의 handler work는 schedulable thread context에서 수행됩니다. 따라서 IRQ 처리에 priority와 affinity를 부여할 수 있고 높은 우선순위 real-time task와의 관계를 scheduler가 제어할 수 있습니다. 단, `IRQF_NO_THREAD`나 low-level interrupt controller처럼 hardirq에 남는 예외가 있고, shared IRQ나 긴 threaded handler는 여전히 latency 문제를 만들 수 있습니다.

### Q21. `spinlock_t`와 `raw_spinlock_t`의 차이는?

**권장 답변**  
non-RT에서는 둘 다 busy-wait spin semantics로 보일 수 있지만, PREEMPT_RT에서 일반 `spinlock_t`는 rtmutex 기반으로 바뀌어 sleep과 priority inheritance가 가능해집니다. 따라서 lock을 잡았다고 preemption/interrupt가 자동으로 꺼진다는 가정을 하면 안 됩니다. `raw_spinlock_t`는 hard interrupt/very low-level scheduler/arch code처럼 실제 non-preemptible spin이 필요한 곳에만 사용해야 합니다. driver에서 무분별하게 raw lock을 쓰면 latency를 악화시키므로 critical section을 최소화해야 합니다.

### Q22. Priority inversion과 priority inheritance를 설명해 주세요.

**권장 답변**  
낮은 우선순위 task가 lock을 가진 상태에서 높은 우선순위 task가 대기하고, 중간 우선순위 task가 CPU를 계속 사용하면 높은 우선순위 task가 간접적으로 오래 지연되는 것이 priority inversion입니다. PI mutex/rtmutex는 lock owner의 effective priority를 waiter 수준으로 일시적으로 올려 lock을 빨리 해제하게 합니다. 다만 긴 critical section, nested lock, non-PI primitive, IRQ-off section은 PI만으로 해결되지 않으므로 구조를 함께 바꿔야 합니다.

### Q23. 기존 driver를 PREEMPT_RT에 맞게 audit한다면?

**체크리스트**

- IRQ handler가 thread로 이동해도 안전한가?
- atomic context라고 가정한 코드가 있는가?
- `spinlock_t` 아래에서 sleep/non-atomic API 호출 여부
- `raw_spinlock_t`, `local_irq_disable`, `preempt_disable` 구간 길이
- per-CPU data가 단순 preempt disable만으로 보호되는가?
- hrtimer/softirq/tasklet/workqueue context assumption
- threaded IRQ priority/affinity와 shared IRQ 영향
- memory allocation flag와 blocking I/O
- lock ordering, lockdep, RT-specific warnings
- teardown에서 IRQ thread/work가 완전히 정리되는가?

### Q24. RT latency를 어떻게 측정합니까?

**권장 답변**  
한 가지 숫자만 보지 않고 층별로 측정합니다.

- `cyclictest`: user-visible wake-up latency의 기본 분포와 maximum
- `rtla timerlat`: timer IRQ latency와 RT thread wake-up latency를 분리하고 원인 trace 확보
- `rtla osnoise`: CPU에 발생하는 IRQ, softirq, thread 등의 interference 분석
- ftrace: `irq`, `sched`, `preemptirq`, function graph/event correlation
- application trace: inference/camera deadline과 kernel event를 end-to-end로 연결

idle state, DVFS, thermal, I/O, network, memory pressure, interrupt storm을 포함한 worst-case workload로 반복하고 percentile뿐 아니라 maximum outlier의 원인을 추적합니다.

### Q25. ZeBu에서 RT를 검증할 수 있습니까?

**권장 답변**  
기능 검증은 가능하지만 절대 latency 수치를 silicon과 동일하게 해석하면 안 됩니다. ZeBu에서는 PREEMPT_RT config boot, interrupt threading, lock/context 문제, firmware/kernel interface, driver functional path, basic scheduling behavior를 조기에 검증할 수 있습니다. 반면 emulator의 시간 모델과 실행 속도 때문에 worst-case latency, bandwidth, power/thermal interaction은 silicon에서 다시 측정해야 합니다. 이 한계를 명확히 구분하는 것이 중요한 engineering judgement입니다.

### Q26. AI inference platform에서 RT Linux가 필요한 이유는?

**권장 답변**  
AI accelerator의 평균 throughput만으로 차량/로봇 system deadline을 보장할 수 없습니다. camera frame arrival, sensor synchronization, command submission, DMA completion, fault recovery, actuator/control task가 일정한 deadline 내에 연결돼야 합니다. RT Linux는 CPU-side scheduling과 IRQ latency의 변동을 줄이는 수단입니다. 그러나 accelerator execution, firmware queue, memory bandwidth, thermal throttling까지 포함한 end-to-end budget을 설계해야 하며 PREEMPT_RT만 적용한다고 determinism이 자동으로 보장되지는 않습니다.

### Q27. RT 성능과 power management가 충돌할 때 어떻게 합니까?

**권장 답변**  
latency-sensitive core와 throughput core를 workload 특성에 따라 분리하고, IRQ/thread affinity, cpuset, scheduler priority를 설계합니다. deep idle state와 aggressive DVFS가 wake-up latency를 키우는지 측정해 허용 범위 내 state만 사용하거나 critical window에서 QoS constraint를 적용합니다. 항상 power를 끄는 것이 아니라 deadline budget, thermal 지속성, average power의 trade-off를 데이터로 결정합니다.

### Q28. 가장 큰 latency outlier를 발견하면 무엇부터 봅니까?

**권장 답변**  
`timerlat` 또는 ftrace에서 outlier 직전 구간을 잡아 hard IRQ-off, preemption-off, raw lock, 긴 threaded IRQ, softirq backlog, scheduler migration, page fault/memory reclaim, SMI/firmware 같은 층으로 분류합니다. 재현 workload와 CPU를 고정하고 하나씩 제거합니다. 원인이 application queueing인지 kernel wake-up인지 accelerator completion인지 timestamp domain을 맞춰 end-to-end로 분해하는 것이 중요합니다.

---

## D. Device driver / storage / low-level

### Q29. Platform driver의 일반적인 probe 순서를 설명해 주세요.

**권장 답변**  
1. DT/ACPI match와 private data allocation
2. MMIO/IRQ/DMA mask resource 획득
3. regulator, power domain, clock, reset, PHY enable
4. hardware reset 및 capability/version 확인
5. DMA buffer/descriptor와 IOMMU 준비
6. interrupt clear 후 handler 등록, device interrupt enable
7. subsystem 등록과 userspace-visible interface 생성
8. runtime PM enable
9. 모든 단계에 역순 cleanup 또는 `devm_*` 적용

중간 실패와 deferred probe에서 resource leak이나 child device 중복 등록이 없도록 설계합니다.

### Q30. MMIO access와 memory barrier가 왜 중요합니까?

**권장 답변**  
CPU, interconnect, device가 서로 다른 ordering을 가질 수 있기 때문입니다. Linux의 `readl`/`writel` 같은 accessor가 제공하는 ordering semantics를 사용하고, descriptor memory를 준비한 뒤 doorbell을 쓰는 순서에는 DMA barrier가 필요할 수 있습니다. 단순 `volatile` pointer는 compiler access만 제어할 뿐 device/CPU ordering을 충분히 보장하지 않습니다. posted write가 있는 bus에서는 필요 시 read-back으로 completion을 확인합니다.

### Q31. Coherent DMA와 streaming DMA의 차이는?

**권장 답변**  
coherent DMA memory는 CPU와 device가 지속적으로 공유하는 descriptor/ring에 적합하며 `dma_alloc_coherent()` 계열을 사용합니다. streaming mapping은 일시적인 buffer transfer에 적합하고 `dma_map_*()`/`dma_unmap_*()` 또는 sync API로 ownership과 cache coherency를 명시합니다. direction, lifetime, scatter-gather, DMA mask, IOMMU mapping을 잘못 쓰면 데이터 corruption이나 fault가 발생합니다.

### Q32. UFS bring-up을 단계별로 설명해 주세요.

**권장 답변**  
UFS host controller clock/reset/regulator/PHY를 준비하고 HCI capability와 interrupt를 초기화합니다. 이후 M-PHY/UniPro link startup, device initialization, power mode/gear/lane negotiation을 거쳐 SCSI host/device를 scan합니다. 실패 시 HCI register, UIC command result, UniPro/PHY state, completion interrupt, timeout/retry, regulator/clock sequencing을 확인합니다. DT의 PHY/clock/reset/interrupt/IOMMU dependency도 함께 봅니다.

### Q33. eMMC와 UFS를 Linux 관점에서 비교하면?

**권장 답변**  
eMMC는 MMC subsystem의 parallel command/data interface를 사용하며 host controller timing과 tuning, bus width/clock, command sequence가 핵심입니다. UFS는 UFSHCI 위에 UniPro link와 M-PHY가 있고 SCSI command model을 사용하므로 link startup, power mode, UIC command, PHY state와 error recovery가 더 복잡합니다. UFS는 full-duplex/high performance와 power state 장점이 있지만 bring-up/debug layer가 더 많습니다.

### Q34. Runtime PM을 driver에 어떻게 적용합니까?

**권장 답변**  
device가 idle인지 판단할 usage count와 autosuspend policy를 정하고, runtime suspend에서 queue quiesce -> interrupt mask -> state save -> clock/power/PHY off 순서를 안전하게 수행합니다. resume은 역순이며 dependency와 error recovery를 고려합니다. system suspend와 runtime suspend callback의 공통/차이를 분리하고, wake-up source와 in-flight DMA가 없는지 확인합니다. RT workload에서는 resume latency가 deadline에 미치는 영향도 측정합니다.

### Q35. 경험이 적은 CSI/V4L2, Ethernet, PCIe/RoCE 질문을 받으면?

**권장 답변**  
“제가 end-to-end로 가장 깊게 소유한 영역은 Linux BSP, UFS/eMMC, clock/GPIO/I2C/SPI/USB/DMA/display 쪽이며, CSI/Ethernet/PCIe/RoCE를 같은 깊이로 했다고 과장하지 않겠습니다. 다만 SoC driver bring-up의 공통 기반인 register, clock/reset/power, IRQ, DMA/IOMMU, DT, error recovery, tracing에는 깊은 경험이 있습니다. 새로운 subsystem은 core framework와 upstream reference driver를 먼저 이해하고, probe-control/data/error/power path를 분리해 실제 이슈 하나를 끝까지 해결하는 방식으로 빠르게 확장해 왔습니다.”

---

## E. Yocto, source architecture, Android GKI

### Q36. Yocto BSP layer를 어떻게 설계합니까?

**권장 답변**  
hardware description과 product policy를 분리합니다. 예를 들어 `meta-soc`에는 SoC 공통 kernel/firmware/driver metadata, `meta-board`에는 machine/DT/bootloader, `meta-oem`에는 고객 configuration, `meta-product`에는 image/package/service policy를 둡니다. `MACHINE`, `DISTRO`, `IMAGE`의 책임을 섞지 않고, 공통 recipe를 작은 `.bbappend` 난립 없이 parameterize합니다. layer dependency와 release branch compatibility를 명시하고 build manifest/SSTATE/license를 관리합니다.

### Q37. Multi-OEM / single-binary kernel은 어떻게 설계했습니까?

**권장 답변**  
공통 kernel code와 config baseline을 유지하고, board/OEM 차이는 DT, module, firmware, command line 또는 제한된 quirk table로 분리합니다. boot 시 hardware identity를 신뢰 가능한 방식으로 식별하고 맞는 DT/overlay/firmware를 선택합니다. 공통 binary의 장점은 test matrix와 maintenance 감소지만, 모든 기능을 무조건 켜면 attack surface와 memory footprint가 커질 수 있으므로 module/config 정책이 필요합니다. incompatible ABI나 early boot 차이는 single-binary 범위 밖으로 명확히 정의해야 합니다.

### Q38. Kernel version upgrade 전략은?

**권장 답변**  
먼저 vendor patch를 upstream/common/product-specific으로 분류하고 old tree의 patch inventory를 만듭니다. 새 LTS에서 upstream 포함 여부를 확인한 뒤 최소 boot config와 DT로 bring-up하고, subsystem별로 patch를 재적용합니다. compile, boot, functional, performance, suspend/resume, stress, ABI/KMI test를 단계별 gate로 운영합니다. 문제는 `git bisect`, config diff, DT diff, trace comparison으로 좁히고, 오래된 workaround는 새 kernel에서 다시 필요성을 검증합니다.

### Q39. Yocto upgrade에서 가장 어려운 점은?

**권장 답변**  
BitBake syntax 변화만이 아니라 toolchain, init system, package version, class behavior, override syntax, license, kernel recipe, image composition이 함께 바뀝니다. layer compatibility를 먼저 맞추고, custom patch 수를 줄이며, reproducible baseline image를 만든 뒤 package/image/BSP를 단계적으로 올립니다. 고객 branch를 동시에 유지할 경우 변경을 backport할지 forward-port할지 정책이 중요합니다.

### Q40. GKI의 목적과 KMI를 설명해 주세요.

**권장 답변**  
GKI는 Android core kernel을 공통화하고 SoC/board support를 loadable vendor module로 분리해 kernel fragmentation을 줄이는 구조입니다. KMI는 GKI kernel과 vendor module 사이의 binary interface로, 안정성이 유지되면 core kernel과 vendor image를 더 독립적으로 업데이트할 수 있습니다. 개발 시에는 exported symbol/ABI list, module dependency, signing, vendor hook, test matrix를 관리해야 합니다. 일반적인 upstream ABI 안정성과 Android KMI 정책을 구분해 설명하겠습니다.

### Q41. GKI와 mainline upstream은 어떤 관계입니까?

**권장 답변**  
GKI는 Android 제품 update와 vendor module compatibility를 위한 delivery architecture이고, upstream은 Linux community의 source-level integration과 maintenance model입니다. 가능한 generic feature와 fix는 upstream하고, Android-specific integration은 GKI/KMI 규칙에 맞춥니다. vendor hook이나 out-of-tree module을 남발하면 장기 비용이 증가하므로 upstream 가능성, product schedule, KMI constraint를 함께 판단합니다.

### Q42. Reproducible build를 어떻게 보장합니까?

**권장 답변**  
source revision과 layer manifest, toolchain/container, configuration, artifact hash, license manifest를 고정합니다. network fetch와 floating branch를 제한하고 mirror/cache를 관리합니다. CI에서 clean build와 incremental build를 비교하고, image/kernel/module/DTB의 provenance를 남깁니다. 동일 source에서 다른 binary가 나오는 timestamp/path/host contamination을 찾아 제거합니다.

---

## F. Debugging, performance, upstream

### Q43. perf와 ftrace를 언제 각각 사용합니까?

**권장 답변**  
`perf`는 PMU sampling과 statistical profiling으로 CPU hotspot, cache miss, branch, call graph를 넓게 찾는 데 적합합니다. ftrace는 kernel event/function/latency를 timestamp 순으로 분석해 IRQ, scheduler, wake-up, function path 같은 인과관계를 보는 데 적합합니다. 먼저 perf로 hotspot을 찾고 ftrace로 특정 path의 ordering/latency를 깊게 보는 식으로 함께 사용합니다. RT 문제에는 timerlat/osnoise와 sched/irq trace가 더 직접적입니다.

### Q44. Boot time을 어떻게 최적화합니까?

**권장 답변**  
목표 boot milestone을 정의하고 bootloader, kernel, userspace를 분리해 측정합니다. kernel에서는 `initcall_debug`, boot-time ftrace, driver probe dependency를 이용해 critical path를 찾습니다. 불필요한 built-in driver 제거, parallel/deferred init, firmware load, storage mount, entropy, module loading을 검토합니다. 단순히 initcall을 늦추는 것이 아니라 실제 서비스 readiness와 failure recovery를 함께 검증합니다. Tegra instant boot에서는 snapshot size와 driver init path를 줄인 경험을 연결할 수 있습니다.

### Q45. Upstream patch를 만드는 과정을 설명해 주세요.

**권장 답변**  
문제를 재현하고 generic fix인지 board-specific enablement인지 scope를 정합니다. patch를 review 가능한 단위로 나누고 binding/driver/DT 순서와 dependency를 고려합니다. `checkpatch`, build matrix, `dtbs_check`, runtime test를 수행하고 `MAINTAINERS`/`get_maintainer.pl`로 수신자를 정합니다. cover letter에 문제, design choice, validation을 적고 review feedback에 기술적 근거로 응답하며 v2/v3 change log를 관리합니다. 제품 branch에는 upstream commit을 추적 가능하게 backport합니다.

### Q46. Upstream이 제품 일정과 충돌하면?

**권장 답변**  
제품 branch에서 최소 안전 fix를 먼저 적용할 수 있지만, upstream path와 divergence 기간을 명확히 관리합니다. generic fix와 product workaround를 분리하고, upstream review에서 architecture가 바뀌면 제품 patch를 재정렬합니다. schedule을 이유로 permanent fork를 만들지 않도록 owner와 deadline을 정하고, CI에서 upstream/backport commit mapping을 추적합니다.

### Q47. Regression을 어떻게 찾습니까?

**권장 답변**  
먼저 재현 조건과 known-good/bad를 고정하고 config, DT, firmware, userspace 차이를 제거합니다. issue가 commit range와 재현성이 있으면 `git bisect`를 사용하고, boot 불가 시 자동화된 pass/fail script나 serial pattern으로 bisect합니다. performance regression은 동일 workload/thermal state에서 여러 번 측정하고 distribution을 비교합니다. 원인 commit을 찾은 뒤 revert가 안전한지, forward fix가 필요한지 판단합니다.

### Q48. 코드 품질을 어떻게 확보합니까?

**권장 답변**  
public interface와 lifetime/ownership을 먼저 정의하고, error path와 teardown을 정상 path와 같은 수준으로 review합니다. compile warning, sparse/smatch/clang, lockdep/KASAN/KCSAN 등 상황에 맞는 도구와 unit/integration/boot stress를 사용합니다. patch를 작게 나누고 commit message에 why와 validation을 남깁니다. 리뷰에서는 style보다 concurrency, power state, failure recovery, ABI compatibility를 우선 봅니다.

---

## G. ARM64, RISC-V, boot firmware, HPC

### Q49. ARM64 Linux boot에서 중요한 contract는?

**권장 답변**  
firmware가 kernel image와 DTB를 올바른 physical address에 배치하고, primary CPU의 x0에 DTB address를 전달합니다. kernel entry 시 MMU는 off여야 하며 interrupt/EL/cache 상태가 architecture boot protocol과 맞아야 합니다. PSCI, GIC, architected timer, reserved memory, DMA device quiesce도 중요합니다. 이후 kernel은 head code에서 page table과 MMU를 세우고 `start_kernel()`로 진행합니다.

### Q50. RISC-V boot chain을 설명해 주세요.

**권장 답변**  
일반적인 Unix-class RISC-V에서는 M-mode firmware가 platform initialization과 privileged service를 담당하고, SBI를 통해 S-mode U-Boot 또는 Linux에 timer, IPI, hart management 같은 service를 제공합니다. 예를 들어 U-Boot SPL -> OpenSBI/fw_dynamic -> S-mode U-Boot -> Linux 구조가 가능합니다. Linux entry에는 hart ID와 DTB address가 전달됩니다. 실제 platform에서는 reset vector, DRAM init, PMP, interrupt controller, timer, hart startup ownership을 명확히 해야 합니다.

### Q51. SBI는 무엇입니까?

**권장 답변**  
SBI는 supervisor OS와 supervisor execution environment 사이의 interface입니다. S-mode Linux가 직접 수행할 수 없는 machine-level operation을 `ecall`로 요청합니다. base, timer, IPI, remote fence, hart state management, system reset 등의 extension이 있으며, OpenSBI가 대표 구현입니다. ARM의 PSCI와 일부 목적이 비슷하지만 architecture와 service boundary는 다릅니다.

### Q52. IHK/McKernel 같은 multi-kernel을 왜 사용합니까?

**권장 답변**  
Linux는 device와 management 기능을 담당하고, lightweight kernel은 계산용 core/memory를 격리해 OS noise와 jitter를 줄이는 것이 목적입니다. HPC workload에 predictable execution과 scalability를 제공하지만, resource partitioning, syscall/service delegation, device access, debugging/operations 복잡도가 증가합니다. 따라서 workload benefit이 관리 비용보다 큰지 측정해야 합니다.

### Q53. Oreboot와 LinuxBoot의 차이와 검토 이유는?

**권장 답변**  
Oreboot는 coreboot 계열 firmware를 Rust 중심으로 다시 구현해 memory safety와 작은 trusted code base를 지향합니다. LinuxBoot는 일부 firmware 단계에서 Linux kernel과 initramfs/u-root를 활용해 hardware initialization과 boot policy를 user-space 도구로 다루는 접근입니다. 둘 다 firmware flexibility와 auditability 관점에서 검토 가치가 있지만, hardware initialization coverage, boot time, security chain, recovery, vendor support를 평가해야 합니다. 제 프로젝트에서는 production 확정이 아니라 architecture study와 pre-development 범위였습니다.

---

## H. 행동/협업 질문

### Q54. Hardware team과 spec 해석이 다를 때 어떻게 합니까?

**권장 답변**  
주장을 반복하기보다 재현 가능한 최소 sequence와 expected/actual register trace를 만듭니다. spec 문장, RTL/model behavior, software access를 한 표에 놓고 ownership을 정합니다. workaround가 필요해도 software-only인지 RTL fix인지, silicon revision에 어떤 영향이 있는지 기록합니다. interface spec과 validation test를 함께 수정해 같은 문제가 반복되지 않게 합니다.

### Q55. 긴급한 bring-up blocker를 어떻게 관리합니까?

**권장 답변**  
최종 증상 대신 dependency tree를 기준으로 critical path를 정하고, issue마다 owner, evidence, next experiment, decision time을 명시합니다. 동시에 한 사람이 여러 가설을 무작정 시도하지 않도록 software/model/RTL test를 병렬화합니다. 임시 workaround는 명시적인 expiry 조건과 제거 owner를 둡니다. 매일 boot milestone과 blocker를 짧게 공유합니다.

### Q56. 기술적으로 동의하지 않는 리뷰를 받으면?

**권장 답변**  
먼저 reviewer가 보호하려는 invariant와 장기 maintenance concern을 이해합니다. 제 설계의 constraint와 data를 제시하고, 대안별 complexity, compatibility, performance를 비교합니다. public upstream에서는 maintainer의 subsystem convention을 존중하되, correctness 문제가 있다면 작은 reproducer나 test로 논의합니다. 의견을 이기는 것이 아니라 더 유지 가능한 solution을 찾는 것이 목표입니다.

### Q57. Senior engineer로서 후배를 어떻게 성장시킵니까?

**권장 답변**  
답을 바로 주기보다 boot/data path를 함께 그리고, 로그에서 다음 가설을 만드는 방법을 보여줍니다. 첫 patch는 scope와 validation plan을 같이 정하고 review에서 why/error path/concurrency를 설명합니다. subsystem ownership을 작게라도 끝까지 맡기고, 장애 회고에서 개인 책임보다 missing guardrail을 찾습니다.

---

# 6. 기술 학습 노트

## 6.1 ARM64 Linux boot chain

```text
Boot ROM
  -> BL1/BL2 (platform initialization, image authentication)
  -> BL31 / TF-A (EL3 runtime, PSCI)
  -> Optional BL32 / OP-TEE
  -> BL33 / U-Boot or UEFI
  -> Linux Image + DTB + optional initramfs
  -> arch/arm64/kernel/head.S
  -> start_kernel()
  -> rest_init() -> kernel_init() -> /sbin/init
```

### Kernel entry에서 확인할 것

- x0: DTB physical address, x1-x3: reserved/zero
- non-secure EL2 또는 EL1
- MMU off, stale I-cache 없음
- DMA-capable devices quiesced
- interrupt controller/timer/PSCI description 일치
- DTB가 reserved memory와 kernel image를 덮지 않음

### 첫 부팅 우선순위

1. early UART
2. memory/MMU
3. architected timer
4. GIC 및 interrupt
5. SMP/PSCI
6. clock/reset/power framework
7. storage/rootfs
8. DMA/IOMMU
9. 기능 driver

### 유용한 옵션

```text
earlycon
ignore_loglevel
initcall_debug
log_buf_len=4M
init=/bin/sh
clk_ignore_unused        # 임시 진단용, 최종 해결책 아님
pd_ignore_unused         # 임시 진단용, 최종 해결책 아님
```

## 6.2 Device Tree와 driver model

DT의 세 주요 역할은 platform identification, runtime configuration, device population입니다. single-binary kernel에서는 hardware 차이를 data로 분리하는 핵심 수단이지만, firmware ABI처럼 관리해야 합니다.

### Probe dependency 예시

```text
Device node
  -> power-domain provider
  -> regulator
  -> clock/reset
  -> PHY
  -> IOMMU
  -> IRQ controller
  -> consumer driver probe
```

`-EPROBE_DEFER`가 반복될 때는 consumer log만 보지 말고 supplier가 왜 등록되지 않았는지 확인합니다.

### DT review checklist

- `compatible`이 generic -> specific 순서와 binding에 맞는가?
- `reg`, `interrupts`, `clocks`, `resets`, `power-domains`, `iommus`가 spec과 일치하는가?
- `status = "okay"`와 pinctrl/regulator dependency가 맞는가?
- address/size cells와 endian/access width가 맞는가?
- reserved-memory와 DMA pool이 겹치지 않는가?
- YAML binding, `dt_binding_check`, `dtbs_check`를 통과하는가?

## 6.3 PREEMPT_RT 핵심 mental model

```text
Non-RT
Device IRQ -> hard IRQ handler (longer work possible) -> wake task

PREEMPT_RT (typical)
Device IRQ -> minimal hardirq -> wake IRQ thread -> schedulable handler work
                                      |
                                      +-> priority / affinity / PI-aware locks
```

### 반드시 기억할 차이

- 대부분의 IRQ가 forced-threaded됨
- `spinlock_t`는 RT에서 sleeping/PI semantics
- `raw_spinlock_t`는 실제 hard spin이 필요한 최소 구간
- `local_irq_disable()`/preempt-off/raw lock 구간이 latency를 결정
- per-CPU data 보호를 단순 preempt disable에만 의존하면 위험
- softirq/timer/workqueue context assumption을 재검토

### RT 측정 순서

```bash
# 기본 wake-up latency
cyclictest -p95 -m -n -i 1000 -D 10m

# IRQ latency와 thread latency 분리
rtla timerlat top -d 5m
rtla timerlat hist -d 5m

# CPU interference 분석
rtla osnoise top -d 5m

# trace correlation
trace-cmd record -e irq -e sched -e power -e workqueue <workload>
```

명령 옵션은 kernel/tool version에 따라 확인하십시오. 면접에서는 명령 암기보다 **무엇을 분리해서 측정하는지**가 중요합니다.

## 6.4 Pre-silicon 환경 비교

| 환경 | 강점 | 적합한 검증 | 주의점 |
|---|---|---|---|
| ARM FVP | ARM architecture/reference system의 빠른 functional model | boot protocol, EL/PSCI/GIC, reference software | custom IP/SoC detail 제한 |
| QEMU | 빠른 full-system emulation, 수정/자동화 용이 | kernel/bootloader/DT, CI, custom device prototype | cycle/timing 정확도 제한 |
| QBox/SystemC VP | custom SoC와 TLM component 연동 | HW/SW interface, custom IP, mixed model | model completeness/behavior contract 관리 필요 |
| Synopsys ZeBu | RTL-oriented hardware emulation | pre-silicon firmware/kernel, register/interrupt sequence | 느린 실행, absolute performance/RT latency 해석 제한 |
| Silicon | 실제 timing/power/PHY/errata | final performance, latency, power, signal integrity | 늦은 문제 발견 비용 큼 |

### Virtual platform에서 먼저 만들 observability

- early UART와 semihosting/debug console
- boot milestone register 또는 trace event
- register access trace
- interrupt injection/count
- DMA memory dump와 fault report
- firmware/kernel version handshake
- reset/reboot automation

## 6.5 Yocto BSP architecture

```text
meta-openembedded / oe-core
          |
       meta-soc        # SoC kernel, firmware, common drivers
          |
       meta-board      # MACHINE, DT, bootloader, board config
          |
       meta-oem        # OEM/customer policy and variants
          |
       meta-product    # image, packages, services, update policy
```

### 설계 원칙

- hardware mechanism과 product policy 분리
- floating branch 금지, manifest로 revision 고정
- one-off `.bbappend`를 늘리기보다 configurable recipe 설계
- kernel/DT/firmware artifact version을 묶어서 추적
- release branch compatibility와 migration plan 명시
- clean build, reproducibility, license/SBOM 고려

## 6.6 Multi-OEM / single-binary architecture

```text
                    Common Kernel Image
                           |
          +----------------+----------------+
          |                |                |
       DT/DTBO          Modules          Firmware
       OEM-A/B/C       feature/OEM       versioned
          |                |                |
          +-------- Runtime identity --------+
```

**장점:** common fixes, test reuse, reduced branch divergence  
**위험:** config bloat, attack surface, incompatible early boot, hidden quirks  
**통제:** supported matrix, stable interface, module policy, DT validation, negative test

## 6.7 Android GKI와 KMI

GKI는 core kernel을 공통화하고 SoC/board support를 vendor module로 이동시키며 안정된 KMI를 제공하는 Android kernel delivery model입니다.

```text
GKI boot image
  - common kernel
  - generic initramfs
        |
Stable KMI / symbol allowlist
        |
Vendor modules + vendor_boot / vendor_dlkm
  - SoC and board-specific support
```

### 질문 대비 포인트

- source API가 아니라 **binary KMI**라는 점
- vendor module의 symbol, dependency, signing, load order
- KMI break detection과 ABI monitoring
- upstream generic fix와 Android-specific vendor integration의 경계

## 6.8 ARM64와 RISC-V bring-up 비교

| 항목 | ARM64 | RISC-V |
|---|---|---|
| Privilege | EL3/EL2/EL1/EL0 | M/S/U, optional H extension |
| Firmware service | PSCI, SMCCC, TF-A | SBI, OpenSBI |
| Kernel DT register | x0 = DTB | a0 = hartid, a1 = DTB in common boot flows |
| Interrupt | GICv2/v3/v4 | PLIC 또는 AIA 계열 |
| Timer | ARM architected timer | time CSR/SBI timer/platform timer |
| SMP start | PSCI CPU_ON/spin-table | SBI HSM/platform hart start |
| 공통 문제 | memory map, cache/coherency, DT, DMA/IOMMU, clock/reset, firmware contract |

## 6.9 UFS data/control path

```text
Block I/O / SCSI command
        -> UFS core
        -> UFS Host Controller Interface (UFSHCI)
        -> UIC command / UniPro link
        -> M-PHY
        -> UFS device
```

### Debug checkpoints

- regulator/clock/reset/PHY sequence
- HCI capability/version
- UIC command completion
- link startup state
- gear/lane/power mode negotiation
- transfer request descriptor and doorbell
- completion IRQ, timeout, error recovery
- IOMMU/DMA mapping and cache coherency

## 6.10 perf, ftrace, rtla 선택 기준

| 도구 | 가장 잘 답하는 질문 |
|---|---|
| `perf stat` | 전체 event count와 workload 비교 |
| `perf record/report` | CPU time이 어디에 쓰이는가? |
| ftrace function/event | kernel path에서 어떤 순서로 무엇이 일어났는가? |
| function_graph | 함수 latency와 nested call은? |
| sched/irq tracepoint | wake-up, scheduling, interrupt delay는? |
| `rtla timerlat` | timer IRQ와 RT thread wake-up latency 원인은? |
| `rtla osnoise` | 해당 CPU를 방해한 IRQ/softirq/thread는? |

## 6.11 Upstream contribution을 면접에서 설명하는 방법

한 patch를 다음 형식으로 90초에 설명합니다.

1. **Problem:** 어떤 platform gap/bug였나?
2. **Why upstream:** vendor-only patch로 남기면 어떤 비용이 있나?
3. **Design:** DT binding/driver/core 중 어디를 바꿨나?
4. **Review:** maintainer가 우려한 점과 수정 내용
5. **Validation:** build/DT/runtime/board matrix
6. **Impact:** 제품 branch와 향후 kernel upgrade에 어떤 이점이 있었나?

### 준비할 대표 patch 3개

- ExynosAuto v9 board/device-tree enablement
- clock/watchdog 또는 UFS 관련 change
- U-Boot RISC-V/driver-model contribution

각 patch에 대해 commit hash, 핵심 diff 10줄, review 질문, test platform을 메모해 둡니다.

## 6.12 HPC multi-kernel 핵심

```text
Compute Node Resources
  +---------------- Linux ----------------+
  | device management / control / service |
  +----------------------------------------+
  +------------- McKernel/LWK -------------+
  | isolated cores/memory, low OS noise    |
  +----------------------------------------+
```

**면접 포인트:** “분석 및 실험”을 “production ownership”으로 확대해 말하지 않습니다. 평가 기준과 trade-off를 설명하는 것이 더 신뢰를 줍니다.

---

# 7. 부족한 영역 질문에 대한 정직한 대응

## 7.1 JTAG

> “JTAG을 제 가장 강한 전문 영역이라고 과장하지 않겠습니다. 제 주된 bring-up 도구는 serial/boot log, low-level register analysis, emulator/virtual platform, ftrace/perf입니다. JTAG이 필요한 상황에서는 early boot breakpoint, PC/register/memory 확인, exception state와 boot milestone correlation에 사용합니다. 실제 사용 범위는 `[본인 경험으로 구체화]`입니다.”

## 7.2 V4L2/CSI

> “Display/MIPI-DSI와 camera SoC 경험은 있지만, V4L2 capture pipeline 전체를 최근에 end-to-end 소유했다고 말하지는 않겠습니다. 다만 media controller graph, buffer queue, DMA/IOMMU, timestamp/synchronization, interrupt/error recovery가 핵심이라는 것을 이해하고 있으며, upstream framework와 reference driver를 기반으로 빠르게 확장할 수 있습니다.”

## 7.3 Ethernet/PCIe/RoCE

> “PCIe flash-cache prototype과 high-speed I/O integration 경험은 있으나, 최신 PCIe/RoCE stack을 제 대표 전문 분야라고 하지는 않겠습니다. 대신 device enumeration, MMIO, IRQ/MSI, DMA/IOMMU, coherency, error recovery, performance tracing의 공통 기반은 갖고 있습니다. 역할에서 필요하다면 subsystem core와 real hardware issue를 기준으로 학습 우선순위를 잡겠습니다.”

**원칙:** 모르는 세부 API를 추측하지 말고, 알고 있는 architecture와 debugging method를 보여준 뒤 학습 계획을 설명합니다.

---

# 8. 면접관에게 할 질문

시간이 5분 남았을 때 2-3개만 선택합니다.

1. “이 역할에서 첫 6개월 동안 가장 먼저 해결해야 할 kernel 또는 bring-up 문제는 무엇입니까?”
2. “현재 pre-silicon environment와 first-silicon validation 사이에서 software team이 가장 크게 느끼는 gap은 무엇입니까?”
3. “Linux kernel team과 silicon, firmware, AI runtime 팀 사이의 interface ownership은 어떻게 나뉩니까?”
4. “Realtime 요구사항은 component-level latency와 end-to-end product deadline 중 어떤 방식으로 정의하고 검증합니까?”
5. “Upstream contribution과 product schedule 사이의 균형을 팀에서는 어떻게 운영합니까?”
6. “이 포지션의 뛰어난 engineer를 1년 뒤 평가할 때 가장 중요한 결과는 무엇입니까?”

급여/복지/재택 질문은 기술면접 첫 질문으로 사용하지 않습니다.

---

# 9. 모의면접 계획

## D-3 ~ D-2

- Portfolio를 12분에 2회 녹화
- Page 4, 6을 각각 5분 deep dive로 별도 연습
- top 20 질문을 소리 내어 답변
- 대표 debugging 사례 3개를 C-D-I-V-R-L로 문서화
- upstream patch 3개를 실제 diff로 다시 확인

## D-1

- 45분 mock interview 1회: 발표 12분 + 질문 30분
- 답변이 3분을 넘는 항목 표시 후 90초로 축약
- `[실제 수치/사례로 교체]` 전부 채우기
- resume와 portfolio 용어 일치 확인
- 공개 가능한 수준인지 confidentiality review

## 당일 30분 전

- Portfolio/PDF local copy, contribution browser tab, 노트 준비
- camera/mic/screen-share 확인
- 소개 30초/90초 각각 1회
- `PREEMPT_RT`, `pre-silicon`, `principal`, `architecture` 발음 확인
- 물과 메모지 준비
- 마지막 공부보다 첫 문장과 대표 사례의 결론을 안정화

---

# 10. 당일 발표/답변 체크리스트

## 발표

- [ ] 시작할 때 “12분 발표” 허락을 구했다.
- [ ] bullet을 읽지 않고 diagram을 가리키며 설명했다.
- [ ] Page 6에 가장 많은 시간을 사용했다.
- [ ] 매 프로젝트마다 “문제-내 역할-결정-검증-교훈”이 있었다.
- [ ] 내부 정보 대신 architecture principle과 debugging method를 말했다.
- [ ] “분석/선행개발”과 “제품화/lead” 범위를 구분했다.

## 답변

- [ ] 첫 문장에 결론을 말했다.
- [ ] 90초 안에 핵심 답변을 끝내고 deep dive 여부를 확인했다.
- [ ] 내가 직접 한 일과 팀의 일을 구분했다.
- [ ] 수치가 없으면 만들지 않고 validation method를 설명했다.
- [ ] 모르는 부분은 인정하고 transferable skill과 학습 방법을 말했다.
- [ ] 질문이 모호하면 한 번 scope를 확인했다.

## 마무리 20초

> “오늘 설명드린 것처럼, 저는 Linux kernel/BSP의 깊이와 pre-silicon부터 production까지의 bring-up 경험, 그리고 upstream과 multi-platform architecture 경험을 함께 가지고 있습니다. 특히 RT Linux와 custom SoC HW/SW interface를 안정적인 platform으로 만드는 데 바로 기여할 수 있다고 생각합니다. 감사합니다.”

---

# 11. Rapid-fire 확인 문제

아래 질문은 답을 20-30초로 말할 수 있어야 합니다.

1. `-EPROBE_DEFER`는 언제 반환하는가?
2. `devm_*`가 모든 cleanup 문제를 해결하지 못하는 이유는?
3. `writel()` 뒤 read-back이 필요한 경우는?
4. DMA address와 physical address가 항상 같은가?
5. `IRQF_ONESHOT`과 threaded IRQ의 관계는?
6. RT에서 `spin_lock_irqsave()` assumption이 어떻게 달라질 수 있는가?
7. raw spinlock critical section을 어떻게 줄이는가?
8. ftrace event와 function tracer의 차이는?
9. `perf stat`과 `perf record`의 차이는?
10. ARM64 kernel entry의 x0는 무엇인가?
11. PSCI와 SBI의 공통점과 차이는?
12. DT overlay의 장단점은?
13. single-binary kernel에서 board identity를 어떻게 신뢰할 것인가?
14. GKI의 KMI break는 어떻게 감지하는가?
15. Yocto의 `MACHINE`, `DISTRO`, `IMAGE` 책임은?
16. UFS의 M-PHY와 UniPro 역할은?
17. rootfs mount failure와 storage driver failure를 어떻게 분리하는가?
18. model timeout을 단순히 늘리면 안 되는 이유는?
19. kernel upgrade 때 vendor patch inventory를 왜 먼저 만드는가?
20. upstream patch를 review 가능한 단위로 나누는 기준은?

---

# 12. 공식 학습 자료

기술 복습은 블로그보다 아래 primary documentation을 우선합니다.

- Linux PREEMPT_RT differences: <https://docs.kernel.org/core-api/real-time/differences.html>
- Linux timerlat tracer: <https://docs.kernel.org/trace/timerlat-tracer.html>
- Linux ftrace: <https://docs.kernel.org/trace/ftrace.html>
- ARM64 Linux boot protocol: <https://docs.kernel.org/arch/arm64/booting.html>
- Linux Device Tree usage model: <https://docs.kernel.org/devicetree/usage-model.html>
- Linux driver model: <https://docs.kernel.org/driver-api/driver-model/driver.html>
- Linux UFS documentation: <https://docs.kernel.org/scsi/ufs.html>
- Yocto BSP Developer’s Guide: <https://docs.yoctoproject.org/bsp-guide/bsp.html>
- Android Generic Kernel Image: <https://source.android.com/docs/core/architecture/kernel/generic-kernel-image>
- RISC-V SBI specification repository: <https://github.com/riscv-non-isa/riscv-sbi-doc>
- U-Boot RISC-V boot documentation: <https://docs.u-boot.org/en/latest/arch/riscv.html>
- QEMU system emulation documentation: <https://qemu.readthedocs.io/en/latest/about/emulation.html>
- RIKEN IHK/McKernel: <https://github.com/RIKEN-SysSoft/mckernel>

---

# Appendix A. 실제 사례를 채울 표

면접 전 아래 표를 반드시 본인의 사실로 완성하십시오.

| 주제 | 상황 | 본인 결정/구현 | 검증 | 결과/교훈 |
|---|---|---|---|---|
| ZeBu PREEMPT_RT bring-up blocker | `[작성]` | `[작성]` | `[작성]` | `[작성]` |
| ExynosAuto upstream patch | `[작성]` | `[작성]` | `[작성]` | `[작성]` |
| Kernel 4.14 -> 5.x regression | `[작성]` | `[작성]` | `[작성]` | `[작성]` |
| Multi-OEM single-binary conflict | `[작성]` | `[작성]` | `[작성]` | `[작성]` |
| Hyundai virtual platform mismatch | `[작성]` | `[작성]` | `[작성]` | `[작성]` |
| perf/ftrace performance issue | `[작성]` | `[작성]` | `[작성]` | `[작성]` |
| Cross-team disagreement | `[작성]` | `[작성]` | `[작성]` | `[작성]` |

# Appendix B. 영어 기술 표현

- “I led the bring-up”보다 구체적으로: **“I owned the critical boot path and coordinated the kernel, firmware, and emulator teams.”**
- “I developed the architecture”: **“I defined the component boundaries, boot dependencies, and versioned interfaces, and validated them on the virtual platform.”**
- 한계 설명: **“The emulator was suitable for functional validation, but not for representative worst-case latency measurements.”**
- 모르는 영역: **“I have not owned that subsystem end to end, so I would not overstate my experience. The closest transferable experience is...”**
- 답변 확장 확인: **“Would you like me to go deeper into the driver implementation or the validation strategy?”**
- 역할 구분: **“I made the architecture decision and implemented the critical path; the subsystem team completed the remaining drivers and test coverage.”**
