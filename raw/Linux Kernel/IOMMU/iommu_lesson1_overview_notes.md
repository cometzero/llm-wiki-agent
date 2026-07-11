# 1강. IOMMU Overview

> Linux Kernel Study - IOMMU / ARM SMMU Series  
> 목표: DMA 장치가 메모리에 접근할 때 왜 IOMMU가 필요한지, 그리고 Linux Kernel에서 왜 DMA API가 중요한지 이해한다.

---

## 0. 1강 학습 목표

이 강의가 끝나면 다음 질문에 답할 수 있어야 합니다.

1. DMA가 무엇이고 왜 필요한가?
2. CPU가 사용하는 주소와 장치가 사용하는 주소는 어떻게 다른가?
3. IOMMU가 없는 시스템에서 어떤 위험이 생기는가?
4. IOMMU가 있으면 DMA address/IOVA가 어떻게 physical address로 변환되는가?
5. `dma_addr_t`는 CPU pointer인가, 장치에게 전달하는 주소인가?
6. IOMMU가 cache coherency까지 자동으로 해결해 주는가?
7. Embedded/Automotive SoC에서 Camera, ISP, NPU, GPU 같은 장치에 IOMMU가 왜 중요한가?

---

## 1. DMA란 무엇인가?

DMA는 **Direct Memory Access**의 약자입니다. 장치가 CPU를 거치지 않고 시스템 메모리를 직접 읽거나 쓰는 방식입니다.

예를 들어 카메라가 영상 프레임을 DRAM에 저장한다고 생각해 보겠습니다.

```text
Camera Sensor / CSI / ISP
        |
        | DMA write
        v
      DRAM Frame Buffer
```

CPU가 모든 픽셀 데이터를 직접 읽고 다시 메모리에 복사하면 CPU 사용량과 memory bandwidth 사용량이 커집니다. 그래서 대용량 데이터 이동은 장치가 직접 수행하도록 하는 것이 일반적입니다.

대표적인 DMA 장치:

- Camera CSI / ISP
- GPU
- NPU / AI accelerator
- VPU / video codec
- Display controller
- Ethernet / PCIe / USB controller
- DMA engine

---

## 2. DMA의 위험: 장치가 메모리를 직접 건드린다

DMA는 성능을 위해 필요하지만 위험도 있습니다.

장치가 잘못된 주소로 DMA를 수행하면 다음 문제가 생길 수 있습니다.

- 커널 메모리 손상
- 다른 프로세스 메모리 손상
- 다른 장치의 buffer 손상
- 보안 영역 또는 hypervisor 영역 침범
- 원인을 찾기 어려운 memory corruption

IOMMU가 없다면 장치의 잘못된 DMA 접근을 하드웨어적으로 제한하기 어렵습니다.

---

## 3. 주소 공간 구분하기

IOMMU를 이해하려면 주소 종류를 구분해야 합니다.

| 용어 | 의미 | 누가 주로 사용하는가 |
|---|---|---|
| VA, Virtual Address | CPU/커널 코드가 사용하는 가상주소 | CPU, kernel code |
| PA, Physical Address | DRAM의 실제 물리주소 | MMU, memory subsystem |
| DMA Address / Bus Address | 장치에게 전달하는 주소 | device hardware |
| IOVA, I/O Virtual Address | IOMMU가 변환하는 장치용 가상주소 | IOMMU, DMA device |

핵심은 이것입니다.

```text
CPU가 쓰는 주소 != 장치가 쓰는 주소일 수 있다
```

Linux DMA API 문서에서도 장치가 DMA에 사용하는 주소는 bus address이며, 시스템에 따라 CPU physical address와 같지 않을 수 있다고 설명합니다. IOMMU와 host bridge가 physical address와 bus address 사이에 mapping을 만들 수 있기 때문입니다.

---

## 4. IOMMU가 없을 때

IOMMU가 없거나 bypass 상태라면 장치는 보통 물리주소와 유사한 DMA address로 메모리에 접근합니다.

```text
Device DMA Address  ------------------>  DRAM Physical Address
```

예:

```text
Device DMA write
  address = 0x8800_0000
  length  = 4 KB
```

장치가 잘못해서 다른 주소를 사용하면 해당 메모리를 그대로 덮어쓸 수 있습니다.

---

## 5. IOMMU가 있을 때

IOMMU는 장치와 DRAM 사이에 위치합니다.

