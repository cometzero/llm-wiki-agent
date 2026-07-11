# 3강. Linux IOMMU Framework

> **목표:** 1강의 IOMMU 개념과 2강의 DMA API 사용법을 Linux Kernel 내부 구조로 연결한다.  
> 이번 강의의 핵심 질문은 다음과 같습니다.
>
> **`dma_map_single()` 호출 뒤 커널 내부에서는 어떤 객체들이 어떤 순서로 움직이는가?**

---

## 0. 3강의 위치

전체 10강 중 3강은 **Linux IOMMU Framework**를 다룹니다.

```text
1강: IOMMU Overview
2강: Linux DMA API와 IOMMU 기본 흐름
3강: Linux IOMMU Framework          ← 이번 강의
4강: ARM SMMU Architecture Overview
5강: ARM SMMUv2 / MMU-500 Hardware
6강: ARM SMMUv3 / MMU-600 / MMU-700 Hardware
7강: ARM SMMU Linux Device Driver
8강: Device Tree / ACPI / Stream ID Integration
9강: Camera → NPU Buffer/Memory Pipeline
10강: 종합 Case Study & Debugging
```

2강에서 우리는 일반 driver가 다음과 같이 DMA API를 사용하는 것을 봤습니다.

```c
dma_addr_t dma_addr;

dma_addr = dma_map_single(dev, cpu_buf, size, DMA_TO_DEVICE);
if (dma_mapping_error(dev, dma_addr))
    return -ENOMEM;

writel(lower_32_bits(dma_addr), regs + DMA_ADDR_LO);
writel(upper_32_bits(dma_addr), regs + DMA_ADDR_HI);
```

3강에서는 이 API 뒤에서 Linux Kernel이 어떤 객체를 만들고, 어떤 계층을 거쳐 실제 IOMMU hardware에 mapping을 반영하는지 살펴봅니다.

---

## 1. 큰 그림: Linux IOMMU 계층

Linux IOMMU 경로는 크게 아래와 같습니다.

```text
Device Driver
    │
    │ dma_map_single(), dma_map_sg(), dma_alloc_coherent()
    ▼
DMA Mapping API
    │
    ▼
DMA-IOMMU Layer
    │
    │ IOVA allocation
    │ default DMA domain 사용
    │ scatter-gather mapping
    ▼
IOMMU Core
    │
    │ iommu_domain
    │ iommu_group
    │ iommu_ops
    │ attach / map / unmap / IOTLB sync
    ▼
Vendor IOMMU Driver
    │
    ├── ARM SMMU v2 driver
    ├── ARM SMMU v3 driver
    ├── Intel VT-d driver
    └── AMD-Vi driver
    ▼
IOMMU Hardware
    ▼
DRAM
```

핵심은 다음입니다.

- 일반 장치 드라이버는 보통 **IOMMU API를 직접 호출하지 않습니다.**
- 일반 장치 드라이버는 **DMA API**를 호출합니다.
- DMA API 내부에서 IOMMU가 필요한 경우, **DMA-IOMMU layer**와 **IOMMU Core**를 통해 mapping을 생성합니다.
- ARM SMMU, Intel VT-d, AMD-Vi 같은 실제 하드웨어 차이는 **vendor IOMMU driver**가 처리합니다.

---

## 2. 왜 IOMMU Framework가 필요한가?

IOMMU 하드웨어는 플랫폼마다 다릅니다.

| 플랫폼 | IOMMU 구현 |
|---|---|
| ARM SoC | ARM SMMU v2/v3 |
| Intel x86 | VT-d / DMAR |
| AMD x86 | AMD-Vi |
| POWER / 기타 | PAMU 등 |

하지만 장치 드라이버가 원하는 것은 보통 단순합니다.

```text
“이 buffer를 이 장치가 DMA 할 수 있게 해주세요.”
```

Linux IOMMU Framework는 이 요청을 다음과 같은 공통 동작으로 추상화합니다.

```text
domain 생성
장치를 domain에 attach
IOVA → PA mapping 생성
DMA 완료 후 unmap
IOTLB invalidate/sync
fault 처리
```

즉, Framework의 목적은 다음입니다.

> **vendor별 IOMMU 차이를 숨기고, 장치 DMA 주소 공간을 공통 방식으로 관리하는 것**

---

## 3. 주소 공간 복습

IOMMU를 이해하려면 주소 공간을 정확히 구분해야 합니다.

### CPU 관점

```text
CPU Virtual Address
        │
        ▼
CPU MMU
        │
        ▼
Physical Address
```

예를 들어 `kmalloc()`이 반환한 pointer는 CPU가 접근하는 virtual address입니다.

```c
void *buf = kmalloc(size, GFP_KERNEL);
```

CPU는 `buf`를 직접 읽고 쓸 수 있습니다.

### Device 관점

장치는 CPU virtual address를 모릅니다. 장치는 DMA address를 사용합니다.

```text
Device DMA Address / IOVA
        │
        ▼
IOMMU
        │
        ▼
Physical Address
```

따라서 DMA API가 반환하는 `dma_addr_t`는 CPU pointer가 아닙니다.

```text
dma_addr_t = device가 사용하는 DMA address
```

IOMMU가 켜져 있다면 이 DMA address는 실제 PA가 아니라 **IOVA**일 가능성이 높습니다.

