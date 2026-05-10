# QEMU 에뮬레이터 내부 구조: TCG, 메모리, 디바이스 모델링 및 디버깅

## Table of Contents

- 1. 개요
- 1.1 서론
- 1.2 전체 구조
- 2. QEMU의 기본 원리 및 핵심 구성 요소
- 2.1. QEMU 소개 및 에뮬레이션 모드
- 2.2. TCG(Tiny Code Generator)와 KVM의 역할
- 2.3. TCG의 변환 과정 및 코드 캐시
- 3. TCG 번역기의 심층 분석
- 3.1. TCG 캐시 관리 및 스택 처리
- 3.2. TCG 번역기의 프런트엔드와 백엔드
- 3.3. TCG의 최적화: 체이닝(Chaining)
- 4. QEMU 에뮬레이터의 디코딩 과정
- 4.1. 프런트엔드 디코딩의 구성 요소
- 4.2. 명령어 패턴(Instruction Pattern) 정의
- 4.3. 명령어 패턴의 세부 정의
- 5. QEMU 에뮬레이터의 프런트엔드 및 백엔드 디코딩 구현
- 5.1. 프런트엔드 디코딩 구현: LUI 명령어 예시
- 5.2. 백엔드 디코딩 구현: 마이크로 연산을 호스트 코드로 변환
- 6. QEMU 시스템 에뮬레이션 및 소스 코드 구조
- 6.1. QEMU 시스템 빌드 및 실행 환경 설정
- 6.2. QEMU 소스 코드의 주요 디렉토리
- 7. QEMU의 장치 모델링: 객체 모델 및 타입 시스템
- 7.1. 장치 모델링의 기본 개념
- 7.2. QEMU 객체 모델(Object Model)
- 7.3. 인스턴스 관련 속성 및 상속 구조
- 8. QEMU 장치 모델링: 클래스 계층 및 인터페이스
- 8.1. 객체 및 클래스 계층 구조
- 8.2. 인터페이스 클래스(InterfaceClass)
- 8.3. PCI 장치 모델링 예시
- 9. QEMU 장치 모델링: 장치 생성 및 초기화
- 9.1. 장치 인스턴스 생성 흐름
- 9.2. 장치 초기화 및 등록
- 10. QEMU PCI 장치 생성 및 사용자 공간 상호작용
- 10.1. PCI 장치 구조 및 TypeInfo 정의
- 10.2. PCI 장치 에뮬레이션 및 동적 캐스팅
- 10.3. PCI 장치 실행 및 사용자 공간 상호작용
- 11. QEMU 하드웨어 머신 에뮬레이션
- 11.1. 하드웨어 머신 등록 및 초기화
- 11.2. 머신 생성 및 장치 초기화
- 12. QEMU의 메모리 관리 시스템
- 12.1. 메모리 에뮬레이션 및 SoftMMU
- 12.2. 메모리 구조체 및 백엔드
- 12.3. 주소 공간 및 가상 주소 변환
- 12.4. RAMBlock의 다양한 유형
- 13. QEMU 및 리눅스 커널 디버깅
- 13.1. QEMU 프로세스 디버깅
- 13.2. 게스트 리눅스 커널 디버깅

## Content

## 1. 개요

### 1.1 서론

QEMU는 다양한 하드웨어를 에뮬레이션하여 다른 아키텍처의 코드를 실행할 수 있게 하는 강력한 가상화 도구이다. 이 보고서는 QEMU의 내부 동작 방식, 특히 동적 바이너리 변환(DBT)과 장치 모델링에 대해 자세히 설명한다. QEMU의 작동 원리를 이해하는 것은 가상화 기술의 핵심을 파악하는 데 매우 중요하다.

### 1.2 전체 구조

QEMU 소개 및 기본 원리

핵심 구성 요소: TCG 번역기

장치 모델링 및 시스템 에뮬레이션

메모리 관리 및 가상 주소 변환

QEMU 및 리눅스 커널 디버깅

## 2. QEMU의 기본 원리 및 핵심 구성 요소 [A]

QEMU는 동적 바이너리 변환(DBT)을 통해 게스트 코드를 호스트 시스템에서 실행하며, TCG(Tiny Code Generator)가 이 변환을 담당한다.

### 2.1. QEMU 소개 및 에뮬레이션 모드 [A]

QEMU의 역할 [A]

QEMU는 다양한 하드웨어를 에뮬레이션하는 가상 머신으로, KVM과 함께 작동하여 에뮬레이션만 수행하거나 전체 시스템을 에뮬레이션할 수 있다. [A]

예를 들어, ARM 기반의 라즈베리 파이(Raspberry Pi)나 오렌지 파이(Orange Pi)와 같은 시스템을 x86 호스트 머신에서 실행할 수 있다. [A]

동적 바이너리 변환(DBT) [A]

QEMU는 동적 바이너리 변환(Dynamic Binary Translation)이라는 개념을 사용하여 특정 아키텍처(예: ARM)용으로 작성된 코드를 호스트 아키텍처(예: x86)가 실행할 수 있는 코드로 변환한다. [A]

이 변환은 런타임(실행 중)에 발생한다. [A]

변환될 코드를 '게스트(Guest)'라고 부르며, 코드가 실행될 하드웨어를 '호스트(Host)'라고 부른다. [A]

QEMU의 에뮬레이션 모드 [A]

전체 시스템 에뮬레이션(Full System Emulation): CPU, 장치, BIOS 등 시스템 전체를 모방하여 QEMU가 모든 요소를 처리한다. [A]

예를 들어, ARM 기반 시스템을 x86 머신에서 실행할 때 QEMU가 전체 시스템을 에뮬레이션한다. [A]

사용자 모드 에뮬레이션(User Mode Emulation): 특정 애플리케이션 하나만 에뮬레이션한다. [A]

예를 들어, ARM용으로 컴파일된 애플리케이션을 x86 머신에서 실행할 때 QEMU가 해당 애플리케이션을 호스트 프로세스 내에서 변환하여 실행한다. [A]

### 2.2. TCG(Tiny Code Generator)와 KVM의 역할 [A]

TCG의 기능 [A]

QEMU에서 동적 바이너리 변환을 수행하는 핵심 구성 요소는 TCG(Tiny Code Generator)이다. [A]

TCG는 런타임에 게스트 코드를 호스트 코드로 변환하는 JIT(Just-In-Time) 컴파일러와 유사하게 작동한다. [A]

