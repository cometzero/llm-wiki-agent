# 2강. Linux DMA API와 IOMMU 기본 흐름

> Linux Kernel Study - IOMMU / ARM SMMU Series  
> 목표: 장치 드라이버가 IOMMU를 직접 제어하지 않고 Linux DMA API를 통해 안전하게 DMA address를 얻고, map/unmap/sync lifecycle을 관리하는 방법을 이해한다.

---

## 0. 2강 학습 목표

이 강의가 끝나면 다음 질문에 답할 수 있어야 합니다.

1. `dma_addr_t`는 CPU pointer인가, device용 address인가?
2. `dma_map_single()`은 내부적으로 어떤 일을 하는가?
3. `DMA_TO_DEVICE`와 `DMA_FROM_DEVICE`는 누구 관점의 방향인가?
4. Streaming DMA mapping과 coherent DMA allocation은 무엇이 다른가?
5. `dma_map_sg()`의 반환값과 `nents`는 어떻게 다르게 사용해야 하는가?
6. DMA mask와 SWIOTLB는 왜 필요한가?
7. IOMMU가 켜진 시스템에서 DMA address는 왜 IOVA일 수 있는가?
8. Cache coherency 문제와 IOMMU translation 문제를 어떻게 구분하는가?
9. NPU/Camera driver에서 DMA API 사용 실수를 어떻게 찾을 수 있는가?

---

## 1. 1강 복습: CPU 주소와 Device 주소는 다를 수 있다

1강에서 핵심은 이것이었습니다.

```text
CPU가 사용하는 주소 != Device가 DMA에 사용하는 주소일 수 있다
```

주소를 다시 정리하면 다음과 같습니다.

| 주소 | 의미 | 주 사용 주체 |
|---|---|---|
| CPU Virtual Address, VA | kernel code가 pointer로 접근하는 주소 | CPU |
| Physical Address, PA | DRAM의 실제 물리주소 | MMU, memory subsystem |
| DMA Address / Bus Address | 장치에게 전달하는 주소 | DMA device |
| IOVA | IOMMU가 변환하는 장치용 virtual address | IOMMU, device |

Linux DMA API 문서도 kernel은 보통 virtual address를 사용하고, I/O device는 DMA를 위해 bus address를 사용한다고 설명합니다. 또한 IOMMU와 host bridge가 physical address와 bus address 사이의 임의 mapping을 만들 수 있다고 설명합니다.

핵심은 다음입니다.

```text
CPU pointer를 device register에 직접 넣으면 안 된다.
Device register에는 DMA API가 반환한 dma_addr_t를 넣어야 한다.
```

---

## 2. 왜 DMA API가 필요한가?

장치 드라이버가 직접 다음을 처리한다고 생각해 보겠습니다.

- 이 플랫폼에 IOMMU가 있는가?
- device가 32-bit DMA만 가능한가, 40-bit 또는 64-bit DMA가 가능한가?
- memory가 device DMA mask 안에 있는가?
- non-coherent DMA라서 cache clean/invalidate가 필요한가?
- physical memory가 scatter되어 있는가?
- IOMMU mapping을 언제 만들고 언제 지워야 하는가?
- SWIOTLB bounce buffer가 필요한가?

이 모든 것을 각 driver가 직접 처리하면 platform마다 코드가 달라지고 버그가 많아집니다. 그래서 Linux는 **DMA API**를 제공합니다.

Driver는 DMA API를 호출합니다.

```text
Device Driver
    |
    | dma_map_single(), dma_map_sg(), dma_alloc_coherent()
    v
Linux DMA Mapping Layer
    |
    | 필요하면 IOMMU/SWIOTLB/cache maintenance 처리
    v
Device가 사용할 dma_addr_t 반환
```

Driver의 기본 규칙은 다음입니다.

```text
physical address를 직접 장치에 주지 않는다.
DMA API가 반환한 dma_addr_t를 장치에 준다.
```

---

## 3. Linux 문서의 X / Y / Z 모델

Linux DMA API 문서의 설명을 단순화하면 다음과 같습니다.

```text
X = CPU virtual address
Y = physical address
Z = DMA address
```

```text
CPU code
  |
  | uses X = void *buffer
  v
CPU MMU translates X -> Y

Device
  |
  | uses Z = dma_addr_t
  v
IOMMU translates Z -> Y
```

예를 들어 driver가 다음을 호출합니다.

```c
dma_addr_t z;

z = dma_map_single(dev, x, size, DMA_TO_DEVICE);
```

여기서 `x`는 CPU가 접근하는 kernel virtual address입니다. DMA API는 필요한 경우 IOMMU mapping을 만들고, 장치에게 전달할 DMA address `z`를 반환합니다. 장치는 `z`로 DMA를 수행하고, IOMMU는 `z`를 실제 system RAM의 physical address `y`로 변환합니다.

---

## 4. `dma_addr_t` 제대로 이해하기

`dma_addr_t`는 장치에게 주는 주소입니다.

```c
#include <linux/dma-mapping.h>

void *cpu_buf;
dma_addr_t dma_handle;
```

구분은 다음과 같습니다.

```text
CPU가 접근하는 주소:       cpu_buf
Device가 접근하는 주소:    dma_handle
```