```text
Device
  |
  | DMA Address / IOVA
  v
IOMMU
  |  address translation + permission check
  v
DRAM Physical Address
```

장치는 실제 physical address를 직접 사용할 필요가 없습니다. 장치에게는 DMA address, 즉 IOVA를 전달하고, IOMMU가 이 주소를 실제 PA로 변환합니다.

예:

```text
Device가 보는 주소:  IOVA 0x1000_0000
실제 DRAM 주소:      PA   0x8800_0000
```

---

## 6. IOMMU의 핵심 기능

### 6.1 주소 변환

```text
IOVA -> Physical Address
```

CPU MMU가 CPU virtual address를 physical address로 바꾸듯이, IOMMU는 장치가 사용하는 DMA address/IOVA를 physical address로 바꿉니다.

### 6.2 접근 권한 검사

IOMMU는 다음을 검사할 수 있습니다.

- 이 장치가 이 주소에 접근해도 되는가?
- read만 가능한가, write도 가능한가?
- 이 장치의 허용된 IOVA range 안인가?
- 매핑이 존재하는가?

잘못된 접근은 IOMMU fault로 보고될 수 있습니다.

### 6.3 장치 격리

각 장치가 접근 가능한 buffer만 mapping할 수 있습니다.

```text
Camera  -> Camera buffer만 접근
NPU     -> Tensor buffer만 접근
Display -> Framebuffer만 접근
```

### 6.4 흩어진 물리 페이지를 연속된 IOVA처럼 보이게 하기

실제 physical memory는 흩어져 있을 수 있습니다.

```text
Physical pages:
[PA A]    [hole]    [PA B]       [PA C]
```

IOMMU mapping을 사용하면 장치에게는 연속 주소처럼 보일 수 있습니다.

```text
Device view:
[IOVA 0][IOVA 1][IOVA 2]
```

이 기능은 영상 buffer, tensor buffer, graphics buffer처럼 큰 buffer를 다룰 때 유용합니다.

---

## 7. MMU vs IOMMU

| 구분 | CPU MMU | IOMMU |
|---|---|---|
| 대상 | CPU access | Device DMA access |
| 입력 주소 | CPU virtual address | DMA address / IOVA |
| 출력 주소 | physical address | physical address |
| 보호 대상 | 프로세스/커널 메모리 | 장치별 DMA 접근 범위 |
| 대표 fault | page fault | IOMMU fault / DMA fault |
| Linux 관련 계층 | memory management | DMA API + IOMMU Framework |

기억법:

```text
MMU   = CPU용 주소 변환기
IOMMU = 장치용 주소 변환기
```

---

## 8. Linux Kernel에서의 기본 흐름

일반 장치 드라이버는 보통 IOMMU를 직접 제어하지 않습니다. 대신 DMA API를 사용합니다.

```text
Device Driver
    |
    | dma_map_single()
    v
DMA Mapping API
    v
DMA-IOMMU Layer
    v
IOMMU Core
    v
Vendor IOMMU Driver
    v
IOMMU Hardware
```

예시 코드:

```c
dma_addr_t dma;

dma = dma_map_single(dev, cpu_buf, size, DMA_TO_DEVICE);
if (dma_mapping_error(dev, dma))
    return -ENOMEM;

writel(lower_32_bits(dma), regs + DMA_ADDR_LO);
writel(upper_32_bits(dma), regs + DMA_ADDR_HI);

/* start device DMA */

dma_unmap_single(dev, dma, size, DMA_TO_DEVICE);
```

해석:

- `cpu_buf`는 CPU가 접근하는 virtual address입니다.
- `dma`는 장치에게 전달할 DMA address입니다.
- IOMMU 사용 시 `dma`는 IOVA일 수 있습니다.
- DMA가 끝나면 `dma_unmap_single()`로 mapping을 해제합니다.

---

## 9. `dma_addr_t`는 CPU pointer가 아니다

`dma_addr_t`는 장치에게 전달하는 DMA address를 담는 타입입니다. CPU가 직접 dereference하는 pointer가 아닙니다.

잘못된 생각:

```c
/* 잘못된 개념: dma를 CPU pointer처럼 사용 */
char *p = (char *)dma;
p[0] = 0x12;
```

올바른 개념:

```text
CPU가 접근할 때: cpu_buf 같은 virtual address 사용
장치가 접근할 때: dma_addr_t 값 사용
```