---

## 4. DMA API와 IOMMU API의 역할 분리

| 구분 | 주 사용자 | 역할 | 대표 API |
|---|---|---|---|
| DMA Mapping API | 일반 장치 드라이버 | buffer를 DMA 가능하게 만들고 DMA address 반환 | `dma_map_single()`, `dma_map_sg()`, `dma_alloc_coherent()` |
| IOMMU Core API | IOMMU driver, VFIO, 특수 subsystem | domain 생성, attach, map, unmap, fault 처리 | `iommu_attach_device()`, `iommu_map()`, `iommu_unmap()` |
| Vendor IOMMU ops | ARM SMMU, Intel VT-d 등 | 하드웨어별 page table/register/queue 제어 | `struct iommu_ops`, `struct iommu_domain_ops` |

일반 rule은 다음입니다.

> **일반 장치 드라이버는 직접 `iommu_map()`을 호출하기보다 DMA API를 먼저 사용해야 합니다.**

예외는 있습니다.

- VFIO
- IOMMUFD
- GPU/NPU의 특수 memory manager
- SVA/PASID 기반 shared address space
- Hypervisor 또는 userspace driver stack

---

## 5. 핵심 객체 한 장 요약

Linux IOMMU Framework의 핵심 객체는 다음입니다.

| 객체 | 쉬운 의미 |
|---|---|
| `struct device` | DMA를 수행하는 장치 또는 I/O device |
| `struct iommu_device` | IOMMU 하드웨어 인스턴스 |
| `struct iommu_ops` | vendor IOMMU driver callback 묶음 |
| `struct iommu_domain` | 장치용 I/O 주소 공간 |
| `struct iommu_group` | 하드웨어적으로 격리 가능한 최소 장치 묶음 |
| `struct iommu_fwspec` | firmware에서 온 IOMMU 연결 정보 |

이 객체들이 연결되면 커널은 다음 질문에 답할 수 있습니다.

```text
이 device는 어떤 IOMMU에 연결되어 있는가?
이 device는 어떤 group에 속하는가?
이 device는 어떤 I/O 주소 공간을 사용하는가?
이 I/O 주소 공간의 map/unmap은 어떤 vendor driver가 처리하는가?
```

---

## 6. `struct device`: 모든 흐름의 시작점

DMA API의 첫 번째 인자는 대부분 `struct device *dev`입니다.

```c
dma_addr_t dma_map_single(struct device *dev,
                          void *cpu_addr,
                          size_t size,
                          enum dma_data_direction direction);
```

이 `dev`가 중요합니다.

`struct device`를 통해 커널은 다음 정보를 판단합니다.

```text
DMA mask
coherent DMA mask
dma_ops
IOMMU 연결 정보
IOMMU group
firmware node
```

잘못된 `dev`를 넘기면 어떻게 될까요?

- 엉뚱한 DMA mask를 적용할 수 있습니다.
- 엉뚱한 IOMMU domain에 mapping될 수 있습니다.
- device register에는 맞지 않는 DMA address가 들어갈 수 있습니다.
- 결과적으로 IOMMU fault 또는 data corruption이 발생할 수 있습니다.

---

## 7. `struct iommu_device`: IOMMU 하드웨어 인스턴스

`iommu_device`는 IOMMU 하드웨어 자체를 커널에서 표현하는 객체입니다.

ARM SoC를 예로 들면 다음과 같습니다.

```text
ARM SMMU hardware
    │
    ▼
arm-smmu-v3 driver probe
    │
    ▼
struct iommu_device 생성
    │
    ▼
iommu_device_register()
    │
    ▼
IOMMU Core에 등록
```

이후 각 DMA master device가 probe될 때, IOMMU Core는 해당 device가 어느 `iommu_device`와 연결되는지 확인합니다.

---

## 8. `iommu_ops`와 `iommu_domain_ops`

IOMMU Core는 vendor driver를 직접 알고 싶어하지 않습니다.

대신 callback table을 사용합니다.

### `struct iommu_ops`

IOMMU driver 전체의 capability와 device-level 동작을 나타냅니다.

예:

```text
probe_device
device_group
default_domain_type
hw_info
```

### `struct iommu_domain_ops`

특정 domain에 대한 실제 동작을 나타냅니다.

예:

```text
attach_dev
map_pages
unmap_pages
iova_to_phys
flush_iotlb_all
iotlb_sync
```

쉽게 말하면 다음과 같습니다.

```text
iommu_ops        = 이 IOMMU driver가 무엇을 할 수 있는가?
domain_ops       = 이 domain에서 map/unmap을 어떻게 수행하는가?
```

---

## 9. `iommu_domain`: 장치용 I/O 주소 공간

`iommu_domain`은 가장 중요한 객체입니다.

쉽게 말하면 다음입니다.

```text
iommu_domain = 장치가 사용하는 I/O 주소 공간
```

예를 들어 NPU용 domain이 있다고 해봅시다.

```text
NPU IOMMU Domain

IOVA 0x1000_0000 → PA 0x8800_0000
IOVA 0x1000_1000 → PA 0x8910_0000
IOVA 0x1000_2000 → PA 0x8A20_0000

permissions: READ / WRITE / CACHE
```