`dma_addr_t`에 대해 기억해야 할 점:

- CPU가 직접 dereference할 수 있는 pointer가 아닙니다.
- Device register에 넣는 DMA source/target address입니다.
- IOMMU가 켜져 있으면 `dma_addr_t`는 실제 PA가 아니라 IOVA일 수 있습니다.
- IOMMU가 없거나 identity mapping이면 PA처럼 보일 수 있지만, driver는 그 사실에 의존하면 안 됩니다.
- `virt_to_phys()` 결과를 device register에 직접 넣는 것은 일반적으로 잘못된 패턴입니다.

Linux DMA API 문서도 `dma_addr_t`는 platform에서 유효한 DMA address를 담을 수 있고, 장치에게 DMA source/target으로 줄 수 있지만 CPU가 직접 참조할 수는 없다고 설명합니다.

---

## 5. DMA API의 두 큰 종류

Linux driver에서 자주 쓰는 DMA API는 크게 두 종류로 나눌 수 있습니다.

| 구분 | Streaming DMA mapping | Coherent DMA allocation |
|---|---|---|
| 대표 API | `dma_map_single()`, `dma_map_sg()` | `dma_alloc_coherent()` |
| memory | 이미 존재하는 buffer를 DMA용으로 map | DMA 가능한 coherent memory를 새로 할당 |
| lifetime | DMA transfer 기간 동안만 유효 | 할당부터 free까지 지속 유효 |
| direction | `DMA_TO_DEVICE`, `DMA_FROM_DEVICE` 등 명시 | 암묵적으로 bidirectional 성격 |
| 주 용도 | frame/tensor/packet 같은 data buffer | descriptor ring, command queue, mailbox |
| 장점 | data path에 유연함 | CPU/device 지속 공유가 단순함 |
| 주의 | map/unmap/sync lifecycle 관리 필요 | 일부 platform에서 비용이 큼, 대용량에는 부적합할 수 있음 |

간단한 구분법:

```text
Data path buffer      -> streaming DMA부터 검토
Control/descriptor    -> coherent DMA부터 검토
```

---

## 6. Streaming DMA lifecycle

Streaming DMA mapping은 일정한 lifecycle을 가집니다.

```text
1. CPU buffer 준비
2. dma_map_*() 호출
3. 반환된 dma_addr_t를 device register에 입력
4. device가 DMA 수행
5. DMA completion 확인
6. dma_unmap_*() 호출
```

그림으로 보면 다음과 같습니다.

```text
CPU buffer
    |
    | dma_map_single()
    v
DMA address 획득
    |
    | register programming
    v
Device DMA
    |
    | IRQ/completion
    v
dma_unmap_single()
```

중요한 규칙:

```text
Every dma_map_{single,sg}() call should have its matching dma_unmap_{single,sg}() call.
```

Mapping은 DMA transfer에 필요한 동안만 유지하는 것이 기본입니다. Unmap 후에는 device가 해당 DMA address를 더 이상 사용하면 안 됩니다.

---

## 7. `dma_map_single()` 기본 패턴

### 7.1 Device가 memory를 읽는 경우: `DMA_TO_DEVICE`

예: NPU input tensor, NIC TX packet, GPU command buffer

```c
#include <linux/dma-mapping.h>

int submit_input(struct device *dev, void __iomem *regs,
                 void *cpu_buf, size_t len)
{
    dma_addr_t dma;

    /* CPU가 input data를 준비했다고 가정 */
    dma = dma_map_single(dev, cpu_buf, len, DMA_TO_DEVICE);
    if (dma_mapping_error(dev, dma))
        return -ENOMEM;

    /* device는 dma address를 읽는다 */
    writel(lower_32_bits(dma), regs + INPUT_ADDR_LO);
    writel(upper_32_bits(dma), regs + INPUT_ADDR_HI);
    writel(START, regs + CONTROL);

    wait_for_completion(...);

    dma_unmap_single(dev, dma, len, DMA_TO_DEVICE);
    return 0;
}
```

`DMA_TO_DEVICE`는 **device 관점에서 memory를 읽는 방향**입니다. CPU가 쓴 내용이 device에서 보이도록 준비되어야 합니다.

---

### 7.2 Device가 memory에 쓰는 경우: `DMA_FROM_DEVICE`

예: Camera frame capture, NIC RX packet, NPU output tensor

```c
int submit_output(struct device *dev, void __iomem *regs,
                  void *cpu_buf, size_t len)
{
    dma_addr_t dma;

    dma = dma_map_single(dev, cpu_buf, len, DMA_FROM_DEVICE);
    if (dma_mapping_error(dev, dma))
        return -ENOMEM;

    /* device는 dma address에 결과를 쓴다 */
    writel(lower_32_bits(dma), regs + OUTPUT_ADDR_LO);
    writel(upper_32_bits(dma), regs + OUTPUT_ADDR_HI);
    writel(START, regs + CONTROL);

    wait_for_completion(...);

    dma_unmap_single(dev, dma, len, DMA_FROM_DEVICE);

    /* 이제 CPU가 결과를 읽는다 */
    consume_output(cpu_buf);
    return 0;
}
```

`DMA_FROM_DEVICE`는 **device 관점에서 memory에 쓰는 방향**입니다. DMA 완료 전 CPU가 buffer를 읽으면 오래된 값이거나 cache에 남은 값일 수 있습니다.