예를 들어, PowerPC 타겟 코드를 x86 호스트 코드로 변환할 때 TCG를 거쳐 변환된다. [A]

KVM의 역할 [A]

호스트와 게스트 아키텍처가 동일한 경우, 코드 변환이 필요 없으므로 KVM(Kernel-based Virtual Machine)이 사용된다. [A]

KVM은 가상 CPU(vCPU)를 빠르게 생성하고 게스트 코드를 하드웨어에서 직접 실행하여 QEMU보다 훨씬 빠르다. [A]

KVM 코드는 리눅스 커널 내부에서 실행되므로 사용자 공간에서 실행되는 QEMU보다 빠르다. [A]

KVM과 Xen과 같은 기술은 QEMU의 '가속기(Accelerator)' 역할을 한다. [A]

QEMU는 KVM을 통해 가상화된 환경에서 게스트 코드를 직접 실행할 수 있도록 지원한다. [A]

### 2.3. TCG의 변환 과정 및 코드 캐시 [A]

변환 과정 [A]

1단계: 중간 코드 생성 [A]

게스트 코드를 '변환 블록(Translation Block, TB)'이라는 작은 단위로 나눈다. [A]

각 변환 블록은 '중간 코드(Intermediate Code)' 또는 '중간 연산(Intermediate Operation)'으로 변환된다. [A]

2단계: 호스트 코드 생성 [A]

중간 코드를 호스트 시스템에서 실행 가능한 '호스트 코드(Host Code)'로 변환한다. [A]

코드 캐시(Code Cache) [A]

QEMU는 변환된 변환 블록을 '코드 캐시(Code Cache)'라는 메모리 영역에 저장한다. [A]

이는 동일한 코드가 다시 실행될 때 재변환을 피하고 성능을 향상시키기 위함이다. [A]

캐시가 가득 차면 QEMU는 캐시를 비우거나, LRU(Least Recently Used) 메커니즘을 사용하여 오래된 블록을 제거하고 새 블록을 저장한다. [A]

## 3. TCG 번역기의 심층 분석 [B]

TCG 번역기는 게스트 코드를 호스트 코드로 변환하는 과정에서 프롤로그/에필로그 처리, 프런트엔드/백엔드 분리, 마이크로 연산 및 헬퍼 함수를 활용한다.

### 3.1. TCG 캐시 관리 및 스택 처리 [B]

캐시된 TB 실행 [B]

TCG는 캐시에 저장된 변환 블록(TB)을 반복적으로 검색하고 실행한다. [B]

S_under_section이라는 함수는 캐시에서 TB를 찾아 실행하는 역할을 한다. [B]

게스트 코드의 스택 처리 [B]

변환된 게스트 코드는 QEMU 호스트 프로세스 내에서 실행되지만, 호스트의 스택과는 별개로 처리된다. [B]

게스트 코드를 실행하기 전후에 '프롤로그(Prologue)'와 '에필로그(Epilogue)'라는 특별한 코드를 추가한다. [B]

프롤로그: 스택 프레임 포인터를 저장하고 새로운 스택 프레임을 생성하여 지역 변수 공간을 확보한다. [B]

에필로그: 스택 포인터와 스택 프레임 포인터를 원래 값으로 복원한다. [B]

이는 일반적인 함수 호출에서 컴파일러가 어셈블리 코드를 생성할 때 스택을 관리하는 방식과 유사하다. [B]

### 3.2. TCG 번역기의 프런트엔드와 백엔드 [B]

번역기 구조 [B]

TCG 번역기는 두 부분으로 나뉜다. [B]

프런트엔드(Front-end): 게스트 코드를 TCG 중간 코드(TCG Operation)로 변환한다. [B]

백엔드(Back-end): TCG 중간 코드를 호스트 시스템에서 실행 가능한 호스트 코드로 변환한다. [B]

프런트엔드 구성 요소 [B]

마이크로 연산(Micro-operations): 게스트의 복잡한 연산을 더 작은 내부 연산으로 분해한다. [B]

예를 들어, add와 같은 연산은 여러 개의 마이크로 연산으로 분해될 수 있다. [B]

가상 레지스터(Virtual Registers): 게스트 레지스터를 표현하기 위해 QEMU 내부에서 사용하는 가상 레지스터(예: R5)이다. [B]

이는 게스트의 실제 레지스터와는 다르며, 내부적으로 레지스터를 관리하는 데 사용된다. [B]

헬퍼 함수(Helper Functions): 복잡한 게스트 명령어를 처리하기 위해 QEMU 내부에 정의된 보조 함수이다. [B]

예를 들어, Q_add와 같이 특정 범위 내에서 덧셈을 수행하는 복잡한 명령어 처리에 사용된다. [B]

프런트엔드 개발의 복잡성 [B]

새로운 하드웨어 아키텍처를 지원하려면 프런트엔드 작업이 더 많다. [B]

새로운 타겟의 명령어 세트를 정의하고, 이를 마이크로 연산으로 변환하는 코드를 작성하며, 필요한 헬퍼 함수를 개발해야 한다. [B]

### 3.3. TCG의 최적화: 체이닝(Chaining) [B]

스위칭 오버헤드 문제 [B]

각 변환 블록(TB)을 실행할 때마다 프롤로그와 에필로그를 호출하고 CPU 함수로 돌아가는 과정은 많은 시간을 소모한다. [B]

체이닝의 도입 [B]

TCG는 여러 변환 블록을 연결(Chaining)하여 프롤로그와 에필로그 호출 횟수를 줄인다. [B]

이를 통해 여러 TB를 한 번의 프롤로그/에필로그 호출로 연속적으로 실행하여 성능을 향상시킨다. [B]

체이닝 동작 방식 [B]

QEMU는 먼저 캐시에서 TB를 찾는다. [B]

TB가 캐시되어 있으면 실행하고, 예외가 발생하면 QEMU 호스트 프로세스에서 처리한다. [B]

TB가 캐시되어 있지 않으면 게스트 코드를 호스트 코드로 변환하고, 이 TB를 기존 TB 체인에 연결한 후 실행한다. [B]

이 과정은 예외 처리 후 다시 반복된다. [B]

## 4. QEMU 에뮬레이터의 디코딩 과정 [D]

QEMU 에뮬레이터는 프런트엔드에서 게스트 명령어를 마이크로 연산으로 변환하고, 백엔드에서 이를 호스트 코드로 변환한다.

### 4.1. 프런트엔드 디코딩의 구성 요소 [C]

프런트엔드 역할 [C]