---

## 10. Embedded / Automotive SoC에서의 의미

Embedded/Automotive SoC에는 DMA master가 많습니다.

```text
Camera -> ISP -> Scaler -> NPU -> GPU/Display
```

각 블록은 DRAM buffer를 읽고 씁니다. 이때 IOMMU는 다음 역할을 합니다.

- 장치별 buffer 접근 제한
- 잘못된 DMA 접근 차단
- 여러 장치가 큰 buffer를 효율적으로 공유하도록 지원
- 가상화 환경에서 VM과 host 간 장치 격리 지원
- 외부 PCIe/USB 장치가 시스템 메모리를 임의 접근하지 못하게 제한

---

## 11. Camera -> NPU 예시

```text
Camera
  | DMA write
  v
Frame Buffer
  |
  | DMA read/write
  v
ISP
  |
  v
Processed Buffer
  |
  | DMA read
  v
NPU
  |
  v
Inference Result
```

IOMMU가 있으면 각 장치가 같은 physical buffer를 보더라도 서로 다른 IOVA로 접근할 수 있습니다.

```text
Physical buffer: PA 0x8800_0000

Camera IOVA:  0x1000_0000
NPU IOVA:     0x4000_0000
Display IOVA: 0x7000_0000
```

중요한 점:

```text
같은 buffer != 항상 같은 device address
```

---

## 12. IOMMU가 해결하지 않는 문제: Cache Coherency

IOMMU는 주소 변환과 접근 권한 검사를 담당합니다. 하지만 CPU cache와 장치 DMA 사이의 데이터 동기화 문제는 별도입니다.

예를 들어 CPU가 buffer에 데이터를 썼는데 그 데이터가 아직 cache에만 있고 DRAM에 반영되지 않았다면, 장치가 DRAM을 읽을 때 오래된 값을 볼 수 있습니다.

non-coherent DMA 환경에서는 다음 API가 중요합니다.

```c
dma_sync_single_for_device(dev, dma, size, DMA_TO_DEVICE);
dma_sync_single_for_cpu(dev, dma, size, DMA_FROM_DEVICE);
```

정리:

```text
IOMMU 문제: 주소 변환, 권한, mapping lifetime
Cache 문제: CPU cache와 device DMA의 데이터 최신성
```

---

## 13. 성능 관점: IOTLB

IOMMU도 변환 결과를 cache할 수 있습니다. 이를 보통 IOTLB라고 부릅니다.

```text
IOTLB = I/O Translation Lookaside Buffer
```

성능에 영향을 주는 요소:

- IOTLB miss
- page table walk 비용
- 너무 잦은 map/unmap
- IOTLB invalidation 비용
- 작은 page 단위 mapping으로 인한 pressure
- scatterlist fragmentation

최적화 방향:

- 불필요한 map/unmap 줄이기
- buffer lifetime과 mapping lifetime 설계
- 큰 mapping 사용 가능성 검토
- DMA-BUF pipeline에서 반복 mapping 비용 줄이기

---

## 14. IOMMU Fault를 볼 때의 질문

IOMMU fault가 발생하면 다음을 확인합니다.

1. 어떤 장치가 접근했는가?
2. 어떤 IOVA에 접근했는가?
3. read인가 write인가?
4. mapping이 존재했는가?
5. 접근 권한이 맞는가?
6. DMA가 unmap 이후에도 계속 발생했는가?
7. DMA mask/address width 설정은 맞는가?

대표 키워드:

```text
IOMMU fault
translation fault
permission fault
Stream ID / SID
IOVA / input address
```

---

## 15. 자주 하는 오해

### 오해 1. `dma_addr_t`는 항상 physical address다

아닙니다. IOMMU 사용 시 `dma_addr_t`는 IOVA일 수 있습니다.

### 오해 2. IOMMU가 있으면 cache 문제도 자동 해결된다

아닙니다. cache coherency는 별도 문제입니다.

### 오해 3. 모든 장치를 완전히 개별 격리할 수 있다

항상 그렇지는 않습니다. 실제 격리 단위는 하드웨어 topology와 IOMMU group 구성에 영향을 받습니다.

### 오해 4. IOMMU는 성능 비용이 없다

아닙니다. IOTLB miss, page table walk, map/unmap, TLB invalidation 비용이 있을 수 있습니다.

---