---

## 8. DMA direction은 device 관점이다

DMA direction은 항상 **device 관점**으로 해석합니다.

| Direction | Device 동작 | 대표 예시 |
|---|---|---|
| `DMA_TO_DEVICE` | device가 memory를 읽음 | NPU input, NIC TX, GPU command |
| `DMA_FROM_DEVICE` | device가 memory에 씀 | Camera frame, NIC RX, NPU output |
| `DMA_BIDIRECTIONAL` | device가 읽고 쓰기 모두 가능 | shared work buffer |
| `DMA_NONE` | 유효한 transfer direction 아님 | debug/initialization 용도 |

헷갈릴 때는 이렇게 생각합니다.

```text
TO_DEVICE   = memory -> device
FROM_DEVICE = device -> memory
```

---

## 9. `dma_mapping_error()`는 반드시 확인한다

`dma_map_single()`은 실패할 수 있습니다.

실패 가능한 이유:

- device의 DMA mask로 해당 memory에 접근할 수 없음
- IOMMU IOVA space 부족
- IOMMU page table allocation 실패
- SWIOTLB bounce buffer 부족
- platform-specific DMA constraint 위반

따라서 다음 패턴을 사용해야 합니다.

```c
dma_addr_t dma;

dma = dma_map_single(dev, buf, size, DMA_TO_DEVICE);
if (dma_mapping_error(dev, dma)) {
    dev_err(dev, "DMA mapping failed\n");
    return -ENOMEM;
}
```

Mapping 실패를 무시하면 device에 잘못된 address를 넣게 되고, 결과는 silent data corruption 또는 IOMMU fault가 될 수 있습니다.

---

## 10. `dma_unmap_*()`와 lifetime

`dma_unmap_single()`은 DMA가 끝난 뒤 호출해야 합니다.

```c
/* completion interrupt 또는 job 완료 처리 경로 */
if (job_done) {
    dma_unmap_single(dev, job->dma, job->len, job->dir);
    job->dma = DMA_MAPPING_ERROR;
    complete(&job->done);
}
```

주의할 점:

- DMA completion 전에 unmap하면 device가 이미 해제된 IOVA를 계속 사용할 수 있습니다.
- Unmap 후 CPU buffer를 재사용하거나 free할 수 있습니다.
- Unmap을 빼먹으면 DMA address space leak이 생길 수 있습니다.
- Double unmap은 DMA API debug에서 잡히거나 더 나쁜 memory corruption을 만들 수 있습니다.

실전에서는 다음 조건을 명확히 해야 합니다.

```text
이 hardware job의 DMA가 정말 끝났다는 신호는 무엇인가?
```

예:

- IRQ status bit
- completion queue entry
- fence signal
- hardware idle bit
- timeout/error path cleanup

---

## 11. map 후 unmap 전 CPU와 device가 번갈아 접근할 때

한 번 map한 buffer를 unmap하지 않고 여러 번 device와 CPU가 번갈아 접근할 수 있습니다. 이때는 sync API가 필요합니다.

대표 API:

```c
dma_sync_single_for_cpu(dev, dma_handle, size, direction);
dma_sync_single_for_device(dev, dma_handle, size, direction);
```

사용 흐름:

```text
Device가 buffer 사용
    |
    | DMA 완료
    v
dma_sync_single_for_cpu()
    |
    | CPU가 buffer 읽기/수정
    v
dma_sync_single_for_device()
    |
    | Device가 다시 buffer 사용
    v
Device DMA
```

예시:

```c
dma = dma_map_single(dev, buf, len, DMA_BIDIRECTIONAL);
if (dma_mapping_error(dev, dma))
    return -ENOMEM;

/* device writes result */
start_device(dma);
wait_for_completion(...);

dma_sync_single_for_cpu(dev, dma, len, DMA_BIDIRECTIONAL);
parse_result(buf);

/* CPU modifies buffer and gives it back to device */
update_command(buf);
dma_sync_single_for_device(dev, dma, len, DMA_BIDIRECTIONAL);
start_device_again(dma);

wait_for_completion(...);
dma_unmap_single(dev, dma, len, DMA_BIDIRECTIONAL);
```

핵심:

```text
CPU가 볼 차례면 for_cpu
Device가 볼 차례면 for_device
```

---

## 12. Cache coherency와 IOMMU는 다른 문제다

IOMMU는 주로 다음을 담당합니다.

```text
DMA address/IOVA -> physical address 변환
장치별 접근 권한 검사
IOMMU fault 보고
IOTLB 관리
```

Cache coherency는 별도 문제입니다.

```text
CPU cache에 있는 최신 데이터와
DRAM/device가 보는 데이터가 일치하는가?
```

시스템이 hardware coherent이면 cache maintenance가 단순해질 수 있습니다. 하지만 non-coherent device라면 DMA API가 필요한 cache clean/invalidate를 수행하거나, driver가 sync API를 적절히 호출해야 합니다.

자주 생기는 오해:

```text
“IOMMU가 있으니 cache 문제도 해결되겠지”
```

틀렸습니다. IOMMU는 주소 변환/보호 장치이고, cache coherency는 별도의 하드웨어/소프트웨어 계약입니다.