게스트 코드를 중간 코드(Intermediate Code) 또는 내부 표현(Internal Notation)으로 변환하는 역할을 한다. [C]

주요 구성 요소 [C]

마이크로 연산(Micro-operations): 게스트의 큰 연산을 작은 내부 연산으로 분해한다. [C]

가상 레지스터(Virtual Registers): 게스트 레지스터를 표현하는 QEMU 내부의 가상 레지스터이다. [C]

헬퍼 함수(Helper Functions): 복잡한 게스트 명령어를 처리하는 보조 함수이다. [C]

백엔드 디코딩 역할 [C]

중간 코드를 호스트 시스템의 명령어(Host Code Instruction)로 변환한다. [C]

### 4.2. 명령어 패턴(Instruction Pattern) 정의 [C]

타겟 명령어 세트 이해 [C]

게스트 명령어를 마이크로 연산으로 변환하려면 먼저 타겟 아키텍처(예: ARM)의 명령어 세트(Instruction Set Architecture, ISA)를 알아야 한다. [C]

QEMU는 i386.decode와 같은 파일을 통해 명령어 패턴을 정의한다. [C]

디코딩 스크립트 [C]

decode.py 스크립트는 정의된 명령어 패턴을 파싱하여 디코딩 함수를 생성한다. [C]

이 함수들은 decode-i386.c와 같은 파일에 포함되어 컴파일된다. [C]

디스어셈블 컨텍스트(Disassemble Context) [C]

명령어와 함께 Disassemble Context라는 구조체가 전달된다. [C]

이 구조체는 타겟 아키텍처의 주소 모드, 디스어셈블러, 권한 레벨 등 다양한 정보를 포함한다. [C]

또한 현재 CPU 상태에 대한 일반적인 정보도 포함한다. [C]

translate.c 파일의 역할 [C]

각 타겟 아키텍처(예: ARM)의 translate.c 파일에는 디코딩된 명령어를 마이크로 연산으로 변환하는 함수들이 구현되어 있다. [C]

이 함수들은 게스트 코드를 파싱하고, 적절한 마이크로 연산으로 변환하여 중간 코드를 생성한다. [C]

### 4.3. 명령어 패턴의 세부 정의 [D]

AST(Abstract Syntax Tree) 활용 [D]

QEMU는 명령어 패턴 파일을 AST로 변환하여 다양한 명령어를 파싱하고 매칭한다. [D]

명령어 패턴 구성 요소 [D]

명령어 이름, Opcode, 필드(Field), 인자(Argument, Arg), 포맷(Format) 등으로 구성된다. [D]

필드(Field) 정의 [D]

%.S16과 같이 %로 시작하며, 명령어에서 특정 비트 범위를 추출하는 방법을 정의한다. [D]

예를 들어, %.S16은 0번째 비트부터 16비트를 추출하고 이를 부호 있는 값으로 처리한다. [D]

여러 비트 필드를 조합하여 하나의 값을 구성할 수도 있다. [D]

expand_sham_8과 같은 헬퍼 함수를 사용하여 필드 값을 확장할 수 있다. [D]

인자(Arg) 정의 [D]

@로 시작하며, 명령어의 인자를 정의한다. [D]

예를 들어, @U_R_D는 IMM과 RD라는 두 인자를 가진다. [D]

이 인자들은 최종적으로 C 구조체로 변환된다. [D]

포맷(Format) 정의 [D]

Z로 시작하며, 명령어의 비트 레이아웃을 정의한다. [D]

.은 정의되지 않은 비트를 나타내며, 이 비트들은 필드나 명령어 패턴 자체에서 정의될 수 있다. [D]

포맷 정의는 인자(Arg)와 필드(Field)를 사용하여 비트 그룹에 값을 할당한다. [D]

명령어 패턴의 최종 구성 [D]

명령어 패턴은 Opcode와 포맷을 결합하여 최종적인 명령어 구조를 정의한다. [D]

정의되지 않은 비트들은 명령어 패턴 자체의 Opcode 값으로 채워진다. [D]

## 5. QEMU 에뮬레이터의 프런트엔드 및 백엔드 디코딩 구현 [E]

QEMU 에뮬레이터는 프런트엔드에서 게스트 명령어를 마이크로 연산으로 변환하고, 백엔드에서 이를 호스트 코드로 변환한다.

### 5.1. 프런트엔드 디코딩 구현: LUI 명령어 예시 [E]

LUI 명령어의 역할 [E]

LUI(Load Upper Immediate) 명령어는 20비트의 즉시 값(Immediate Value)을 레지스터의 상위 20비트에 로드하고, 나머지 12비트는 0으로 채운다. [E]

예를 들어, 32비트 레지스터에 20비트 값을 로드하면 나머지 12비트는 0이 된다. [E]

QEMU의 LUI 처리 [E]

QEMU는 게스트 코드에서 LUI 명령어를 디코딩할 때, 이미 20비트 값을 추출하여 버퍼에 저장하고 나머지 12비트는 0으로 채운다. [E]

translate_LUI 함수는 gen_op_mov_i 함수를 호출하고, 이 함수는 tcg_gen_mov_i32 함수를 호출하여 32비트 mov 마이크로 연산을 생성한다. [E]

마이크로 연산 생성 [E]

tcg_gen_op_i2 함수는 연산 유형, 마이크로 연산 유형, 20비트 즉시 값(나머지 0), 그리고 RD 레지스터(QEMU의 가상 레지스터)를 인자로 받아 마이크로 연산을 생성한다. [E]

RD 레지스터는 게스트의 실제 레지스터에 해당하는 QEMU의 가상 레지스터이다. [E]

따라서 LUI 명령어는 최종적으로 mov 마이크로 연산으로 변환된다. [E]

### 5.2. 백엔드 디코딩 구현: 마이크로 연산을 호스트 코드로 변환 [E]

백엔드의 역할 [E]

프런트엔드에서 생성된 중간 마이크로 연산을 호스트 시스템의 실제 코드로 변환한다. [E]

또한 내부 가상 레지스터(예: ARDI)를 호스트 시스템의 실제 레지스터로 변환한다. [E]

예를 들어, 호스트 머신이 ARM인 경우, ARM 아키텍처에 맞는 코드로 변환한다. [E]

tcg_target_op_defs 함수 [E]

이 함수는 TCG 중간 코드를 받아 호스트 코드로 변환하는 역할을 한다. [E]