## 16. 1강 핵심 요약

```text
DMA    = 장치가 CPU를 거치지 않고 메모리에 직접 접근하는 방식
IOMMU  = DMA address/IOVA를 physical address로 변환하고 접근 권한을 검사하는 하드웨어
dma_addr_t = CPU pointer가 아니라 장치에게 전달하는 DMA address
IOVA   = 장치가 보는 가상 주소
IOTLB  = IOMMU 변환 결과 cache
SMMU   = ARM SoC에서 사용하는 IOMMU 계열
```

가장 중요한 한 문장:

```text
IOMMU는 DMA 장치를 위한 MMU다.
```

---

# 퀴즈

## 객관식 10문항

### Q1. DMA에 대한 설명으로 가장 적절한 것은?

A. CPU가 모든 데이터를 직접 복사하는 방식  
B. 장치가 CPU를 거치지 않고 메모리를 직접 읽고 쓰는 방식  
C. 커널이 파일 시스템을 통해 데이터를 복사하는 방식  
D. 장치 레지스터를 가상주소로 바꾸는 방식

### Q2. IOMMU의 핵심 역할이 아닌 것은?

A. DMA address를 physical address로 변환  
B. 장치별 접근 권한 검사  
C. CPU cache coherency를 항상 자동 보장  
D. 잘못된 DMA 접근 차단 또는 fault 보고

### Q3. IOMMU가 켜진 시스템에서 `dma_addr_t`는 무엇일 수 있는가?

A. CPU가 직접 dereference할 수 있는 pointer  
B. 항상 physical address  
C. 장치가 사용하는 DMA address이며 IOVA일 수 있음  
D. 커널 virtual address

### Q4. IOMMU fault가 발생할 수 있는 상황은?

A. 장치가 매핑되지 않은 IOVA에 접근  
B. 장치가 허용되지 않은 write를 시도  
C. unmap 이후 장치가 계속 DMA 수행  
D. 모두 가능

### Q5. CPU MMU와 IOMMU의 차이를 가장 잘 설명한 것은?

A. 둘 다 CPU virtual address만 변환한다  
B. MMU는 CPU 접근, IOMMU는 장치 DMA 접근을 변환/보호한다  
C. IOMMU는 파일 시스템 주소를 변환한다  
D. MMU는 device register만 변환한다

### Q6. 흩어진 물리 페이지를 장치에게 연속 주소처럼 보이게 할 수 있는 이유는?

A. CPU가 데이터를 복사하기 때문  
B. IOMMU page table이 IOVA->PA mapping을 제공하기 때문  
C. DRAM이 항상 연속으로 할당되기 때문  
D. 장치가 page table을 직접 수정하기 때문

### Q7. Embedded/Automotive SoC에서 IOMMU가 중요한 이유는?

A. Camera, ISP, NPU, GPU 등이 모두 DMA master일 수 있기 때문  
B. 모든 장치가 파일 시스템만 사용하기 때문  
C. CPU가 DRAM에 접근하지 않기 때문  
D. IOMMU가 interrupt controller이기 때문

### Q8. IOTLB에 대한 설명으로 적절한 것은?

A. IOMMU 변환 결과를 cache하는 구조  
B. CPU L1 data cache와 완전히 같은 역할  
C. 파일 시스템 block cache  
D. 장치 firmware 저장소

### Q9. 다음 중 IOMMU가 직접 해결하지 않는 문제는?

A. DMA 주소 변환  
B. 장치 접근 권한 검사  
C. Stream/장치별 격리  
D. non-coherent DMA의 cache 동기화 문제 전체

### Q10. Camera->NPU pipeline에서 같은 DMA-BUF를 공유할 때 가능한 상황은?

A. Camera와 NPU가 항상 같은 IOVA를 사용한다  
B. 같은 물리 buffer라도 장치별 IOVA가 다를 수 있다  
C. IOMMU가 있으면 DMA-BUF가 필요 없다  
D. NPU는 DMA를 하지 않는다

---

## 정답 및 해설

