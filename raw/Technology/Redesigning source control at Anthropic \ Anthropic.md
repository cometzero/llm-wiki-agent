---
title: Redesigning source control at Anthropic \ Anthropic
origin: lilys_ai
lilys_project_id: 11734201
lilys_project_url: https://lilys.ai/digest/11734201
lilys_created_at: '2026-10-13T22:08:52.501Z'
lilys_collection: ''
source_type: webPage
lilys_note_id: '13901293'
sources:
- id: '115396'
  source_type: webPage
  url: https://www.anthropic.com/engineering/redesigning-source-control
  title: Redesigning source control at Anthropic \ Anthropic
  status: ready
---

# Redesigning source control at Anthropic \ Anthropic

## LilysAI note

> Anthropic이 **AI 시대의 코드 관리 문제**를 어떻게 해결했는가? AI가 생성하는 폭발적인 코드량으로 인해 기존 Git 시스템의 한계에 부딪히자, Anthropic은 AI 에이전트의 '항상 온라인' 특성을 활용한 새로운 버전 관리 시스템 **Scion**을 자체 개발하여 200배 효율을 달성했습니다.

## 1. Anthropic의 소스 제어 시스템 재설계 배경[^1]

![A rapidly growing graph showing an exponential increase in code changes merged per day, starting from a low baseline and skyrocketing upwards. Below the graph, a human developer is struggling with a tangled, overflowing Git repository, while an AI agent calmly and efficiently manages a streamlined, cloud-based version control system with data flowing seamlessly between clients and servers.](https://resource.lilys.ai/images/genimg_6dc9cd98ddcdb817.png)

Anthropic은 AI 시대의 폭발적인 코드량 증가로 인해 기존 Git 시스템의 한계에 부딪히자, AI 에이전트의 '항상 온라인' 특성을 활용한 새로운 버전 관리 시스템 Scion을 자체 개발했다.

### 1.1. AI 시대의 코드 관리 병목 현상[^2]

1. **AI의 코드 생성 능력 증대**[^3]
   1. Claude는 연구 반복, 복잡한 프로그램 최적화, 새로운 서비스 구축을 전례 없는 속도와 규모로 자율적으로 수행한다.
   2. 이로 인해 코딩 자체가 병목 현상이 아니게 되었다.
2. **기존 개발 인프라의 한계**[^4]
   1. 소스 제어, 빌드, CI 등 인간 규모에 맞춰 구축된 개발 인프라가 병목 현상이 되었다.
   2. 2026년 5월, Anthropic은 하루 평균 약 2,500건의 코드 변경을 병합했지만, 9월에는 하루 30,000건 이상을 병합했다.

<img src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F1e2a750dba61db4a76b72eec5b0cf50b8a7f878c-3840x2160.png&w=3840&q=75">

2026년 1월부터 9월까지 Anthropic의 모노레포에 병합된 일일 변경 사항

3. **Scion 개발 및 마이그레이션**[^5]
   1. 이러한 성장을 지원하기 위해 Anthropic은 자체 버전 관리 시스템인 Scion을 구축하고 5개월 만에 모노레포를 Git에서 완전히 마이그레이션했다.
   2. 동시에 코드 검토 도구(Antique), 코드 검색, 풍부한 소스 제어 IAM 시스템 등 다양한 관련 시스템을 구축했다.
   3. Claude의 코드 작성 능력은 이러한 상황을 초래한 원인이자, 동시에 고품질의 확장 가능한 시스템을 빠르게 구축할 수 있게 한 원동력이 되었다.

### 1.2. Git의 분산 시스템 한계와 Anthropic의 특이한 워크로드[^6]

1. **Anthropic의 독특한 워크로드**[^7]
   1. Anthropic은 다른 어떤 회사보다 Claude를 소프트웨어 작성에 훨씬 더 많이 사용하므로, 인간 규모에 맞춰 구축된 도구들이 한계에 부딪히는 지점을 가장 먼저 경험한다.
   2. 이러한 문제는 단기적으로는 흔치 않지만, AI 코딩 도구를 사용하는 다른 조직들도 곧 경험할 것으로 예상된다.
2. **Git의 분산 시스템 설계와 한계**[^8]
   1. Git은 분산 시스템으로, 모든 클론은 오프라인 상태에서도 차이점 계산, 기록 읽기, 체크아웃이 가능한 완전한 자체 포함 저장소이다.
   2. 대부분의 저장소에는 적합한 설계이지만, Anthropic의 모노레포는 이 설계 공간에 맞지 않게 되었다.
   3. 메인 브랜치 기록만 거의 100GB에 달하고, 압축된 작업 복사본은 25GB가 넘는다.
   4. CI를 위해 하루에 약 2,500만 건의 코드 체크아웃이 발생하며, 이는 하루 600PB 이상의 Git 트래픽에 해당한다.
3. **Git 확장 도구의 비효율성**[^9]
   1. Git은 얕은 클론, 스파스 체크아웃, 프라미서 리모트와 같은 부분 저장소 작업 도구를 제공한다.
   2. 대규모 모노레포를 위한 내부 Git 미러 및 스냅샷과 같은 표준 해결 방법도 사용했다.
   3. Anthropic은 부하를 처리하기 위해 수백 개의 내부 Git 미러를 운영했지만, 병합 속도가 증가함에 따라 운영이 어려워졌다.
   4. 스냅샷은 새로 고침 간에 메인 브랜치 팁에서 멀어졌고, 부분 클론에서 diff 및 blame과 같은 기록 의존 작업이 작동하도록 유지하는 데 더 많은 노력이 필요했다.

<img src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fff019752973f6d83d2f6ba3bf56636aced3ea82c-3840x1238.png&w=3840&q=75">

Git 체크아웃 확장을 위한 일반적인 설정

4. **중앙 집중식 시스템으로서의 Git 사용과 문제점**[^10]
   1. Anthropic은 대부분의 회사와 마찬가지로 Git을 하나의 권위 있는 복사본을 가진 중앙 집중식 시스템으로 사용하고 있었다.
   2. 그러나 거의 모든 클라이언트가 항상 온라인 상태인 에이전트와 작업이었다.
   3. Git의 분산 및 오프라인 작업에 탁월한 특성들이 저장소가 커짐에 따라 확장 능력을 저해했다.
   4. 이에 Anthropic은 에이전트가 항상 온라인이라는 사실을 염두에 두고 소스 제어를 설계하면 어떤 모습일지 질문하게 되었다.

### 1.3. 에이전트 규모 소스 제어를 위한 Scion의 설계 원칙[^11]

1. **클라이언트는 항상 온라인**[^12]
   1. Git은 클라이언트가 오프라인으로 작업하며 저장소의 전체 복사본이 필요하다고 가정한다.
   2. Scion은 거의 모든 클라이언트가 에이전트와 작업이므로, 서버가 항상 연결 가능하고 클라이언트가 필요할 때 데이터를 가져오도록 설계되었다.
2. **클라이언트-서버 비대칭성**[^13]
   1. Git에서는 모든 클라이언트가 완전한 서버 역할을 할 수 있다.
   2. Scion에서는 서버가 파일 기록 및 blame에 대한 질문에 답하고, 커밋을 생성하며, 병합 및 리베이스를 수행한다.
   3. 클라이언트는 제한된 로컬 객체 캐시를 유지하고, 작업 복사본 파일을 디스크에 배치하며, 파일 시스템 변경 사항을 모니터링하고, 서버와 작업할 수 있는 인체공학적인 방법을 제공한다.
   4. 클라이언트는 자체적으로 계산할 수 있는 것이 거의 없지만, 그 대가로 로컬에 훨씬 적은 데이터가 필요하다.
3. **포괄적인 소스 제어 서비스로 다양한 애플리케이션 지원**[^14]
   1. Git에서는 CI 작업이나 도구가 저장소에 대한 질문(예: 누가 마지막으로 줄을 변경했는지, 두 커밋이 어떻게 관련되어 있는지)을 하려면 저장소의 로컬 복사본을 유지하거나 공급업체별 API가 답을 제공하기를 바라야 한다.
   2. Scion에서는 클라이언트가 사용하는 모든 소스 제어 쿼리가 API를 통해 노출되므로, 많은 경우 작업에 로컬 저장소가 전혀 필요하지 않다.
   3. 자동화된 이분법 및 되돌리기 파이프라인과 같은 많은 내부 도구는 소스 제어에 대한 저렴하고 프로그래밍 방식의 액세스 없이는 대규모로 실용적이지 않을 것이다.
4. **모든 것이 수평적으로 확장 가능해야 함**[^15]
   1. Anthropic은 한때 수백 개의 Git 미러를 운영했지만, 이는 용량을 크게 압박했고 저장소가 미러의 디스크 또는 메모리 제한을 초과하자 더 이상 확장되지 않았다.
   2. Scion에서는 저장소의 데이터가 분산되어 있으며 모든 구성 요소가 독립적으로 확장 가능하다.
   3. 서버에서도 저장소의 완전히 구체화된 복사본이 존재하지 않는다.
   4. Git의 압축된 객체 묶음인 팩파일과 같은 것이 없으므로 저장소 유지 관리가 필요 없다.
5. **커밋은 저렴하고, 증분적이며, 잠금-없음이어야 함**[^16]
   1. Git에서는 로컬에서 커밋한 다음 작업을 공유하기 위해 푸시한다.
   2. Scion에서는 모든 커밋, 리베이스 또는 병합이 서버에서 발생하므로 푸시할 것이 없지만, 각 작업은 빨라야 한다.
   3. 커밋을 생성하고 다운스트림 데이터 구조를 업데이트하는 비용은 변경 크기에 비례해야 하며, 전체 저장소 크기에 비례해서는 안 된다. 그렇지 않으면 서버가 따라갈 수 없다.
   4. Scion의 개발 수명 주기는 메인 참조 또는 릴리스 브랜치를 제외하고 참조(브랜치 및 태그와 같은 커밋에 대한 포인터)를 사용하지 않도록 권장한다. 이는 모든 서버가 동의해야 하는 전역 상태가 임박한 확장 문제이기 때문이다.
6. **작업 복사본은 선택 사항이며, 기본적으로 스파스함**[^17]
   1. 모노레포가 매우 크고 CI를 위해 하루에 수천만 번 코드를 체크아웃하기 때문에, 가능한 한 체크아웃을 피하고자 했다.
   2. Scion을 사용하면 커밋과 해당 병합 기반 간의 차이점이 필요한 CI 작업은 서버에 요청할 수 있다.
   3. 쓰기 작업도 마찬가지로 체크아웃을 건너뛰고 API를 통해 전적으로 작동할 수 있다.
   4. Scion의 프로토콜은 클라이언트가 요청하는 디렉터리만 포함하는 스파스 체크아웃과 필요할 때 파일을 구체화하는 가상화된 체크아웃을 중심으로 한다. 따라서 작업에 디스크에 파일이 필요할 때 클라이언트는 실제로 읽는 파일에 대해서만 비용을 지불한다.

## 2. Scion의 작동 방식 및 확장성[^18]

Scion은 에이전트 규모의 소스 제어를 위해 Git과 근본적으로 다른 접근 방식을 취하며, 데이터 구조와 확장성 측면에서 혁신적인 설계를 적용했다.

### 2.1. Scion의 데이터 구조[^19]

1. **변경 세트(Changeset) 중심의 작업 단위**[^20]
   1. Scion에서 작업 단위는 "변경 세트(changeset)"이며, 이는 쓰기 선행 로그의 항목이다.
   2. 변경 세트는 Git의 커밋에서 기대할 수 있는 대부분의 정보를 저장한다.
   3. Git 커밋이 트리에 대한 포인터를 저장하는 반면, 변경 세트는 첫 번째 부모와 비교하여 변경된 파일 목록과 블롭 스토리지에 있는 압축된 파일 콘텐츠에 대한 콘텐츠 주소 지정 포인터를 저장한다.
   4. 변경 세트는 서버 측에서 생성되며 즉시 모든 곳에서 사용할 수 있다.

<img src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F71c83868210b4b571abb068ea4cd76de749566b1-3840x2995.png&w=3840&q=75">

Scion의 변경 세트 형태

2. **높은 처리량과 참조 관리**[^21]
   1. 이러한 구조는 팩파일이 없고, 잠금이나 서버 간 조정이 없으며, 이동할 참조가 없기 때문에 매우 높은 처리량으로 변경 세트를 수락할 수 있게 한다.
   2. Scion은 기술적으로 참조를 지원하지만, 커밋 생성이나 가져오기에 참조가 포함되지 않으므로, 참조를 이동하는 것은 변경 세트 생성과 별개로 단일 Spanner 행에서 비교 및 교환으로 이루어진다.
3. **파생 데이터 구조 및 이점**[^22]
   1. 변경 세트는 변경된 내용만 기록하므로, 자체적으로는 누가 마지막으로 줄을 편집했는지 또는 어떤 커밋이 파일에 영향을 미쳤는지와 같은 질문에 빠르게 답할 수 없다.
   2. 이러한 질문에 답하기 위해 Scion은 변경 세트에서 추가 데이터 구조를 구축한다. 여기에는 파일 blame 및 경로 기록을 위한 전용 구조와 커밋 그래프를 위한 스킵 리스트가 포함된다.
   3. 변경 세트의 직접적인 부분이 아닌 모든 것을 "파생 데이터"라고 부르며, 이를 하나의 일반적인 메커니즘을 통해 계산한다.
   4. 각 유형의 파생 데이터는 재귀적으로 정의되므로, 변경 세트에 대한 값은 해당 변경 세트의 부모 값에서 계산된다.
   5. 이 메커니즘은 세 가지 이점을 제공한다.
      1. 새로운 데이터 구조가 특정 작업을 더 빠르게 만들 때 새로운 유형의 파생 데이터를 쉽게 추가할 수 있다.
      2. 각 유형에 대해 데이터를 즉시 계산할지 또는 작업을 연기할지 선택할 수 있으므로 필요 없는 데이터를 구체화하는 것을 피할 수 있다.
      3. 클라이언트가 이러한 데이터 구조의 내부를 볼 수 없으므로 클라이언트를 변경하지 않고도 최적화할 수 있다.
   6. 시스템이 성장함에 따라 복사 감지 또는 경로 기반 파일 검색을 수행하기 위한 새로운 인덱스와 같은 새로운 유형의 파생 데이터를 여러 번 추가했다.

### 2.2. Scion의 확장성 아키텍처[^23]

1. **수평적 확장 가능한 서버 아키텍처**[^24]
   1. 소규모 Scion 서버 플릿은 변경 세트 가져오기, 차이점 계산, 병합 기반 찾기, 블롭 가져오기와 같은 클라이언트가 필요로 하는 모든 작업에 대한 소스 제어 API를 제공한다.
   2. 모든 소스 제어 데이터는 콘텐츠 주소 지정 방식이므로, 데이터가 저장되면 변경되지 않으며 어떤 서버도 다른 서버와 확인하지 않고 캐시할 수 있다.
   3. 결과적으로 서버는 수평적으로 확장 가능하며 조정이 거의 필요 없다.
   4. 서버는 기본적으로 파생 데이터를 즉석에서 계산하고 결과를 Spanner에 다시 쓸 수 있는 대규모 캐시이다.
2. **로컬 저장소 유지 관리 불필요**[^25]
   1. Scion의 많은 소비자는 더 이상 자체 로컬 저장소를 유지할 필요가 없다.
   2. 특히 커밋 조상 및 blame에 대한 소스 제어 질문이 필요한 CI 작업이나 도구의 경우, 저장소를 가져오고 유지 관리하는 것이 상당한 유지 관리 부담이었다.
   3. 마이그레이션 초기에는 자체 클라이언트, 저장소 형식 또는 프로토콜이 없었을 때 Scion은 이러한 "메타데이터" 쿼리에만 응답했다.
   4. 파일 콘텐츠를 가져오고 작업 복사본을 구체화하는 것은 훨씬 더 데이터 집약적인 작업이며, 자체 설계가 필요했다.
3. **scn 클라이언트의 효율적인 프로토콜**[^26]
   1. Scion의 `scn` 클라이언트는 Git의 가져오기 프로토콜과 여러 중요한 면에서 다르며, 결과적으로 Git 서버보다 훨씬 적은 CPU를 요구하는 고도로 확장 가능한 아키텍처를 제공한다.
   2. Scion의 협상은 클라이언트가 이미 가지고 있는 것을 서버에 알리지 않고, 클라이언트가 원하는 트리와 블롭에만 작동한다.
   3. 루트 트리에서 시작하여 클라이언트는 누락된 트리에 대해 로컬 저장소를 확인하고 재귀적으로 요청한 다음, 블롭에 대해 이 프로세스를 반복한다.
   4. 모든 요청은 변경되지 않는 특정 객체에 대한 것이므로, 어떤 캐시도 이에 응답할 수 있으며, 아키텍처는 전통적인 계층형 캐시와 매우 유사하다.
   5. 단일 멀티 기가바이트 팩파일 응답이 없으므로 프로세스도 효율적이고 재개 가능하다.
   6. 스파스 및 가상화된 체크아웃은 특별한 지원이 필요하지 않다. 클라이언트가 원하지 않는 트리를 요청하지 않기 때문이다.
4. **Scion의 체크아웃 아키텍처**[^27]
   1. 플릿에서 클라이언트는 소켓을 통해 노드 전체의 객체를 저장하는 데몬인 `scion-daemon`과 통신한다.
   2. 대부분의 노드는 모노레포에 액세스해야 하며, 동일한 노드의 작업은 대부분 동일한 객체를 재사용한다.
   3. 각 데몬은 주기적으로 새로 고쳐지는 스냅샷에서 시작한 다음, 해당 지역의 트리 및 블롭 캐시 서버인 `scion-cache`와만 통신한다.
   4. 이 캐시 서버는 데몬이 사용할 디스크 형식으로 메모리에서 직접 객체를 스트리밍하므로, 클라이언트의 누락된 객체를 계산하거나 델타 압축을 수행하는 데 시간을 소비할 필요가 없다.
   5. 캐시에 객체가 없으면, 필요한 경우 Spanner 또는 클라우드 스토리지에서 읽는 권위 있는 `scion-servers`에 요청한다.
   6. `scion-daemon`, `scion-cache`, `scion-server`는 모두 이 프로토콜에 대해 동일한 RPC에 응답하므로, 클라이언트는 캐시 토폴로지를 알 필요가 없다.
   7. 이론적으로 어떤 계층도 다른 계층과 통신할 수 있지만, 장애 도메인을 격리하기 위해 계층화를 엄격하게 적용한다.
   8. 지역 `scion-cache`의 장애가 업스트림 `scion-servers`를 압도하여 전체 시스템을 다운시키는 상황을 피하고자 한다.

<img src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcba1eaaa67385fd00f210badaacd147de480120b-3840x1718.png&w=3840&q=75">

Scion의 체크아웃 아키텍처

5. **Scion 인프라의 효율성 향상**[^28]
   1. 이 시스템의 각 계층은 99% 이상의 캐시 적중률을 유지하며 장기적인 상태를 요구하지 않으므로, 필요할 경우 쉽게 확장할 수 있다.
   2. Scion 인프라의 CPU 및 메모리 요구 사항은 이전 Git 미러링 인프라보다 200배 작다.
   3. CI 및 연구 작업은 코드를 두 자릿수 더 빠르게(몇 분이 아닌 몇 초 만에) 체크아웃하여 플릿 전체에서 상당한 용량을 확보했다. CI만으로도 25%의 CPU 용량 이득을 얻었다.
   4. 클라이언트나 캐시 모두 저장소 유지 관리를 수행할 필요가 없어 작업의 수명 주기 관리가 단순해진다.

## 3. Scion 구축을 통해 얻은 교훈[^29]

Scion 구축은 Claude Mythos Preview 및 Claude Tag 출시와 동시에 진행되었으며, 이 두 가지는 Scion의 필요성을 증폭시키고 구축 속도를 크게 가속화했다.

### 3.1. AI를 활용한 개발의 변화[^30]

1. **Claude를 통한 개발 가속화**[^31]
   1. Scion 구축은 Claude Mythos Preview 및 Claude Tag가 내부적으로 사용 가능해진 시점과 거의 동시에 시작되었다.
   2. 이 두 가지 릴리스는 Scion의 필요성을 증폭시키는 동시에 구축 속도를 의미 있게 가속화했다.
2. **Claude의 코드 최적화 능력**[^32]
   1. Git-to-Scion 수집 파이프라인의 첫 번째 버전을 수동으로 작성했지만, Claude Mythos Preview의 초기 내부 스냅샷을 사용한 후 놀라운 결과를 얻었다.
   2. Claude에게 전체를 다시 작성하도록 요청하자, 추가 지시 없이 메모리를 20배 적게 사용하고 4배 빠른 버전을 생성했으며, 수집 순서 및 데이터 구조에 대한 모든 암묵적인 불변성을 유지했다.

### 3.2. 에이전트 규모 소프트웨어 개발의 새로운 양상[^33]

1. **소규모 팀의 빠른 개발 및 마이그레이션**[^34]
   1. 7명으로 구성된 팀이 Scion과 Antique(코드 검토 도구)를 포함한 6개 이상의 관련 시스템을 구축하고 5개월 만에 완전히 마이그레이션했다.
   2. 이 모든 과정은 하루에 병합되는 코드 볼륨이 10배 증가하는 동안 이루어졌다.
   3. 과거에는 이러한 소스 제어 시스템을 개발하고 배포하는 데 수년의 반복적인 마이그레이션과 훨씬 더 많은 엔지니어가 필요했을 것이다.
   4. 이러한 빠르고 민첩한 마이그레이션이 미래에는 더 흔해질 것으로 예상된다.

<img src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fdd91296719203f38229824bb9bc9e9a61c76ed67-3840x2160.png&w=3840&q=75">

2026년 1월부터 9월까지 Scion 및 Antique 코드베이스에 병합된 주간 변경 사항

2. **엔지니어 역할의 변화**[^35]
   1. 이 시스템에 참여한 모든 엔지니어는 이제 Claude가 자신들보다 코드를 더 잘 작성한다고 평가한다.
   2. 그러나 엔지니어들은 여전히 고수준 시스템 간 구성 요소에 대한 귀중한 이해와 설계 수준의 절충안을 제공하며, 해결하고자 하는 문제와 달성해야 할 규모에 대해 정보에 입각한 선택을 했다.
   3. 에이전트는 때때로 핵심 시스템 제약 조건을 위반하여 애초에 허용되어서는 안 되는 패턴을 만족시키려 한다.
   4. 예를 들어, 코드 검토 도구에 묻는 대신 커밋 로그를 선형적으로 읽어 변경 사항이 언제 메인에 병합되었는지 무차별적으로 찾아보려는 여러 시스템이 있었다.
   5. Anthropic은 또한 적대적 검토를 광범위하게 사용하는데, 이는 여러 면에서 매우 효과적이지만 근시안적일 수 있으므로, 숙련된 엔지니어는 가상의 우려에 대응하여 시스템의 일부를 과도하게 설계하는 것을 Claude가 피하도록 유도해야 했다.
   6. 예를 들어, 한 검토는 다른 내부 서비스를 과도하게 신뢰하지 않아 Claude가 과도한 유효성 검사 및 복잡성을 추가하게 만들었다.
   7. 팀원들은 여전히 시스템에 대한 모든 변경 요청을 검토하지만, 이제는 모든 코드 라인을 읽는 대신 변경 의도를 검토한다.
3. **최적화 및 품질의 상당한 개선**[^36]
   1. Claude가 인간보다 훨씬 빠르게 엄청난 양의 코드를 작성할 수 있는 능력 덕분에 Scion은 Anthropic이 작업했던 코드베이스 중 가장 잘 테스트되고 잘 방어된 코드베이스 중 하나이다.
   2. 촉박한 일정에도 불구하고, Anthropic은 이전에 겪었던 모든 사소하지 않은 인프라 및 소스 제어 상호 작용에 대한 밀폐된 시뮬레이션을 구축할 수 있었으며, 퍼징 및 정교한 속도 제한도 구현했다.
   3. Claude는 또한 조상 쿼리에 대한 알고리즘 최적화와 같이 전문가가 며칠 또는 몇 주간의 분석과 튜닝이 필요했을 상당한 최적화를 쉽게 찾아냈고, 다음 날 다시 수행했다.

<img src="https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc706fa6efb4b9e5cd2566cb080acbfce7218042d-3840x4684.png&w=3840&q=75">

네이티브 Scion 저장소에서 관찰된 성능 개선 사항

### 3.3. 새로운 운영 우수성 및 사고방식의 변화[^37]

1. **모노레포 보안의 새로운 기반 마련**[^38]
   1. 대규모 모노레포에서 안전, 보안 및 규정 준수를 관리하는 것은 크기와 규모를 관리하는 것만큼 중요하다.
   2. Scion은 이러한 점을 처음부터 염두에 두고 구축되었다.
   3. 저장소에 대한 풍부한 액세스 제어와 개별 디렉터리에 권한을 적용하여 모노레포의 이점을 잃지 않고 가장 민감한 코드를 보호할 수 있는 기능을 지원한다.
   4. 또한, 구축된 코드 검토 도구는 승인에 대한 복잡한 의미론적 제약 조건을 표현할 수 있어, 주석만 있는 변경 사항과 민감한 논리적 변경 사항을 구분하여 인간 검토자가 가장 중요한 변경 사항에 집중할 수 있도록 한다.
2. **새로운 수준의 운영 우수성**[^39]
   1. Anthropic 팀은 Claude Tag를 적극적으로 사용하여 시스템의 각 구성 요소를 모니터링한다.
   2. 예를 들어, Claude에게 단일 구성 요소의 상태에 집착하도록 지시하는 Slack 채널을 만들었다.
   3. 이러한 Claude를 "슈퍼팬"이라고 부르며, `scion-daemon` 슈퍼팬, `scion-cache` 슈퍼팬, Antique 병합 큐 슈퍼팬 등이 있다.
   4. 이들은 원격 측정 및 로그에 액세스할 수 있으며, 차트를 새로 고치고 이상한 점을 찾는 것 외에는 할 일이 없는 숙련된 엔지니어처럼 행동한다.
   5. 모든 시스템에 대한 전통적인 경고도 있지만, 슈퍼팬은 이러한 경고를 단편적으로 보이게 하는 미묘하고 새로운 문제를 감지할 수 있다.
3. **기존 가정의 재고**[^40]
   1. 이 프로젝트는 인간 규모에 맞춰 설계된 다른 워크플로우를 매우 면밀히 검토하게 했다.
   2. 예를 들어, 적절한 병합 큐는 에이전트 규모에서는 별 의미가 없다.
   3. 수백 또는 수천 개의 변경 사항이 테스트가 실행되는 동안 병합될 수 있다면 CI는 무엇을 의미하는가?
   4. 병합 큐에 대한 전역 저장소 잠금이라는 업계 표준을 효과적으로 복제할 수 없었기 때문에, 대신 병합 후 및 배포 전 자동화 테스트에 투자했다.
   5. 이는 동시 변경 사항이 충돌할 수 있음을 의미하지만, Claude는 일반적으로 인간이 충돌을 식별하는 것보다 빠르게 이러한 충돌을 해결할 수 있다.

## 4. 더 넓은 생태계에 기여[^41]

Scion은 AI 에이전트의 역량 증가로 인해 발생하는 확장성 문제에 대한 Anthropic의 해답 중 하나이며, 다른 팀들이 유사한 문제를 해결하는 데 도움이 될 수 있는 사례를 공유한다.

### 4.1. Scion의 일반적인 사용 대체 불가능성 및 Anthropic의 특수성[^42]

1. **Git의 일반적인 사용 대체 불가능**[^43]
   1. Scion은 일반적인 용도로 Git을 대체하기에 적합하지 않다.
   2. 여기서 설명한 개념은 수만 명의 엔지니어 또는 수많은 에이전트가 코드를 왕성하게 작성하는 진정으로 거대한 모노레포에만 의미가 있다.
2. **Anthropic의 독특한 환경**[^44]
   1. Anthropic은 내부 사용을 위한 토큰 지출 능력이 다른 어떤 기업이 현실적으로 지출하고자 하는 것보다 훨씬 많다는 점에서 독특하다.
   2. 이는 자체 소프트웨어 개발 요구 사항을 해결하고 Claude의 기능을 테스트하기 위함이다.

### 4.2. Scion의 광범위한 적용의 어려움[^45]

1. **Git과의 상당한 차이점**[^46]
   1. Scion은 Git과 크게 다르므로, 기업은 개발 수명 주기의 모든 부분을 마이그레이션해야 한다.
   2. 또한 자체 코드 검토, 코드 검색 및 CI가 필요하다.
   3. Anthropic의 이러한 구성 요소는 매우 맞춤형이므로 다른 조직에서 채택하기 어려울 것이며, 모두를 만족시키려는 공개 버전을 구축하려는 시도는 실제로 유용하지 않을 수 있다.

### 4.3. Git 생태계에 대한 기여 및 협력 제안[^47]

1. **문제의 보편화 및 지식 공유의 중요성**[^48]
   1. 이러한 종류의 문제가 향후 6~12개월 내에 더 보편화될 것으로 예상되며, Git을 사용하는 모든 회사가 유사한 문제에 홀로 직면하는 것은 비효율적인 엔지니어링 자원 낭비일 것이다.
   2. 따라서 Anthropic이 할 수 있는 가장 영향력 있는 일은 사고방식을 공유하여 다른 개발자들이 전체 모델에서 벗어나지 않고도 Scion의 가장 성공적인 부분 중 일부를 Git에 적용할 수 있도록 하는 것이다.
2. **Git 서버 아키텍처 및 프로토콜 개선 제안**[^49]
   1. Git 서버는 Git 클라이언트와 동일한 방식으로 작동할 필요가 없으며, 상당한 확장성 개선을 제공하는 새로운 서버 아키텍처가 존재한다.
   2. Git 플랫폼은 Scion과 같은 포괄적인 서버 측 RPC를 제공할 수 있으며, Git 클라이언트가 통신하는 방법을 배울 수 있도록 포지 전반에 걸쳐 표준화된 방식으로 제공될 수도 있다.
   3. 협상 프로토콜도 오늘날과 정확히 같을 필요는 없으며, Git의 다양한 스파스 및 얕은 기능을 잘 조합할 수 있다.
3. **Git 커뮤니티와의 협력 강조**[^50]
   1. Git 커뮤니티는 수백만 명의 개발자를 위해 플랫폼을 확장하는 데 거의 20년을 보냈다.
   2. Anthropic의 기여는 훨씬 더 좁다. 에이전트 기반 소프트웨어 개발이 이러한 시스템과 어떻게 상호 작용하는지에 대한 초기 관점을 공유하여 GitHub, GitLab 및 OSS 커뮤니티와 협력하여 개발자의 변화하는 요구 사항을 지원하는 것이다.
   3. 소프트웨어 개발 수명 주기가 AI의 기하급수적 성장과 교차하는 시점에서 모두가 함께 노력해야 한다.

[^1]: Redesigning source control at Anthropic \ Anthropic — "Redesigning source control at Anthropic Oct 13, 2026 At Anthropic, coding is no longer the bottleneck to building systems or doing research. Claude is able to autonomously iterate on research loops, micro-optimize complex programs, and build new services from the ground up at a speed and scale we ha…"
[^2]: Redesigning source control at Anthropic \ Anthropic — "At Anthropic, coding is no longer the bottleneck to building systems or doing research. Claude is able to autonomously iterate on research loops, micro-optimize complex programs, and build new services from the ground up at a speed and scale we haven’t seen before. The bottleneck, now, is all of the…"
[^3]: Redesigning source control at Anthropic \ Anthropic — "At Anthropic, coding is no longer the bottleneck to building systems or doing research. Claude is able to autonomously iterate on research loops, micro-optimize complex programs, and build new services from the ground up at a speed and scale we haven’t seen before. The bottleneck, now, is all of the…"
[^4]: Redesigning source control at Anthropic \ Anthropic — "The bottleneck, now, is all of the developer infrastructure built for human scale: source control, builds, and CI. In May 2026, Anthropic averaged around 2,500 code changes merged per day; as of September, we merged over 30,000 per day. We don’t expect this rate of growth to slow down anytime soon; …"
[^5]: Redesigning source control at Anthropic \ Anthropic — "In order to support this growth, we built Scion, an in-house version control system, and fully migrated our monorepo from git in five months. We also built and shipped a code review surface (called Antique), code search, a rich source control IAM system, novel ways of managing and landing large amou…"
[^6]: Redesigning source control at Anthropic \ Anthropic — "Growing our monorepo Before we explore what we built, we should acknowledge how unusual our workload is. Unsurprisingly, Anthropic uses Claude to write software far more than almost any other company, so we’re often the first to see where tools built for human scale start to strain. Source control i…"
[^7]: Redesigning source control at Anthropic \ Anthropic — "Before we explore what we built, we should acknowledge how unusual our workload is. Unsurprisingly, Anthropic uses Claude to write software far more than almost any other company, so we’re often the first to see where tools built for human scale start to strain. Source control is just one example of…"
[^8]: Redesigning source control at Anthropic \ Anthropic — "Git is a decentralized system: every clone is a complete, self-contained repository that can compute diffs, read history and blame, and check out any revision while fully offline. For the vast majority of repositories, this is the right design, and it’s a large part of why git became the standard. A…"
[^9]: Redesigning source control at Anthropic \ Anthropic — "Git offers tools for working with a slice of a repository, such as shallow clones, sparse checkouts, and promisor remotes. Beyond these, there are standard workarounds for large monorepos, like internal git mirrors and repository snapshots (seeds) kept in blob storage. We’ve used all of them—at our …"
[^10]: Redesigning source control at Anthropic \ Anthropic — "Taking a step back, we noticed that, like most companies, we were using git as a centralized system with one authoritative copy, but nearly all of our clients were agents and jobs that are online by definition. The properties that make git excellent for distributed, offline work were actively underm…"
[^11]: Redesigning source control at Anthropic \ Anthropic — "Principles for agent-scale source control With agentic coding, many common assumptions about how software is developed are evolving. We embraced these changes when building Scion, which allowed us to take a fundamentally different approach than git on several core principles. Source control for huge…"
[^12]: Redesigning source control at Anthropic \ Anthropic — "Clients are always online. Git assumes that clients work offline and need a complete copy of the repository. Since nearly all of our clients are agents and jobs, we designed Scion’s client and protocols around a server that is always reachable, and have clients fetch data when they need it."
[^13]: Redesigning source control at Anthropic \ Anthropic — "Client-server asymmetry. In git, every client is capable of being a full-fledged server. In Scion, the server answers questions about file history and blame, creates commits, performs merges and rebases, and so on. The client maintains a bounded local object cache, lays out the working copy files on…"
[^14]: Redesigning source control at Anthropic \ Anthropic — "A comprehensive source control service can power many novel applications. With git, a CI job or tool that needs to ask a question about the repository, such as who last changed a line or how two commits are related, has to maintain a local copy of the repo or hope that vendor-specific APIs provide t…"
[^15]: Redesigning source control at Anthropic \ Anthropic — "Everything must be horizontally scalable. At our peak, we ran several hundred git mirrors, which significantly strained capacity and no longer scaled once the repo outgrew the mirrors’ disks or memory limits. In Scion, the repository’s data is distributed, and every component is independently scalab…"
[^16]: Redesigning source control at Anthropic \ Anthropic — "Commits must be cheap, incremental, and lock-free. In git, you commit locally and then push to share your work. In Scion, every commit, rebase, or merge happens on the server, so there’s nothing to push, but each of those operations needs to be fast. The cost of creating a commit and updating its do…"
[^17]: Redesigning source control at Anthropic \ Anthropic — "The working copy is optional, and sparse by design. Because our monorepo is so large, and because we check out code tens of millions of times a day for CI, we wanted to avoid checkouts whenever we could. With Scion, a CI job that needs the diff between a commit and its merge base, for example, can a…"
[^18]: Redesigning source control at Anthropic \ Anthropic — "How Scion works It’s helpful to understand how these principles came together in practice when building Scion. These insights can apply to other source control systems or, more broadly, to other stages of the software development lifecycle. Data structures In Scion, the unit of work is a “changeset,…"
[^19]: Redesigning source control at Anthropic \ Anthropic — "Data structures In Scion, the unit of work is a “changeset,” an entry in a write-ahead log. A changeset stores most of what you’d expect from a commit in git. But where a git commit stores a pointer to the tree, a changeset stores a list of the files that changed relative to its first parent,1 along…"
[^20]: Redesigning source control at Anthropic \ Anthropic — "In Scion, the unit of work is a “changeset,” an entry in a write-ahead log. A changeset stores most of what you’d expect from a commit in git. But where a git commit stores a pointer to the tree, a changeset stores a list of the files that changed relative to its first parent,1 along with content-ad…"
[^21]: Redesigning source control at Anthropic \ Anthropic — "This structure lets us accept changesets with very high throughput because there are no packfiles to accept, no locking or cross-server coordination, and no refs to move around. Scion does technically support refs, but since neither creating nor fetching commits involves them, moving one is a compar…"
[^22]: Redesigning source control at Anthropic \ Anthropic — "A changeset records only what’s changed, so on its own, it can’t quickly answer questions like who last edited a line or which commits affected a file. To answer those, Scion builds additional data structures from the changesets, including dedicated structures for file blame and path history and ski…"
[^23]: Redesigning source control at Anthropic \ Anthropic — "Scaling Scion A small fleet of Scion servers provides source control APIs for any operation a client needs, such as getting changesets, computing diffs, finding merge bases, and fetching blobs. All source control data is content-addressed, so a piece of data never changes once it’s stored, and any s…"
[^24]: Redesigning source control at Anthropic \ Anthropic — "A small fleet of Scion servers provides source control APIs for any operation a client needs, such as getting changesets, computing diffs, finding merge bases, and fetching blobs. All source control data is content-addressed, so a piece of data never changes once it’s stored, and any server can cach…"
[^25]: Redesigning source control at Anthropic \ Anthropic — "Scion’s many consumers no longer need to maintain local repositories of their own. Fetching and maintaining the repository used to be a significant maintenance burden for CI jobs or tools that needed to ask source control questions, particularly about commit ancestry and blame. Early in the migratio…"
[^26]: Redesigning source control at Anthropic \ Anthropic — "Scion’s scn client deviates from git’s fetch protocols in several important ways and, as a result, lends itself to a highly scalable architecture that requires significantly less CPU than git servers. Scion’s negotiation doesn’t tell the server what the client already has; instead, it operates exclu…"
[^27]: Redesigning source control at Anthropic \ Anthropic — "In the fleet, the client talks over a socket to a daemon, scion-daemon, that stores objects for the whole node. Most of our nodes need access to the monorepo, and jobs on the same node reuse most of the same objects. Each daemon starts from a periodically refreshed snapshot, then talks only to the t…"
[^28]: Redesigning source control at Anthropic \ Anthropic — "Each tier of this system maintains a cache hit rate of over 99% and does not require long-lived state, so it’s easy to scale up if needed. Our Scion infrastructure footprint is now 200x smaller than our previous git mirroring infrastructure in terms of CPU and memory requirements. CI and research jo…"
[^29]: Redesigning source control at Anthropic \ Anthropic — "What we learned building Scion We started building Scion around the same time as Claude Mythos Preview and Claude Tag became available internally. Both of these releases simultaneously amplified the need for Scion and meaningfully accelerated how quickly we could build it. Here’s a particularly stri…"
[^30]: Redesigning source control at Anthropic \ Anthropic — "We started building Scion around the same time as Claude Mythos Preview and Claude Tag became available internally. Both of these releases simultaneously amplified the need for Scion and meaningfully accelerated how quickly we could build it. Here’s a particularly striking example. Earlier in the ye…"
[^31]: Redesigning source control at Anthropic \ Anthropic — "We started building Scion around the same time as Claude Mythos Preview and Claude Tag became available internally. Both of these releases simultaneously amplified the need for Scion and meaningfully accelerated how quickly we could build it."
[^32]: Redesigning source control at Anthropic \ Anthropic — "Here’s a particularly striking example. Earlier in the year, we had largely handwritten the first version of the git-to-Scion ingestion pipeline as a prototype. We thought it was good—until we got our hands on an early internal snapshot of Claude Mythos Preview. We asked it to rewrite the whole thin…"
[^33]: Redesigning source control at Anthropic \ Anthropic — "https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fdd91296719203f38229824bb9bc9e9a61c76ed67-3840x2160.png&w=3840&q=75 What we learned building and operating Scion offers some interesting lessons for what building agent-scale software could l…"
[^34]: Redesigning source control at Anthropic \ Anthropic — "Rapid development with a small team will become more common. A team of seven people built both Scion and Antique (our code review tool, which we could easily write a whole other blog post about), not to mention half a dozen related systems, and fully migrated to them in five months. We did all this …"
[^35]: Redesigning source control at Anthropic \ Anthropic — "Engineers are no less valuable, but their work is changing. All of the engineers who worked on this system would now rate Claude as better at writing code than them. But our engineers still supplied the invaluable understanding of the high-level inter-system components and the design-level tradeoffs…"
[^36]: Redesigning source control at Anthropic \ Anthropic — "We were able to substantially improve optimization and quality. By virtue of Claude’s ability to write immense amounts of code much faster than we could ourselves, Scion is among the most well-tested and well-defended codebases we have ever worked on. Even on our tight timeline, we were able to buil…"
[^37]: Redesigning source control at Anthropic \ Anthropic — "https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fc706fa6efb4b9e5cd2566cb080acbfce7218042d-3840x4684.png&w=3840&q=75 We laid the groundwork for new forms of monorepo security. Managing safety, security, and compliance in a massive monorepo …"
[^38]: Redesigning source control at Anthropic \ Anthropic — "We laid the groundwork for new forms of monorepo security. Managing safety, security, and compliance in a massive monorepo is as important as managing the size and scale. We built Scion with these in mind from the start. It supports rich access control on repositories, as well as the ability to appl…"
[^39]: Redesigning source control at Anthropic \ Anthropic — "A new level of operational excellence is possible. Our team uses Claude Tag heavily, which has helped us monitor each component of the system. For example, we created Slack channels where we tasked Claude with being obsessively focused on the health of a single component. We call these Claudes “supe…"
[^40]: Redesigning source control at Anthropic \ Anthropic — "We’re completely rethinking our priors. This project prompted us to take a very hard look at other workflows designed for human scale. A proper merge queue, for example, doesn’t make much sense at agent scale. What does CI even mean when hundreds or even thousands of changes can merge while tests ar…"
[^41]: Redesigning source control at Anthropic \ Anthropic — "Contributing to the wider ecosystem We see Scion as just one part of the answer to the scaling concerns that increasingly capable AI agents have raised. We’re sharing these details as an example of how teams can tackle similar challenges, though we don’t expect our solution, or our considerations, t…"
[^42]: Redesigning source control at Anthropic \ Anthropic — "Scion is by no means a suitable replacement for git for general use. The concepts we’ve outlined here really only make sense for truly enormous monorepos, with either tens of thousands of engineers or swarms of agents prolifically writing code. Plus, Anthropic is unique in that our ability to spend …"
[^43]: Redesigning source control at Anthropic \ Anthropic — "Scion is by no means a suitable replacement for git for general use. The concepts we’ve outlined here really only make sense for truly enormous monorepos, with either tens of thousands of engineers or swarms of agents prolifically writing code."
[^44]: Redesigning source control at Anthropic \ Anthropic — "Plus, Anthropic is unique in that our ability to spend tokens for internal use far exceeds what any other business would realistically want to spend. We do this both to address our own software development needs, and to test Claude’s capabilities."
[^45]: Redesigning source control at Anthropic \ Anthropic — "Practically speaking, it’s difficult to offer Scion in a form that would be broadly useful to other organizations. It diverges significantly from git, meaning companies would need to migrate every piece of the development lifecycle, and it requires its own code review, code search, and CI. Our inter…"
[^46]: Redesigning source control at Anthropic \ Anthropic — "It diverges significantly from git, meaning companies would need to migrate every piece of the development lifecycle, and it requires its own code review, code search, and CI. Our internal versions of these components are highly bespoke, so they would be difficult for other organizations to adopt, a…"
[^47]: Redesigning source control at Anthropic \ Anthropic — "However, we anticipate that this class of problems will become more commonplace over the next six to 12 months, and it would be an inefficient use of engineering resources for every company using git to face similar challenges alone. Given that, we think the most impactful thing we can do is to shar…"
[^48]: Redesigning source control at Anthropic \ Anthropic — "However, we anticipate that this class of problems will become more commonplace over the next six to 12 months, and it would be an inefficient use of engineering resources for every company using git to face similar challenges alone. Given that, we think the most impactful thing we can do is to shar…"
[^49]: Redesigning source control at Anthropic \ Anthropic — "A git server doesn’t have to work the same way as a git client does; novel server architectures exist that provide significant scaling improvements. Git platforms can provide comprehensive server-side RPCs like Scion, perhaps even in a standardized way across forges that the git client can learn to …"
[^50]: Redesigning source control at Anthropic \ Anthropic — "Lastly, we want to acknowledge that the git community has spent nearly two decades scaling the platform for millions of developers. Our contribution is far narrower: sharing our early view into how agentic software development interacts with these systems, so that we can partner with GitHub, GitLab,…"