NPU는 IOVA만 봅니다.

```text
NPU DMA read 0x1000_0000
```

IOMMU는 domain의 page table을 보고 PA로 변환합니다.

```text
IOVA 0x1000_0000 → PA 0x8800_0000
```

CPU 프로세스마다 주소 공간이 다르듯, DMA master도 domain에 따라 서로 다른 I/O 주소 공간을 가질 수 있습니다.

---

## 10. IOMMU Domain Type

Linux에서는 상황에 따라 여러 domain type을 사용합니다.

| Domain type | 개념 | 주 사용처 | 주의점 |
|---|---|---|---|
| DMA / Translated | IOVA → PA 변환 | 일반 DMA API default domain | 보호/유연성 좋음, map/unmap 비용 있음 |
| Identity / Passthrough | IOVA == PA 또는 bypass 성격 | 성능/호환성, 일부 부팅 설정 | 격리 약화 가능 |
| Blocked | DMA 접근 차단 | 초기화, release, 보안 상태 | 장치 동작 전 attach 필요 |
| Unmanaged / User | 사용자가 mapping 직접 관리 | VFIO, IOMMUFD, VM passthrough | group ownership과 보안 검증 중요 |
| SVA / PASID | 프로세스 주소 공간 공유 | GPU/NPU, PCIe ATS/PRI | 하드웨어/드라이버 지원 필요 |

Kernel version에 따라 enum 이름과 allocation API는 조금씩 변할 수 있습니다. 반드시 target BSP의 `include/linux/iommu.h`를 기준으로 확인해야 합니다.

---

## 11. DMA domain

DMA domain은 일반 장치 드라이버가 가장 자주 만나는 domain입니다.

흐름은 다음과 같습니다.

```text
driver buffer
    │
    ▼
dma_map_*()
    │
    ▼
IOVA allocation
    │
    ▼
iommu_map()
    │
    ▼
device DMA address 반환
```

특징:

- DMA API의 default path에서 사용됩니다.
- IOVA allocator가 장치 주소 공간에서 빈 영역을 선택합니다.
- IOMMU Core/vendor driver가 IOVA → PA mapping을 생성합니다.
- unmap 시 mapping 제거와 IOTLB invalidation이 수행됩니다.

장점:

- 장치별 보호 가능
- scatter-gather physical memory를 contiguous IOVA로 제공 가능
- DMA mask 제약 대응 가능

단점:

- map/unmap 비용
- IOTLB miss 비용
- page table memory 사용

---

## 12. Identity / Passthrough domain

Identity domain은 대체로 다음과 같이 이해할 수 있습니다.

```text
IOVA == PA
```

예:

```text
Device DMA address 0x8800_0000
        │
        ▼
IOMMU identity mapping
        │
        ▼
Physical address 0x8800_0000
```

사용 이유:

- 성능
- 기존 driver와의 호환성
- 특정 boot policy
- IOMMU 기능은 켜지만 DMA translation은 기본적으로 우회하고 싶은 경우

주의점:

- translated domain보다 격리 수준이 약할 수 있습니다.
- 장치가 접근 가능한 물리 메모리 범위가 넓어질 수 있습니다.
- Automotive/security 시스템에서는 무분별한 bypass를 피해야 합니다.

---

## 13. Blocked domain

Blocked domain은 장치 DMA를 막는 상태입니다.

```text
Device DMA request
        │
        ▼
IOMMU
        │
        X blocked
```

사용 예:

- 장치가 아직 driver에 bind되지 않은 상태
- driver release 이후 안전한 상태
- 사용하지 않는 DMA master를 차단
- 보안 정책상 default deny가 필요한 경우

Automotive SoC에서는 사용하지 않는 DMA master가 DRAM을 접근하지 못하도록 blocked 상태를 유지하는 설계가 중요합니다.

---

## 14. Unmanaged / User domain

Unmanaged 또는 user-managed domain은 일반 kernel DMA path가 아니라 userspace/VM이 mapping을 관리하는 경우에 사용됩니다.

대표 예:

- VFIO
- IOMMUFD
- QEMU device passthrough
- userspace driver
- nested translation

개념적 흐름:

```text
QEMU / userspace
    │
    ▼
VFIO / IOMMUFD
    │
    ▼
IOMMU domain
    │
    ▼
IOMMU hardware
```

VM에 장치를 직접 넘기는 경우, 장치는 guest memory에 DMA를 수행합니다. 이때 IOMMU가 없으면 장치가 host memory 전체를 건드릴 수 있습니다.

IOMMU domain은 guest가 허용한 memory만 장치가 접근하도록 제한합니다.

---

## 15. `iommu_group`: 격리 가능한 최소 단위

`iommu_group`은 다음을 의미합니다.

```text
iommu_group = 하드웨어적으로 격리 가능한 최소 장치 묶음
```

중요한 점:

> **항상 “장치 하나 = 독립 격리 가능”은 아닙니다.**

예를 들어 PCIe bridge 아래 장치들이 완전히 분리되지 않으면, 여러 장치가 같은 group에 속할 수 있습니다.

```text
IOMMU Group 7
 ├── PCIe bridge
 ├── Device A
 ├── Device B
 └── Function C
```

VFIO는 group을 ownership 단위로 사용합니다.