TCG_G_MOV와 같은 마이크로 연산 유형을 확인하고, 해당 유형에 맞는 tcg_gen_op_mov와 같은 함수를 호출한다. [E]

이 함수는 다시 tcg_out_mov_reg와 같은 하드웨어 관련 함수를 호출하여 실제 ARM Opcode(예: 0xE1A00000)를 생성한다. [E]

명령어 구성 및 출력 [E]

tcg_out_op 함수는 Opcode와 같은 정보를 사용하여 실제 호스트 명령어(예: ARM mov 명령어)를 구성한다. [E]

구성된 명령어는 tcg_out32 함수를 통해 코드 포인터(Code Pointer)가 가리키는 변환 블록(Translation Block)에 기록된다. [E]

코드 포인터는 다음 명령어를 기록할 위치로 이동하여 연속적인 명령어 생성을 가능하게 한다. [E]

## 6. QEMU 시스템 에뮬레이션 및 소스 코드 구조 [F]

QEMU는 다양한 소스 코드 디렉토리를 통해 하드웨어 에뮬레이션, 장치 모델링, 메모리 관리 등을 구현하며, 이를 통해 전체 시스템을 에뮬레이션한다.

### 6.1. QEMU 시스템 빌드 및 실행 환경 설정 [F]

목표 [F]

x86 호스트에서 x86 게스트 리눅스 커널을 실행하는 QEMU 프로세스를 생성한다. [F]

호스트와 타겟이 동일하므로 KVM 가속기를 사용한다. [F]

필수 구성 요소 빌드 [F]

QEMU 소스 코드: QEMU를 빌드한다. [F]

리눅스 소스 코드: 리눅스 커널을 빌드한다. [F]

BusyBox: 초기 루트 파일 시스템(Initial RootFS)인 ramfs를 생성하기 위해 BusyBox를 빌드한다. [F]

BusyBox는 cp, echo 등과 같은 기본적인 유틸리티를 포함한다. [F]

RAMFS 생성: BusyBox를 사용하여 ramfs.img 파일을 생성한다. [F]

리눅스 커널 빌드: KVM 게스트 구성을 포함하여 리눅스 커널을 빌드한다. [F]

QEMU 빌드 및 실행 [F]

QEMU 소스 코드를 빌드한다. [F]

QEMU를 실행할 때 qemu-system-x86_64 명령어를 사용하며, 빌드된 리눅스 커널 이미지(bzImage), ramfs.img, 그리고 KVM 가속기 활성화 옵션(-enable-kvm)을 전달한다. [F]

이 명령어를 통해 리눅스 게스트가 QEMU 인스턴스 내에서 실행된다. [F]

여러 QEMU 인스턴스를 동시에 실행하여 여러 게스트를 에뮬레이션할 수 있다. [F]

ls pci 명령어를 통해 게스트 리눅스 시스템 내에서 PCI 장치를 확인할 수 있다. [F]

### 6.2. QEMU 소스 코드의 주요 디렉토리 [F]

hw (Hardware) [F]

CPU, 버스(Bus), 전원(Power), 부팅 장치(Boot Device) 등 다양한 하드웨어 에뮬레이션 코드를 포함한다. [F]

qdev.c 파일은 장치 모델링 코드와 관련이 있다. [F]

target [F]

게스트 코드를 호스트 코드로 변환하는 TCG 관련 코드(디코딩 및 변환)를 포함한다. [F]

monitor [F]

QEMU 인스턴스 실행 중에 드라이브 추가, 스냅샷 생성 등 런타임 작업을 관리하는 코드를 포함한다. [F]

QMP(QEMU Machine Protocol)는 JSON 기반 프로토콜로, libvirt와 같은 외부 도구가 QEMU와 통신하는 데 사용된다. [F]

qom (QEMU Object Model) [F]

QEMU의 객체 모델 코드를 포함하며, 장치 모델링의 기반이 된다. [F]

펌웨어, 객체 클래스 등 객체 모델의 세부 사항을 정의한다. [F]

vl.c (Main Interpreter) [F]

QEMU의 메인 인터프리터 코드를 포함하며, 초기화 및 특정 하드웨어 머신 시작을 담당한다. [F]

memory [F]

가상 메모리 관리 및 게스트 가상 주소를 호스트 물리 주소로 변환하는 코드를 포함한다. [F]

host-memory.c는 VM에 할당되는 호스트 메모리를 관리하고 생성한다. [F]

util/main-loop.c [F]

QEMU의 메인 이벤트 루프를 관리하는 파일로, QEMU 아키텍처는 이벤트 기반으로 동작한다. [F]

## 7. QEMU의 장치 모델링: 객체 모델 및 타입 시스템 [H]

QEMU는 객체 모델을 기반으로 장치를 모델링하며, TypeInfo와 TypeImpl 구조체를 통해 장치 클래스와 인스턴스를 정의하고 관리한다.

### 7.1. 장치 모델링의 기본 개념 [G]

장치 및 버스 에뮬레이션 [G]

QEMU는 다양한 장치(PCI, USB, DRAM 등)와 버스를 에뮬레이션하여 CPU가 이들과 통신할 수 있도록 한다. [G]

QEMU는 Device Model 구현을 통해 장치를 정의하고 시스템에 등록한다. [G]

TypeInfo 구조체 및 등록 [G]

새로운 장치를 생성하려면 TypeInfo 구조체를 정의하고 type_register 함수를 통해 시스템에 등록한다. [G]

TypeInfo는 장치의 이름(name)과 부모(parent) 타입을 포함한다. [G]

예를 들어, PCI 장치를 등록할 때 type_init 함수를 호출하고, 이 함수 내에서 TypeInfo를 구성한 후 type_register를 호출한다. [G]

TypeImpl 구조체 및 해시 테이블 [G]

type_register 함수는 내부적으로 type_register_internal을 호출하여 TypeImpl이라는 내부 구조체를 생성한다. [G]

TypeImpl은 TypeInfo에 대응하는 동적 구조체로, 런타임에 발생하는 다양한 연산 데이터를 저장한다. [G]

이 TypeImpl은 type_table이라는 해시 테이블에 이름(name)을 키로 하여 저장된다. [G]

모듈 초기화 [G]

type_init 함수는 __attribute__((constructor)) 매크로를 사용하여 QEMU의 main 함수가 실행되기 전에 호출된다. [G]

이를 통해 모든 장치 타입이 main 함수 시작 전에 시스템에 등록된다. [G]

module_init 함수는 module_load_init을 호출하여 등록된 모든 type_init 함수를 순회하며 실행한다. [G]