---

## 13. Coherent DMA: `dma_alloc_coherent()`

Coherent DMA allocation은 CPU와 device가 지속적으로 공유하는 memory를 할당합니다.

```c
void *cpu_addr;
dma_addr_t dma_addr;

cpu_addr = dma_alloc_coherent(dev, size, &dma_addr, GFP_KERNEL);
if (!cpu_addr)
    return -ENOMEM;

/* CPU는 cpu_addr 사용 */
init_descriptor_ring(cpu_addr);

/* Device는 dma_addr 사용 */
writel(lower_32_bits(dma_addr), regs + RING_BASE_LO);
writel(upper_32_bits(dma_addr), regs + RING_BASE_HI);

...

dma_free_coherent(dev, size, cpu_addr, dma_addr);
```

반환값이 두 개라는 점이 중요합니다.

```text
cpu_addr = CPU가 접근하는 virtual address
dma_addr = device가 접근하는 DMA address
```

Coherent DMA가 적합한 경우:

- descriptor ring
- command queue
- completion queue
- mailbox/shared metadata
- small control structure

주의할 점:

- 일부 platform에서는 coherent memory가 비쌀 수 있습니다.
- 최소 allocation 단위가 page에 가까워 작은 buffer를 많이 만들면 낭비가 생길 수 있습니다.
- 대용량 frame/tensor buffer에 무조건 coherent를 쓰는 것은 좋은 전략이 아닐 수 있습니다.

---

## 14. Streaming DMA vs Coherent DMA 선택 기준

| Buffer 종류 | 권장 API | 이유 |
|---|---|---|
| NPU command descriptor ring | `dma_alloc_coherent()` | CPU/device가 자주 공유하는 작은 metadata |
| Camera frame buffer | `dma_map_sg()` 또는 DMA-BUF mapping | 크고 여러 장치가 공유할 가능성 |
| NPU input tensor | `dma_map_single()` 또는 `dma_map_sg()` | job 단위로 map/unmap 가능 |
| NPU output tensor | `dma_map_single()` 또는 `dma_map_sg()` | device write 완료 후 CPU/NPU consumer가 사용 |
| NIC TX/RX packet | `dma_map_single()` 또는 `dma_map_sg()` | packet lifetime이 명확함 |
| Firmware shared mailbox | `dma_alloc_coherent()` | CPU/firmware/device가 control data 공유 |

간단한 판단 기준:

```text
long-lived control structure -> coherent
job/packet/frame data buffer -> streaming
multi-device buffer sharing -> DMA-BUF + per-device DMA mapping
```

---

## 15. Scatter-Gather DMA: `dma_map_sg()`

큰 buffer는 physical memory에서 연속되어 있지 않을 수 있습니다.

```text
Physical memory:
[PA A]      [hole]      [PA B]          [PA C]
```

Scatter-gather list는 이런 흩어진 memory 조각들을 표현합니다.

```text
sg[0] -> PA A, len A
sg[1] -> PA B, len B
sg[2] -> PA C, len C
```

`dma_map_sg()`는 이 scatterlist를 device가 사용할 DMA segment로 mapping합니다.

```c
int mapped;

mapped = dma_map_sg(dev, sg, nents, DMA_TO_DEVICE);
if (mapped == 0)
    return -ENOMEM;

for_each_sg(sg, s, mapped, i) {
    dma_addr_t addr = sg_dma_address(s);
    unsigned int len = sg_dma_len(s);

    program_hw_segment(i, addr, len);
}

dma_unmap_sg(dev, sg, nents, DMA_TO_DEVICE);
```

중요한 규칙:

```text
dma_map_sg() 반환값 = 실제 mapping된 DMA segment 수
unmap에 넘기는 nents = 처음 dma_map_sg()에 넘긴 original nents
```

Linux DMA API 문서도 `dma_unmap_sg()`의 `nents` argument는 `dma_map_sg()`에 넘겼던 것과 같아야 하며, `dma_map_sg()`가 반환한 count를 넘기면 안 된다고 설명합니다.

---

## 16. DMA mask

모든 장치가 전체 physical memory 또는 전체 DMA address range를 볼 수 있는 것은 아닙니다.

예:

```text
Device A: 32-bit DMA만 가능 -> 0x0000_0000 ~ 0xffff_ffff
Device B: 40-bit DMA 가능
Device C: 64-bit DMA 가능
```

Driver는 probe 시점에 장치 capability에 맞게 DMA mask를 설정해야 합니다.

```c
if (dma_set_mask_and_coherent(dev, DMA_BIT_MASK(40))) {
    if (dma_set_mask_and_coherent(dev, DMA_BIT_MASK(32)))
        return -ENODEV;
}
```

DMA mask가 잘못되면 다음 문제가 생길 수 있습니다.

- 장치가 상위 address bit를 못 보고 address truncation 발생
- `dma_map_single()` 실패
- SWIOTLB bounce buffer 사용으로 성능 저하
- IOMMU mapping은 되었지만 device capability와 맞지 않아 DMA 실패

---

## 17. SWIOTLB란?

SWIOTLB는 Software I/O Translation Lookaside Buffer의 약자로, 흔히 **bounce buffer** mechanism으로 설명합니다.