```text
VM에 Device A만 넘기고 싶은데,
Device A와 Device B가 같은 group이면?

→ Device B도 같은 격리 단위에 있으므로 host가 계속 안전하게 사용할 수 없을 수 있음
```

따라서 device passthrough를 분석할 때 가장 먼저 확인할 것은 group입니다.

```bash
find /sys/kernel/iommu_groups -maxdepth 2 -type l
```

---

## 16. Default domain

Default domain은 장치가 기본으로 attach되는 domain입니다.

대략적인 probe 흐름:

```text
device probe
    │
    ▼
iommu_probe_device()
    │
    ▼
iommu_group 생성 또는 참여
    │
    ▼
default domain 선택
    │
    ▼
DMA ops setup
```

default domain은 보통 다음 중 하나입니다.

- DMA translated domain
- identity/passthrough domain
- blocked domain

무엇이 선택되는지는 다음의 영향을 받습니다.

- kernel config
- boot parameter
- IOMMU driver default policy
- platform firmware
- device 특성

---

## 17. 부팅/probe 시점의 흐름

Embedded ARM SoC 기준으로 보면 다음과 같습니다.

```text
1. Firmware가 IOMMU topology를 제공한다.
   - Device Tree: iommus property
   - ACPI: IORT 등

2. ARM SMMU driver가 probe된다.

3. SMMU driver가 iommu_device를 등록한다.

4. 각 DMA master device가 probe된다.

5. IOMMU Core가 device의 IOMMU 연결 정보를 확인한다.

6. device가 iommu_group에 들어간다.

7. default domain이 설정된다.

8. DMA API가 해당 domain을 사용한다.
```

---

## 18. Firmware 정보와 `iommus` property

ARM Device Tree 예시는 다음과 같습니다.

```dts
smmu: iommu@2b400000 {
    compatible = "arm,smmu-v3";
    reg = <0x0 0x2b400000 0x0 0x100000>;
    #iommu-cells = <1>;
};

npu@12340000 {
    compatible = "vendor,npu";
    reg = <0x0 0x12340000 0x0 0x10000>;
    iommus = <&smmu 0x20>;
    dma-coherent;
};
```

여기서 중요한 부분은 다음입니다.

```dts
iommus = <&smmu 0x20>;
```

의미:

```text
이 NPU의 DMA transaction은 smmu를 거친다.
이 장치의 Stream ID는 0x20이다.
```

이 정보가 틀리면 다음 문제가 발생할 수 있습니다.

- 장치가 IOMMU를 bypass함
- 잘못된 Stream ID로 fault 발생
- device가 expected domain에 attach되지 않음
- DMA API가 예상과 다른 주소를 반환함

---

## 19. `dma_map_single()` 내부 경로

IOMMU가 켜진 시스템에서 `dma_map_single()`이 호출되면 개념적으로 다음이 일어납니다.

```text
1. driver가 CPU virtual address를 넘긴다.
2. DMA Mapping Layer가 physical page를 확인한다.
3. device의 dma mask와 addressing 제약을 확인한다.
4. IOMMU path가 필요하면 DMA-IOMMU Layer로 진입한다.
5. IOVA allocator가 빈 IOVA range를 할당한다.
6. IOMMU Core가 domain에 IOVA → PA mapping을 요청한다.
7. Vendor IOMMU driver가 page table entry를 작성한다.
8. 필요한 IOTLB sync를 수행한다.
9. dma_addr_t, 즉 device DMA address를 반환한다.
10. driver는 이 주소를 device register에 쓴다.
```

그림으로 보면:

```text
driver
  │
  ▼
dma_map_single()
  │
  ▼
dma_ops
  │
  ▼
iommu_dma_map
  │
  ▼
iova alloc
  │
  ▼
iommu_map
  │
  ▼
SMMU page table entry
```

---

## 20. IOMMU Core API: attach / map / unmap

개념적으로 IOMMU Core API는 다음과 같이 사용할 수 있습니다.

```c
struct iommu_domain *domain;

domain = iommu_paging_domain_alloc(dev);

iommu_attach_device(domain, dev);

iommu_map(domain, iova, phys_addr, size, prot, GFP_KERNEL);

/* device DMA */

iommu_unmap(domain, iova, size);
```

의미:

| API | 의미 |
|---|---|
| `iommu_paging_domain_alloc()` | paging 가능한 IOMMU domain 생성 |
| `iommu_attach_device()` | device를 domain에 연결 |
| `iommu_map()` | IOVA range를 physical memory에 mapping |
| `iommu_unmap()` | IOVA mapping 제거 |
| `iommu_iova_to_phys()` | IOVA가 어떤 PA로 변환되는지 확인 |

일반 장치 드라이버가 위 API를 직접 호출하지 않는 이유는 다음입니다.

- domain ownership을 직접 관리해야 합니다.
- buffer lifetime을 직접 관리해야 합니다.
- IOTLB sync를 직접 고려해야 합니다.
- concurrent DMA 중 unmap 위험을 직접 피해야 합니다.
- DMA mask, bounce buffering, cache sync 같은 주변 조건을 놓치기 쉽습니다.

그래서 일반 드라이버는 DMA API를 사용합니다.

---

## 21. IOMMU page table과 io-pgtable