### 7.2. QEMU 객체 모델(Object Model) [H]

객체 모델의 목적 [H]

QEMU는 TypeInfo와 TypeImpl을 통해 새로운 장치(타입)를 생성할 때, 기존 클래스의 인스턴스를 생성하거나 새로운 클래스와 인스턴스를 동시에 생성할 수 있도록 한다. [H]

이는 일반적인 객체 지향 프로그래밍과 달리 클래스와 인스턴스 생성을 동시에 처리할 수 있는 유연성을 제공한다. [H]

클래스 관련 속성 [H]

class_size: 클래스에 할당될 메모리 크기를 정의한다. [H]

class_size가 0이면 새로운 클래스를 생성하는 대신 기존 클래스의 인스턴스를 생성하려는 의도로 해석된다. [H]

class_init: 타입이 초기화될 때 호출되는 함수이다. [H]

이 함수는 클래스 멤버와 유사한 properties를 생성하는 데 사용된다. [H]

class_data: 클래스 초기화 함수에 전달될 데이터를 정의한다. [H]

interfaces: 클래스가 상속받을 인터페이스 목록을 정의한다. [H]

이를 통해 다중 상속과 유사한 기능을 구현할 수 있다. [H]

### 7.3. 인스턴스 관련 속성 및 상속 구조 [H]

인스턴스 관련 속성 [H]

instance_size: 객체(인스턴스)에 할당될 메모리 크기를 정의한다. [H]

QEMU에서는 클래스 크기와 인스턴스 크기가 다를 수 있다. [H]

예를 들어, PCI 장치의 class_size는 PCIDeviceClass의 크기이고, instance_size는 PCIDevice의 크기이다. [H]

인스턴스는 장치 자체를 나타내며, 클래스는 공통 속성을 정의한다. [H]

instance_init: 인스턴스가 생성될 때 호출되는 함수이다. [H]

instance_exit: 인스턴스가 소멸될 때 호출되는 함수이다. [H]

객체 모델의 상속 구조 [H]

ObjectClass: 모든 클래스의 기본 클래스(Base Class)이다. [H]

Object: 모든 인스턴스의 기본 객체이다. [H]

C 프로그래밍에서 상속은 구조체 내부에 다른 구조체를 포함하는 방식으로 구현된다. [H]

예를 들어, DeviceClass는 ObjectClass를 포함하고, DeviceState는 Object를 포함한다. [H]

TypeImpl의 추가 속성 [H]

properties: class_init 함수에서 생성된 클래스 속성들을 ObjectProperty 구조체로 저장한다. [H]

interfaces: TypeInfo에서 정의된 인터페이스 이름들을 TypeImpl에 저장한다. [H]

각 인터페이스 이름은 InterfaceClass 구조체와 연결되어, ObjectClass를 통해 클래스가 상속받는 인터페이스를 정의한다. [H]

## 8. QEMU 장치 모델링: 클래스 계층 및 인터페이스 [I]

QEMU의 장치 모델은 ObjectClass와 Object를 기반으로 클래스 계층을 구축하며, InterfaceClass를 통해 다중 상속과 유사한 기능을 제공한다.

### 8.1. 객체 및 클래스 계층 구조 [I]

TypeImpl의 포인터 [I]

TypeImpl 구조체는 class 포인터를 통해 해당 타입의 ObjectClass를 가리킨다. [I]

interfaces 포인터는 GSList를 가리키며, 이 리스트는 클래스가 상속받는 InterfaceClass들을 포함한다. [I]

Object 및 ObjectClass 구조체 [I]

Object 구조체는 ObjectClass를 가리키는 포인터를 포함하며, TypeImpl을 통해 해당 객체의 타입을 알 수 있다. [I]

ObjectClass는 TypeImpl을 가리키는 포인터와 base 포인터(부모 클래스)를 포함한다. [I]

ObjectClass는 모든 클래스의 기본 클래스이며, Object는 모든 인스턴스의 기본 객체이다. [I]

예시: DeviceClass는 ObjectClass를 포함하고, DeviceState는 Object를 포함한다. [I]

여러 Object가 하나의 ObjectClass를 가리킬 수 있어 다중 인스턴스를 표현한다. [I]

### 8.2. 인터페이스 클래스(InterfaceClass) [I]

InterfaceClass 생성 [I]

InterfaceClass는 TypeInfo를 정의하고 type_register 함수를 통해 생성된다. [I]

TypeInfo는 name과 parent 타입(예: TYPE_INTERFACE)을 가지지만, instance_size와 같은 인스턴스 관련 속성은 정의하지 않는다. [I]

이는 인터페이스가 인스턴스를 가지지 않고, 오직 클래스만 존재하기 때문이다. [I]

InterfaceClass의 내부 구조 [I]

QEMU는 TypeInfo에 대응하는 TypeImpl을 생성하고, 이 TypeImpl에 InterfaceClass 구조체를 연결한다. [I]

InterfaceClass는 ObjectClass를 포함하는데, 이는 모든 클래스가 ObjectClass로부터 상속받아야 하기 때문이다. [I]

ObjectProperty와 같은 속성들은 class_init 함수에서 생성될 수 있다. [I]

### 8.3. PCI 장치 모델링 예시 [I]

PCI 장치 클래스 및 상태 구조체 [I]

PCIDeviceClass 구조체는 DeviceClass를 포함하고, DeviceClass는 ObjectClass를 포함한다. [I]

PCIDevice 구조체(인스턴스)는 DeviceState를 포함하고, DeviceState는 Object를 포함한다. [I]

이러한 계층 구조는 C 언어에서 구조체 내부에 다른 구조체를 첫 번째 멤버로 포함하는 방식으로 구현된다. [I]

Casting을 통한 접근 [I]

이 구조 덕분에 PCIDeviceClass 포인터를 DeviceClass나 ObjectClass 포인터로 캐스팅하여 상위 구조체에 접근할 수 있다. [I]

이는 객체 모델의 유연성을 제공한다. [I]

PCI TypeInfo 정의 [I]

PCIDevice의 TypeInfo는 name으로 TYPE_PCI_DEVICE를, parent로 TYPE_DEVICE를 가진다. [I]

instance_size는 sizeof(PCIDevice)이고, class_init 함수는 pci_device_class_init이다. [I]

pci_device_class_init 함수는 object_class_property_add를 사용하여 PCI 장치에 특화된 속성(예: vendor_id, device_id)을 추가한다. [I]

