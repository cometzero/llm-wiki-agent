​

## 📌 Zephyr 기반 VIRTIO 백엔드를 Xen에서 구현하는 목적은 무엇인가?
Xen에서 Zephyr 기반 VIRTIO 백엔드를 구현하여 <mark>오픈 소스 기능 안전성을 달성</mark>하고, 자동차 등 복잡한 시스템의 통합 및 효율화를 목표로 합니다.


## 💡 이러한 구현이 가져올 수 있는 이점은 무엇인가?

- 기능 안전성 인증 가능성 향상
- 시스템 비용 및 리소스 감소 (메모리, SoC)
- 개발 시간 단축 및 단일 장애 지점 제거

고성능 컴퓨팅(HPC)의 트렌드가 자동차 산업까지 확산되면서 **Zephyr RTOS와 Xen 하이퍼바이저를 결합**하여 차량용 전자제어장치(ECU)를 통합하는 **기능 안전(Functional Safety) 시스템** 구현 방안을 깊이 있게 다룹니다. 이 콘텐츠는 **VIRTIO 백엔드**를 초경량 Zephyr로 대체하여 소스 코드 라인 수를 획기적으로 줄임으로써, 까다로운 기능 안전 인증 비용을 절감하고 자동차 시스템의 복잡도를 낮출 수 있는 **혁신적인 아키텍처 제안**을 구체적으로 제시합니다. 기존 리눅스 기반의 복잡한 시스템 대신 **혼합 중요도 시스템(Mixed-Critical Systems)**을 효율적으로 구축하고 싶은 개발자들에게 실질적인 설계 방향과 극복해야 할 하드웨어적 난제들을 명확히 알려줍니다.
## 1. Zephyr, Xen, VIRTIO 개요 및 자동차 산업 동향 