IOMMU domain은 내부적으로 page table을 가집니다.

```text
iommu_domain
    │
    ▼
io-pgtable ops
    │
    ▼
hardware page table format
```

ARM SMMU의 경우 Arm translation table 형식을 사용하는 경우가 많습니다.

고려할 요소:

- page size
- granule
- stage 1 vs stage 2
- access permission
- memory attributes
- shareability
- cacheability
- contiguous bit / block mapping 가능성

성능 관점:

- 작은 page mapping이 많으면 IOTLB pressure가 증가합니다.
- scatterlist fragmentation이 심하면 page table entry가 많아집니다.
- 대용량 영상/NPU buffer는 alignment와 mapping 재사용이 중요합니다.

---

## 22. IOVA allocator

IOMMU가 켜져 있으면 장치는 PA가 아니라 IOVA를 사용할 수 있습니다.

IOVA allocator는 장치 주소 공간에서 빈 영역을 찾습니다.

```text
IOVA aperture

0x0000_0000                                      0xFFFF_FFFF
| reserved | mapping A | free | mapping B | new map | free |
```

관련 개념:

- IOVA aperture: mapping 가능한 IOVA 범위
- reserved region: MSI doorbell, firmware region 등으로 제외되는 영역
- DMA mask: 장치가 표현 가능한 주소 bit width
- IOVA fragmentation: 빈 공간이 흩어져 큰 mapping 실패 가능

실전 문제:

- DMA mapping 실패
- IOVA leak
- unmap 누락
- DMA mask 불일치
- SWIOTLB fallback

---

## 23. Scatter-Gather와 IOMMU

물리 메모리는 흩어져 있을 수 있습니다.

```text
Physical pages:
PA A      PA B
    PA C         PA D
```

IOMMU는 이를 장치에게 연속된 IOVA처럼 보이게 할 수 있습니다.

```text
Device view:
IOVA 0x1000_0000 → PA A
IOVA 0x1000_1000 → PA B
IOVA 0x1000_2000 → PA C
IOVA 0x1000_3000 → PA D
```

이것이 중요한 분야:

- V4L2 camera capture
- DRM/KMS display buffer
- GPU buffer object
- NPU tensor buffer
- DMA-BUF sharing
- NVMe/network scatter-gather DMA

DMA-BUF pipeline에서 `sg_table`이 중요한 이유도 여기에 있습니다.

---

## 24. IOTLB

IOMMU도 CPU의 TLB처럼 translation cache를 가집니다.

```text
IOTLB = I/O Translation Lookaside Buffer
```

동작:

```text
Device DMA IOVA
    │
    ▼
IOTLB lookup
    │
    ├── hit  → 빠르게 PA 확인
    └── miss → page table walk
```

unmap할 때 중요한 이유:

```text
iommu_unmap()
    │
    ├── page table entry 제거
    └── stale IOTLB entry invalidate 필요
```

만약 stale IOTLB entry가 남아 있으면, 장치가 이미 해제된 memory에 계속 DMA할 수 있습니다.

---

## 25. `iommu.strict`와 성능/보안 trade-off

Linux에는 IOTLB invalidation 정책을 조절하는 parameter가 있습니다.

| 모드 | 동작 | 장점 | 단점 |
|---|---|---|---|
| Strict | unmap 시 hardware IOTLB를 동기적으로 invalidate | 격리/보안 강함 | throughput 저하 가능 |
| Lazy | IOTLB invalidation을 지연/배치 | map/unmap 많은 workload에서 성능 유리 | unmap 후 격리성이 약해질 수 있음 |
| Passthrough | 기본 DMA를 IOMMU translation 없이 사용 | 단순/호환/성능 목적 | DMA protection 약화 가능 |

예:

```text
iommu.strict=1       strict mode
iommu.strict=0       lazy mode
iommu.passthrough=1  default DMA bypass
iommu.passthrough=0  default DMA translated
```

실전 판단:

- safety/security/virtualization 중요 → translated + strict 선호
- throughput 극단적으로 중요 → lazy 검토 가능
- 단, 위험과 보안 boundary를 문서화해야 함

---

## 26. IOMMU fault 처리

IOMMU fault는 장치 DMA 접근이 IOMMU 정책에 의해 거부되었다는 뜻입니다.

대표 fault:

| Fault | 의미 |
|---|---|
| Translation fault | IOVA mapping 없음 |
| Permission fault | read/write 권한 위반 |
| Address size fault | IOVA가 aperture 또는 DMA mask 밖 |
| Stream/context fault | 잘못된 Stream ID 또는 context 설정 |

Debug 순서:

```text
1. dmesg에서 faulting device 확인
2. Stream ID 또는 requester ID 확인
3. fault IOVA 확인
4. access type 확인: read/write
5. 해당 IOVA가 driver가 map한 dma_addr_t 범위인지 확인
6. 최근 unmap/free 시점 확인
7. device가 DMA 완료 전에 buffer를 해제하지 않았는지 확인
```

가장 흔한 원인:

- `dma_unmap_single()` 이후 device가 계속 DMA
- driver가 `dma_addr_t` 대신 PA를 device register에 입력
- DMA direction 오류
- buffer lifetime 문제
- DMA-BUF fence/sync 누락
- wrong Stream ID