## 9. QEMU 장치 모델링: 장치 생성 및 초기화 [J]

QEMU는 object_new 함수를 통해 장치 인스턴스를 생성하고, type_initialize 함수를 통해 클래스를 초기화하며, qdev_realize 함수를 통해 장치를 시스템에 등록한다.

### 9.1. 장치 인스턴스 생성 흐름 [J]

module_load_init 호출 [J]

QEMU 시작 시 module_load_init 함수가 호출된다. [J]

이 함수는 시스템에 등록된 모든 TypeInfo에 대해 object_new 함수를 호출한다. [J]

object_new 함수 [J]

object_new는 주어진 name을 기반으로 TypeImpl을 찾아 object_new_with_type 함수를 호출한다. [J]

object_new_with_type은 실제 인스턴스(객체)를 생성하기 전에 두 가지 주요 작업을 수행한다. [J]

type_initialize 함수를 호출하여 해당 타입의 클래스를 초기화한다. [J]

object_instance_init 함수를 호출하여 인스턴스를 생성한다. [J]

type_initialize 함수 [J]

이 함수는 클래스가 이미 초기화되었는지 확인하고, 그렇지 않으면 클래스에 필요한 메모리를 할당한다. [J]

할당된 메모리는 TypeImpl의 class_pointer에 저장되며, 이는 ObjectClass를 가리킨다. [J]

type_initialize는 재귀적으로 부모 클래스부터 최상위 Object 클래스까지 초기화를 진행한다. [J]

예를 들어, PCIDeviceClass의 type_initialize는 DeviceClass의 type_initialize를 호출하고, DeviceClass는 ObjectClass의 type_initialize를 호출한다. [J]

각 클래스의 class_init 함수가 호출되어 속성 설정 및 초기화 작업을 수행한다. [J]

### 9.2. 장치 초기화 및 등록 [J]

object_instance_init 함수 [J]

이 함수는 instance_size만큼 메모리를 할당하여 실제 장치 인스턴스(객체)를 생성한다. [J]

생성된 객체는 ObjectClass와 TypeImpl에 연결된다. [J]

object_class_property_add를 통해 클래스 속성들이 객체에 추가된다. [J]

object_instance_init는 재귀적으로 부모 객체부터 최상위 Object까지 초기화를 진행한다. [J]

qdev_device_add 함수 [J]

qdev_device_add 함수는 qdev_device_new를 호출하여 장치 인스턴스를 생성한다. [J]

qdev_device_new는 object_new를 호출하여 장치 객체를 생성한다. [J]

device_init 함수 [J]

device_init 함수는 장치 인스턴스의 instance_init 함수로, 장치의 기본 초기화 작업을 수행한다. [J]

이 함수는 장치의 realized 상태를 false로 설정하여 아직 시스템에 완전히 등록되지 않았음을 나타낸다. [J]

qdev_realize 함수 [J]

qdev_realize 함수는 device_realize 함수를 호출하여 장치를 시스템에 등록한다. [J]

device_realize는 장치의 realized 상태를 true로 설정하고, device_class_realize 함수를 호출하여 클래스별 초기화 작업을 수행한다. [J]

qdev_unrealize 및 qdev_free 함수 [J]

장치가 시스템에서 제거될 때 qdev_unrealize 함수가 호출되어 realized 상태를 false로 되돌린다. [J]

qdev_free 함수는 장치 객체를 해제하고 시스템에서 등록을 해제한다. [J]

## 10. QEMU PCI 장치 생성 및 사용자 공간 상호작용 [L]

QEMU에서 PCI 장치를 생성하고 사용자 공간에서 해당 장치와 상호작용하는 방법을 설명한다.

### 10.1. PCI 장치 구조 및 TypeInfo 정의 [K]

PCI 장치 구조체 [K]

새로운 PCI 장치 인스턴스를 생성하기 위해 PCIAmuDevice라는 구조체를 정의한다. [K]

이 구조체는 PCIDevice 구조체를 포함해야 하며, PCIDevice는 다시 Object 구조체를 포함한다. [K]

QEMU 빌드 시스템에 장치 추가 [K]

hw/misc 디렉토리에 장치 관련 파일을 추가하고, meson.build 및 Kconfig 파일에 장치 정보를 등록하여 QEMU 빌드 시스템에 포함시킨다. [K]

TypeInfo 정의 [K]

PCIAmuDevice의 TypeInfo를 정의한다. [K]

name은 TYPE_PCI_AMU_DEVICE로, parent는 TYPE_PCI_DEVICE로 설정한다. [K]

instance_size는 sizeof(PCIAmuDevice)로 설정한다. [K]

PCIAmuDevice 구조체는 PCIDevice 외에 mem_bar와 io_bar와 같은 추가 속성을 포함한다. [K]

class_init 함수는 pci_amu_device_class_init으로 설정하며, 이 함수는 vendor_id, device_id, revision_id, class_code 등 PCI 장치의 일반적인 속성을 설정한다. [K]

interfaces는 PCI_INTERFACE_NAME으로 설정하여 PCI 인터페이스를 상속받도록 한다. [K]

### 10.2. PCI 장치 에뮬레이션 및 동적 캐스팅 [K]

동적 캐스팅(Dynamic Casting) [K]

QEMU는 object_dynamic_cast 매크로를 사용하여 특정 Object 포인터가 PCIAmuDevice 타입의 인스턴스인지 런타임에 확인하고, 해당 타입으로 안전하게 캐스팅한다. [K]

이는 장치 포인터의 유효성을 확인하고 올바른 타입으로 접근하는 데 사용된다. [K]

메모리 및 I/O 영역 등록 [K]

pci_register_bar 함수를 사용하여 mem_bar (메모리 영역)와 io_bar (I/O 영역)를 등록한다. [K]

각 BAR(Base Address Register)는 이름, 크기(예: 16바이트), 그리고 읽기/쓰기 콜백 함수(mmio_read, mmio_write, io_read, io_write)를 가진다. [K]

콜백 함수는 게스트가 해당 메모리/I/O 영역에 접근할 때 QEMU 호스트에서 호출된다. [K]

콜백 함수 내에서는 object_dynamic_cast를 사용하여 PCIAmuDevice 인스턴스를 가져와 실제 읽기/쓰기 작업을 수행한다. [K]

msi_notify와 같은 함수를 호출하여 MSI(Message Signaled Interrupts) 기능을 에뮬레이션할 수 있다. [K]