상황 예:

```text
Device는 32-bit DMA만 가능
원래 buffer는 4GB 이상 physical memory에 있음
```

이때 device가 원래 buffer에 직접 접근할 수 없으므로, kernel은 device가 접근 가능한 낮은 memory에 bounce buffer를 만들고 복사를 수행할 수 있습니다.

```text
Original buffer <-> Bounce buffer <-> Device DMA
```

특징:

- IOMMU가 없거나 DMA mask 제약이 있을 때 fallback으로 사용될 수 있습니다.
- 복사가 개입하므로 성능 비용이 있습니다.
- DMA API를 사용하면 driver가 SWIOTLB 개입 여부를 직접 알 필요가 없습니다.
- 하지만 성능 분석 시 “왜 느린가?”의 원인이 될 수 있습니다.

---

## 18. IOMMU가 켜진 DMA path

IOMMU가 있는 시스템에서 streaming DMA mapping은 개념적으로 다음 계층을 지나갑니다.

```text
Driver
  |
  | dma_map_single()
  v
DMA Mapping API
  |
  | dev->dma_ops
  v
DMA-IOMMU layer
  |
  | IOVA allocation
  | IOVA -> PA mapping request
  v
IOMMU Core
  |
  | iommu_domain map
  v
Vendor IOMMU Driver
  |
  | page table entry update
  | IOTLB maintenance
  v
IOMMU Hardware
```

ARM SoC라면 vendor IOMMU driver는 보통 `arm-smmu` 또는 `arm-smmu-v3`입니다.

간단한 pseudo call flow:

```text
dma_map_single()
  -> dma_map_page_attrs()
    -> dev->dma_ops->map_page()
      -> iommu_dma_map_page()
        -> iommu_map_pages()
          -> arm_smmu_map_pages() 또는 arm_smmu_v3 map callback
```

정확한 함수명과 call path는 kernel version과 architecture에 따라 달라질 수 있습니다. 하지만 핵심 계층은 다음으로 이해하면 됩니다.

```text
DMA API -> DMA-IOMMU layer -> IOMMU Core -> ARM SMMU driver -> SMMU hardware
```

---

## 19. IOVA allocation과 IOMMU page table

IOMMU가 켜져 있으면 DMA API는 device에게 줄 IOVA range를 할당하고, 그 IOVA가 실제 physical page를 가리키도록 mapping을 만듭니다.

예:

```text
Physical pages:
PA 0x8800_0000
PA 0x8A10_0000
PA 0x8C20_0000

Device view:
IOVA 0x1000_0000
IOVA 0x1000_1000
IOVA 0x1000_2000

IOMMU mapping:
IOVA 0x1000_0000 -> PA 0x8800_0000
IOVA 0x1000_1000 -> PA 0x8A10_0000
IOVA 0x1000_2000 -> PA 0x8C20_0000
```

장치 입장에서는 연속 address처럼 보이지만, 실제 physical page는 흩어져 있을 수 있습니다. 이것이 IOMMU의 큰 장점 중 하나입니다.

---

## 20. IOTLB와 성능

IOMMU도 주소 변환 결과를 cache합니다. 이를 보통 IOTLB라고 부릅니다.

```text
IOTLB = I/O address translation cache
```

Mapping을 만들거나 지울 때는 다음 비용이 생길 수 있습니다.

- IOVA allocation/free
- IOMMU page table update
- IOTLB invalidate/sync
- cache maintenance
- SWIOTLB copy, 해당 시

성능 관점에서 주의할 패턴:

```text
작은 buffer를 매우 높은 빈도로 map/unmap
매 frame마다 많은 SG segment를 새로 mapping
DMA-BUF attach/detach를 반복
IOTLB miss가 많은 access pattern
```

개선 방향:

- buffer pool 사용
- long-lived mapping 검토
- batching
- SG segment 수 감소
- larger page mapping 가능성 검토
- DMA-BUF 재사용

단, mapping을 오래 유지하면 lifetime/ownership/security 관리가 더 중요해집니다.

---

## 21. Mini Case: NPU input/output buffer

NPU job 하나를 생각해 보겠습니다.

```text
CPU prepares input tensor
NPU reads input tensor
NPU writes output tensor
CPU reads output tensor
```

Direction은 다음처럼 다릅니다.

```text
input tensor:  CPU -> NPU  => DMA_TO_DEVICE
output tensor: NPU -> CPU  => DMA_FROM_DEVICE
```

Pseudo code:

```c
input_dma = dma_map_single(dev, input, in_len, DMA_TO_DEVICE);
if (dma_mapping_error(dev, input_dma))
    return -ENOMEM;

output_dma = dma_map_single(dev, output, out_len, DMA_FROM_DEVICE);
if (dma_mapping_error(dev, output_dma)) {
    dma_unmap_single(dev, input_dma, in_len, DMA_TO_DEVICE);
    return -ENOMEM;
}

program_npu_input(input_dma, in_len);
program_npu_output(output_dma, out_len);
start_npu();

wait_for_completion(...);

dma_unmap_single(dev, output_dma, out_len, DMA_FROM_DEVICE);
dma_unmap_single(dev, input_dma, in_len, DMA_TO_DEVICE);

consume_output(output);
```

주의할 점:

- input과 output의 direction을 혼동하지 않습니다.
- 두 번째 mapping 실패 시 첫 번째 mapping을 cleanup해야 합니다.
- DMA completion 전에 unmap하지 않습니다.
- output을 CPU가 읽기 전에 unmap 또는 sync가 필요합니다.

---

## 22. Mini Case: Camera frame capture

Camera/CSI/ISP pipeline은 보통 device가 frame buffer에 DMA write를 수행합니다.

```text
Camera / CSI / ISP
    |
    | DMA write
    v
Frame Buffer
```

Camera capture buffer는 `DMA_FROM_DEVICE` 성격입니다.

이후 frame buffer가 NPU input으로 사용되면, NPU 관점에서는 device가 memory를 읽는 것이므로 `DMA_TO_DEVICE` 성격이 됩니다.

```text
Camera writes frame     -> DMA_FROM_DEVICE from Camera device perspective
NPU reads frame         -> DMA_TO_DEVICE from NPU device perspective
Display reads frame     -> DMA_TO_DEVICE-like device read perspective
```

같은 physical buffer라도 각 device마다 DMA mapping과 IOVA가 다를 수 있습니다.

```text
Camera IOVA  -> same physical pages
NPU IOVA     -> same physical pages
Display IOVA -> same physical pages
```

이 부분은 9강의 Camera -> NPU DMA-BUF pipeline에서 더 자세히 다룹니다.

---

## 23. 자주 하는 실수

### 실수 1. `virt_to_phys()`를 사용해서 device register에 넣음

잘못된 패턴:

```c
phys_addr_t pa = virt_to_phys(buf);
writel(pa, regs + DMA_ADDR);
```

문제:

- IOMMU mapping을 우회합니다.
- DMA mask를 무시합니다.
- cache maintenance를 놓칠 수 있습니다.
- 일부 memory는 physical address를 얻더라도 DMA 가능하지 않을 수 있습니다.

올바른 패턴:

```c
dma_addr_t dma = dma_map_single(dev, buf, len, DMA_TO_DEVICE);
if (dma_mapping_error(dev, dma))
    return -ENOMEM;

writel(dma, regs + DMA_ADDR);
```

---

### 실수 2. Mapping 실패를 무시

잘못된 패턴:

```c
dma = dma_map_single(dev, buf, len, DMA_TO_DEVICE);
writel(dma, regs + DMA_ADDR);
```

올바른 패턴:

```c
dma = dma_map_single(dev, buf, len, DMA_TO_DEVICE);
if (dma_mapping_error(dev, dma))
    return -ENOMEM;
```

---

### 실수 3. `dma_map_sg()` 반환값과 `nents` 혼동

잘못된 패턴:

```c
mapped = dma_map_sg(dev, sg, nents, dir);
...
dma_unmap_sg(dev, sg, mapped, dir);  /* wrong */
```

올바른 패턴:

```c
mapped = dma_map_sg(dev, sg, nents, dir);
...
dma_unmap_sg(dev, sg, nents, dir);   /* correct */
```

---

### 실수 4. DMA 완료 전에 unmap

잘못된 흐름:

```text
start device
unmap immediately
later device still uses DMA address
```

이는 use-after-unmap DMA bug입니다.

---

### 실수 5. Direction을 CPU 관점으로 해석

잘못된 해석:

```text
CPU가 device로 data를 보낸다 -> FROM_DEVICE?
```

올바른 해석:

```text
Device가 memory를 읽는다 -> DMA_TO_DEVICE
Device가 memory에 쓴다 -> DMA_FROM_DEVICE
```

---

## 24. DMA API debugging

DMA API 사용 오류를 찾기 위해 kernel에는 DMA API debugging facility가 있습니다.

Kernel config:

```text
CONFIG_DMA_API_DEBUG
```

Debugfs 예:

```bash
mount -t debugfs none /sys/kernel/debug

ls /sys/kernel/debug/dma-api/
cat /sys/kernel/debug/dma-api/error_count
cat /sys/kernel/debug/dma-api/dump

dmesg | grep -i "DMA-API"
```

확인 가능한 문제 예:

- map/unmap mismatch
- double unmap
- wrong direction
- sync API misuse
- invalid DMA memory 사용

주의:

```text
DMA API debug는 성능 영향이 있으므로 production kernel에서는 신중하게 사용한다.
```

Linux DMA API 문서도 DMA API checking code를 kernel config로 켤 수 있으며, 성능 영향이 있으므로 production kernel에서는 사용하지 말라고 설명합니다. 또한 debugfs의 `dma-api/` directory에서 error count와 current DMA mappings 등을 확인할 수 있다고 설명합니다.

---

## 25. Driver 작성 체크리스트

NPU/Camera/ISP/VPU driver를 리뷰할 때 다음을 확인합니다.

### Probe 단계

- [ ] `struct device *dev`가 올바른 device인가?
- [ ] `dma_set_mask_and_coherent()`를 장치 capability에 맞게 호출했는가?
- [ ] device tree 또는 ACPI에서 IOMMU/coherent 속성이 올바른가?

### Mapping 단계