---

## 27. VFIO와 IOMMU group

VFIO는 userspace가 device에 직접 접근할 수 있게 해주는 framework입니다.

```text
QEMU VM
    │
    ▼
VFIO
    │
    ▼
IOMMU domain
    │
    ▼
PCIe device
```

가장 위험한 것은 DMA입니다.

장치가 host memory 전체에 접근하면 시스템 무결성이 깨집니다.

따라서 VFIO는 IOMMU group을 ownership 단위로 사용합니다.

```text
IOMMU group 전체가 안전하게 host에서 분리되어야
userspace/VM에 넘길 수 있음
```

확인 명령:

```bash
find /sys/kernel/iommu_groups -maxdepth 2 -type l
```

---

## 28. IOMMUFD

IOMMUFD는 `/dev/iommu` file descriptor 기반으로 userspace가 I/O page table을 관리하기 위한 API입니다.

주요 객체:

| IOMMUFD 객체 | 의미 |
|---|---|
| IOAS | I/O address space. IOVA range에 userspace memory를 map/unmap |
| DEVICE | iommufd에 bind된 device |
| HWPT_PAGING | 실제 hardware I/O page table. `struct iommu_domain`에 대응 |
| HWPT_NESTED | nested translation에서 user-managed stage-1 page table |
| FAULT | PRI/Page fault 처리를 위한 fault queue |

IOMMUFD는 기존 VFIO type1 backend의 내부 IOMMU logic을 일반화하는 방향입니다.

---

## 29. Embedded/Automotive SoC에서의 의미

자동차/임베디드 SoC에는 DMA master가 많습니다.

```text
Camera CSI
ISP
Scaler
NPU
GPU
VPU
Display
Ethernet AVB/TSN
PCIe
USB
DMA Engine
```

예를 들어 Camera → ISP → NPU → Display pipeline을 보면:

```text
Camera
  │ DMA write
  ▼
Frame buffer
  │
  ▼
ISP
  │ DMA read/write
  ▼
Processed buffer
  │
  ▼
NPU
  │ DMA read/write
  ▼
Tensor/result buffer
  │
  ▼
Display/GPU
```

IOMMU Framework의 역할:

- 각 장치가 접근 가능한 buffer만 mapping
- device별 DMA 주소 공간 분리
- 같은 physical buffer를 장치별 IOVA로 mapping
- 잘못된 DMA 접근 fault 처리
- virtualization/hypervisor 환경에서 device isolation 지원

Safety/security 관점:

- 사용하지 않는 DMA master는 blocked
- active master는 필요한 buffer만 최소 mapping
- passthrough/identity mapping 사용 여부 문서화
- fault log와 safety monitor 연계 검토

성능 관점:

- map/unmap 최소화
- IOTLB pressure 감소
- large mapping 활용
- buffer alignment 고려
- cache coherency 확인

---

## 30. Debugging checklist

### 기본 확인

```bash
dmesg | grep -i iommu
dmesg | grep -i smmu
dmesg | grep -i fault
cat /proc/cmdline
```

### IOMMU group 확인

```bash
find /sys/kernel/iommu_groups -maxdepth 2 -type l
```

### DMA API debug

DMA API debug가 활성화된 kernel이라면:

```bash
ls /sys/kernel/debug/dma-api/
cat /sys/kernel/debug/dma-api/all_errors
```

### 확인 질문

```text
1. IOMMU/SMMU driver가 probe되었는가?
2. 장치가 기대한 group에 들어갔는가?
3. kernel parameter가 passthrough/strict/lazy를 바꿨는가?
4. fault IOVA가 driver가 map한 dma_addr_t 범위인가?
5. unmap/free 이후 장치가 DMA를 계속하지 않는가?
6. cache sync 문제인지 translation fault인지 구분했는가?
7. DMA-BUF importer/exporter의 lifetime이 맞는가?
8. fence 또는 synchronization이 빠지지 않았는가?
```

---

## 31. Kernel Source Reading Map

| 파일/디렉터리 | 볼 내용 |
|---|---|
| `include/linux/iommu.h` | 핵심 struct, enum, public API |
| `drivers/iommu/iommu.c` | IOMMU Core: group/domain/probe/default domain |
| `drivers/iommu/dma-iommu.c` | DMA API와 IOMMU 연결, IOVA allocation |
| `drivers/iommu/io-pgtable-arm.c` | ARM 계열 page table entry 생성 |
| `drivers/iommu/arm/arm-smmu/` | ARM SMMUv2/MMU-500 driver |
| `drivers/iommu/arm/arm-smmu-v3/` | ARM SMMUv3/MMU-600/MMU-700 계열 driver |
| `drivers/iommu/iommufd/` | IOMMUFD userspace API backend |

추천 읽는 순서:

```text
include/linux/iommu.h
    ↓
drivers/iommu/iommu.c
    ↓
drivers/iommu/dma-iommu.c
    ↓
drivers/iommu/arm/arm-smmu-v3/
    ↓
drivers/iommu/io-pgtable-arm.c
```

---

## 32. 실전에서 자주 보는 문제