### 10.3. PCI 장치 실행 및 사용자 공간 상호작용 [L]

QEMU 실행 및 장치 주입 [L]

QEMU를 빌드한 후, qemu-system-x86_64 명령어를 사용하여 리눅스 커널 이미지와 루트 파일 시스템을 로드한다. [L]

-device 옵션을 사용하여 pci-amu-device를 PCI 버스 0에 주입한다. [L]

게스트 리눅스 시스템에서 lspci 명령어를 실행하면 새로 추가된 PCI 장치(1234:AABB)를 확인할 수 있다. [L]

사용자 공간에서 장치 접근 [L]

게스트 리눅스에서 /sys/bus/pci/devices/0000:00:00.0/resource1과 같은 경로를 통해 I/O BAR에 접근할 수 있다. [L]

echo 명령어를 사용하여 BAR에 값을 쓸 수 있으며, hexdump 명령어를 사용하여 BAR에서 값을 읽을 수 있다. [L]

예를 들어, echo -ne '\xAA\xBB\xCC\xDD' > resource1 명령어로 값을 쓰고, hexdump -C resource1 명령어로 값을 읽을 수 있다. [L]

이 작업은 QEMU 호스트의 io_write 및 io_read 콜백 함수를 트리거한다. [L]

PCI 구성 공간 확인 [L]

/sys/bus/pci/devices/0000:00:00.0/config 파일을 통해 PCI 장치의 구성 공간(Configuration Space)을 확인할 수 있다. [L]

hexdump -C config 명령어를 사용하여 구성 공간의 헤더(예: 처음 64바이트)를 덤프할 수 있다. [L]

이 헤더에는 vendor_id (1234), device_id (AABB), revision_id (55), class_code (FFFF) 등 pci_amu_device_class_init에서 설정한 값들이 포함되어 있다. [L]

## 11. QEMU 하드웨어 머신 에뮬레이션 [M]

QEMU는 MachineClass와 MachineState를 통해 전체 하드웨어 머신을 에뮬레이션하며, 장치 모델링과 유사한 객체 모델을 사용한다.

### 11.1. 하드웨어 머신 등록 및 초기화 [M]

머신 등록 매크로 [M]

새로운 하드웨어 머신(예: pc-i440fx-2.1)을 QEMU에 등록하려면 TYPE_PC_MACHINE과 같은 매크로를 사용한다. [M]

이 매크로는 type_init 함수를 호출하여 TypeInfo 구조체를 시스템에 등록한다. [M]

TypeInfo 정의 [M]

머신 TypeInfo는 name과 parent 타입(예: TYPE_MACHINE)을 가진다. [M]

class_init 함수는 pc_machine_class_init과 같이 머신 클래스를 초기화하는 함수로 설정된다. [M]

클래스 계층 [M]

PCMachineClass는 MachineClass를 상속받고, MachineClass는 ObjectClass를 상속받는다. [M]

PCMachineState (인스턴스)는 MachineState를 상속받고, MachineState는 Object를 상속받는다. [M]

### 11.2. 머신 생성 및 장치 초기화 [M]

머신 생성 함수 [M]

pc_init_i440fx와 같은 머신 초기화 함수는 pc_init_i440fx_internal을 호출한다. [M]

이 함수는 object_new를 사용하여 MachineState 및 MachineClass 구조체를 생성하고 초기화한다. [M]

이는 PCI 장치 생성 과정과 유사하게 작동한다. [M]

CPU 및 장치 초기화 [M]

머신 초기화 과정에서 object_new를 사용하여 x86 CPU와 같은 핵심 장치들을 생성한다. [M]

qdev_realize 함수를 호출하여 생성된 장치들을 시스템에 등록한다. [M]

이는 장치 모델링에서 qdev_realize를 사용하여 장치를 시스템에 등록하는 것과 동일한 메커니즘이다. [M]

## 12. QEMU의 메모리 관리 시스템 [N]

QEMU는 SoftMMU라는 가상 메모리 시스템을 통해 게스트의 물리 주소를 호스트의 가상 주소로 변환하고, 다양한 유형의 메모리 블록을 지원한다.

### 12.1. 메모리 에뮬레이션 및 SoftMMU [N]

SoftMMU의 역할 [N]

QEMU의 메모리 시스템은 SoftMMU라고 불리며, 하드웨어 메모리 컴포넌트(예: DIMM)를 에뮬레이션한다. [N]

이는 물리적인 RAM 스틱을 PC에 추가하는 것과 유사하게 작동하여, 운영체제가 부팅될 때 추가된 메모리를 감지할 수 있도록 한다. [N]

DIMM 에뮬레이션 [N]

DIMM(Dual In-line Memory Module)은 여러 개의 칩으로 구성되며, 각 칩은 용량을 가진다. [N]

QEMU는 이러한 메모리 슬롯을 실제 하드웨어처럼 에뮬레이션하여, 특정 게스트에 메모리를 동적으로 추가할 수 있도록 한다. [N]

게스트는 추가된 메모리를 감지하고 사용할 수 있다. [N]

### 12.2. 메모리 구조체 및 백엔드 [N]

PCIDIMMDevice 구조체 [N]

PCIDIMMDevice는 PCI 장치 유형으로, 주소, 시스템 내 슬롯 번호 등 DIMM 관련 정보를 포함한다. [N]

이 구조체는 host_mem_pointer를 통해 HostMemoryBackend 구조체를 가리킨다. [N]

HostMemoryBackend 구조체 [N]

HostMemoryBackend는 게스트에 할당될 호스트 메모리를 관리한다. [N]

이 구조체는 MemoryRegion 구조체를 포함하며, MemoryRegion은 RAMBlock을 가리킨다. [N]

RAMBlock은 호스트의 실제 메모리 블록에 대한 정보를 담고 있다. [N]

HostMemoryBackend는 memdev 또는 파일(file)을 통해 메모리를 표현할 수 있다. [N]

FileBackend 정의 [N]

FileBackend는 TypeInfo를 통해 정의되며, parent는 TYPE_MEMORY_BACKEND로 설정된다. [N]

class_init 함수는 file_backend_class_init으로 설정되며, 이 함수는 HostMemoryBackendClass를 가져와 memory_region_ram_file 함수를 호출하여 파일 기반의 호스트 메모리를 초기화한다. [N]

### 12.3. 주소 공간 및 가상 주소 변환 [N]

AddressSpace 구조체 [N]

AddressSpace 구조체는 여러 MemoryRegion을 묶어 하나의 주소 공간을 표현한다. [N]