| 문제 | 정답 | 해설 |
|---|---:|---|
| Q1 | B | DMA는 장치가 CPU를 거치지 않고 메모리에 직접 접근하는 방식입니다. |
| Q2 | C | IOMMU는 cache coherency를 항상 자동 보장하지 않습니다. |
| Q3 | C | `dma_addr_t`는 장치에게 전달하는 DMA address이며 IOMMU 사용 시 IOVA일 수 있습니다. |
| Q4 | D | translation fault, permission fault, unmap 이후 DMA 등 모두 가능합니다. |
| Q5 | B | MMU는 CPU 접근, IOMMU는 장치 DMA 접근을 담당합니다. |
| Q6 | B | IOMMU page table이 연속 IOVA를 흩어진 PA에 mapping할 수 있습니다. |
| Q7 | A | Embedded/Automotive SoC에는 여러 DMA master가 존재합니다. |
| Q8 | A | IOTLB는 IOMMU translation cache입니다. |
| Q9 | D | cache 동기화 문제는 DMA API sync와 coherency 설정 문제입니다. |
| Q10 | B | 같은 physical buffer라도 장치별 IOVA는 다를 수 있습니다. |

---

# 복습 콘텐츠

## 1분 요약

IOMMU는 장치가 사용하는 DMA address를 실제 physical address로 변환하고, 장치가 허용된 메모리만 접근하도록 검사하는 하드웨어입니다. CPU MMU가 CPU virtual address를 변환하듯이, IOMMU는 DMA 장치의 주소를 변환합니다. Linux 드라이버는 보통 IOMMU를 직접 제어하지 않고 DMA API를 사용합니다. `dma_addr_t`는 CPU가 직접 접근하는 pointer가 아니라 장치에게 전달하는 DMA address입니다.

## 5분 복습 질문

1. IOMMU를 한 문장으로 설명해 보세요.
2. `VA`, `PA`, `DMA Address`, `IOVA`를 각각 설명해 보세요.
3. IOMMU가 없는 DMA 시스템의 위험을 2가지 말해 보세요.
4. `dma_map_single()`이 반환하는 값은 무엇인가요?
5. IOMMU와 cache coherency 문제를 어떻게 구분하나요?
6. IOMMU fault가 발생하면 어떤 정보를 먼저 확인해야 하나요?
7. Camera와 NPU가 같은 buffer를 공유할 때 IOVA가 달라질 수 있는 이유는 무엇인가요?

## 플래시카드

| 앞면 | 뒷면 |
|---|---|
| DMA | 장치가 CPU를 거치지 않고 메모리를 직접 읽고 쓰는 방식 |
| IOMMU | DMA address를 PA로 변환하고 접근 권한을 검사하는 장치용 MMU |
| IOVA | IOMMU가 변환하는 I/O virtual address |
| `dma_addr_t` | 장치에게 전달하는 DMA address를 담는 타입 |
| IOTLB | IOMMU 내부의 translation cache |
| SMMU | ARM SoC에서 사용하는 IOMMU 계열 |
| IOMMU fault | 장치의 잘못된 DMA 접근에 대한 변환/권한 오류 |
| Cache coherency | CPU cache와 장치 DMA 사이의 데이터 최신성 문제 |

## 실습 과제

가능한 Linux target board 또는 개발 PC에서 다음을 확인해 보세요.

```bash
dmesg | grep -i iommu
dmesg | grep -i smmu
find /sys/kernel/iommu_groups -maxdepth 2 -type l
cat /proc/iomem | head
```

정리 양식:

```text
Target:
Kernel version:
IOMMU/SMMU 관련 dmesg:
IOMMU group 존재 여부:
Camera/NPU/GPU 장치의 IOMMU 연결 추정:
궁금한 점:
```

---

# 다음 강의 예고

## 2강. Linux DMA API와 IOMMU 기본 흐름

다음 강의에서는 다음 내용을 코드 중심으로 학습합니다.

- `dma_map_single()`
- `dma_unmap_single()`
- `dma_alloc_coherent()`
- streaming DMA vs coherent DMA
- `dma_sync_single_for_cpu()` / `dma_sync_single_for_device()`
- `dma_addr_t`와 IOMMU mapping lifetime

---

# References

- Linux Kernel Documentation, Dynamic DMA mapping Guide: https://docs.kernel.org/core-api/dma-api-howto.html
- Linux Kernel Documentation, Dynamic DMA mapping using the generic device: https://docs.kernel.org/core-api/dma-api.html
- Arm, Memory Management Unit: IO Memory Handling: https://www.arm.com/products/silicon-ip-system/system-controllers/mmu
- Arm Developer, Arm System Memory Management Unit Architecture Specification: https://developer.arm.com/documentation/ihi0062/