| 증상 | 가능 원인 | 확인 포인트 |
|---|---|---|
| IOMMU translation fault | unmap 후 DMA, 잘못된 `dma_addr_t`, mapping 누락 | fault IOVA와 driver log 비교 |
| DMA mapping error | DMA mask 부족, IOVA aperture 부족, SWIOTLB 부족 | `dma_set_mask`, `/proc/cmdline`, `dmesg` |
| 간헐적 data corruption | cache sync 누락, direction 오류, buffer lifetime 문제 | `dma_sync_*`, direction, fence |
| VFIO bind 실패 | group 내 다른 device가 host driver에 bind | `/sys/kernel/iommu_groups` 확인 |
| 성능 저하 | map/unmap 과다, IOTLB miss, 작은 page mapping | mapping reuse, batch, large buffer alignment |

---

# 퀴즈

## Q1
일반 장치 드라이버가 보통 직접 호출하지 않는 API는?

A. `dma_map_single()`  
B. `iommu_map()`  
C. `dma_unmap_single()`

## Q2
`iommu_domain`을 가장 쉽게 설명하면 무엇인가?

## Q3
`iommu_group`이 중요한 이유는 무엇인가?

## Q4
`dma_addr_t`를 CPU가 직접 dereference하면 안 되는 이유는 무엇인가?

## Q5
identity domain과 translated DMA domain의 차이는 무엇인가?

## Q6
`dma_map_single()` 호출 뒤 IOMMU가 켜진 시스템에서 반환되는 주소는 무엇일 가능성이 높은가?

## Q7
IOTLB invalidate가 필요한 시점은 언제인가?

## Q8
`iommu.strict=0` lazy mode의 장점과 위험은 무엇인가?

## Q9
VFIO가 device 하나가 아니라 group을 ownership 단위로 보는 이유는 무엇인가?

## Q10
Camera → NPU DMA-BUF pipeline에서 같은 physical buffer의 IOVA가 장치마다 다를 수 있는 이유는 무엇인가?

---

# 정답 및 해설

## A1
정답은 **B. `iommu_map()`**입니다.

일반 장치 드라이버는 보통 DMA API를 사용합니다. `iommu_map()`은 IOMMU Core API에 가까우며, IOMMU driver, VFIO/IOMMUFD, 특수 subsystem에서 직접 사용하는 경우가 많습니다.

## A2
`iommu_domain`은 **장치가 사용하는 I/O 주소 공간**입니다.

IOVA → PA mapping과 접근 권한 정보를 담습니다.

```text
IOVA 0x1000_0000 → PA 0x8800_0000
IOVA 0x1000_1000 → PA 0x8910_0000
```

## A3
`iommu_group`은 **하드웨어적으로 격리 가능한 최소 장치 묶음**이기 때문입니다.

PCIe bridge, multi-function device, interconnect topology 때문에 장치 하나 단위로 격리가 보장되지 않을 수 있습니다. VFIO는 이 group을 ownership 단위로 사용합니다.

## A4
`dma_addr_t`는 CPU pointer가 아니라 **장치가 사용하는 DMA address**입니다.

CPU가 직접 접근하는 주소는 CPU virtual address입니다. DMA address와 CPU address space 사이에는 IOMMU translation이 있을 수 있으므로, CPU가 `dma_addr_t`를 직접 dereference하면 안 됩니다.

## A5
translated DMA domain은 IOVA → PA 변환을 수행합니다.

```text
IOVA 0x1000_0000 → PA 0x8800_0000
```

identity domain은 대체로 IOVA와 PA가 같거나 bypass 성격입니다.

```text
IOVA 0x8800_0000 → PA 0x8800_0000
```

translated domain은 보호와 유연성이 좋고, identity/passthrough는 단순하지만 격리성이 약해질 수 있습니다.

## A6
IOMMU가 켜진 시스템에서는 반환되는 `dma_addr_t`가 **IOVA**일 가능성이 높습니다.

driver는 이 주소를 device register에 써주고, device는 이 IOVA로 DMA를 수행합니다. IOMMU는 IOVA를 PA로 변환합니다.

## A7
IOTLB invalidate는 mapping을 제거하거나 page table entry를 바꾼 뒤 stale translation을 없애야 할 때 필요합니다.

특히 `iommu_unmap()` 이후 기존 IOVA가 더 이상 유효하지 않도록 hardware IOTLB를 invalidate해야 합니다.

## A8
`iommu.strict=0` lazy mode는 IOTLB invalidation을 지연/배치하여 throughput을 높일 수 있습니다.

위험은 unmap 직후에도 stale translation이 잠시 남을 수 있어, strict mode보다 device isolation이 약해질 수 있다는 점입니다.

## A9
하드웨어 topology 때문에 device 하나 단위의 격리가 항상 보장되지 않기 때문입니다.

같은 bridge 아래 장치들이 IOMMU를 거치지 않고 서로 transaction을 전달할 수 있거나, IOMMU가 requester를 구분하지 못하는 경우가 있습니다. 따라서 VFIO는 group 전체를 ownership 단위로 봅니다.

## A10
각 장치가 서로 다른 `iommu_domain`에 attach될 수 있기 때문입니다.

같은 physical pages라도 Camera domain, NPU domain, Display domain에 각각 다른 IOVA range로 mapping될 수 있습니다.