root 포인터를 통해 루트 MemoryRegion을 가리키며, 이 루트는 동일한 주소 공간에 속하는 다른 MemoryRegion들을 참조한다. [N]

가상 주소 변환 흐름 [N]

게스트의 물리 주소(Guest Physical Address, GPA)는 PCIDIMMDevice를 통해 HostMemoryBackend로 연결된다. [N]

HostMemoryBackend는 MemoryRegion을 포함하고, MemoryRegion은 RAMBlock을 가리킨다. [N]

RAMBlock은 호스트의 실제 메모리 주소와 길이를 포함한다. [N]

MemoryRegion은 AddressSpace의 root를 가리키며, AddressSpace는 GPA를 Host Virtual Address(HVA)로 변환한다. [N]

QEMU는 사용자 공간에서 실행되는 애플리케이션이므로, HVA는 호스트 커널의 페이지 테이블을 통해 Host Physical Address(HPA)로 변환된다. [N]

### 12.4. RAMBlock의 다양한 유형 [N]

RAM 유형 [N]

일반적인 RAM을 나타내며, 읽기/쓰기가 가능하다. [N]

DMA 유형 [N]

DMA(Direct Memory Access) 메모리 영역을 나타낸다. [N]

게스트가 이 영역에 읽기/쓰기를 시도하면 QEMU 호스트에 콜백이 발생하여 특정 장치 에뮬레이션을 처리한다. [N]

ROM 유형 [N]

읽기 전용 메모리(Read-Only Memory)를 나타내며, 쓰기가 불가능하다. [N]

ROM_DEVICE 유형 [N]

읽기는 일반 RAM과 같지만, 쓰기 시에는 MMIO(Memory-Mapped I/O)와 유사하게 콜백이 발생하여 호스트가 처리한다. [N]

IOMMU 유형 [N]

IOMMU(Input/Output Memory Management Unit)를 에뮬레이션한다. [N]

이 영역으로 가는 주소는 다른 RAMBlock으로 변환되어 접근된다. [N]

## 13. QEMU 및 리눅스 커널 디버깅 [O]

QEMU는 GDB를 사용하여 QEMU 프로세스 자체와 게스트 리눅스 커널을 디버깅할 수 있는 환경을 제공한다.

### 13.1. QEMU 프로세스 디버깅 [O]

기존 PCI 장치 상호작용 확인 [O]

이전에 생성한 PCI 장치(1234:AABB)에 값을 쓰고 읽는 작업을 다시 수행하여 장치가 정상적으로 작동하는지 확인한다. [O]

이 작업은 /sys/bus/pci/devices/.../resource1 경로를 통해 이루어진다. [O]

QEMU 디버깅의 필요성 [O]

단순히 값이 쓰고 읽히는 것을 확인하는 것만으로는 내부 동작을 파악하기 어렵다. [O]

QEMU 프로그램 자체와 에뮬레이션된 장치의 내부 동작을 디버깅해야 한다. [O]

게스트가 I/O 장치에 접근할 때 QEMU 호스트의 콜백 함수가 호출되므로, 이 부분을 디버깅해야 한다. [O]

GDB를 이용한 QEMU 디버깅 [O]

GDB(GNU Debugger)를 사용하여 QEMU 프로세스(qemu-system-x86_64)를 디버깅한다. [O]

VS Code와 같은 IDE에서 launch.json 파일을 설정하여 GDB를 QEMU에 연결한다. [O]

launch.json 설정에는 QEMU 실행 파일 경로, 아키텍처, 작업 디렉토리, 그리고 QEMU에 전달할 인자(args)가 포함된다. [O]

args에는 리눅스 커널 이미지, 루트 파일 시스템, -device 옵션으로 추가할 PCI 장치, 그리고 -serial mon:stdio와 같은 시리얼 포트 리다이렉션 설정이 포함된다. [O]

-serial mon:stdio는 게스트의 콘솔 출력을 VS Code의 디버그 콘솔로 리다이렉션한다. [O]

디버깅 세션 실행 [O]

VS Code에서 GDB QEMU 디버깅 세션을 시작하면 QEMU 프로세스가 시작되고 main 함수 진입점에서 멈춘다. [O]

screen /dev/pts/2와 같은 명령어를 사용하여 게스트 리눅스 콘솔에 연결한다. [O]

게스트에서 PCI 장치에 값을 쓰면(예: echo ... > resource1), QEMU 호스트의 io_write 콜백 함수에 설정된 브레이크포인트에서 디버거가 멈춘다. [O]

이를 통해 QEMU 내부에서 장치와의 상호작용을 단계별로 디버깅할 수 있다. [O]

### 13.2. 게스트 리눅스 커널 디버깅 [O]

게스트 커널 디버깅의 필요성 [O]

QEMU 프로세스뿐만 아니라 게스트 리눅스 커널 자체의 동작도 디버깅해야 할 때가 있다. [O]

디버깅용 커널 빌드 [O]

리눅스 커널을 빌드할 때 -g 플래그를 추가하여 디버깅 심볼을 포함시킨 vmlinux 파일을 생성한다. [O]

GDB를 이용한 커널 디버깅 설정 [O]

launch.json에 GDB 리눅스 커널 디버깅 설정을 추가한다. [O]

program은 디버깅 심볼이 포함된 vmlinux 파일로 설정한다. [O]

target remote localhost:1234와 같이 QEMU가 제공하는 GDB 서버에 연결하도록 설정한다. [O]

stopAtEntry를 false로 설정하고, break를 start_kernel 함수에 설정하여 커널 시작 시 멈추도록 한다. [O]

QEMU를 실행할 때 -s -S 옵션을 추가하여 GDB 서버를 활성화하고, QEMU가 GDB 클라이언트의 연결을 기다리도록 한다. [O]

-no-kaslr 옵션을 사용하여 커널 주소 공간 레이아웃 무작위화(KASLR)를 비활성화하여 디버깅을 용이하게 한다. [O]

디버깅 세션 실행 [O]

QEMU를 GDB 서버 모드로 실행한 후, VS Code에서 GDB 리눅스 커널 디버깅 세션을 시작한다. [O]

GDB가 QEMU의 GDB 서버에 연결되면 start_kernel 함수에서 멈춘다. [O]

continue 명령어를 실행하면 게스트 리눅스 커널이 계속 실행되고, 게스트 콘솔에서 lspci 명령어를 통해 장치를 확인할 수 있다. [O]