- [ ] CPU pointer를 직접 device register에 넣지 않는가?
- [ ] `dma_map_single()` 또는 `dma_map_sg()` 반환값을 확인하는가?
- [ ] `dma_mapping_error()`를 호출하는가?
- [ ] 실패 경로에서 이미 mapping된 buffer를 cleanup하는가?

### Transfer 단계

- [ ] DMA direction이 device 관점으로 맞는가?
- [ ] hardware가 실제로 DMA 완료했음을 확인하는가?
- [ ] timeout/error path에서도 unmap이 수행되는가?

### Sync 단계

- [ ] CPU와 device가 map/unmap 사이에 번갈아 접근하는가?
- [ ] 그렇다면 `dma_sync_*_for_cpu()`와 `dma_sync_*_for_device()`가 있는가?

### SG 단계

- [ ] `dma_map_sg()` 반환값과 original `nents`를 구분하는가?
- [ ] hardware segment limit을 초과하지 않는가?
- [ ] SG merge 가능성에 대응하는가?

### Debug 단계

- [ ] DMA-API warning이 없는가?
- [ ] IOMMU fault log와 DMA mapping lifecycle을 함께 확인했는가?

---

## 26. Kernel Source Reading Map

2강에서 보면 좋은 kernel source 위치입니다.

```text
include/linux/dma-mapping.h
    DMA API declarations and wrappers

kernel/dma/
    generic DMA mapping implementation

drivers/iommu/dma-iommu.c
    DMA API와 IOMMU domain을 연결하는 계층

drivers/iommu/iommu.c
    IOMMU core: domain/group/device handling

include/linux/iommu.h
    IOMMU core structures and APIs
```

읽는 순서 추천:

1. `include/linux/dma-mapping.h`에서 API 이름을 익힙니다.
2. `kernel/dma/` 아래에서 generic DMA mapping 흐름을 봅니다.
3. `drivers/iommu/dma-iommu.c`에서 IOVA allocation과 IOMMU mapping으로 연결되는 부분을 봅니다.
4. 3강에서 `include/linux/iommu.h`, `drivers/iommu/iommu.c`를 본격적으로 읽습니다.

---

## 27. 실습 과제

### 과제 1. Kernel log 확인

```bash
dmesg | grep -i DMA-API
dmesg | grep -i iommu
dmesg | grep -i smmu
```

확인할 것:

- DMA API warning이 있는가?
- IOMMU/SMMU가 enable되어 있는가?
- fault log가 있는가?

### 과제 2. Driver code에서 DMA direction 해석

```bash
grep -R "dma_map_single" drivers/ -n | head
```

3개 예제를 골라 다음을 정리합니다.

| Driver | API | Direction | Device 동작 | Unmap 위치 |
|---|---|---|---|---|
| 예: npu | `dma_map_single` | `DMA_TO_DEVICE` | input read | job complete |

### 과제 3. `dma_map_sg()` 패턴 확인

```bash
grep -R "dma_map_sg" drivers/ -n | head
```

확인할 것:

- 반환값을 어떤 변수에 저장하는가?
- hardware에 programming하는 loop는 반환값 기준인가?
- unmap에는 original `nents`를 넘기는가?

### 과제 4. NPU pseudo driver 작성

다음 흐름을 pseudo code로 작성합니다.

```text
input tensor map: DMA_TO_DEVICE
output tensor map: DMA_FROM_DEVICE
NPU start
IRQ completion
output unmap
input unmap
```

실패 경로도 포함합니다.

---

## 28. 퀴즈

### Q1. `dma_addr_t`는 CPU가 직접 dereference할 수 있는 pointer인가?

A. 그렇다  
B. 아니다

### Q2. `DMA_TO_DEVICE`는 누구 관점의 방향인가?

A. CPU 관점  
B. Device 관점

### Q3. `dma_map_single()` 호출 후 반드시 확인해야 하는 것은?

A. `dma_mapping_error()`  
B. `virt_to_phys()`  
C. `ioremap()`  
D. `kmalloc()`

### Q4. `dma_map_sg(dev, sg, nents=5, dir)`가 3을 반환했다. `dma_unmap_sg()`에는 몇 개를 넘겨야 하는가?

A. 3  
B. 5

### Q5. `dma_alloc_coherent()`가 가장 적합한 buffer는?

A. NPU command descriptor ring  
B. 4K video frame 전체  
C. 큰 tensor weight 전체  
D. 파일 시스템 page cache

### Q6. Device가 DMA로 memory에 결과를 쓴 뒤 CPU가 그 결과를 읽으려 한다. map을 유지하는 상황에서 CPU 접근 전 호출할 sync API는?

A. `dma_sync_single_for_device()`  
B. `dma_sync_single_for_cpu()`

### Q7. DMA mask가 너무 작게 설정되면 어떤 문제가 생길 수 있는가?

A. 장치가 접근할 수 없는 DMA address가 반환될 수 있다.  
B. mapping failure 또는 bounce buffer 사용이 발생할 수 있다.  
C. address truncation 문제가 생길 수 있다.  
D. 위 모두 가능하다.

### Q8. SWIOTLB는 무엇을 위해 사용될 수 있는가?

A. 장치가 접근할 수 없는 memory를 bounce buffer를 통해 접근 가능하게 하기 위해  
B. CPU scheduler를 빠르게 하기 위해  
C. page cache를 압축하기 위해  
D. interrupt latency를 줄이기 위해