```text
같은 PA buffer

Camera IOVA  → 0x1000_0000
NPU IOVA     → 0x4000_0000
Display IOVA → 0x7000_0000
```

---

# 복습 카드

## Card 1. `iommu_domain`

장치용 I/O 주소 공간입니다. IOVA → PA mapping을 담습니다.

## Card 2. `iommu_group`

하드웨어적으로 격리 가능한 최소 장치 묶음입니다.

## Card 3. `iommu_ops`

IOMMU Core가 vendor IOMMU driver를 호출하기 위한 callback 집합입니다.

## Card 4. `dma_addr_t`

장치가 사용하는 DMA address입니다. CPU pointer가 아닙니다.

## Card 5. IOVA

I/O Virtual Address입니다. 장치가 보는 주소이며, IOMMU가 PA로 변환할 수 있습니다.

## Card 6. IOTLB

IOMMU의 translation cache입니다. unmap 후 stale entry 제거를 위해 invalidate가 필요합니다.

## Card 7. Default domain

장치가 기본적으로 attach되는 IOMMU domain입니다. DMA API가 이 domain을 사용할 수 있습니다.

## Card 8. Identity domain

IOVA와 PA가 같게 보이거나 bypass 성격을 갖는 domain입니다. 성능/호환성에는 유리할 수 있지만 보호는 약해질 수 있습니다.

## Card 9. Unmanaged domain

VFIO/IOMMUFD/VM passthrough처럼 userspace 또는 상위 subsystem이 mapping을 직접 관리하는 domain입니다.

## Card 10. DMA-IOMMU Layer

DMA API와 IOMMU Core 사이에서 IOVA allocation, scatter-gather mapping, default DMA domain 관리를 담당하는 계층입니다.

---

# 5분 복습 질문

아래 질문에 말로 답해보세요.

1. `dma_map_single()`이 반환한 `dma_addr_t`는 PA인가, IOVA인가?
2. `struct device`가 DMA mapping에서 중요한 이유는?
3. `iommu_domain`과 CPU `mm_struct`를 비교하면 어떤 점이 비슷하고 다른가?
4. `iommu_group`이 VFIO에서 ownership 단위가 되는 이유는?
5. `iommu.strict=0`이 성능을 높일 수 있는 이유는?
6. IOMMU fault가 발생하면 가장 먼저 확인할 값은 무엇인가?
7. Camera와 NPU가 같은 DMA-BUF를 공유해도 IOVA가 다를 수 있는 이유는?

---

# 실습 과제

## 과제 1. IOMMU group 확인

개발 보드 또는 Linux PC에서 다음을 실행합니다.

```bash
find /sys/kernel/iommu_groups -maxdepth 2 -type l
```

확인할 것:

- group 개수
- 각 group에 어떤 device가 들어 있는지
- PCIe device가 bridge와 같이 묶여 있는지

## 과제 2. boot parameter 확인

```bash
cat /proc/cmdline
```

확인할 것:

- `iommu=`
- `iommu.strict=`
- `iommu.passthrough=`
- `intel_iommu=` 또는 platform-specific parameter

## 과제 3. SMMU/IOMMU probe log 확인

```bash
dmesg | grep -i iommu
dmesg | grep -i smmu
```

확인할 것:

- IOMMU driver가 probe되었는가?
- default domain 관련 log가 있는가?
- fault log가 있는가?

## 과제 4. Kernel source 읽기

다음 순서로 source를 열어봅니다.

```text
include/linux/iommu.h
    ↓
drivers/iommu/iommu.c
    ↓
drivers/iommu/dma-iommu.c
```

읽을 때 찾을 키워드:

```text
struct iommu_domain
struct iommu_ops
struct iommu_domain_ops
struct iommu_group
iommu_attach_device
iommu_map
iommu_unmap
iommu_probe_device
default_domain
```

---

# 다음 강의 연결

4강에서는 ARM SMMU Architecture Overview를 다룹니다.

3강에서 배운 Linux 객체를 ARM SMMU 하드웨어 개념으로 연결합니다.

```text
Linux IOMMU Core       ARM SMMU Hardware
------------------------------------------------
iommu_domain      →   translation context / page table
iommu_group       →   isolation topology
device/fwspec     →   Stream ID
iommu_map         →   SMMU page table entry update
IOTLB invalidate  →   SMMU TLB maintenance command
fault handler     →   SMMU fault/event queue
```

다음 강의의 핵심 문장:

> **ARM SMMU는 Stream ID를 기준으로 DMA transaction의 translation context를 선택한다.**

---

# 참고 자료

- Linux Kernel Documentation - Dynamic DMA mapping Guide: <https://docs.kernel.org/core-api/dma-api-howto.html>
- Linux Kernel Documentation - Dynamic DMA mapping using the generic device: <https://docs.kernel.org/core-api/dma-api.html>
- Linux Kernel Documentation - VFIO: <https://docs.kernel.org/driver-api/vfio.html>
- Linux Kernel Documentation - IOMMUFD: <https://docs.kernel.org/userspace-api/iommufd.html>
- Linux Kernel Documentation - Kernel command-line parameters: <https://docs.kernel.org/admin-guide/kernel-parameters.html>
- Linux source: `include/linux/iommu.h`, `drivers/iommu/iommu.c`, `drivers/iommu/dma-iommu.c`