### 1.1. Zephyr RTOS, Xen 하이퍼바이저, VIRTIO 소개 
![image](https://resource-release.s3.ap-northeast-2.amazonaws.com/thumbnails/FeB8F3zNpkg/43.jpg)
1. **Zephyr RTOS (Real-Time Operating System)** 소개 
  1. 오픈소스이며 실시간 운영체제이다.
  2. 최소 2KB 메모리부터 작동하는 <mark>초경량(lightweight) 운영체제</mark>이다.
  3. Bluetooth, IPV4/V6 및 MOD for FACOM 등을 지원한다.

2. **Xen 하이퍼바이저** 소개 
  1. 2003년에 출시되었으며 초기에는 독점적인 리더십을 가졌었다.
  2. 이후 KVM 등이 보급되면서, Xen은 기능 안전(Functional Safety)을 염두에 두고 지속적으로 개발되어 왔다.

3. **VIRTIO (Virtual I/O Device)** 소개 
  1. 기능 안전 사양인 <mark>OB 사양</mark>에 강력하게 전념하고 있으며, Oasis 조직에서 2014년에 첫 번째 에디션이 발행되었다.
  2. 이는 스토리지 버퍼와 사용 가능 버퍼(Available Buffers)를 사용하는 AC 전송 아키텍처를 이용하여 가상 장치를 구현한다.
  3. VIRTIO의 작동 방식:
  1. 두 개의 버퍼(사용 가능 버퍼, 사용된 버퍼)를 사용한다.
  2. 프론트 가상 머신(Front VM)이 사용 가능 버퍼에 데이터를 넣는다.
  3. 이후 처리 과정에서 해당 데이터를 사용된 버퍼에 다시 넣는다.


### 1.2. 자동차 시스템의 복잡도 증가 및 통합 트렌드 
![image](https://resource-release.s3.ap-northeast-2.amazonaws.com/thumbnails/FeB8F3zNpkg/352.jpg)
1. **자동차 전자 제어 장치(ECU) 현황** 
  1. 자동차에는 <mark>100개 이상의 ECU</mark>가 내장되어 있으며, 다양한 기능들이 통합되어 있다.
  2. 차량은 엄격한 안전 요구사항을 가지므로, ISO 26262 등 기능 안전 인증을 필수적으로 요구한다.

2. **통합 디자인으로의 전환 필요성** 
  1. 기존의 매우 비싼 시스템의 개수를 줄이기 위해 단일 시스템으로 통합하려는 트렌드가 강해지고 있다.
  2. **전통적인 설계 (도메인 아키텍처)**는 각 기능마다 자체 컨트롤러를 갖는 형태였다. 
  3. **새로운 통합 설계**는 강력한 컴퓨팅 자원을 가진 단일 ECU로 제어를 통합하고, 게이트웨이를 통해 엔드 장치에 명령을 전송하는 방식이다. 
  1. 이는 뇌와 신경의 관계에 비유된다.
  4. 이러한 기술 중 하나로 주목받는 것이 <mark>안드로이드(Android)</mark>를 QNX와 결합하여 자유롭고 독립된 환경에서 시스템을 실행하는 방식이다. 
  5. AGL(Automotive Grade Linux) 역시 시스템을 결합하고 있으며, 현재 성능 인증으로의 마이그레이션을 고려 중이다. 


## 2. Zephyr 기반 VIRTIO 백엔드 아키텍처 제안 및 장점 


### 2.1. Zephyr 활용 및 VIRTIO 백엔드 대체 제안 
![image](https://resource-release.s3.ap-northeast-2.amazonaws.com/thumbnails/FeB8F3zNpkg/630.jpg)
1. **Zephyr 활용 분야 제안** 
  1. 현재 Zephyr는 기능 안전 인증이 <em>불가능</em>하지만, 하이퍼바이저 뒤에서 실행되는 <mark>VIRTIO 백엔드 영역</mark>에서는 유용할 수 있다고 제안한다.
  2. 발표자는 AGL 프로젝트의 일환으로 이 기능에 대한 Pull Request(PR)를 제출했다. 

2. **기존 Xen 기반 AGL 시스템 구성 (비교 대상)** 
  1. AGL 프로젝트는 Yocto AGL과 HMI(Human-Machine Interface) 등을 구현한다.
  2. Xen 기반 시스템은 Relaxation 기반 위에 Android와 AGL이 실행되며, Zephyr가 존재한다.
  3. 이 시스템에서 **Dom0 (제어 역할 VM)**이 드라이버 기능을 담당한다.
  4. Dom0은 DomD(Device Driver Domain)와 함께 작동하며, 디바이스 드라이버와 같은 상위 계층은 가상 머신(VMs)이 처리하도록 설계되어 있다.

3. **Zephyr 기반 VIRTIO 백엔드 아키텍처 (제안)** 
  1. 기존에는 드라이버 기능이 **리눅스(Linux)**에 의존했지만, 드라이버 레지스터에만 접근하는 역할이므로 반드시 리눅스일 필요는 없다고 판단한다. 
  2. 따라서, 매우 크고 복잡한 시스템인 리눅스를 <mark>Zephyr로 대체</mark>할 수 있다고 제안한다. 
  3. 이 대체가 성공적으로 이루어질 경우 기능 안전 인증을 달성할 수 있으며, 시스템의 메모리 사용량과 복잡도가 감소하는 이점을 얻는다. 


### 2.2. 소스 코드 라인 수 감소를 통한 기능 안전 인증 비용 절감 효과 
![image](https://resource-release.s3.ap-northeast-2.amazonaws.com/thumbnails/FeB8F3zNpkg/840.jpg)
1. **시스템 통합의 이점** 
  1. 리소스 감소: 시스템 메모리와 비용이 줄어든다.
  2. 다중 VM 분할 허용: 시스템을 여러 VM으로 분할할 수 있게 된다.
  3. 개발자 시간 절약: 분할을 위한 개발 시간이 절약된다.
  4. **고장 지점 분리**: 분할이 가능해지면 다른 부분에 장애가 발생해도 영향을 받지 않는 고장 지점 분리가 가능하다.
  - 예시: 네트워크에 문제가 발생해도 GPU 드라이버에는 영향을 주지 않는다.

2. **소스 코드 라인(LoC) 감소의 중요성** 
  1. 소스 코드 라인 수(SLOC, Source Lines Of Code)를 **획기적으로 줄일** 수 있다.
  2. 이는 인증 비용 절감으로 이어진다.
  3. 라인 수가 줄어들면 <mark>재인증 비용(rebut cost)이 절감</mark>되고, 인증 범위 내로 들어오게 된다.

3. **기존 연구와의 연관성** 
  1. 이 아이디어는 발표자가 처음 제시한 것이 아니며, Zephyr 개발팀(특히 Cambridge 팀의 Braham과 그의 형제)이 논문에서 **드라이버 격리(drive by isolation)**와 다중 도메인으로의 위임(delegation to multiple brains)을 언급했다.
  2. 이 개념은 20년 전부터 존재했으나 대중화되지 못했다.
  3. Zephyr는 단일 바이너리, 작은 소스 코드, 다수의 드라이버 지원 덕분에 이 개념을 실현할 가능성이 있다.


## 3. 구현 현황 및 하드웨어적 난관 


### 3.1. VIRTIO 백엔드 구현 및 현재 상태 
![image](https://resource-release.s3.ap-northeast-2.amazonaws.com/thumbnails/FeB8F3zNpkg/993.jpg)
1. **VIRTIO 작동 방식 수정 및 구현** 
  1. Xen을 사용하여 가상 머신을 실행한다.
  2. VIRTIO 인프라(Virtio inf machine)는 특정 게스트 VM 간의 <mark>메모리 공유</mark>로 이해되지만, 이를 명확히 수정하여 사용한다.
  3. VIRTIO 디바이스는 일반적으로 Xen 하이퍼콜(hypercall) 함수를 사용하여 메모리 접근을 수행한다.
  4. 발표자의 PR(91605)에는 하드웨어 추상화 계층(HAL)이 포함되어 있는데, 이는 리눅스 설계에서 영감을 받아 Vring 라이브러리를 호출하고, VIRTIO 버퍼를 처리하는 방식을 단순화했다.

2. **구현의 초기 단계와 향후 계획** 
  1. 현재는 <mark>단지 첫 단계를 밟았을 뿐</mark>이며, GPU 장치 업데이트를 포함한 PR은 아직 갈 길이 멀다.
  2. 하지만 단순 기능(simple functionality)은 이미 구현되었다.
  3. VIRTIO 백엔드의 Vring 구조와 같은 부분이 구현되었다.
  4. 향후 QEMU/KVM과 같은 <mark>다른 하이퍼바이저</mark>도 지원하는 것을 고려하고 있으며, 공유 메모리와 MMU(Memory Management Unit) 지원이 필요하다.


### 3.2. 혼합 중요도 시스템 구현의 하드웨어적 난제 
![image](https://resource-release.s3.ap-northeast-2.amazonaws.com/thumbnails/FeB8F3zNpkg/1245.jpg)
1. **페이지 경계를 고려한 주변 장치 위임** 
  1. PR 개발은 혼합 중요도 시스템(Mixed-Critical Systems)을 실현하는 데 아직 부족하다.
  2. 주변 장치(peripherals)를 위임할 때는 <mark>페이지 경계(page boundary)</mark>를 염두에 두어야 한다.
  3. 드라이버 구조는 보안 기능과 관련된 여러 드라이버에 의해 사용되며, 이는 부팅 시퀀스 제어에서 가장 명확하게 드러난다.

2. **SOC 설계 의존성 및 레지스터 분리 문제** 
  1. SOC(System on Chip) 설계에 따라 어려움이 발생할 수 있다.
  2. 메모리를 페이징 단위(paging units)로 VM에 할당하기 때문에 <mark>레지스터 구성</mark>이 증가하는 경우가 발생한다. 
  3. 주변 장치 시작 주소가 0x60500인 경우, 이 레지스터 구성은 작동 문제를 야기할 수 있으며, GPU I/O가 PSO(Peripheral Space Offset) 중간에 분할되어 여러 VM으로 나뉘는 현상이 나타난다. 
  4. **핀 제어(pin control) 및 클럭 제어(clock control)** 기능은 분리하기 매우 어렵다. 
  1. 이는 여러 드라이버가 하나의 변수를 조작하는 구조 때문이다.
  2. 예시: 하나의 PWM(Pulse Width Modulation) 장치에서 핀 제어 드라이버와 클럭 드라이버의 제어 비트가 도메인별로 분리하기 어렵다.
  3. 이러한 난관으로 인해 기능을 분리하기가 매우 어렵고, 아직 해결책을 찾지 못했다.

3. **보안 기능의 통합 복잡성** 
  1. 최근 보안 기능은 단일 **하드웨어 보안 모듈(HSM)**에 통합되고 있다.
  2. 이는 ARM의 <mark>TrustZones</mark> 및 일부 독점적인 바이너리를 사용하는 복잡한 구성을 포함하며, 이 복잡한 시퀀스가 문제 해결을 어렵게 한다.


### 3.3. 향후 발전 가능성이 있는 기술적 과제와 전망 
![image](https://resource-release.s3.ap-northeast-2.amazonaws.com/thumbnails/FeB8F3zNpkg/1571.jpg)
1. **디바이스 트리(Device Tree) 구성 문제** 
  1. 디바이스 조각(device fragment)을 DTE(Device Tree Entry)로 구성하여 리눅스 부팅 시 주입하는 방식이 존재한다.
  2. 이 방식은 바이너리 내에 정적으로 컴파일된 정보를 전달하지 않기 때문에 잘 작동하지 않으며, <mark>정보를 주입하여 전달할 필요</mark>가 있다.

2. **가상화 인터럽트 제어(GICv3)** 
  1. GICv3(Generic Interrupt Controller version 3)는 이미 시장에 출시되어 있다.
  2. 이 기능은 VM에 인터럽트를 주입하는 능력을 가지고 있어 인터럽트 집중적인 부분의 **성능을 극적으로 향상시킬 잠재력**이 있다.
  3. 현재는 일부 서버 프로세서에만 해당 기능이 있지만, 미래에는 자동차 애플리케이션에 적용될 가능성이 높다.
  4. VM 이탈(VM exit) 및 VM 진입(VM entry)을 통한 인터럽트 처리가 매우 무거운 프로세스이므로, GICv3는 성능 향상에 도움이 된다.
  5. 장기적으로는 Xen과 같은 하이퍼바이저에 영향을 미쳐 VM 간 IPC(Inter-Process Communication)에 사용될 가능성도 있다.

3. **HPC 기반 기술과의 접목** 
  1. HPC(고성능 컴퓨팅)와 유사한 기술(예: DPDK 기반)을 적용할 가능성이 있다.
  2. DPDK는 일반적으로 고성능 NIC(네트워크 인터페이스 컨트롤러)를 사용하여 네트워크 처리 시 인터럽트를 우회하고 매우 낮은 지연 시간으로 네트워크 처리를 수행한다.
  3. 향후 Top 500에 사용되는 프로세서처럼 무거운 AI 처리가 차량에 현실화될 경우, 이러한 기술이 더욱 필요해질 것이다.

4. **결론 및 향후 과제** 
  1. SDP(Software Defined Platform)를 실현하기 위해서는 Zephyr를 사용한 구현이 필수적이다.
  2. 다중 도메인 개념은 개발 초기부터 존재했지만, 아직 해야 할 일이 많이 남아 있다.
  3. 특히 현재는 **VM 설계 문제**가 해결해야 할 주요 과제이다.


### 3.4. 질의 응답 (메모리 공유 및 시간 함수) 
![image](https://resource-release.s3.ap-northeast-2.amazonaws.com/thumbnails/FeB8F3zNpkg/1863.jpg)
1. **메모리 공유 관련 질문** 
  1. VIRTIO의 버퍼 시스템은 처리 속도에 좋은지 질문이 나왔다.
  2. 발표자는 VIRTIO가 <mark>메모리 공유</mark>에 초점을 맞추고 있다고 답변하며, 메모리 공유 방식의 효율성을 확인했다.