### Q9. `dma_unmap_single()` 이후 device가 같은 DMA address를 계속 사용하면 어떤 종류의 버그인가?

A. 정상 동작  
B. use-after-unmap DMA bug  
C. CPU page fault  
D. syscall error

### Q10. IOMMU가 있으면 cache coherency 문제가 자동으로 해결되는가?

A. 그렇다  
B. 아니다

---

## 29. 정답 및 해설

### A1. B

`dma_addr_t`는 CPU pointer가 아닙니다. Device가 DMA source/target으로 사용하는 주소입니다.

### A2. B

DMA direction은 device 관점입니다. `DMA_TO_DEVICE`는 device가 memory를 읽는 경우입니다.

### A3. A

`dma_map_single()`은 실패할 수 있으므로 `dma_mapping_error()`로 확인해야 합니다.

### A4. B

`dma_map_sg()` 반환값 3은 hardware에 programming할 mapped segment 수입니다. `dma_unmap_sg()`에는 처음 넘긴 original `nents`, 즉 5를 넘겨야 합니다.

### A5. A

Descriptor ring, command queue, completion queue 같은 control structure는 CPU/device가 지속 공유하므로 coherent DMA가 적합합니다. 대용량 data buffer에는 streaming DMA 또는 DMA-BUF 기반 mapping을 먼저 검토합니다.

### A6. B

Device가 쓴 내용을 CPU가 읽기 전에는 `dma_sync_single_for_cpu()`가 필요합니다. 단, unmap으로 동기화가 완료되는 usage라면 별도 sync 없이 unmap 후 CPU가 읽는 패턴도 가능합니다.

### A7. D

DMA mask가 장치 capability와 맞지 않으면 mapping failure, SWIOTLB 사용, address truncation 등의 문제가 생길 수 있습니다.

### A8. A

SWIOTLB는 device가 직접 접근할 수 없는 memory를 bounce buffer를 통해 접근 가능하게 하는 fallback으로 사용될 수 있습니다.

### A9. B

Unmap 이후의 DMA address는 더 이상 유효하지 않습니다. Device가 계속 사용하면 use-after-unmap DMA bug입니다.

### A10. B

IOMMU는 주소 변환과 접근 보호를 담당합니다. Cache coherency는 별도 문제입니다.

---

## 30. 5분 복습 카드

### 카드 1. `dma_addr_t`

```text
장치에게 전달하는 DMA address.
CPU가 직접 dereference하지 않는다.
```

### 카드 2. Streaming DMA

```text
map -> device DMA -> completion -> unmap
```

### 카드 3. Coherent DMA

```text
CPU와 device가 지속적으로 공유하는 DMA-capable memory.
Descriptor/control path에 적합.
```

### 카드 4. DMA direction

```text
항상 device 관점.
TO_DEVICE   = device가 memory를 읽음
FROM_DEVICE = device가 memory에 씀
```

### 카드 5. `dma_map_sg()`

```text
반환값 = mapped DMA segment 수
unmap nents = original nents
```

### 카드 6. IOMMU path

```text
DMA API -> DMA-IOMMU layer -> IOMMU Core -> ARM SMMU driver -> SMMU hardware
```

### 카드 7. Cache coherency

```text
IOMMU translation과 cache visibility는 별도 문제.
non-coherent 환경에서는 sync API가 중요.
```

---

## 31. 한 장 요약

```text
Driver는 CPU pointer를 device에 주지 않는다.
Driver는 DMA API를 호출한다.
DMA API는 platform에 맞는 DMA address를 반환한다.
IOMMU가 있으면 그 DMA address는 IOVA일 수 있다.
Device는 dma_addr_t로 DMA를 수행한다.
IOMMU는 IOVA를 physical address로 변환한다.
DMA가 끝나면 driver는 unmap한다.
CPU/device가 번갈아 접근하면 sync한다.
```

핵심 공식:

```text
CPU uses:     void *cpu_buf
Device uses:  dma_addr_t dma
IOMMU maps:   dma_addr_t/IOVA -> physical address
```

---

## 32. 다음 강의 예고

3강에서는 Linux IOMMU Framework 내부를 다룹니다.

핵심 주제:

- `struct iommu_domain`
- `struct iommu_group`
- `struct iommu_ops`
- default DMA domain
- identity domain / DMA domain / unmanaged domain
- VFIO/IOMMUFD와 IOMMU group
- IOMMU fault와 domain attach 흐름

2강 질문:

```text
DMA API가 IOVA mapping을 만든다.
```

3강 질문:

```text
그 mapping은 어느 domain에 만들어지고,
장치는 어떤 group/domain에 attach되는가?
```

---

## 33. 참고 자료

1. Linux Kernel Documentation - Dynamic DMA mapping Guide  
   https://docs.kernel.org/core-api/dma-api-howto.html

2. Linux Kernel Documentation - Dynamic DMA mapping using the generic device  
   https://docs.kernel.org/core-api/dma-api.html

3. Linux Kernel source reading targets  
   - `include/linux/dma-mapping.h`
   - `kernel/dma/`
   - `drivers/iommu/dma-iommu.c`
   - `drivers/iommu/iommu.c`
   - `include/linux/iommu.h`
