# LWN.net Weekly Edition for May 21, 2026 — 한국어 기술 번역

- 원문 Bigpage: https://lwn.net/Articles/1072730/bigpage
- 원문 Edition: https://lwn.net/Articles/1072730/
- Article ID: `1072730`
- 선택 기준: LWN Archives에서 최신 Weekly Edition(2026-05-28, `1073782`)은 유료/최신호 가능성이 높아 건너뛰고, 바로 전 Weekly Edition(2026-05-21, `1072730`)의 공개 `bigpage`를 선택했다.
- 접근 확인: 공개 페이지에서 가져온 내용만 사용했으며, 로그인/유료 콘텐츠 우회는 하지 않았다.
- 생성시각: 2026-05-29T10:06:41+09:00

## 전체 요약

- 이번 호는 openSUSE 사이트 이용 약관의 연령 제한 논란, Fedora/openSUSE 같은 배포판 커뮤니티 운영 이슈, pgBackRest 프로젝트 지속 여부 등 커뮤니티 거버넌스와 프로젝트 유지보수의 현실을 다룬다.
- 저장장치와 파일시스템 영역에서는 buffered atomic writes, writethrough, `io_uring` 연계, COW(reverse mapping) 맥락 보존 등 데이터 무결성과 성능을 동시에 겨냥한 커널 논의가 이어진다.
- LSFMM+BPF Summit 관련 기사들은 정책 그룹(policy groups), HugeTLB live update 보존, BPF 기반 메모리 제어, swap table·flash-friendly swap·swap backend 추상화, per-CPU allocator, CXL, MGLRU 개선 등 Linux 메모리 관리의 핵심 변화들을 폭넓게 정리한다.
- OpenPGP 이메일 summit 기사는 PQC(post-quantum cryptography), Autocrypt v2, HKPv2, 키 이전(key migration) 등 장기 보안성과 실제 이메일 사용성 사이의 절충점을 설명한다.
- 보안 업데이트 표와 Kernel patches of interest는 배포판 보안 권고, 커널 릴리스, 아키텍처·빌드 시스템·드라이버·파일시스템·메모리·네트워킹·보안·가상화 패치 흐름을 운영자가 추적하기 쉽게 한데 모은다.

---

### [2026년 5월 21일 LWN.net 주간판에 오신 것을 환영합니다](https://lwn.net/Articles/1073760/)

#### 요약

- 이번 호에는 openSUSE 사이트 이용 약관(ToS)의 연령 제한 논란과 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit 보도가 포함되어 있습니다.
- 스토리지, 파일시스템, 메모리 관리, BPF, CXL, OpenPGP 커뮤니티 동향 등 다양한 커널·오픈소스 주제를 다룹니다.
- 짧은 소식, 공지, 보안 업데이트, 패치 관련 내부 페이지도 함께 제공됩니다.

이번 호에는 다음 특집 기사가 들어 있습니다.

- openSUSE “사이트 이용 약관”이 연령 제한에 대한 불만을 불러오다
  : 많은 Linux 사용자와
  개발자는 어린 나이에 시작했기 때문에, 더 어린 사람들을
  배제할 수 있는 제안은 반발을 낳았습니다.
- 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit의 계속되는 보도
  :
  - 버퍼드 원자적 쓰기(buffered atomic writes), 라이트스루(writethrough), 그리고 그 밖의 주제
  : PostgreSQL 등을 위한 버퍼드 원자적 쓰기로 가는 길을 다룬
  여러 세션 묶음
  - COW를 맥락 안에 두기(일명 익명 역방향 매핑, anonymous reverse mapping)
  : 커널의 역방향 매핑(reverse-mapping) 코드를
  갱신하고 단순화하려는 시도.
  - 커널을 위한 정책 그룹(policy groups)
  : 컨트롤 그룹(control-group) 모델에
  맞지 않는 정책을 관리하기 위한 더 나은 인터페이스가 있는가?
  - 라이브 업데이트 중 HugeTLB 보존
  : 실행 중인 시스템에서 커널을 교체하면서도,
  그 시스템에서 동작하는 가상 머신이 사용하는 거대 페이지(huge pages)를
  보존한다는 목표를 어떻게 지원할 것인가.
  - BPF로 메모리 관리 제어하기
  : BPF를 메모리 관리(memory-management) 서브시스템과
  통합하면 무엇이 가능할지, 그리고 그 과정의 장애물은 무엇인지.
  - 스왑 테이블(swap tables), 플래시 친화적 스왑(flash-friendly swap), swap_ops 등
  : 커널 스왑(swap) 서브시스템의 현재와 미래 상태를 다룬
  세 개의 세션.
  - per-CPU 메모리 할당자 개선
  : 확장성을 개선하기 위한 할당자가
  그 자체로 확장성 문제를 가지고 있습니다.
  - CXL에서 무슨 일이 진행 중인가
  : Compute Express Link(CXL) 장치를 커널에서
  지원하려는 노력의 진행 상황.
  - MGLRU를 어떻게 할 것인가
  : 커널에는 두 개의 별도 회수(reclaim) 구현이 있으며,
  그중 하나가 다세대 LRU(multi-generational LRU)입니다. 이 둘을 어떻게 하나로 통합할 수 있을까요?
  - 더 빠른 this_cpu 연산을 찾아서
  : x86이 아닌 아키텍처에서 per-CPU 변수를 더 빠르게 만들기 위한
  한 가지 방안.
- 제10회 OpenPGP 이메일 서밋
  : OpenPGP 커뮤니티에서 진행 중인 일을
  요약합니다.

이번 주 판에는 다음 내부 페이지도 포함되어 있습니다.

- 짧은 소식
  : 커뮤니티 전반의 짧은 뉴스 항목.
- 공지
  : 뉴스레터, 컨퍼런스, 보안 업데이트, 패치 등.

이번 주 판도 즐겁게 읽어 주시기 바랍니다. 늘 그렇듯 LWN.net을 후원해 주셔서 감사합니다.

[댓글 (게시된 글 없음)](https://lwn.net/Articles/1073760/#Comments)

### [openSUSE “사이트 이용 약관”이 연령 제한에 대한 불만을 불러오다](https://lwn.net/Articles/1072689/)

#### 요약

- openSUSE의 [사이트 이용 약관](https://en.opensuse.org/Terms_of_site)(terms of site, ToS)이 웹 사이트 사용자를 “만 16세 이상 또는 관할권의 성년 연령 이상”으로 제한하면서 커뮤니티의 반발을 샀습니다.
- 비판자들은 단순 열람까지 막는 듯한 문구가 Linux와 오픈소스에 어린 나이에 참여해 온 관행과 맞지 않으며, openSUSE 행동 강령(code of conduct)의 포용 원칙에도 어긋난다고 지적했습니다.
- SUSE 측은 이 요구가 프로젝트나 openSUSE 이사회가 요청한 것이 아니라 법무 검토 과정에서 나온 것이라고 설명했고, 이후 일반적인 공개 콘텐츠 열람에는 연령 제한이 없도록 문구를 수정하기로 했습니다.
- 다만 16세 미만 사용자의 계정 생성과 기여에는 “검증 가능한 부모 또는 법적 보호자 동의(verifiable consent)”를 어떻게 처리할지가 아직 남은 과제로 제시되었습니다.

작성:

Joe Brockmeier

2026년 5월 19일

Linux 커뮤니티의 많은 사람은 아주 어린 나이에, 흔히 16번째 생일이 되기도 한참 전에 이 운영체제를 사용하기 시작했고 오픈소스에 기여하기 시작했습니다. 따라서 openSUSE의 [사이트 이용 약관](https://en.opensuse.org/Terms_of_site)(ToS)이 최근 바뀌어 프로젝트 웹 사이트 사용자가 자신의 관할권에서 “만 16세 이상 또는 성년 연령 이상”이어야 한다고 요구하자 반대가 제기되었습니다.[^c01n1] 이후 약관은 수정되었지만, 16세 미만 사용자가 계정을 만들려면 여전히 부모의 승인이 필요합니다.

#### 들어오려면 16세 이상이어야 함

연령 제한은 [사이트 이력에 따르면](https://en.opensuse.org/index.php?title=Terms_of_site&diff=prev&oldid=203579) 2026년 3월 10일에 추가된 것으로 보입니다. openSUSE 사이트 약관은 사이트를 조금이라도 사용하는 것이 ToS에 동의한다는 뜻이라고 명시했습니다. “어느 시점이든 귀하에게 약관이 더 이상 수용 가능하지 않다면, 즉시 이 웹 사이트의 모든 사용을 중단해야 합니다.” 제한 조항이 16세 미만의 사용도 금지했기 때문에, 이 ToS는 더 어린 사용자에게 openSUSE 문서, 블로그 글 등을 읽는 것조차 하지 말라고 말하는 셈이었습니다.

아마 SUSE의 법무 부서 누군가는 이런 문구가 필요하고 어떤 식으로든 집행 가능하다고 믿었을지도 모릅니다. 현실에서는 openSUSE 웹 사이트를 단순히 둘러보는 사람들의 압도적 다수가, 특별히 찾지 않는 한 ToS를 보거나—하물며 동의하거나—할 가능성은 낮습니다.

하지만 ToS는 openSUSE에 대한 [기여](https://en.opensuse.org/Terms_of_site#Contributions_to_openSUSE), [Open Build Service](https://openbuildservice.org/) 사용 등도 포괄합니다. openSUSE를 가볍게 쓰는 사용자에게는 영향을 주지 않을 수도 있지만, (준수된다면) openSUSE 프로젝트에 의미 있는 방식으로 참여하는 것은 막게 됩니다. 작성된 그대로라면, ToS는 16세 미만 사용자가 부모의 허락을 받더라도 사이트를 *읽는* 것조차 허용하지 않았습니다.[^c01n2]

5월 8일, [Teckids](https://teckids.org/) 창립자이자 의장인 Dominik George는 openSUSE 프로젝트 메일링 리스트에서 이 제한에 대해 [불만을 제기했습니다](https://lwn.net/ml/all/01db98bc-ee20-4833-978f-69811119778c%40naturalnet.de/). 그는 어린이를 위한 디지털 공간을 다룬 경험이 10년이 넘는다고 말했습니다. “그래서 저는 장담할 수 있습니다. 미성년자를 금지해야 할 법적 이유는 없습니다.”

그는 또한 새 약관이 [openSUSE의 행동 강령](https://en.opensuse.org/Code_of_Conduct)에도 어긋난다고 주장했습니다. 이 강령은 프로젝트가 여러 요소—나이를 포함하되 이에 한정되지 않는—와 관계없이 “모두에게 긍정적인 경험을 제공하는 데 전념한다”고 말합니다. George는 프로젝트가 약관 변경을 되돌리거나, 적어도 계정 생성에만 적용되도록 문구를 고쳐야 한다고 요구했습니다.

일부 다른 Linux 프로젝트도 계정 생성에 연령 요건을 두고 있지만, 제가 찾아본 바로는 단순히 웹 사이트를 둘러보는 데까지 연령 요건을 부과하려는 곳은 없었습니다. [Fedora Accounts](https://accounts.fedoraproject.org/)의 새 계정 양식(직접 링크할 수 없음)은 사용자가 16세 이상임을 확인하도록 요구합니다. Canonical의 [서비스 약관](https://canonical.com/legal/terms-of-service)은 계정을 만들려면 사용자가 13세 이상이어야 하고, 13세에서 18세 사이에는 부모의 허락을 받아야 한다고 요구합니다. Debian에는 중앙화된 계정 서비스가 없지만, 제가 살펴본 여러 서비스 중 계정 생성에 연령 요건을 둔 곳은 없었습니다.

#### 논의

5월 11일, Luboš Kocman은 George의 피드백을 SUSE의 법무 및 데이터 프라이버시 팀과 공유했다고 [답했습니다](https://lwn.net/ml/all/CAKVpbdB8jS3OtF-osteh2AxbB7e7_Ph-oXNfZZScYVehPjo2zA@mail.gmail.com/). openSUSE 이사회 구성원이자 SUSE 직원인 Jeff Mahoney는 그 연령 요건이 프로젝트나 [openSUSE 이사회](https://en.opensuse.org/openSUSE:Board)가 요청한 것이 아니라고 [말했습니다](https://lwn.net/ml/all/fc46c825-9252-4680-928b-3f845ec6a430@suse.com/). “이사회(또는 이사회 주변) 구성원 중에는 16세보다 어린 나이에 Linux를 사용하기 시작한 사람이 있으며, 의도는 젊은 사람들의 참여를 금지하는 것이 아니었습니다.” 그는 ToS를 “미국 중심적이지 않게” 갱신해 달라는 요청이 있었고, 그것이 SUSE 법무팀의 검토로 이어졌다고 말했습니다.

Neal Gompa는 Fedora가 유럽연합의 [일반 개인정보 보호법](https://gdpr-info.eu/)(General Data Protection Regulation, GDPR)을 준수하기 위해 최소 연령 요건을 13세에서 16세로 올릴 필요가 있었다고 [말했습니다](https://lwn.net/ml/all/CAEg-Je-cpYZttYvYnCRLxcbVSSBq3Uzk+CQBZvjZjf2OdpfROA@mail.gmail.com/). 사용자가 계정을 만들 때, 또는 어떤 주체가 개인 식별 정보(personally-identifiable information)를 수집할 때 부모 동의가 언제 필요한지를 둘러싸고 다소 긴 논쟁이 이어졌습니다. George는 웹 사이트 *사용*에 최소 연령을 요구하는 EU 법은 없다고 [말했고](https://lwn.net/ml/all/e6f916ce-2c64-4dc0-9855-eec4442f2fc8@naturalnet.de/), [나중의 답변](https://lwn.net/ml/all/9BB784A1-B9F1-437B-8F00-B78A8B6CAEB2@naturalnet.de/)에서는 계정 등록에는 아마도 계약법 때문에 보호자 동의가 필요할 것이라고 했습니다. “하지만 프라이버시 법이 부과한 제한 때문은 아닙니다.”[^c01n3]

Patrick Fitzgerald는 GDPR의 관련 부분을 “속독했다”고 [말하며](https://lwn.net/ml/all/kcEE.yImoiegMTJ6Rd9s9M+WHGQ.gKM8QGPh3AE@uklonkpo01.i-layer.local/), 그것이 적용된다고 생각하지 않는다고 했습니다. “어린 사용자를 막아야 한다는 법적 요구 사항은 전혀 보이지 않습니다. 저는 14세에 컴퓨터를 쓰기 시작했습니다. 물론 그때는 인터넷이 널리 이용 가능해지기 조금 전이었습니다.”

몇 차례 의견 교환이 있은 뒤, George는 미성년자가—아마 부모 동의를 통해서일 텐데, 그는 이를 명시적으로 말하지는 않았습니다—약관을 수락할 방법이 있는 한 openSUSE가 “전 세계의 모든 계약법을 ToS에 복사해 붙여 넣는 것”에는 “대체로 괜찮다”고 [말했습니다](https://lwn.net/ml/all/010F5E74-508D-41C7-9430-4F92F103D363@naturalnet.de/). 하지만 그는 그런 접근법을 택하지는 않을 것이라고 했습니다. “중복되고 지루하며, 불필요한 일이기 때문”입니다. 다만 그는 “현실에서 이런 고려 사항들이 그렇게 사소하지는 않다”는 점은 인정했습니다.

#### 되돌림

5월 13일, Kocman은 이 사안이 SUSE 법무팀에 가 있으며 자신이 매일 상기시키고 있다고 메일링 리스트에 [답했습니다](https://lwn.net/ml/all/CAKVpbdAyLhkjWc+ZR4JBE0xNbb2kf9pDENCD97yutv1brbeyMg@mail.gmail.com/). 5월 15일, Jeff Mahoney는 SUSE 법무팀이 문구를 다음과 같이 바꾸는 데 동의했다고 리스트에 [업데이트를 제공했습니다](https://lwn.net/ml/all/23f68197-28fa-425a-8cd4-0d84216bd83a%40suse.com/).

> openSUSE 계정을 생성함으로써, 귀하는 자신이 만 16세 이상이거나 귀하 관할권의 디지털 동의 연령(age of digital consent) 이상임을 진술합니다. 귀하가 만 16세 미만(또는 귀하 관할권에 적용되는 디지털 동의 연령 미만)인 경우, 부모 또는 법적 보호자의 검증 가능한 동의가 있을 때에만 계정을 만들 수 있습니다. 이 사이트에서 공개적으로 이용 가능한 콘텐츠를 일반적으로 둘러보거나 수동적으로 접근하는 데에는 어떠한 연령 요건도 적용되지 않습니다.

그는 일이 끝난 것은 아니라고 덧붙였습니다. “우리는 16세 미만 기여자를 금지하고 싶지도 않지만, 아직 ‘검증 가능한 동의’를 처리할 시스템이 마련되어 있지 않습니다.” 그는 그것이 미국과 EU에서 법적 요구 사항이라고 말했습니다. 그는 공유할 내용이 생기면 커뮤니티에 업데이트를 가져오겠다고 약속했습니다.

SUSE가 “검증 가능한 동의”에 어떻게 접근할지 지켜보는 것은 흥미로울 것입니다. 부모나 보호자가 동의했다는 것을 보여 주려면, SUSE가 (적어도 일부) 사용자의 나이도 확인해야 함을 뜻하는 듯합니다. 연령 증명(age attestation)과 연령 확인(age verification)이라는 주제는 여러 이유로 최근 [논란이 되어 왔습니다](https://lwn.net/Articles/1064706/). 사용자에게 나이 증명을 요구하는 어떤 시스템도 인기를 얻기는 어려울 가능성이 큽니다.[^c01n4]

전 세계 여러 정부는 다양한 방식으로 서비스 제공자에게 책임을 떠넘겨, 인터넷을 어린이에게 “안전하게” 만들겠다며 효과가 의심스러운 안전 범퍼를 세우도록 하는 법을 계속 장부에 올리고 있습니다. 그러나 오픈소스 커뮤니티 참여에 연령 장벽(age-gating)을 요구하는 법적 요건이 누구를 더 안전하게 만드는지는 보기 어렵습니다. 그런 요건은 오픈소스 프로젝트나 그 후원자의 법적 책임만 키울 뿐입니다.[^c01n5]

[댓글 (17개 게시됨)](https://lwn.net/Articles/1072689/#Comments)

[^c01n1]: 오픈소스 프로젝트의 이용 약관(ToS)은 단순한 웹 서비스 약관을 넘어, 코드 기여, 계정 생성, 빌드 인프라 사용 같은 커뮤니티 참여 경로를 규정할 수 있습니다. 따라서 연령 제한 문구 하나가 문서 열람과 기여 참여 모두에 영향을 미치는 실질적 장벽이 될 수 있습니다.
[^c01n2]: Open Build Service(OBS)는 openSUSE와 여러 배포판에서 패키지를 빌드하고 배포하는 핵심 인프라입니다. 이런 계정 기반 개발 도구에 접근할 수 없으면 패키징, 테스트, 버그 수정 같은 실제 기여가 크게 제한됩니다.
[^c01n3]: GDPR은 아동의 개인정보 처리에 부모 동의가 필요한 경우를 규정하지만, 모든 웹 사이트의 단순 열람에 일괄적인 최소 연령을 부과하는 법은 아닙니다. 실제 적용은 계정 생성, 개인정보 수집 범위, 계약 관계, 각 회원국의 디지털 동의 연령 설정에 따라 달라질 수 있습니다.
[^c01n4]: 연령 확인 시스템은 프라이버시와 보안 측면에서 민감합니다. 신분증, 결제 정보, 제3자 검증 서비스 등을 요구하면 개인정보 유출 위험이 커지고, 익명·가명 참여가 중요한 자유 소프트웨어 커뮤니티의 진입 장벽도 높아질 수 있습니다.
[^c01n5]: “연령 장벽”(age-gating)은 특정 나이 미만의 접근이나 참여를 막는 정책·기술적 조치를 뜻합니다. 성인 콘텐츠나 상업 서비스에서는 흔히 논의되지만, 문서 읽기와 공개 개발 참여가 중심인 오픈소스 프로젝트에 적용하면 교육·멘토링·초기 기여 기회를 줄이는 부작용이 큽니다.

---

### [버퍼드 원자적 쓰기, 라이트스루, 그리고 그 밖의 것들](https://lwn.net/Articles/1072019/)

#### 요약

- 2026년 LSFMM+BPF에서 PostgreSQL을 주요 사례로, 버퍼드 원자적 쓰기(buffered atomic writes)의 필요성과 설계 방향이 논의되었다.
- PostgreSQL은 현재 찢긴 쓰기(torn writes)를 피하기 위해 전체 페이지 쓰기(full-page-writes)와 WAL(write-ahead log)에 의존하지만, 8KB 원자적 쓰기가 가능하면 성능과 저장 공간 효율이 크게 개선될 수 있다.
- `RWF_WRITETHROUGH`는 데이터를 페이지 캐시(page cache)에 복사한 뒤 즉시 블록 장치(block device)로 I/O를 발행하는 새 `pwritev2()` 플래그로 제안되었다.
- 라이트스루(writethrough)는 라이트백(writeback) 경로와 원자성 요구 사항을 맞추기 어려운 문제를 피하고, 버퍼드 I/O(buffered I/O)에서 원자적 쓰기를 구현하기 위한 단순한 기반이 될 수 있다.
- 초기 성능 측정에서는 여러 파일에 대한 다중 스레드 랜덤 쓰기에서 개선이 보였지만, 같은 파일에 쓰는 경우 inode 잠금(inode lock) 경합으로 성능 저하가 나타났다.

글쓴이

Jake Edge

2026년 5월 14일

LSFMM+BPF

2026년 [Linux Storage, Filesystem, Memory Management, and BPF Summit](https://events.linuxfoundation.org/lsfmmbpf/) 시작 부분에서 이어진 두 세션(결국 세 번째 시간대까지 넘쳐 이어졌다)에서는 [원자적 버퍼드 쓰기 기능](https://lwn.net/Articles/1060063/)이 논의되었다. 첫 번째 세션에서 Pankaj Raghav와 Andres Freund는 PostgreSQL 데이터베이스 시스템이라는 해결책의 사용 사례와 함께, 문제의 배경을 설명했다. 두 번째 세션에서는 Ojaswin Mujoo가 라이트스루(writethrough)에 기반한 접근법으로 이 기능을 발전시킬 수 있는 잠재적 경로를 설명했다. 여기서 라이트스루란 사실상 커널이 페이지 캐시(page cache)의 라이트백(writeback)을 기다리지 않고 데이터를 즉시 디스크에 쓰는 것을 뜻한다.[^p03n1] 예상할 수 있듯이, 두 트랙이 합쳐진 이 세션들에서는 모인 파일시스템(filesystem) 및 스토리지(storage) 개발자들 사이에 상당한 토론이 오갔다.

![[Andres Freund]](https://static.lwn.net/images/2026/lsfmb-freund-sm.png)

Freund는 PostgreSQL이 현재 8KB 기본 페이지의 [찢긴(부분) 쓰기(torn writes)를 방지하기 위해](https://transactional.blog/blog/2025-torn-writes) 무엇을 하는지 설명하는 것으로 시작했다. 블록 계층(block layer)에서 원자적 보장(atomic guarantees)을 제공하지 않으면, PostgreSQL은 페이지가 완전히 기록되도록 보장하기 위해 [전체 페이지 쓰기(full-page-writes)](https://wiki.postgresql.org/wiki/Full_page_writes) 기능을 사용해 선행 기록 로그(write-ahead log, WAL)에 기록한다. 원자적 8KB 쓰기가 가능해지면 여러 이점이 따른다. 예를 들어 전체 페이지 쓰기를 끄면 초당 트랜잭션 수(transactions per second, TPS)가 약 1.7배 증가하고, TPS 변동성도 14배 줄어든다. 또한 페이지의 디스크상 무결성을 보장하기 위해 같은 페이지를 두 번 쓸 필요가 없어지므로 쓰기 증폭 계수(write amplification factor, WAF)도 낮아진다. 한편 [시점 복구(point-in-time recovery)를 위한 연속 아카이빙](https://www.postgresql.org/docs/current/continuous-archiving.html)은 WAL을 아카이브 로그에 저장해야 하므로 저장 공간 사용량이 빠르게 크게 늘 수 있다고 그는 말했다. 간단한 벤치마크에서는 전체 페이지 쓰기를 사용할 때 누적 WAL 크기가 14배 증가하는 것으로 나타났다.[^p03n2]

한 참석자는 PostgreSQL에 필요한 원자적 페이지 크기가 얼마인지 물었다. Freund는 PostgreSQL이 8KB보다 더 큰 덩어리로 쓸 수 있기를 바라지만, 필요한 것은 8KB 덩어리가 찢기지 않는다는 보장뿐이라고 말했다. Randy Jennings는 스토리지가 이러한 원자적 쓰기를 지원할 수 있어야 하는지 물었다. Freund는 원자적 쓰기 기능에는 그것이 필수라고 답했다.

Ted Ts'o는 “원자적 쓰기 사가(whole atomic-writes saga)”가 수년간 이어져 왔으며, 예를 들어 이전 여러 서밋에서도 다루어졌다고 지적했다. 그는 클라우드 업체들이 쓰는 소프트웨어 정의 스토리지(software-defined storage)가 직접 I/O(direct I/O)를 사용하는 데이터베이스에 필요한 원자적 보장을 제공할 수 있었기 때문에 이 논의가 시작되었다고 말했다. 그 기능을 사용하면 2배의 성능 개선이 흔했다. 이제 PostgreSQL처럼 버퍼드 쓰기(buffered writes)를 사용하는 데이터베이스도 같은 성능 향상을 얻고자 하며, 이것이 버퍼드 원자적 쓰기(buffered-atomic-writes) 기능이 등장한 이유다. 특히 이제 NVMe 장치가 클라우드 스토리지에서 가능했던 것과 같은 원자적 쓰기 단위(atomic-write granularity)를 제공할 수 있게 되었기 때문에 더 그렇다고 그는 말했다.

![[Pankaj Raghav]](https://static.lwn.net/images/2026/lsfmb-raghav-sm.png)

Raghav는 버퍼드 I/O에 쓰이는 라이트백(writeback)이 원자적 쓰기와 근본적으로 양립하기 어려운 이유를 설명했다. 라이트백이 일어날 때까지 페이지를 페이지 캐시에 남겨두면, 그 페이지들이 수정될 수 있는 긴 시간 창이 생긴다. 또한 메모리 압박(memory pressure)이 있을 경우 페이지 폴트(page faults)나 회수(reclaim)가 잠재적으로 찢긴 쓰기를 초래할 수 있다.

그래서 [`pwritev2()`](https://man7.org/linux/man-pages/man2/pwritev2.2.html)에 대해 새 플래그 `RWF_WRITETHROUGH`가 제안되었다. 이 플래그는 데이터를 페이지 캐시에 복사한 뒤, 제공된 버퍼의 데이터를 블록 장치에 쓰기 위해 즉시 직접 I/O를 발행한다. Matthew Wilcox는 새 플래그가 `RWF_DSYNC`와 어떻게 다른지 물었다. Jan Kara는 `RWF_DSYNC`가 쓰기 작업이 디스크까지 내려가 성공적으로 완료되었다는 훨씬 더 강한 보장을 제공한다고 말했다. `RWF_WRITETHROUGH`는 단지 쓰기가 발행되었음을 나타낼 뿐이다. Raghav는 `RWF_WRITETHROUGH` 플래그 자체가 원자적 동작을 구현하는 것은 아니며, 그 동작은 이 플래그를 사용하는 별도 기능으로 추가되어야 한다고 말했다.[^p03n3]

Christoph Hellwig는 버퍼드 원자적 쓰기의 필요성을 만들어내는 PostgreSQL의 버퍼드 I/O 사용 방식을 좋아하지는 않지만, `RWF_WRITETHROUGH` 자체에는 문제가 없다고 말했다. Amir Goldstein은 웃음 속에서 “제 생각엔 그가 ‘반대 없음(no objection)’이라고 말한 것 같네요”라고 말했다.

John Garry는 `pwritev2()` 호출이 하드웨어가 원자적 쓰기를 지원할 수 있는지, 그리고 이를 수행하는 데 어떤 정렬(alignment)이 필요한지를 어떻게 확실히 알 수 있는지 궁금해했다. Raghav는 직접 I/O(`O_DIRECT`) 원자적 쓰기에 쓰이는 것과 같은 메커니즘을 사용할 계획이라고 말했다. Ts'o는 `O_DIRECT`에 대해서는 이 문제가 이미 해결되었다고 말했다. 정렬 요구 사항은 블록 장치에서 오며, `RWF_ATOMIC` 플래그와 함께 `pwritev2()`를 사용한다는 것은 모든 버퍼가 적절히 정렬되어 있음을 뜻한다.

middle-ad

Wilcox는 작게 시작하자고 제안했다. 예컨대 `RWF_WRITETHROUGH`가 데이터를 페이지 캐시에 복사한 뒤 수행하는 직접 I/O를 사용해 `RWF_DSYNC`를 구현해볼 수 있다는 것이다. 그러나 Hellwig는 쓰기에서 직접 I/O 경로를 문자 그대로 사용하는 것이 타당하다고 보지는 않았다. 단순히 일반적인 블록 쓰기(block write)로 구현하는 편이 더 나을 수 있다는 것이다. 직접 I/O 경로는 고려하지 않아도 될 수 있는 많은 코너 케이스(corner cases)를 처리하지만, 그는 그것이 어디까지나 “직감(gut feeling)”일 뿐이므로 실제로 시도해볼 가치는 있다고 말했다. 그는 일부 개발자들이 직접 I/O 코드 경로의 복잡성에 대해 불만을 제기해왔으므로, 이번 작업이 더 단순한 인터페이스를 위한 출발점이 될 수도 있다고 언급했다.

#### 라이트스루

다음 발표자는 Mujoo였다. 그는 커널에서 원자적 쓰기 지원이 어떻게 발전해왔는지 시간순으로 설명하는 것으로 시작했다. 직접 I/O의 경우 2025년 1월 Linux 6.13에서 단일 파일시스템 블록(filesystem block)을 원자적으로 쓸 수 있었다. 2025년 6월에는 6.16 커널이 여러 파일시스템 블록을 원자적으로 처리할 수 있는 기능을 추가했다. 버퍼드 I/O 쪽에서는 세 가지 설계가 있었고, 2026년 4월 라이트스루 접근법으로 이어졌다. 처음 두 설계는 특정 쓰기 작업이 라이트백 경로와 쉽게 통신해 원자적으로 처리되도록 보장할 방법이 없다는 문제를 겪었다.

![[Ojaswin Mujoo]](https://static.lwn.net/images/2026/lsfmb-mujoo-sm.png)

이전 세션에서 언급했듯이, 라이트스루 접근법은 `pwritev2()` 호출에서 장치로의 I/O를 즉시 시작함으로써 그 문제를 피한다. 이렇게 하면 페이지 캐시 페이지에 대해 원자적 범위(atomic ranges)를 추적할 필요가 없어진다. 그 범위를 추적하는 일이 처음 두 설계를 더 복잡하게 만들었으므로, 쓰기 경로(write path)와 I/O 제출 경로(I/O-submission path)를 결합하면 일이 단순해질 것으로 보인다. 그는 같은 기법이 원자적 쓰기 외의 다른 용도에도 쓰일 수 있다고 말했다.

그는 라이트스루 메커니즘을 설명하는 순서도를 차례로 짚었다. 쓰기에서 데이터가 페이지 캐시로 복사되고, folio 범위로부터 [`bio_vec`](https://elixir.bootlin.com/linux/v7.0.6/source/include/linux/bvec.h#L19)이 생성되며, I/O 작업이 시작된다. 비동기 쓰기(asynchronous write)가 아니면, 최초 쓰기는 블록 I/O(block I/O)가 완료되기를 기다린 뒤 호출자에게 반환된다. 비동기 I/O의 경우 I/O 완료 처리는 직접 I/O에서 처리되는 방식과 유사하게 백그라운드의 워크큐(workqueue)가 담당한다.

그는 여러 사용 사례가 있다고 말했다. 버퍼드 원자적 쓰기는 원자적 범위를 추적하기 위한 추가 코드 없이 라이트스루에 기반할 수 있다. `RWF_DSYNC`를 사용한 쓰기는 [`generic_write_sync()`](https://elixir.bootlin.com/linux/v7.0.6/source/include/linux/fs.h#L2648) 호출을 제출 단계(submission phase)에서 완료 단계(completion phase)로 옮김으로써 라이트스루를 사용해 비동기 버퍼드 쓰기를 지원할 수 있다. 라이트스루가 두 단계 사이의 공유 컨텍스트(shared context)를 제공하기 때문이다. 마찬가지로 강제 단위 접근(forced unit access, FUA)을 동반한 `RWF_DSYNC`와 `RWF_DONTCACHE` 쓰기처럼, 쓰기와 라이트백 사이의 추적이 필요한 다른 사용 사례도 라이트스루를 사용할 수 있을지 모른다.

그는 여러 스레드가 각기 다른 파일에 랜덤 쓰기를 수행할 때 쓰기 속도가 35~60% 개선됨을 보여주는 성능 그래프 몇 개를 제시했다. 그러나 모든 스레드가 같은 파일에 쓰는 경우 최대 65%의 성능 저하도 나타났다. 그는 이것이 I/O 제출 경로 안에서 잡히는 inode 잠금(inode lock) 경합 때문이라고 보고 있다.[^p03n4]

[^p03n1]: 커널 관점에서 라이트스루는 페이지 캐시에 더티(dirty) 상태로 오래 머무르는 시간을 줄여, 이후 라이트백 스레드가 임의 시점에 데이터를 내보내며 원자성 보장을 깨뜨릴 가능성을 낮춘다.
[^p03n2]: 파일시스템과 데이터베이스 런타임(runtime) 모두에서 WAL 증가는 쓰기 대역폭, 체크포인트(checkpoint), 복구 시간, 아카이브 저장 공간 비용에 직접 영향을 준다.
[^p03n3]: `RWF_WRITETHROUGH`는 “즉시 I/O를 제출한다”는 전달 경로 의미에 가깝고, 실제 원자성은 블록 장치의 지원, 정렬 조건, 파일시스템의 범위 검증 같은 별도 조건이 함께 맞아야 제공된다.
[^p03n4]: 같은 inode에 대한 동시 쓰기는 파일시스템 내부 직렬화 지점을 만들 수 있으며, 이는 라이트스루처럼 I/O 제출을 쓰기 경로에 붙이는 설계에서 더 두드러진 병목으로 나타날 수 있다.

---

### [버퍼드 원자적 쓰기, writethrough, 그리고 그 밖의 것들](https://lwn.net/Articles/1072019/) (계속 2부)

#### 요약
PostgreSQL 같은 실제 워크로드에서 버퍼드 원자적 쓰기(buffered atomic writes)와 writethrough 의미론을 어떻게 정의하고 구현할지, 그리고 새 플래그를 계속 추가하는 대신 `io_uring`으로 I/O 단계를 더 세분화할 수 있는지를 두고 논의가 이어졌다.

Ts'o는 그 성능 저하가 실제로 PostgreSQL에 문제가 될지 궁금해했다. Freund는 여러 스레드가 쓰기를 수행하지만, 실제 워크로드에서 같은 파일에 대한 동시 쓰기가 많이 발생할지는 자신도 분명하지 않다고 말했다.

Hellwig는 I/O 제출(submission) 과정 전체에 걸쳐 inode 잠금을 유지할 실질적인 이유가 없으므로, inode 잠금을 잡고 있는 임계 구역을 줄일 수 있다고 보았다. Mujoo는 현재 inode 잠금을 잡은 채 실행되는 코드 일부를 분리하는 방안을 살펴볼 수 있다고 했고, Hellwig는 그것이 가능할 것이며 다른 코드 경로를 단순화하는 데도 도움이 될 수 있다고 생각했다.

writethrough 작업이 수행되는 동안 페이지 캐시(page cache)의 페이지에 writeback이 발생하지 않도록 막아야 하는 필요성에 대한 논의도 있었다. Hellwig는 체크섬(checksum) 같은 것에 영향을 줄 수 있는 전송 중(in-flight) 버퍼의 변경을 막아야 하며, 이는 writeback 잠금을 잡는 방식으로 달성할 수 있다고 말했다. 그는 [iomap 계층](https://docs.kernel.org/filesystems/iomap/)의 기본 모드는 페이지 잠금은 잡지 않고 writeback 잠금만 잡은 채 I/O를 제출하는 것이라고 말했다.[^p04n1]

논의는 [`xa_lock`](https://www.kernel.org/doc/html/latest/core-api/xarray.html#locking)에 대한 경합을 줄이고, direct I/O에서 쓰는 것처럼 정렬된(aligned) 버퍼드 I/O에 공유 잠금을 사용할 수 있는지로 옮겨갔다. Kara는 그것이 합리적인 생각이라고 보는 듯했고, Hellwig는 그런 잠금을 도입하기에 적절한 시점은 새 플래그(예: `RWF_WRITETHROUGH`)가 추가될 때라고 제안했다. Hellwig는 제안된 writethrough 기능이 `RWF_DSYNC`와 거의 같지만, 블록 장치가 실제로 캐시를 디스크로 flush한다는 보장은 하지 않는다는 점이 다르다고 말했다. 공유 잠금을 나중에 추가하면 그 사용을 제어하기 위한 새 플래그를 그때 추가해야 할 것이므로, 그의 생각에는 writethrough 기능과 함께 이를 포함하는 편이 타당하다.

#### io_uring

Josef Bacik은 이런 종류의 대화를 하는 것이 싫다며, 한걸음 물러서서 새 플래그를 추가해 처리하는 I/O 경로의 여러 특수 사례들을 어떻게 피할지 살펴보고 싶다고 말했다. "여기서 우리가 해야 할 일은 이것을 처리하는 방식을 다시 생각하는 것"이라며, 잠재적 해법으로 [io_uring](https://man7.org/linux/man-pages/man7/io_uring.7.html)을 검토해보자고 제안했다.[^p04n2] I/O에 필요한 각각의 저수준 작업(페이지 캐시 갱신, I/O 작업 제출 등)을 별도의 io_uring 작업으로 만들고, 이를 사용자 공간이 원하는 어떤 I/O 방식으로든 조립할 수 있게 하자는 것이다.

그렇게 하면 사용자 공간이 "이 모든 서로 다른 기능을 섞어 맞출" 수 있고, 커널 개발자들이 모든 다양한 특수 사례에서 새 `pwritev2()` 플래그들이 어떻게 상호작용하는지 파악해야 할 필요를 피할 수 있다. Christian Brauner는 io_uring 기반 해법에서도 결국 같은 문제가 생길 것을 우려했다. 몇 년 뒤에는 서로 다른 작업들이 어떻게 상호작용하는지에 대한 논의가 필요해질 것이라는 얘기다. Hellwig는 Bacik의 설명이 상당히 추상적이라고 보았고, 문제를 io_uring으로 옮기는 것이 왜 상황을 더 낫게 만드는지 이해하지 못했다.

Goldstein은 사용자들이 io_uring 인터페이스 사용법을 이해하기 어려울 수 있다고 우려했다. 한편 플래그는 작업들을 조합할 수 있는 서로 다른 방식의 수를 제한하는 수단이므로, io_uring으로 옮기면 필요한 테스트 매트릭스(testing matrix)가 크게 늘어날 것이라고 보았다. Bacik은 새로운 사용 사례가 나올 때마다 쓰기 작업이 페이지 캐시, writeback, iomap 등과 상호작용하는 방식에 약간의 변형이 생긴다고 말했다. 노출될 수 있는 전체 매트릭스 중에서 플래그는 선택지를 제한하지만, 결국 그것이 더 많은 플래그로 이어진다는 것이다.[^p04n3]

그는 I/O 테스트는 이미 "엉망"이며, io_uring으로 옮기면 잠재적으로 더 나빠질 수 있다고 말했다. 하지만 그것은 "사용자 공간이 원하는 것의 복잡성을 사용자 공간으로 밀어내는" 것으로, 다양한 휴리스틱(heuristic)과 정책 결정을 커널 코드에 굳혀 넣는 것보다는 낫다고 했다. 후자의 결과는 사용자 공간 개발자들이 자기 특정 사용 사례가 지원되는 것들 중 하나가 아니라는 이유로 불만을 갖게 되고, 그 뒤 또 다른 플래그 제안과 메일링 리스트 및 서밋에서의 긴 논의가 이어지는 것이다.

Ts'o는 그 접근법이 실행 가능한지 판단하려면 먼저 코드를 봐야 한다고 말했다. 다만 그의 우려는 여러 하위 작업 때문에 잠금을 여러 번 잡아야 할 수 있다는 점이었다. 잠금을 최적화하기 위해 일련의 작업을 분석하는 방법이 있을 수도 있지만, 그것이 없다면 현재 방식에 비해 성능이 떨어질 수 있다. 작업을 분석하고 잠금 획득을 결합하는 것 역시 테스트 매트릭스를 늘리는데, 사안이 작업 순서에 의존하게 되기 때문이며 "이것이 나를 겁나게 한다"고 그는 말했다.

Hellwig는 논의가 여전히 너무 추상적이라고 느꼈기에, 구체적으로 어떤 io_uring 작업을 말하는 것인지 궁금해했다. Brauner는 "Jens [Axboe]는 왜 이렇게 조용하지?"라고 물었다. 그 말에 웃음이 터졌고, 결국 io_uring 유지관리자인 Axboe가 답했지만, 그가 그 아이디어에 강한 입장을 갖고 있지는 않다는 점은 분명했다. Bacik은 어떤 "새롭고 특별한 것"을 하기 위해 "2년마다 새 플래그를 추가하는" 것은 단순히 이치에 맞지 않는다고 말했다.

새 io_uring 명령들의 복잡성은 대부분의 개발자들이 그것을 사용할 수 없을 것이라는 우려로 이어졌다. 커널 개발자들이 서로 다른 종류의 I/O를 어떻게 수행해야 하는지 정의하고 있는 데에는 이유가 있다는 것이다. Bacik은 동기식 I/O(synchronous I/O) 선택지는 계속 여러 종류의 플래그로 처리할 수 있지만, 더 새롭고 더 정교한 비동기 사용 사례들은 io_uring 기반 접근법으로 유도할 수 있다고 말했다.

Hellwig는 다양한 작업의 의미론(semantics)을 명확히 명시해 완전히 정의할 수 있을지에 대해 다소 회의적이었고, 설령 그렇게 하더라도 테스트 부담은 커진다고 보았다. 다른 이들은 기존의 모든 플래그와 그 조합에 비해 테스트 양상이 그렇게 크게 달라질지는 확신하지 못했다. Brauner는 쓰기의 의미론 변경이 계속될 것이며, 예컨대 5년 뒤에는 io_uring 기반 해법을 두고 같은 종류의 논의를 해야 할 것이라고 우려했다. 그저 문제를 뒤로 미루는 것일 수 있다는 얘기다.

Axboe가 대신 시스템 호출(system call)을 추가할 수도 있다고 지적하자, Bacik은 아마 완전히 진지한 말은 아니었겠지만 io_uring 대신 "새 시스템 호출 17개"를 제안했어야 했느냐고 물었다. 그는 단지 io_uring이 "더 좋아 보였다"고 생각했을 뿐이라고 했다. 그는 어떤 기능 전체를 하나의 포괄적인 플래그 안에 억지로 밀어 넣으려 하면 문제가 생긴다고 우려한다. I/O를 수행하기 위해 조합되는 조각들을 나눌 방법을 찾는 편이 더 이치에 맞는다는 것이다.

현재 존재하는 I/O API의 전체 설계와, 커널 개발자들이 처음부터 다시 시작한다면 무엇을 다르게 할 수 있을지에 대한 논의도 있었다. 예를 들어 Ts'o는 `O_DIRECT`가 수십 년 전 Oracle에 의해 설계되었고, 명확히 규정되지 않았기 때문에 파일시스템들이 이를 서로 다르게 구현한다고 지적했다.[^p04n4] 하지만 API를 어떤 식으로 전면 개편하더라도 여러 해 동안 널리 사용되지는 않을 것이며, 그동안 현재 API는 계속 유지되어야 한다.

Goldstein은 세션을 마무리하면서 그 부분의 논의를 이렇게 요약했다. 새 플래그를 추가하는 방식은 아마 더 쉬운 접근법일 것이다. 사용자 공간 개발자들은 시스템 호출 API에 익숙하고 그것을 이해하기 때문이다. 하지만 그 플래그는 먼저 잘 문서화되어야 하며, 그래야 검토자들이 그것이 타당하고 나머지 모든 것과 잘 맞는지 확인하려고 할 수 있다. 명확히 규정할 수 없다면, 그 기능이 올바른 방향에 있지 않다는 꽤 분명한 신호다.

[여기에 오류가 있다면 양해를 구합니다. 회의실의 음향이 듣기와 녹음 모두에 문제가 있었습니다. 오해나 발언자 식별 오류가 있었을 수 있습니다.]

[댓글(게시된 것 없음)](https://lwn.net/Articles/1072019/#Comments)

[^p04n1]: `iomap`은 파일 오프셋과 실제 블록 매핑을 다루는 공통 계층으로, 파일시스템별 I/O 경로를 단순화한다. 어떤 잠금을 잡고 writeback을 진행하느냐는 데이터 일관성과 병렬성에 직접 영향을 준다.
[^p04n2]: `io_uring`은 비동기 I/O 요청을 링 버퍼를 통해 제출·완료하는 Linux 인터페이스다. 여기서는 단일 플래그 대신 작은 I/O 단계들을 조합하게 해 커널 API 설계 부담을 줄일 수 있는지 논의됐다.
[^p04n3]: 테스트 매트릭스가 커진다는 것은 페이지 캐시, writeback, direct I/O, 동기화 플래그 등의 조합을 모두 검증해야 함을 뜻한다. 저장장치 경로에서는 일부 조합만 빠져도 데이터 손상이나 성능 회귀로 이어질 수 있다.
[^p04n4]: `O_DIRECT`는 페이지 캐시를 우회하려는 I/O 모드지만, 역사적으로 의미가 충분히 엄밀히 정의되지 않아 파일시스템과 커널 버전에 따라 정렬 요구사항이나 fallback 동작이 달라질 수 있다.

---

### [COW를 맥락 안에 유지하기(일명 익명 역매핑)](https://lwn.net/Articles/1072378/)

#### 요약

- 커널의 역매핑(reverse mapping)은 특정 물리 페이지를 참조하는 페이지 테이블 항목을 찾아 메모리를 관리하는 데 쓰인다.
- 익명 페이지(anonymous page)의 역매핑은 오래된 설계와 누적된 복잡성 때문에 이해하기 어렵고 확장성 문제도 안고 있다.
- Lorenzo Stoakes는 VMA 단위 추적 대신 프로세스의 `mm_struct` 단위에서 익명 매핑을 추적하는 COW 컨텍스트(COW context)를 제안했다.
- 이 구조는 프로세스 계층을 따라 공유된 COW(copy-on-write) 관계를 추적해 객체 수와 잠금 경합을 줄이는 것을 목표로 한다.
- RCU(read-copy-update)를 활용한 빠른 조회가 가능하지만, 동기화와 페이지 테이블 해제 시점 같은 어려운 문제가 남아 있다.

글쓴이

Jonathan Corbet

2026년 5월 14일

LSFMM+BPF

커널의 역매핑(reverse-mapping) 장치는 메모리의 특정 페이지를 참조하는 페이지 테이블 항목(page-table entry)을 찾아내는 일을 맡고 있다. 익명 페이지(anonymous page)의 역매핑(reverse mapping)은 파일 기반(file-backed) 페이지의 경우와는 다르게 처리된다. 2026년 Linux Storage, Filesystem, Memory Management, and BPF Summit의 메모리 관리 트랙 세션 제안에서 Lorenzo Stoakes는 커널의 익명 페이지 역매핑 구현이 그 복잡성 때문에 "매우 망가진 추상화"라고 말했다. 성능 문제도 있다. Stoakes는 자신이 "COW 컨텍스트(COW context)"라고 부르는 대체안을, 아직 다듬어지지 않은 형태로 소개하기 위해 그 자리에 섰다.[^p05n1]

시스템의 페이지 테이블은 가상 주소를 그 주소가 가리키는 물리 페이지(있다면)로 매핑한다. 하지만 물리 페이지에서 그것을 참조하는 페이지 테이블 항목으로 거꾸로 찾아가는 하드웨어 메커니즘은 없다. 그럼에도 커널이 메모리를 관리하려면 이런 역매핑(reverse mapping)이 필요하다. 오래전에는 익명 페이지의 역매핑을 시스템의 모든 페이지 테이블을 훑어보는 방식으로 수행했다. 말할 필요도 없이, 이는 가능한 해결책 중 가장 빠른 방식은 아니었다. Rik van Riel은 2002년에 페이지 테이블 스캔을 없애기 위해 [역매핑 메커니즘을 추가](https://lwn.net/2002/0124/kernel.php3)했고, Andrea Arcangeli는 2년 뒤 그 장치를 [상당히 재작업](https://lwn.net/Articles/75198/)했다. 그 뒤 20여 년 동안 코드는 상당히 진화했는데, 대체로 더 복잡해지는 방향이었다. 익명 페이지의 역매핑에 할애된 부분은 특히 따라가기 어렵다.

Stoakes는 그 복잡성에 대한 불만으로 발표를 시작하면서, 코드의 여러 부분이 난해하다고 말했다. 또한 역매핑 코드가 전체 `fork()` 작업 동안 잠금을 잡고 있어 높은 잠금 경합(lock contention)과 그에 따른 확장성 문제를 만든다는 점도 아쉬워했다. 역매핑을 제공하기 위해 매우 많은 수의 커널 객체가 사용되며, 이 때문에 메모리 오버헤드도 크다.[^p05n2]

그는 대안을 작업해 왔으며, 그 첫 초안 형태는 [이 저장소 브랜치](https://git.kernel.org/pub/scm/linux/kernel/git/ljs/linux.git/log/?h=project/cow-context)에서 볼 수 있다. 현재 역매핑 코드는 가상 메모리 영역(VMA, virtual memory area) 수준에서 동작한다. 하나의 프로세스가 많은 수의 VMA를 가질 수 있으므로, 추적해야 할 대상도 그만큼 많다. Stoakes는 대신 `mm_struct` 수준에서 익명 매핑을 추적하는 데 쓰이는 "COW 컨텍스트(COW context)"를 제안하고 있다. 프로세스마다 하나의 [`mm_struct` 구조체](https://elixir.bootlin.com/linux/v7.0.5/source/include/linux/mm_types.h#L1123)가 있으며, 이는 프로세스의 주소 공간을 설명하는 핵심 자료구조다. 프로세스당 COW 컨텍스트가 하나만 필요하므로, 이것이 VMA별 구조였다면 필요했을 수보다 훨씬 적은 수만 유지하면 된다.

COW 컨텍스트(COW context)는 `mm_struct`와 연결되어 있지만 별도의 구조체로 관리된다. COW 컨텍스트를 왜 `struct mm_struct` 안에 직접 넣지 않을까? COW 컨텍스트 구조체들은 프로세스 계층을 표현하기 위해 서로 연결되지만, 자신과 연결된 프로세스보다 더 오래 살아남아야 할 수도 있다. 어떤 프로세스가 여러 자식을 만든 뒤 종료하더라도, 그 COW 컨텍스트는 여전히 존재해야 한다. 아직 살아 있는 프로세스들을 만들어 낸 일련의 `fork()`에 대한 커널의 모델을 유지해야 하기 때문이다. 이들 프로세스는 익명 페이지에 대한 매핑을 계속 공유하고 있을 가능성이 높다.

각 페이지(엄밀히 말하면 각 폴리오(folio); 둘의 차이에 대한 논의는 [이 기사](https://lwn.net/Articles/1064861/)를 보라)는 자신을 처음 매핑한 프로세스의 COW 컨텍스트를 가리키는 포인터를 얻는다. 그 폴리오의 모든 매핑을 찾아야 할 때가 오면 이 포인터를 따라가면 된다. 그러면 매핑을 가질 수 있는 프로세스 계층의 맨 위에 있는 COW 컨텍스트를 얻을 수 있고, 그 시점부터는 COW 컨텍스트 트리를 걸으며 존재할 수 있는 다른 매핑을 찾으면 된다. 물론 복잡한 문제들이 있다. 그중 다수는 프로세스가 자신의 주소 공간을 다시 매핑(remap)할 수 있다는 사실과 관련되어 있다. 즉, 하나의 폴리오가 서로 다른 프로세스에서 서로 다른 가상 주소에 매핑될 수 있다는 뜻이다. 이런 재매핑을 추적하는 일은 패치 세트에 상당한 복잡성을 더한다. Stoakes는 `MAP_PRIVATE`로 매핑된 파일들도 그 나름의 고통을 가져온다고 덧붙였다.[^p05n3]

어떤 프로세스가 많은 자식 프로세스를 만들었다면, 순회해야 할 COW 컨텍스트도 많을 수 있다. 이 순회를 최적화하기 위해 폴리오를 그것이 매핑된 계층 구조 중 가능한 한 가장 낮은 부분의 COW 컨텍스트에 연결하려는 노력이 들어간다. 그 결과 역매핑 조회는 대부분의 경우 빠르다.

새 구조의 장점 중 하나는 조회를 잠금 대신 RCU(read-copy-update) 보호 아래에서 수행할 수 있다는 점이다. 이는 좋은 일이기도 하고 나쁜 일이기도 하다. RCU는 훨씬 빠르지만, 잠금이 제공하는 동기화 지점은 갖고 있지 않다. 따라서 그는 매핑 단위의 어떤 잠금 형태를 도입해야 할 것이다. 더 "무모한" 대안은 경쟁 상태(race)를 어느 정도 그냥 허용하는 것이다. 다만 그렇게 하려면 RCU 유예 기간(grace period)이 지난 뒤에야 페이지 테이블을 해제하도록 지연시켜야 한다.[^p05n4]

세션 시간이 다 되어 가면서 Stoakes는 발표를 마무리했다. 발표에서 비롯된 실질적인 토론은 없었다. 그는 현재의 코드에 거친 부분과 미완성 부분이 많다는 점을 인정했다. 그는 이것이 결국 성공하지 못할 수도 있는 연구 프로젝트라고 말했다. 하지만 적어도 그는 익명 역매핑(anonymous reverse mapping)에 대해 훨씬 더 많은 것을 배우게 될 것이다.

[댓글(아직 없음)](https://lwn.net/Articles/1072378/#Comments)

[^p05n1]: 익명 역매핑(anonymous reverse mapping)은 스왑 회수, 페이지 마이그레이션, NUMA 밸런싱, 메모리 압박 시 페이지 회수처럼 "이 물리 페이지를 누가 보고 있는가"를 알아야 하는 경로에서 핵심이다.
[^p05n2]: `fork()` 중 긴 구간의 잠금은 많은 스레드나 프로세스를 만드는 워크로드에서 지연 시간을 키울 수 있다. COW(copy-on-write)는 복사를 미루는 최적화지만, 공유 상태를 추적하는 메타데이터가 확장성을 좌우한다.
[^p05n3]: VMA 단위에서 `mm_struct` 단위로 추적 범위를 바꾸면 객체 수는 줄어들 수 있지만, 주소 공간 재배치와 `MAP_PRIVATE` 파일 매핑처럼 프로세스마다 주소가 달라질 수 있는 경우를 정확히 표현해야 한다.
[^p05n4]: RCU(read-copy-update)는 읽기 측 비용을 낮추는 대신, 객체 해제 시점을 유예 기간 이후로 미뤄야 한다. 메모리 관리 코드에서는 이 지연이 페이지 테이블 수명과 TLB 무효화 순서 같은 세부사항과 맞물린다.

---

### [메모리 관리를 위한 정책 그룹](https://lwn.net/Articles/1072517/)

#### 요약

- Chris Li는 2026 LSFMM+BPF Summit에서 기존 control groups(cgroups)가 자원 관리에는 적합하지만, 계층적이지 않은 정책(policy) 표현에는 한계가 있다고 설명했다.
- 제안된 policy groups(정책 그룹)는 자원(resource)이 아니라 정책을 관리하는 구조로, swap tiers처럼 속도가 다른 스왑 장치 접근 정책을 표현하는 데 도움이 될 수 있다.
- 참석자들은 policy groups를 cgroup에 붙일지, 확장 속성(extended attributes), 별도 가상 파일시스템, BPF, 또는 프로세스 직접 연결 방식으로 구현할지에 대해 의견이 갈렸다.
- 대체로 새로운 제어 구조를 추가하는 것은 피하는 편이 낫다는 분위기였고, Li는 정책을 프로세스에 직접 붙이는 방안을 더 검토하겠다고 했다.

작성자

Jonathan Corbet

2026년 5월 14일

LSFMM+BPF

Chris Li는 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

의 memory-management(메모리 관리) 트랙 세션을 시작하면서, 커널의

control-group 서브시스템

은 자원 관리(resource management)에는 잘 동작한다고 말했다. 하지만 control groups는 다른 사용 사례에는 덜 잘 맞는다. 그는 자신이 겪어 온 몇 가지 단점을 해결하기 위한 개선안인 "policy groups"(정책 그룹)을 발표하러 왔다. 다만 이 기능이 어떤 모습이어야 하는지에 대한 합의는 아직 멀어 보인다.

[![[Chris Li]](https://static.lwn.net/images/conf/2026/lsfmm/ChrisLi-sm.png)](https://lwn.net/Articles/1072520/) 자원 관리는 control groups의 설계 깊숙이 들어가 있다. 이 초점은 부모 그룹에 허용된 자원이 그 자식 그룹 중 어느 하나에 주어진 자원보다 크거나 같아야 한다는 핵심 가정을 이끈다. Control groups는 또한 통합된 계층 구조로 조직된다. 이는 10여 년 전 [control-group 재설계 작업](https://lwn.net/Articles/484251/)의 핵심 요구사항이었다. 그러나 이 설계에는 한계가 있다. 자원 관리 모델에 맞지 않는 경우에는 어울리지 않고, 통합 계층 구조가 모든 사용 사례에 맞는 것도 아니며, control groups는 프로세스에 묶여 있지 않은 정책에는 효과적인 도구가 아니다.[^p06n1]

그는 자원 모델에 맞지 않는 정책의 예로 서비스 수준 목표(service-level objectives)를 생각해 보라고 말했다. 자식 그룹에는 부모보다 더 빠르거나 더 느린 서비스 수준이 부여될 수 있다. Li가 특히 관심을 두는 영역은 서로 다른 속도의 스왑 장치에 대한 접근을 조절하는 것이다. Control groups를 이 모델에 맞추기 어렵다는 점이 [swap-tiers 작업](https://lwn.net/ml/all/20260126065242.1221862-1-youngjun.park@lge.com/)의 업스트림 진입을 가로막고 있다. 통합 계층 구조에 맞지 않는 사례로는 Android의 포그라운드 작업과 백그라운드 작업 구분이 있다. 애플리케이션은 그런 조직화의 일부를 내부적으로 수행할 수 있지만, 그 결과가 시스템이 보는 프로세스 계층 구조와 맞지 않을 수 있다. 프로세스가 아닌 사례에는 파일시스템 할당 제어와 네트워크 제어 정책이 포함된다.

제안된 policy groups는 아직 구체화되지 않은 방식으로 control groups에 연결되며, 이러한 한계를 해결하려는 것이다. Policy groups는 자원보다 정책을 관리하는 데 초점을 맞추고, 동일한 계층 모델에 강제로 끼워 넣어지지 않을 것이다. 그는 네트워크 네임스페이스, NUMA 메모리 정책, [kernel samepage merging](https://lwn.net/Articles/953141/) 같은 동작을 제어하기 위한 [`prctl()`](https://man7.org/linux/man-pages/man2/prctl.2.html) 사용 등, 이런 종류의 제어를 위한 다른 시도들도 있었다고 말했다. Policy groups는 이런 종류의 기능에 더 형식화된 구조를 가져오게 될 것이다.[^p06n2]

Liam Howlett은 정책 관련 기능들이 보통 `prctl()`을 사용한다고 말하며, 그것이 정말 이 작업에 잘 맞는지 물었다. 그는 `prctl()` 안에는 어쩌면 다른 방식으로 구현되어야 할 기능들이 많이 욱여넣어져 있다고 제안했다. Suren Baghdasaryan은 강제하려는 정책이 본질적으로 계층적이지 않다면 왜 policy groups가 control groups와 연관되어야 하는지 물었다. Li는 정책을 프로세스 계층 구조에 붙여야 할 필요는 여전히 있다고 답했다.

Lennart Poettering은 control-group 재설계가 이 서브시스템을 독립적인 계층 구조들로부터 멀어지게 했으며, 그것은 좋은 일이었다고 말했다. 그 개념을 되살리는 것은 피하는 편이 더 낫다는 것이다. 최근 커널에서는 control groups에 확장 속성(extended attributes)을 붙이는 것이 가능하다. 그는 이것들을 정책을 붙이는 데 사용할 수 있다고 제안했다. [BPF Linux security module](https://docs.kernel.org/bpf/prog_lsm.html)은 이런 방식으로 control groups에 붙은 확장 속성을 사용한다. 그는 확장 속성이 policy groups에도 꽤 잘 맞을 수 있다고 말했다. Li는 이 접근 방식이 일부 사례에는 동작할 수 있지만, 본질적으로 프로세스에 묶여 있지 않은 사례에는 맞지 않는다고 답했다.

Roman Gushchin은 policy groups가 아마도 control groups에 전혀 붙어서는 안 된다고 말했다. 또 다른 참석자는 이 모든 정책을 단일 프레임워크 아래에 묶는 것이 실수일 수 있다고 말했다. 예를 들어 어떤 정책은 파일시스템에 붙이고, 다른 정책은 control group에 붙이는 편이 더 나을 수 있다는 것이다. 전체적인 정책 프레임워크가 유용할 수는 있겠지만, 일반적으로 적용 가능한 해법을 알아낸 사람은 아무도 없었다.

Li는 올바른 접근법이 새로운 policy-group 가상 파일시스템을 만드는 것일 수 있는지 물었다. 그것은 계층 구조를 구현하기보다 평평한(flat) 뷰를 제공할 수 있다. Poettering은 커널에서 또 하나의 제어 인터페이스를 다뤄야 하는 상황을 기대하고 있지는 않다고 답했다. Li가 프로세스의 스왑 서비스 수준을 설정하려면 Poettering은 어떤 방법을 제안하겠느냐고 묻자, Poettering은 확장 속성 아이디어를 되풀이했다.[^p06n3]

시간이 다 되어 가면서 논의의 초점은 흐려졌다. 새로운 네임스페이스 유형을 추가하자는 제안은 많은 지지를 얻지 못했다. 가능하다면 새로운 제어 구조를 추가하지 않는 편이 더 낫다는 점에는 어느 정도 의견이 모인 듯했다. BPF를 사용하는 방안도 제안되었지만, BPF를 지원하지 않는 시스템들(특히 임베디드 영역)이 있으므로 Li는 그 접근은 피하고 싶다고 말했다. 세션은 Li가 정책을 프로세스에 직접 붙이는 방법을 더 면밀히 살펴보겠다고 말하며 마무리되었다.

[댓글(게시된 것 없음)](https://lwn.net/Articles/1072517/#Comments)

[^p06n1]: 메모리 관리(memory management)에서 cgroup 계층은 memcg(memory cgroup)처럼 사용량·한도·회수 압력을 부모/자식 관계로 모델링하는 데 강하다. 하지만 서비스 수준이나 우선순위처럼 계층을 거꾸로 가로지르는 정책은 같은 구조에 넣기 어렵다.
[^p06n2]: 스왑 계층화(swap tiers)는 빠른 장치와 느린 장치를 정책적으로 구분해야 하므로, 단순한 메모리 한도보다 "어떤 작업이 어떤 스왑 장치를 얼마나 선호하는가"를 표현할 방법이 필요하다. 이는 memcg의 기존 자원-accounting 모델과 별도의 policy groups 논의를 촉발한다.
[^p06n3]: 새 가상 파일시스템이나 새 네임스페이스를 추가하면 커널 ABI와 사용자 공간 관리 도구가 장기적으로 유지해야 할 표면이 늘어난다. 반대로 확장 속성이나 기존 cgroup 인터페이스를 재사용하면 통합성은 좋아지지만, 프로세스에 직접 묶이지 않는 파일시스템·네트워크 정책을 표현하기 어려울 수 있다.

---

### [라이브 업데이트 중 HugeTLB 보존](https://lwn.net/Articles/1072531/)

#### 요약

- Linux 커널의 kexec handover와 live update orchestrator는 실행 중인 호스트 커널을 교체하면서 가상 머신의 메모리를 보존하는 것을 목표로 한다.
- 현재 병합된 기능은 공유 메모리 기반 memfd 보존에는 제한적으로 대응하지만, hugetlbfs(HugeTLB 파일시스템) 기반의 대형 페이지 메모리는 아직 live update를 통과해 보존하지 못한다.
- 제안된 방식은 보존 대상 HugeTLB 페이지를 먼저 동결하고, 크기와 위치 같은 메타데이터를 기록한 뒤 새 커널에서 hugetlbfs-backed memfd로 복원하는 것이다.
- 복원 과정에서는 제어 그룹 과금, 페이지 캐시 편입, 부팅 시 사전 할당되는 huge page 수 조정 등 커널 메모리 관리 상태를 일관되게 맞춰야 한다.
- CMA(contiguous memory allocator)와의 상호작용은 아직 해결되지 않았으며, 현재 패치에서는 live update가 활성화된 경우 CMA와 hugetlbfs의 병용을 비활성화한다.

글쓴이

Jonathan Corbet

2026년 5월 15일

LSFMM+BPF

최근 Linux 커널에서는

kexec handover 및 live update orchestrator

기능 구현에 많은 노력이 투입되어 왔다. 하지만 그 작업은 아직 끝나지 않았다. 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

에서 Pratyush Yadav는 live update(라이브 업데이트) 과정 동안

hugetlbfs

가 제공하는 메모리를 보존하는 기능을 추가하는 문제를 다룬 메모리 관리 트랙 세션을 이끌었다.

Yadav는 먼저 live update의 사용 사례가, 실행 중인 시스템에서 그 커널 아래 실행 중인 가상 머신을 방해하지 않고 호스트 커널을 교체하는 것이라고 설명했다. [kexec handover](https://docs.kernel.org/core-api/kho/index.html) 장치는 커널 교체 중 보존할 메모리 영역을 표시한다. 이는 커널 내부 인터페이스이며 사용자 공간 API는 없다. 메모리가 표시되고 나면 새 커널을 부팅하기 위해 [`kexec_load()` 시스템 호출](https://www.man7.org/linux/man-pages/man2/kexec_load.2.html)이 호출되며, 그 뒤 보존된 메모리는 원래 소유 프로세스로 복원된다. [live update orchestrator](https://docs.kernel.org/core-api/liveupdate.html)는 이 기능에 대한 사용자 공간 인터페이스를 제공하여, 사용자가 보존할 자원을 표시하고 새 커널에서 이를 복원할 수 있게 한다.[^p07n1]

[![[Pratyush Yadav]](https://static.lwn.net/images/conf/2026/lsfmm/PratyushYadav-sm.png)](https://lwn.net/Articles/1072536/) Kexec handover와 live update orchestrator는 6.19 개발 주기 동안 병합되었으며, 메모리 기반 파일시스템에 있는 파일을 보존하는 기능을 제한적으로 지원한다. 이 기능은 공유 메모리가 뒷받침하는 memfd([`memfd_create()`](https://man7.org/linux/man-pages/man2/memfd_create.2.html)로 생성되는 익명 파일)는 처리할 수 있지만, 그 외의 경우는 많지 않다. 이 기능을 사용해 가상 머신의 내용을 보존할 수는 있지만, memfd에서 가상 머신을 실행하는 것은 상대적으로 비효율적이다. hugetlbfs(HugeTLB 파일시스템) 서브시스템에서 얻은 소수의 huge page(아마 1GB 크기일 수도 있음)에 배치된 가상 머신은 더 효율적으로 실행되지만, 그 메모리는 아직 live update를 견뎌 보존되지 않는다.[^p07n2]

Yadav의 목표는 그런 가상 머신과 그에 연결된 메모리를 live-update 과정 전체에 걸쳐 이어 가져갈 수 있게 하는 것이다. 바람직하게는, hugetlbfs 자체를 마운트할 필요가 없도록 특수한 memfd를 통해 hugetlbfs 페이지를 얻을 수 있어야 한다. 의도는 보존되는 상태의 양을 최소화하는 데 있다. 보존되는 모든 것은 커널 ABI의 일부가 되므로, 그 양은 적을수록 좋다. 그는 또한 hugetlbfs 자체에 필요한 변경 수를 최소화하기 위해서도 작업하고 있다.

이 기능은 먼저 보존할 huge page의 내용을 동결하여, 업데이트 과정 중 변경 사항이 손실되지 않도록 하는 방식으로 동작한다. 이를 수행하는 방법은 두 가지다. 첫 번째는 관련 hugetlbfs inode에 플래그를 추가한 다음, 변경이 일어나려 할 때 그 플래그를 확인하는 것이다. 공유 메모리 파일시스템은 이런 방식으로 동작한다. 여기에 더해, 관련 메모리는 업데이트 중 마이그레이션이나 컴팩션이 일어나지 않도록 고정(pin)된다. 이 선택지는 동작할 수 있지만, 일부 개발자들은 이를 다소 임시방편(hack)에 가깝다고 본다. 대안은 새로운 address-space 플래그를 통해 filemap 코드가 동결 상태를 인식하도록 만드는 것이다. 이 경우에도 변경을 허용하기 전에 플래그를 확인하게 된다. 이 선택지가 올바르게 동작하도록 하려면 관리해야 할 여러 세부 사항이 있으며, 이는 가상 파일시스템 계층이 동결 과정을 인식해야 함을 뜻한다.[^p07n3]

middle-ad 페이지가 동결되고 나면 각 페이지에 대한 일부 메타데이터, 즉 크기와 위치가 기록된다. 동결된 페이지와 메타데이터는 모두 보존 대상으로 표시된다. 그런 다음 업데이트가 진행될 수 있다.

새 커널이 실행되면, hugetlbfs가 뒷받침하는 새로운 memfd가 생성되고, 그 구성 요소인 각 huge page가 다시 사용 상태로 배치되며, hugetlbfs 상태도 그에 맞게 갱신된다. 할당된 메모리에 대한 제어 그룹 과금이 수행되고, 새 페이지들은 페이지 캐시에 추가된다. 이 시점에서 메모리 보존의 관점으로는 업데이트 과정이 완료된다.

Yadav에 따르면 huge-page 할당과 관련해 약간의 복잡한 문제가 있다. hugetlbfs는 부팅 과정에서 정해진 수의 huge page를 사전 할당하는 방식으로 동작한다. hugetlbfs가 뒷받침하는 가상 머신을 복원하는 과정 역시 필요한 huge page를 할당하게 된다. 원래 커널에서는 그 페이지들이 hugetlbfs에서 할당되었지만, 새 커널에서는 대신 별도로 할당된다. 이로 인해 전체적으로 huge page가 과다 할당될 수 있다. 해결책은 새 커널이 부팅될 때 보존된 huge page 수를 세고, 그에 맞춰 hugetlbfs가 사전 할당하는 수를 줄이는 것이다.

아직 해결되지 않은 문제는 이 기능과 [contiguous memory allocator(CMA)](https://lwn.net/Articles/486301/)의 상호작용이다. 원래 huge page가 CMA에서 얻어진 것이라면, 업데이트 후 새 페이지를 다시 CMA에 삽입해야 하지만, CMA는 자신의 메모리 영역을 확장할 방법을 제공하지 않는다. 따라서 현재 패치들은 live update가 활성화된 경우 CMA와 함께 hugetlbfs를 사용하는 것을 그냥 비활성화한다. 언젠가는 CMA의 상태도 보존할 수 있게 되겠지만, 현재 버전의 작업에서는 그렇게 되지 않는다.[^p07n4]

Yadav는 상태 요약으로 발표를 마무리하면서, [RFC 패치 세트](https://lwn.net/ml/all/20251206230222.853493-1-pratyush@kernel.org/)가 2025년 12월에 게시되었다고 말했다. 그 작업의 일환으로 그는 kexec handover에서 여러 문제를 발견했고, 이를 고치기 위해 [상당한 인프라 작업](https://lwn.net/ml/all/20260429133928.850721-1-pratyush@kernel.org/)이 필요했다. 그는 받은 피드백에 대응한 뒤 곧 갱신된 패치 세트를 게시할 예정이다.

유일한 질문은 Mike Rapoport에게서 나왔다. 그는 CMA 페이지를 이동 가능하게 만들면 kexec handover와의 통합에 도움이 될지 물었다. Yadav는 그런 변경이 무언가를 망가뜨릴 가능성이 높으며, 아마 큰 도움도 되지 않을 것이라고 말했다.

[댓글(1개 게시됨)](https://lwn.net/Articles/1072531/#Comments)

[^p07n1]: live update에서 메모리 영역을 보존한다는 것은 단순히 페이지 내용을 복사하는 문제가 아니라, 새 커널이 해당 물리 페이지와 소유 프로세스, 파일 객체, 매핑 정보를 모두 일관된 커널 상태로 다시 연결해야 함을 의미한다.
[^p07n2]: HugeTLB 페이지는 일반 페이지보다 크고 TLB miss를 줄일 수 있어 대형 VM 메모리에 유리하지만, 일반 페이지 캐시나 익명 메모리와 다른 예약·할당 규칙을 가지므로 커널 전환 중 보존이 더 까다롭다.
[^p07n3]: 페이지 동결과 pinning은 업데이트 중 데이터 무결성을 보장하지만, 동시에 메모리 마이그레이션·컴팩션·회수(reclaim)를 제한하여 메모리 압박 상황에서 커널의 선택지를 줄일 수 있다.
[^p07n4]: CMA는 장치 DMA 등을 위해 연속된 물리 메모리를 제공하는 영역이므로, live update 후 huge page를 그 영역에 재편입하지 못하면 연속 메모리 보장과 HugeTLB 예약 상태가 서로 어긋날 수 있다.

---

### [BPF로 메모리 관리 제어하기](https://lwn.net/Articles/1072538/)

#### 요약

- 2026년 LSFMM+BPF Summit에서 Roman Gushchin은 메모리 관리에 BPF 인터페이스를 붙이려는 제안들이 왜 아직 메인라인에 들어가지 못했는지 설명했다.
- 주요 장애물은 트리 밖(out-of-tree) BPF 프로그램, control group에 대한 struct ops 부착 제한, 안전한 fallback의 어려움, hot path 성능 비용, 그리고 ABI 안정성 문제다.
- 토론에서는 오래 유지될 수 있는 범용 hook만 추가해야 하며, 특정 구현 세부사항에 묶이는 hook은 피해야 한다는 의견이 나왔다.
- Shakeel Butt는 BPF를 활용해 memory control groups(메모리 제어 그룹)을 더 유연하게 재구상하는 방안을 제시했다.
- 새 인터페이스는 알림, background reclaim, lock 보유 thread를 고려한 throttling, memory tiering 제어 등을 지원해야 한다는 요구사항이 논의되었다.

글쓴이

Jonathan Corbet

2026년 5월 15일

LSFMM+BPF

Roman Gushchin은 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

의 메모리 관리 트랙 세션을 시작하면서, 커뮤니티가 메모리 관리를 위한 BPF 기반 인터페이스를 추가하려는 제안을 많이 보아 왔다고 말했다. 하지만 그중 어느 것도 메인라인에 들어가지는 못했다. 그는 BPF가 어떤 방식으로 도움이 될 수 있는지, 그리고 지금까지 BPF 기반 해법이 받아들여지지 못하게 만든 장애물이 무엇인지 살펴보고자 했다. 이 세션 뒤에는 Shakeel Butt가 이끈, memory control groups(메모리 제어 그룹)를 위한 새로운 BPF 기반 인터페이스의 요구사항이 어떤 모습일 수 있는지에 대한 토론이 이어졌다.[^p08n1]

#### BPF 통합의 장애물

그는 먼저 기존의 시도들이 여러 다양한 메모리 관리 휴리스틱을 포착하려 했다고 말했다. BPF를 사용해 [out-of-memory 처리](https://lwn.net/Articles/1019230/), [NUMA balancing](https://lwn.net/ml/all/20260113121238.11300-1-laoar.shao@gmail.com/), [memory control groups](https://lwn.net/ml/all/cover.1770194182.git.zhuhui@kylinos.cn/), [page-cache eviction](https://lwn.net/ml/all/0b1293ca-7a1f-4358-bc20-15784452238d@columbia.edu/) 등을 제어하자는 제안들이 있었다. 아직 추진되지 않은 더 흥미로운 아이디어들도 있는데, 여기에는 readahead 제어, [`madvise()`](https://man7.org/linux/man-pages/man2/madvise.2.html), [kernel samepage merging](https://lwn.net/Articles/953141/), guest-memory 제어가 포함된다. 특히 readahead는 복잡한 휴리스틱들의 집합이지만 성능에는 중요하다.

[![[Roman Gushchin]](https://static.lwn.net/images/conf/2026/lsfmm/RomanGushchin-sm.png)](https://lwn.net/Articles/1072542/) 그는 메모리 관리 서브시스템에 BPF 인터페이스를 추가하는 데에는 여러 장애물이 있으며, 중요도가 낮은 것부터 높은 것까지 차례로 다루겠다고 말했다. 첫 번째는 트리 밖(out-of-tree) BPF 프로그램에 대한 우려였다. 커널 개발자들은 production-quality 코드가 메인라인에 들어오는 것을 보고 싶어 하지만, 현재 BPF는 그렇게 작동하고 있지 않다. 예를 들어 production-quality [sched_ext scheduler](https://lwn.net/Articles/974387/)들이 있지만, 모두 완강하게 트리 밖에 머물러 있다. BPF maintainer인 Alexei Starovoitov는 "sched_ext was a mistake"라고 말했다. production scheduler를 메인라인으로 함께 가져오지 못했다는 뜻에서였다. 그는 이제 그 상황을 고치기는 어렵다고 말했다. 트리 안(in-tree)에 좋은 out-of-memory handler가 있으면 좋을 것이다. 다른 이점이 없더라도, 개발자들이 제안된 인터페이스를 판단하는 데 도움이 될 것이기 때문이다.

커널 트리에 BPF 프로그램을 포함하는 것 자체는 논란이 없어 보인다고 Gushchin은 말했다. 따라서 진짜 질문은 개발자들이 어디까지 나아가야 하느냐이다. 첫 단계는 사람들이 검토하고 실험할 수 있도록 소스만 포함하는 것이 될 수 있다. Starovoitov는 포함된 BPF 프로그램을 자동으로 로드하는 것이 좋은 두 번째 단계일 수 있다고 말했다. 그렇게 하면 사람들이 포함된 BPF 프로그램을 쉽게 사용할 수 있다. Gushchin은 [systemd-oomd](https://www.freedesktop.org/software/systemd/man/latest/systemd-oomd.service.html)의 BPF 구현이 그 서브시스템이 어떻게 동작하는지 보여주는 좋은 예가 될 것이라고 제안했다.

또 다른 장애물은 현재 [struct ops](https://lwn.net/Articles/811631/) 프로그램을 control group에 붙일 수 없다는 점이다. BPF *program*은 붙일 수 있지만, struct ops 인터페이스를 사용하는 프로그램은 붙일 수 없다. 그는 out-of-memory handler를 위한 구현을 가지고 있지만, sched_ext는 다른 해법을 사용한다.

그다음에는 안전성과 fallback 문제가 있다. 망가진 BPF 메모리 관리 프로그램은 시스템을 쉽게 사용할 수 없게 만들 수 있다. Gushchin의 관점에서는 이것이 해결하기 가장 어려운 문제다. 이 맥락에서 "안전성"이 무엇을 의미하는지 정의하는 것조차 어렵기 때문이다. 시간 기반 fallback은 구현하기 어렵고 보기에도 좋지 않다고 그는 말했다. 메모리 관리 동작을 감시되는 kfunc으로 감쌀 수는 있지만, 그러면 성능을 해칠 수 있는 비범용 해법으로 이어진다. 허용 가능한 서비스 수준을 정의해야 한다. 모든 패킷을 버리는 traffic-control 프로그램은 괜찮지만, 시스템 task의 절반을 굶기는 sched_ext scheduler는 그렇지 않다. 결함 있는 BPF 프로그램이 로드되어 시스템이 더 이상 메모리를 reclaim할 수 없게 되면 무슨 일이 일어나야 하는가? middle-ad[^p08n2]

hot path의 성능에 대한 우려는 항상 존재할 것이며, 가장 뜨거운 경로에 BPF 프로그램을 추가하는 일을 정당화하기 어렵게 만들 것이다. 메모리 관리 서브시스템은 성능을 위해 batching에 크게 의존한다. 그래서 BPF 프로그램이 batching이 끝나기 전 또는 후에 실행되어야 하는지라는 질문이 생긴다. 그는 batching이 먼저 일어나야 한다고 제안했지만, 그렇게 하면 batching 자체를 BPF 프로그램으로 제어할 수 없게 된다.

마지막으로, 가장 중요한 장애물은 ABI 안정성이라고 그는 말했다. 이 우려는 최근 메일링 리스트에서 [David Hildenbrand가 제기](https://lwn.net/ml/all/014f3c0a-7c6f-4f64-95cd-b7b69d804880@kernel.org/)한 바 있다. 직접 참석한 자리에서 Hildenbrand는 BPF 프로그램을 위한 hook을 제공한다는 것이 무엇을 의미하는지를 두고 약간의 혼란이 있었다고 말했다. 그것들은 영구적인 메모리 관리 기능인가? 커뮤니티는 그런 hook을 무기한 유지하겠다고 약속하고 싶지 않을 수 있다. 그 우려 때문에 transparent huge page 관리를 위한 hook을 제공하지 않기로 결정하게 되었다. 5년 뒤의 모습이 어떨지 아무도 모른다고 그는 말했으므로, 인터페이스를 제대로 설계하는 것은 불가능할 것이다.

그는 언젠가 메모리 관리 개발자들이 깨어나서 인터페이스의 어떤 측면은 다르게 만들어야 했다고 깨닫게 될 것이라고 말했다. 그 깨달음에 따라 행동하면 프로그램이 깨지고 사람들은 화를 낼 것이다. 어쩌면 해법은 커널 트리 자체에서 유지되는 BPF 프로그램만 지원하겠다고 약속하는 것일지도 모른다. Hildenbrand는 BPF 사용의 가치를 보지만, 인터페이스를 추가하면 서브시스템이 장래에 후회할 기능을 계속 유지해야 하는 처지에 놓일 수 있다고 우려한다며 말을 맺었다.

이 시점에서 세션 시간은 끝났다. 결론에서 Gushchin은 가장 범용적인 종류의 BPF hook만 추가하는 것이 중요하다고 말했다. 예를 들어 out-of-memory score를 할당하는 hook은 나쁜 아이디어일 것이다. 미래의 out-of-memory killer가 그것을 사용하지 않을 수도 있기 때문이다. 하지만 압박 상황에서, 어쩌면 일부 process를 죽이는 방식으로, 어느 정도 메모리를 해제하는 hook은 유용할 수 있다.[^p08n3]

#### memory control groups 재구상하기

[![[Shakeel Butt]](https://static.lwn.net/images/conf/2026/lsfmm/ShakeelButt-sm.png)](https://lwn.net/Articles/1072550/) Butt는 곧바로 이어서 커널의 [memory controller](https://docs.kernel.org/admin-guide/cgroup-v1/memory.html)가 어떻게 진화하기를 바라는지, 그리고 BPF가 거기에 어떻게 맞아들어갈 수 있는지에 대해 논의했다. 그는 memory controller가 메모리 자원을 계층적으로 분배하며, hard limit과 soft limit을 모두 구현한다고 설명하면서 시작했다. 어떤 group이든 메모리가 충분할 때에는 hard limit까지 사용할 수 있지만, 메모리가 부족해지면 soft limit으로 다시 압박을 받게 된다.

그는 memory controller에 여러 과제가 있다고 말했다. limit enforcement는 유연하지 않고 방해가 된다. 동기적으로 일어나기 때문에 latency에 민감한 thread에서 예상치 못한 stall을 일으킬 수 있다. 그 인터페이스들은 진화시키기 어렵다는 점이 드러났다. 중대한 변경은 기존 ABI를 깨뜨릴 것이고, 커널 개발자들은 그렇게 해서는 안 되기 때문이다. 그는 대안을 실험할 수 있게 해 주는 메커니즘이 있으면 좋겠다고 말했다.

새 인터페이스의 목표는 다양한 use case를 지원할 수 있는 기능을 제공하는 것이다. 한 가지 예시 use case는 [그의 세션 제안서](https://lwn.net/ml/linux-mm/20260307182424.2889780-1-shakeel.butt@linux.dev/)에 제시되었고 세션 중에도 반복되었다.

> 정책: "system-level memory utilization을 95% 미만으로 유지한다. lock을 보유한 allocator를 throttling하지 않음으로써 priority inversion을 피한다. 각 workload의 사용량을 관련 성능 지표의 regression 없이 working set까지 줄인다. load shedding과 memory trimming 결정에서 workload와 협력한다. 그리고 극심한 memory pressure 아래에서는 OOM killer 및 중앙 job scheduler와 협력해 workload를 kill하고 정리한다."

그는 새로운 memory controller가 application이 대응할 수 있는 memory-use notification을 제공해야 한다고 말했다. 실행 중인 thread를 멈추지 않고 memory limit을 강제할 수 있도록 background reclaim을 지원해야 한다. memory-use throttling은 priority-inversion 문제를 피하기 위해 lock을 보유한 thread를 인식해야 한다. user space는 다른 방식으로도 throttling에 영향을 줄 수 있어야 하며, 예를 들어 어느 정도 예외가 되어야 하는 특정 thread를 식별할 수 있어야 한다. controller는 또한 memory tiering을 지원하여 page가 tier 사이에서 어떻게 이동되는지 제어할 수 있어야 한다.[^p08n4]

이 새로운 인터페이스가 어떻게 작동할지 자세히 다룰 시간은 많지 않았다. 전반적으로 이 작업은 초기 단계에 있는 것으로 보인다. Butt는 memory usage 증가를 BPF 프로그램에 알리기 위해 새로운 BPF callback인 `bpf_memcg_charge_succeed()`를 추가할 수 있다고 말했다. 그러면 그 프로그램은 background reclaim을 시작하는 식으로 응답할 수 있다. 다른 callback은 control group이 usage watermark에 도달했거나 usage limit에 걸렸을 때 프로그램에 알릴 수 있으며, 대응 방법에 대한 hint를 프로그램이 제공하는 방식에 의존하게 된다. 그 프로그램은 어떤 형태의 reclaim을 시작할 수도 있지만, application이 memory usage를 줄여 대응할 것이라는 기대 아래 해당 상황을 application에 알릴 수도 있다.

끝에서 청중 한 명은 application이 어떤 유형의 메모리를 사용하고 있는지 introspect할 수 있는 기능이 유용할 것이라고 말했다. Butt는 이 기능은 이미 작업 중이라고 답했다.

[댓글(1개 게시됨)](https://lwn.net/Articles/1072538/#Comments)

[^p08n1]: BPF를 메모리 관리에 적용한다는 것은 단순한 관찰 도구를 넘어, reclaim·OOM 대응·throttling 같은 정책 결정 지점에 프로그램 가능한 로직을 넣는다는 뜻이다. 이는 workload별 최적화를 가능하게 하지만 커널 내부 정책의 안정성과 책임 경계를 더 복잡하게 만든다.

[^p08n2]: 메모리 관리 BPF 프로그램은 잘못 동작할 때 네트워크 패킷 손실보다 더 치명적인 결과를 낳을 수 있다. reclaim 실패나 allocator stall은 전체 시스템의 forward progress를 막을 수 있으므로, verifier만으로는 충분하지 않은 runtime fallback과 서비스 수준 정의가 필요하다.

[^p08n3]: ABI 안정성 문제는 memory-management hook이 사실상 LSM-like hooks처럼 장기 유지되는 확장 지점이 될 수 있느냐의 문제와 맞닿아 있다. 특정 알고리즘의 세부 변수에 연결된 hook은 향후 커널 내부 구현이 바뀔 때 부채가 되기 쉽다.

[^p08n4]: memory control groups에 BPF callback을 붙이면 기존 cgroup ABI를 깨지 않고 새 정책을 시험할 여지가 생긴다. 다만 그만큼 user space 정책, kernel reclaim, OOM killer, scheduler 사이의 상호작용을 명확히 정의해야 한다.

---

### [스왑 테이블(swap tables), 플래시 친화적 스왑(flash-friendly swap), swap_ops 등](https://lwn.net/Articles/1072657/)

#### 요약

- 2026년 LSFMM+BPF 메모리 관리 트랙에서는 커널 스왑(swap) 서브시스템의 성능, 유지보수성, 저장장치 친화성을 다룬 세 세션이 열렸다.
- Kairui Song은 swap tables 도입 이후 페이지당 오버헤드가 줄었고, 장기적으로는 이를 더 낮추기 위한 로드맵을 설명했다.
- swap cache 사용 개선, folio 기반화, readahead, THP 스왑, 동적 swap 영역 크기 조정 같은 과제가 논의됐다.
- 가상 스왑 계층(virtual swap layer)은 swap 장치 제거, 조각 모음, huge page 스왑을 더 쉽게 만들 수 있는 방향으로 제안됐다.
- Youngjun Park은 임베디드 장치에서 플래시 수명을 늘리기 위한 flash-friendly 스왑 패턴과 중복 제거 기반 설계를 소개했다.

작성

Jonathan Corbet

2026년 5월 18일

LSFMM+BPF

커널의 스왑(swap) 서브시스템은 익명 페이지가 (바라건대) 사용되고 있지 않고, 그 페이지들이 차지한 메모리가 다른 곳에 필요할 때 해당 익명 페이지들을 보조 저장장치에서 관리하는 일을 맡고 있다. 오랫동안 별다른 사랑을 받지 못했던 이 서브시스템은 최근 개발자들의 관심이 다시 늘어났으며, 그래서 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

에서 메모리 관리 트랙의 세 개 개별 세션 주제가 된 것은 놀랄 일이 아니었다. 그중 두 세션은 스왑 코드의 성능과 유지보수성을 개선하는 데 초점을 맞췄고, 하나는 저장장치 트랙과 공동으로 진행되어 스와핑(swapping)을 솔리드 스테이트 저장장치에 더 친화적으로 만드는 방법을 다뤘다.

middle-ad

#### 상태와 로드맵

[![[Kairui Song]](https://static.lwn.net/images/conf/2026/lsfmm/KairuiSong-sm.png)](https://lwn.net/Articles/1072666/) 첫 번째 세션은 Kairui Song이 스왑 서브시스템의 최근 변경 사항과 다음에 올 작업을 매우 빠른 속도로 소개한 발표였다. Song은 먼저 swap table을 도입하고 스왑 서브시스템의 많은 복잡성을 제거한 자신의 작업을 설명했다. 이 작업의 자세한 내용은 [이 기사](https://lwn.net/Articles/1056405/)와 [그 후속 기사](https://lwn.net/Articles/1057102/)를 참고하면 된다. 그의 변경 사항이 7.0에 병합되기 전에는 스왑 서브시스템이 페이지당 3~11바이트의 오버헤드를 발생시켰지만, 이제 그 오버헤드는 2~10바이트로 줄었다. 이 소식은 회의장에서 박수를 받았다.[^p09n1]

하지만 Song의 작업은 끝나지 않았다. 그는 정적 오버헤드를 0바이트로 줄이려 하며, 최대치는 여전히 10바이트가 될 것이다. 오버헤드 상한을 8바이트로 낮추려는 목표는 단기적으로 실현되지 않을 예정이다. [메모리 리소스 컨트롤러](https://docs.kernel.org/admin-guide/cgroup-v1/memory.html)의 refault 추적에는 더 많은 데이터가 필요하기 때문이다. 장기적으로는 여전히 페이지당 최대 오버헤드를 3바이트까지 줄이기를 바라고 있다.

일부 연산이 swap cache를 우회해야 할 필요는 제거됐고, 대부분의 스왑 지향 헬퍼는 이제 folio 기반이다. 이제 대부분의 연산에는 folio lock만 필요하다. 그는 일부 lockless 알고리즘을 적용해 더 최적화할 기회가 있다고 말했다. folio 할당을 swap cache와 통합하는 작업은 아직 진행 중이다. 현재 익명 및 공유 메모리 folio에는 readahead를 우회할 수 있는 자체 할당 로직이 있다. 그는 이 코드를 길고 복잡하며 경쟁 조건이 있는(racy) fallback loop라고 설명했다. 그는 이를 단일 할당 헬퍼로 대체하는 작업을 하고 있다.[^p09n2]

다른 작업은 시스템이 swap cache를 더 잘 활용하게 하는 데 맞춰져 있다. 더 나은 readahead 지원은 그 방향에서 중요한 단계다. [zram 서브시스템](https://docs.kernel.org/admin-guide/blockdev/zram.html)은 이제 이를 활용할 수 있지만, 그것이 실제로 이로운지는 완전히 분명하지 않다고 그는 말했다. zram은 이미 충분히 빠른 것일 수도 있다.

스와핑 I/O는 비동기식이며 시간이 걸린다. 이는 메모리 압박이 시작된 시점과 그 압박을 완화할 수 있게 하는 I/O가 완료되는 시점 사이에 긴 지연이 있을 수 있음을 뜻한다. 그런 일이 벌어질 때쯤이면, 시스템이 과도하게 반응해 실제로 필요한 것보다 더 많은 페이지를 swap out했음이 드러날 수도 있다. 쓰기(writeout)가 완료되는 즉시 swap cache에서 페이지를 제거하면 이 문제를 완화할 수 있다. 그는 왜 지금 항상 그렇게 하지 않는지 확신하지 못하며, 이 부분에는 더 많은 조사가 필요하다.

아직 해결해야 할 다른 문제도 여럿 있다. PMD 수준 huge page의 스와핑은 가능한 만큼 효율적이지 않다. readahead가 최대 절전(hibernation)에 사용되는 페이지를 가져오게 될 수 있는데, 이는 낭비이지만 아주 큰 문제는 아니다. 다만 우회책은 보기 좋지 않다. 그는 최대 절전용으로 예약된 페이지를 표시하기 위해 특수 비트를 추가하는 방안을 생각하고 있다. swap 영역의 크기를 실행 중에 조정할 수 있기를 원하는 사용자들도 있다. 이제는 이를 구현하는 것이 실용적일 것이다.

익명 folio와 공유 메모리(shmfs) folio가 같은 장치로 스왑될 때 또 다른 문제가 생긴다. shmfs 기반 transparent huge page(THP)가 스왑되고 있으면 익명 페이지의 슬롯과 겹칠 수 있다. 현재 그런 일이 발생하면 문제가 된 folio는 단순히 버려진다. 하지만 readahead가 THP 지원을 얻게 되면 이 문제는 더 나빠질 것이다. 그는 이 문제를 해결하기 위해 새로운 swap-table 유형을 만드는 방안을 검토하고 있다. Matthew Wilcox는 문제가 논리적 readahead(소유 프로세스의 주소 공간 내부 기준)와 물리적 readahead의 혼동에서 비롯될 수 있다고 말했다. 그는 어딘가에서 우리가 뭔가 잘못하고 있는 것 같다고 제안했다.

Song은 swap table의 compaction도 살펴보고 있다. 시스템은 swap 공간을 cluster 단위로 관리하며, 이 cluster들은 least-recently-used 목록으로 조직된다. 가득 찬 cluster를 목록에서 제거할 수 있을지도 모른다. 그렇게 하면 성능은 높아지겠지만 메모리 압박은 증가할 수 있다.

위의 모든 내용이 30분짜리 시간대에 압축되어 들어갔지만, Song의 이야기는 아직 끝나지 않았다. 그는 swap file을 "swap mapping"으로 이름 바꿀 시기가 오고 있다고 말했다. 지금의 스와핑은 파일 기반 메모리에 쓰이는 mapping과 매우 비슷해 보인다. 다만 writeback 정책과 locking 방식은 다르다. 새로운 가상 스왑 계층(virtual swap layer)을 추가하면 이 중 많은 부분을 추상화할 수 있으며, 이는 조각 모음(defragmentation)과 migration 같은 여러 다른 문제도 해결할 수 있다. 그는 이 계층의 전체 설계를 보여주는 슬라이드를 띄웠다.

> ![[Virtual swap
>   layer design](https://static.lwn.net/images/conf/2026/lsfmm/virtual-swap.jpg)

이 아이디어의 초기 구현을 담은 [RFC 패치 세트](https://lwn.net/ml/all/20260220-swap-table-p4-v1-0-104795d19815@tencent.com/)가 게시되어 있다. 이 구현은 기존 swap 인프라를 재사용하지만, mapping의 추가 계층을 더한다. 무엇보다도 이 설계는 swap 장치 제거를 더 빠르게 할 수 있게 한다. 제거될 장치에 페이지를 둔 모든 프로세스의 page-table entry를 더 이상 조정할 필요가 없기 때문이다. 또한 swap 장치의 조각 모음도 쉽게 만든다.[^p09n3]

Johannes Weiner는 이 설계가 swap 장치에서 큰 연속 공간 덩어리를 요구하지 않고도 huge page를 swap out하기 쉽게 만들 수 있다고 지적했다. David Hildenbrand는 가상 테이블의 크기가 얼마나 될지, 그리고 그것이 fragmentation을 겪을 수 있는지 물었다. Song은 그 문제를 피할 만큼 테이블을 크게 만들 수 있다고 답했다.

#### 플래시 친화적 스와핑(flash-friendly swapping)

[![[Youngjun Park]](https://static.lwn.net/images/conf/2026/lsfmm/YoungjunPark-sm.png)](https://lwn.net/Articles/1072676/) 스와핑은 많은 I/O를 발생시킬 수 있으며, 제대로 관리하지 않으면 솔리드 스테이트 저장장치의 수명을 크게 단축할 수 있다. Youngjun Park은 swap을 적극적으로 사용하는 임베디드 장치 작업을 하고 있으며, 그는 그런 장치들이 swap 저장장치를 너무 일찍 소모해 버리지 않기를 바란다. 이 세션은 메모리 관리 트랙과 저장장치 트랙이 공동으로 진행했다.

그는 플래시 저장장치가 시간이 지나면 마모된다고 말했다. 데이터를 다시 쓰면 erase cycle이 발생하므로, 데이터를 장치에 복사하면 추가 write와 추가 마모가 생긴다. 내장 flash translation layer(FTL)는 wear leveling을 어느 정도 지원하지만 충분하지 않다. 그 결과 스와핑은 플래시 장치에 부담을 준다. 스와핑은 wear-leveling 알고리즘에 부담을 주는 임의 4KB 연산의 지속적인 흐름을 만들어 내지만, flash-friendly write pattern은 존재하며 이를 활용할 수 있다.

문제가 된 임베디드 장치는 zram과 유사하게 메모리 안에서 페이지를 압축하는 맞춤형 메커니즘을 사용해 RAM으로 swap한다. 이 페이지들은 shrinker로 등록된 커널 스레드에 의해 영구 저장장치로 flush된다. 이 스레드는 erase block에 정렬된 순차 write를 수행한다. write 연산을 줄이는 deduplication 계층도 있다. 특히 이전 최대 절전 라운드에서 저장되어 다시 쓸 필요가 없는 페이지와 일치하는 경우가 많다. 그 결과 저장장치 수명이 크게 늘어난다고 그는 말했다.[^p09n4]

Christoph Hellwig는 Park에게 "보기 좋지 않더라도" 코드를 공유해 달라고 요청했다. 그래야 다른 사람들이 무슨 일이 벌어지고 있는지 이해하는 데 도움이 되기 때문이다. Park은 그것이 block device로 구현되어 있으며 upstream하기 어렵다고 답했다. Hellwig는 요점이 코드를 병합하는 것이 아니라 논의를 진전시키는 데 있다고 말했다. 그는 그 안에 좋은 아이디어가 몇 가지 있다고 했다. 코드는 아마 대대적인 재구성이 필요하겠지만, 동작하는 출발점이 있으면 도움이 된다는 것이다.

[^p09n1]: swap tables의 핵심 효과는 메타데이터 오버헤드와 복잡한 상태 관리를 줄여, 메모리 압박 상황에서 스왑 경로가 더 예측 가능하게 동작하도록 만드는 데 있다. 페이지당 몇 바이트의 차이도 대규모 메모리 시스템에서는 의미 있는 총량이 된다.
[^p09n2]: swap cache는 디스크나 압축 백엔드로부터 읽어 온 스왑 페이지를 커널 페이지 캐시처럼 재사용하게 해 주지만, 잘못된 보존 정책은 메모리 압박 완화를 늦출 수 있다. zswap은 zram과 달리 보통 디스크 swap 앞단의 압축 캐시로 동작하므로, swap cache 정책과 상호작용이 성능에 직접 영향을 줄 수 있다.
[^p09n3]: 가상 스왑 계층은 프로세스의 PTE가 물리 swap 위치에 직접 묶이는 정도를 줄여 장치 제거, migration, defragmentation을 쉽게 만들 수 있다. 이는 스왑을 단순한 블록 주소 배열이 아니라 재배치 가능한 mapping으로 다루려는 방향이다.
[^p09n4]: flash-friendly 설계의 핵심은 임의 4KB 쓰기를 줄이고, erase block 정렬 순차 쓰기와 중복 제거로 write amplification을 낮추는 것이다. 커널 swap 경로가 이런 저장장치 특성을 알면 SSD/eMMC/UFS 기반 장치의 수명과 지연시간 모두에 영향을 줄 수 있다.

---

### [Swap table, flash 친화적 swap, swap_ops, 그 밖의 것들](https://lwn.net/Articles/1072657/) (계속, 2부)

#### 요약

- 논의는 Park의 flash-friendly swap 접근, zswap writeback 대안, 장치별 최적 I/O 패턴 정보를 얻기 어려운 문제를 다루었다.
- Park의 시스템에서 swap 트래픽의 상당 부분이 hibernation에서 비롯되므로, swap과 hibernation을 분리하자는 제안이 나왔다.
- 이어서 swap 저장 계층을 추상화하는 `swap_ops`가 논의되었으며, zram·flash-friendly layer·압축 page I/O 같은 modular swap backend(스왑 백엔드)를 가능하게 할 수 있다는 점이 제시되었다.

Weiner는 Park에게 [zswap](https://docs.kernel.org/admin-guide/mm/zswap.html)에 어떤 형태의 writeback을 덧붙여 사용하는 방안을 검토해 보았는지 물었다. 답은 그 선택지도 고려했지만, 명시되지 않은 이유로 사용하지 않았다는 것이었다. Wilcox는 설명된 접근 방식이 놀랍다고 말하며, erase block 전체를 덮어쓰는 쪽이 대체로 더 잘 동작한다고 했다. Chris Li는 특정 장치에 최적인 I/O 패턴을 설명하는 매개변수를 알아내기가 어렵다고 언급하면서, vendor들이 그런 정보를 더 자유롭게 공개하도록 장려하고 싶다고 말했다.[^p10n1]

세션의 마지막 부분은 Park의 시스템이 hibernation에 크게 의존한다는 사실에 초점을 맞추었다. 이 hibernation이 swap 트래픽의 상당 부분을 만들어 내는 원천이다. 그래서 어쩌면 swap과 hibernation을 분리하고, 여전히 swap 장치를 사용하되 swap 코드와 그 I/O 패턴은 피하는 별도의 hibernation target을 만들 수 있게 하는 편이 더 나을 수 있다는 제안이 나왔다.

#### swap backend 추상화하기

swap 서브시스템은 block device와 직접 인터페이스하도록 설계되었고, block-I/O 작업을 내부에서 생성한다. 하지만 swap 서브시스템의 저장 계층에 다른 종류의 장치를 배치할 수 있게 하는 기능에도 관심이 있다. 이 개념은 "swap_ops"라는 이름으로 불리며, Baoquan He가 [토론 대상으로 제안](https://lwn.net/ml/linux-mm/aZiFvzlBJiYBUDre@MiWiFi-R3L-srv/)했다. 그러나 Li가 세션에서 설명했듯 He는 [Red Hat이 중국 기반 개발 조직 전체를 폐쇄](https://www.theregister.com/software/2026/04/10/red-hat-rhelocates-its-chinese-engineering-team-to-india/5222097)한 일의 영향을 받았고, 그래서 Li가 대신 논의를 진행하게 되었다.

Li는 `swap_ops`의 핵심 아이디어가 modular swap backend(모듈식 swap backend)를 가능하게 하고 일부 swap 동작의 customisation을 허용하는 서브시스템이 되는 것이라고 설명을 시작했다. 그는 이것이 swap을 위한 virtual filesystem(VFS) layer가 될 것이라고 말했다. 이 아이디어는 2023년 LSFMM+BPF 모임에서 처음 [제안](https://lwn.net/Articles/932077/)되었고, [2024년](https://lwn.net/Articles/982887/)과 [2025년](https://lwn.net/Articles/1016136/)에도 추가로 논의되었다. VFS와 비슷한 점은 여럿 있다. 예를 들어 VFS가 filesystem의 시작 부분에 superblock을 갖는다면, swap layer에는 swap header가 있다. VFS의 file은 swap 서브시스템의 folio와 꽤 비슷하고, inode는 swap entry와 유사하며, 그 밖에도 대응되는 요소들이 있다. 하지만 `swap_ops` layer는 훨씬 낮은 overhead를 가지며, directory에 해당하는 기능은 지원하지 않을 것이다.[^p10n2]

Li에 따르면 이 개념을 구현한 patch series가 있다. He는 5월 12일에 [그 series를 갱신](https://lwn.net/ml/all/20260512104201.716213-3-baoquan.he@linux.dev/)했다. Li는 그 가치를 보여 주는 예로, 현재 zram 서브시스템이 block device를 emulate하고 있다는 점을 들었다. zram이 `swap_ops` backend로 구현된다면 많은 코드를 제거할 수 있을 것이다. 다른 가능한 backend로는 Park가 설명한 것 같은 flash-friendly layer, 혹은 raw flash와 함께 동작하는 backend까지 있을 수 있지만, 회의장에서는 그 아이디어를 그다지 받아들이지 않았다. 결국에는 compressed page I/O 지원도 추가될 수 있을 것이다.

마지막에 Li는 backend가 swap slot 할당을 처리하도록 허용하는 것이 합리적일 수도 있다고 말했다. page를 backend들 사이에서 옮기는 최선의 방법을 찾아내는 작업도 남아 있다. Li는 거기서 발표를 마쳤고, 참석자들의 질문은 없었다.[^p10n3]

[댓글(아직 게시되지 않음)](https://lwn.net/Articles/1072657/#Comments)

[^p10n1]: flash 저장장치는 erase block 단위의 지우기와 write amplification 같은 특성이 성능과 수명에 큰 영향을 준다. 따라서 kernel의 swap I/O 패턴이 장치 내부의 flash translation layer와 얼마나 잘 맞는지가 중요하지만, 그 최적 패턴은 vendor별 구현에 강하게 의존한다.

[^p10n2]: `swap_ops`가 VFS와 닮았다는 말은 swap 공간을 더 추상적인 객체와 operation 집합으로 다루겠다는 뜻이다. 다만 일반 filesystem처럼 directory tree나 pathname lookup을 제공하려는 것은 아니며, swap hot path에 맞게 더 가벼운 인터페이스를 목표로 한다.

[^p10n3]: swap slot 할당까지 backend가 맡게 되면 각 저장 매체의 특성에 맞춘 배치와 이동 정책을 구현하기 쉬워질 수 있다. 반대로 kernel 공통 swap 코드와 backend 사이의 책임 경계가 더 복잡해지는 비용도 생긴다.

---

### [per-CPU memory allocator 개선](https://lwn.net/Articles/1072840/)

#### 요약

- 커널의 per-CPU 데이터는 전역 경합을 줄여 성능을 높이지만, 현재 per-CPU memory allocator 자체는 전역 락과 초기화 비용이라는 병목을 갖고 있다.
- RSS 카운터처럼 빈번히 할당·해제되는 per-CPU 객체에서는 CPU 수가 많을수록 배열 초기화 비용과 락 경합이 두드러진다.
- 제안된 해법으로는 단일 스레드 모드에서 시작하는 이중 모드 per-CPU 카운터, slab allocator와의 긴밀한 통합, 그리고 mm_cid 기반 인덱싱이 논의되었다.
- 참석자들은 RSS 전용 최적화보다 더 일반적인 mm_cid 접근법에 무게를 두었지만, `get_user_pages_remote()`와 `ptrace()` 같은 원격 접근 사례는 추가 검토가 필요하다.
- 세션은 Desnoyers가 mm_cid 기반 패치 세트를 준비해 논의를 진전시키는 방향으로 대체로 정리되었다.

작성자

Jonathan Corbet

2026년 5월 19일

LSFMM+BPF

커널에는 per-CPU 데이터를 사용해 성능을 개선할 수 있는 곳이 많다. 하지만 알고 보니, per-CPU 데이터를 위한 커널의 allocator에도 그 자체의 성능 문제가 있다. Harry Yoo는 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

의 메모리 관리 트랙에서 세션을 이끌며, 이러한 문제를 해결하고 per-CPU 데이터의 할당 및 초기화를 가속하는 방법을 살펴보았다.

동적 per-CPU allocator는 2009년 2.6.30 커널 릴리스에 맞춰 [Tejun Heo가 추가](https://git.kernel.org/linus/fbf59bc9d74d)했으며, 그 기반이 되는 per-CPU 데이터 인프라의 기원은 Git 이전의 고대사 속에 묻혀 있다. 이 API 사용자용 문서는 아마 작업 중일 것이며, 곧 나타나기를 기대해 볼 수 있다. per-CPU 영역을 할당하면 CPU 번호로 인덱싱되는 객체 배열이 만들어지며, 각 CPU의 메모리는 경합을 피하기 위해 서로 다른 캐시 라인에 놓인다. 이 데이터의 흔한 사용처는 통계 카운터를 만드는 것이다. 각 CPU는 필요할 때 자기 자신의 카운터를 빠르게 증가시킬 수 있고, 전체값이 필요하면 모든 per-CPU 값의 합을 계산해 얻을 수 있다.[^p11n1]

[![[Harry Yoo]](https://static.lwn.net/images/conf/2026/lsfmm/HarryYoo-sm.png)](https://lwn.net/Articles/1072855/) 이 자리가 메모리 관리 개발자들의 모임이었던 만큼, 각 프로세스의 resident set size(RSS)를 추적하는 데 쓰이는 per-CPU 카운터([`rss_stat`](https://elixir.bootlin.com/linux/v7.0.6/source/include/linux/mm_types.h#L1266), 각 프로세스의 `mm_struct` 구조체에 저장됨)에 특히 관심이 모였다. 메모리 할당과 해제는 자주 일어나는 작업이므로, 프로세스 전역 RSS 카운터를 관리하는 것은 스레드가 많은 프로세스에서 비용이 클 수 있다. 이런 카운터를 per-CPU 배열로 나누면 전역 카운터에서의 경합은 피할 수 있지만, 이 세션에서 논의된 것처럼 다른 성능 문제로 이어질 수 있다.

Yoo는 현재 per-CPU allocator에 두 가지 구체적인 단점이 있다고 말하며 시작했다. 하나는 확장성을 염두에 두고 설계되지 않았다는 점이다. 이 allocator는 메모리 할당과 해제에 전역 락을 사용한다. 여러 CPU가 동시에 per-CPU 메모리를 할당하는 모습은 드물지 않으며, 그 결과 해당 락에서 경합이 발생한다. 다른 문제는 per-CPU 배열을 초기화하는 비용이 클 수 있다는 점인데, 특히 CPU가 많고 데이터 자체의 수명이 짧은 경우 그렇다. 그는 지금까지 여러 해법이 제안되었고, 그 결과 너무 많은 아이디어만 떠다니는 반면 실제 진전은 충분하지 않다고 말했다.[^p11n2]

그런 아이디어 중 하나로 Yoo는 이중 모드 per-CPU 카운터를 들었다. 이는 RSS 카운터와 관련된 성능 문제의 해법으로 Gabriel Krisman Bertazi가 [제안](https://lwn.net/ml/linux-mm/20251127233635.4170047-1-krisman@suse.de/)한 것이다. 이 제안에 따르면 새 프로세스를 위해 카운터 집합을 할당할 때, 그 시점의 프로세스 자체에는 스레드가 하나뿐이므로 단일 스레드 모드로 생성한다. 그러면 초기화 비용이 크게 줄어든다. 해당 프로세스가 같은 주소 공간을 공유하는 새 스레드를 만들면, 카운터는 완전한 per-CPU 모드로 업그레이드된다. 많은 프로세스가 결국 스레드를 만들지 않는다는 점을 고려하면, 이 제안은 상당수 경우 초기화 비용을 완전히 없애 준다.

[Yoo의 이 시리즈](https://lwn.net/ml/linux-mm/20250424080755.272925-1-harry.yoo@oracle.com/)에 제시된 대안은 per-CPU allocator를 slab allocator와 더 긴밀히 통합하고, 오래전에 제거되었던 slab destructor 동작을 복원하는 것이다. 그렇게 하면 per-CPU 객체를 slab cache 안에 보존할 수 있으며, 특히 constructor는 최초 할당 시에만 호출하면 된다. 이 방식은 per-CPU 객체 사용자들이 객체를 해제할 때 합리적인 상태로 남겨 두는 경우에만 동작한다. Yoo는 이 접근법에서는 데드락을 피하기 위해 destructor에서의 락 획득을 제한하도록 어느 정도 주의가 필요하다고 말했다.[^p11n3]

middle-ad 마지막으로, Mathieu Desnoyers(원격 연결로 세션에 참석)는 이 작업에 "per-MM concurrency IDs"(또는 "mm_cids")를 사용하는 방안을 [제안](https://lwn.net/ml/linux-mm/355143c9-78c7-4da1-9033-5ae6fa50efad@efficios.com/)했다. mm_cid는 restartable-sequences 서브시스템의 일부로 유지되는 가상 CPU ID이다. 실제 CPU 번호는 시스템이 이론상 지원할 수 있는 CPU 수만큼 커질 수 있지만, mm_cid는 실행 중인 프로세스가 가진 스레드 수와 그 프로세스가 실행을 허용받은 CPU 수 양쪽에 의해 제한된다. 따라서 일반적으로 훨씬 작은 수가 된다. 256-CPU 시스템에서 네 개의 스레드를 가진 프로세스는 255만큼 큰 CPU 번호를 볼 수 있지만, 그 프로세스의 최대 mm_cid는 3이 된다. 이 기능에 관한 자세한 내용은 [이 기사](https://lwn.net/Articles/885818/)와 [`rseq()` 매뉴얼 페이지](https://lwn.net/Articles/1033957/)를 참고하라.

Desnoyers가 세션에서 설명한 제안의 핵심은 per-CPU 데이터를 실제 CPU ID가 아니라 mm_cid로 인덱싱할 수 있다는 것이다. 그렇게 해도 각 CPU의 배열 접근은 여전히 격리할 수 있지만, 배열 자체는 훨씬 작아질 수 있다. 개별 엔트리는 처음 사용될 때 초기화되어 초기화 비용을 낮게 유지한다.

Kiryl Shutsemau는 [`get_user_pages_remote()`](https://elixir.bootlin.com/linux/v7.0.6/source/mm/gup.c#L2547)가 자신이 실행 중인 CPU가 아닌 다른 CPU에서 페이지를 할당할 수 있다고 지적했고, Shakeel Butt는 일반적으로 다른 CPU의 카운터에 대한 원격 접근이 어떻게 되는지 궁금해했다. Shutsemau는 [`ptrace()`](https://man7.org/linux/man-pages/man2/ptrace.2.html)로 프로세스를 조작하는 경우처럼 원격 접근이 일어나는 다른 사례들도 제기했다. 그런 경우 문제의 코드는 자신이 조작하는 프로세스의 일부가 아니므로 mm_cid가 일치하지 않는다. Desnoyers는 그런 경우는 흔치 않을 것이며, 별도 카운터를 추가해 처리하는 것이 최선일 수 있다고 말했다.

Yoo는 메인라인에 어떤 형태로든 해법이 필요하다고 말하며 결론을 재촉했다. Davidlohr Bueso는 mm_cid 아이디어를 지지한다는 뜻을 보이며, 무엇이 이 방법의 채택을 막을 문제가 될지 물었다. Shutsemau는 `get_user_pages_remote()` 문제를 다시 제기했지만, 그것이 실제로 문제인지 아닌지를 판단하려면 더 자세히 살펴봐야 한다고 말했다. Suren Baghdasaryan은 mm_cid 해법이 전반적으로 얼마나 많은 추가 오버헤드를 더할지 궁금해했다.

다른 한 참석자는 RSS 카운터가 부정확한 것으로 알려져 있으며, Desnoyers가 이를 개선하기 위한 [패치 시리즈](https://lwn.net/ml/all/20260227153730.1556542-1-mathieu.desnoyers@efficios.com/)를 배포해 왔다고 지적했다. 그는 per-CPU 문제에 대해 제안된 일부 해법은 RSS 카운터 형식에 특화되어 있다며, mm_cid 해법이 더 일반적이고 더 바람직할 것이라고 시사했다.[^p11n4]

Yoo는 다시 한번 결론이 무엇이어야 하는지 묻고 세션을 마무리했다. 회의장은 mm_cid 접근법을 택하는 쪽으로 합의가 형성되는 듯했다. Butt는 Desnoyers가 그 해법을 구현한 패치를 보내야 한다고 제안했다. Desnoyers는 그 아이디어가 현재로서는 머릿속에만 존재하므로, 제대로 된 패치 세트를 구성하려면 시간이 좀 걸릴 것이라고 말했다.

[댓글(1개 게시됨)](https://lwn.net/Articles/1072840/#Comments)

[^p11n1]: per-CPU memory allocator는 전역 원자 연산이나 락을 회피하기 위해 같은 논리 객체를 CPU별 인스턴스로 복제한다. 이 방식은 쓰기 경합을 줄이는 대신, 합산 시 전체 CPU의 값을 순회해야 하는 읽기 비용을 만든다.
[^p11n2]: CPU 수가 늘어날수록 per-CPU 배열의 크기와 초기화 범위가 커진다. allocator가 내부적으로 관리하는 chunks(청크)와 메타데이터도 함께 커질 수 있어, 짧은 수명의 객체에서는 실제 작업보다 준비 비용이 더 두드러질 수 있다.
[^p11n3]: slab allocator와 per-CPU allocator를 결합하면 객체 재사용으로 constructor 비용을 줄일 수 있지만, 해제 시점의 상태 불변식이 더 중요해진다. destructor에서 락을 잡는 설계는 allocator 경로의 락 순서와 충돌해 데드락을 만들 수 있다.
[^p11n4]: NUMA(Non-Uniform Memory Access) 시스템에서는 per-CPU 배치가 단순한 캐시 라인 분리 이상의 의미를 갖는다. CPU별 데이터가 어느 NUMA 노드의 메모리에 놓이는지에 따라 원격 메모리 접근 비용과 allocator 확장성이 달라질 수 있다.

---

### [CXL에서 무슨 일이 끓어오르고 있나](https://lwn.net/Articles/1072858/)

#### 요약

- CXL(Compute Express Link)은 데이터센터에서 CPU 근처에 (공유 가능) 메모리 노드를 제공하려는 기술이지만, 커널의 메모리 관리 문제를 더 복잡하게 만들고 있다.
- PCIe 버스를 통해 제공되는 CXL 메모리는 원격 NUMA 메모리보다 지연 시간이 더 나쁜 경우가 많지만, 인터리빙 등 높은 구성 가능성으로 성능을 조정할 수 있다.
- 표준과 하드웨어 구현이 빠르게 변하면서, 커널은 ACPI식 “code-first” 접근에 가깝게 관례를 문서화하고 제조사 간 호환성을 유도하고 있다.
- 오류 처리, 가속기 지원, vfio-cxl, 동적 용량(dynamic capacity), device DAX 및 guest_memfd 연동이 주요 개발 영역이다.
- 반면 CXL 호스트 브리지가 사라질 때의 오류 격리, 피어 투 피어(peer-to-peer) 동작, CXL 암호화 지원은 당분간 기대하기 어렵다.

작성자

Jonathan Corbet

2026년 5월 19일

LSFMM+BPF

CXL(Compute Express Link)

은 데이터센터에서 가까운 CPU에 (공유될 수도 있는) 메모리를 제공하는 “메모리 노드(memory nodes)”를 구축할 수 있게 하려는 기술이다. Dan Williams는 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

의 메모리 관리 트랙 세션을 시작하면서, CXL이 “

2021년부터 메모리 관리 문제를 더 악화시켜 왔다

”고 말했다. 그는 이 세션에서 CXL이 앞으로도 그 기록을 어떻게 이어갈 것으로 예상되는지 개괄했다.

middle-ad

Williams는 먼저 CXL이 PCIe 버스를 통해 메모리를 제공하는 방식이라고 설명했다. 일반적으로 CXL은 원격 NUMA 노드의 메모리에 접근하는 것보다 더 나쁜 지연 시간을 보인다. CXL의 강점이자 과제는 구성 가능성이 매우 높다는 점이다. 예를 들어 성능을 개선하는 인터리브드 메모리 접근을 설정할 수 있다. 한 가지 문제는 커널이 CXL 메모리에 대한 일부 접근을 제어할 수 있는 반면, 시스템 펌웨어도 그와 관련해 무언가를 하려 한다는 것이다. 또 다른 과제는 CXL 메모리의 핫플러그 특성에서 나온다. CXL 메모리가 사라지면 시스템 RAM의 일부도 사라질 수 있다.

[![[Dan Williams]](https://static.lwn.net/images/conf/2026/lsfmm/DanWilliams-sm.png)](https://lwn.net/Articles/1072861/) CXL 표준은 빠르게 진화하고 있으며, 제조사들은 채택된 표준에서 흥미로운 방식으로 벗어난 하드웨어를 내놓고 있다. 커널은 이러한 변화와 관련해 ACPI의 “code-first” 정책과 비슷한 방식을 따르며, 커널 트리 안에 그것들을 [문서화하고 있다](https://docs.kernel.org/driver-api/cxl/conventions.html). 바라는 바는 제조사들에게 “누군가가 이런 방식으로 망가뜨렸으니, 여러분 것도 같은 방식으로 망가뜨려 달라”는 메시지를 보내는 것이다.

오류 처리도 진화 중인 영역이다. CXL 프로토콜 오류는 PCIe 내부 오류로 커널에 보고되지만, PCIe 코어 코드가 이를 처리할 필요가 없도록 사이드 채널을 통해 처리된다. CXL 코드는 오류 처리 경로에 커널 패닉을 도입하고 있다. 이는 보통 커널 코드에서 환영받는 일은 아니지만, Williams는 그런 상황에서는 어차피 펌웨어가 시스템을 패닉 상태로 만들 것이라고 말했다.[^p12n1]

가속기 지원(예를 들어 메모리 대 메모리 압축)은 커널에 들어가기 직전이다. 알고 보니 가속기는 지원하기가 비교적 단순하다. 또 다른 개발 영역은 [vfio-cxl](https://lwn.net/ml/all/20251209165019.2643142-1-mhonap@nvidia.com/)로, CXL 가속기를 가상 머신으로 내보낼 수 있게 하는 메커니즘이다.

동적 용량(dynamic capacity)은 시스템 설계자들에게 오랫동안 꿈과 같은 기능이었다고 Williams는 말했다. 많은 DIMM을 사서 한 상자에 넣고, 케이블을 연결하면 여러 호스트가 그 메모리를 매핑할 수 있다. 하지만 그러면 커널은 어떻게든 그 메모리를 사용자 공간에서 사용할 수 있게 만들어야 한다. 계획은 [device DAX](https://docs.kernel.org/arch/powerpc/vmemmap_dedup.html)를 인터페이스로 사용하는 것이지만, 전용 메모리를 위한 사설 노드를 어떻게 만들 것인지에 대한 질문이 남아 있다(이 주제는 다음 날 다시 다뤄질 예정이었다). [guest_memfd](https://lwn.net/Articles/949277/)와의 통합도 필요하다.[^p12n2]

CXL 지원에서 *아직 끓어오르지 않고 있는* 것은 무엇일까? 개발이 이뤄지지 않는 영역 중 하나는 오류 격리(error isolation)다. CXL 호스트 브리지가 사라지면 관련된 모든 장치가 실패하고, 테라바이트 단위의 시스템 RAM이 사라질 수 있다. 적어도 메모리가 관련된 경우, 시스템이 그런 사건에서 살아남을 수 있는 방법을 상상하기는 어렵다. 가속기 사용자에 대한 오류 격리는 더 실현 가능할 수도 있다. 또한 현재 CXL 장치에서 피어 투 피어(peer-to-peer) 작업을 지원하는 작업도 없지만, “언젠가는 누군가가 원하게 될 것”이다. 마지막으로 Williams가 “또 다른 두문자어 양동이”라고 표현한 CXL 암호화도 가까운 미래에 지원될 것으로 예상되지는 않는다.[^p12n3]

세션은 거기서 끝났고, 참석자들 사이에 실제 토론은 없었다.

[댓글(1개 게시됨)](https://lwn.net/Articles/1072858/#Comments)

[^p12n1]: CXL 장치의 오류가 PCIe 오류처럼 보이더라도 실제 복구 경로는 CXL 전용 처리에 의존한다. 시스템 메모리와 직접 연결된 장치에서 오류가 나면 커널이 안정적으로 계속 실행될 보장이 낮아져, 패닉이 현실적인 선택지가 될 수 있다.
[^p12n2]: 동적 용량과 device DAX는 CXL memory expander나 CXL fabric 뒤의 메모리를 “파일처럼 매핑 가능한” 장치 메모리로 노출하는 방향과 맞닿아 있다. 이는 페이지 할당기, NUMA 토폴로지, 가상 머신의 guest_memfd 통합까지 영향을 준다.
[^p12n3]: CXL 호스트 브리지 장애는 단순한 장치 장애가 아니라 커널이 RAM으로 쓰던 주소 공간의 소실을 의미할 수 있다. 따라서 일반적인 핫플러그 장치처럼 격리·복구하기 어렵고, fabric 수준의 신뢰성 설계가 중요해진다.

---

### [MGLRU를 어떻게 해야 하는가?](https://lwn.net/Articles/1072866/)

#### 요약

- 커널 메모리 회수(reclaim) 경로에는 전통적인 LRU와 MGLRU가 함께 존재하며, `mm/vmscan.c` 안에서 중복과 복잡성을 키우고 있다.
- Shakeel Butt와 Emil Tsalapatis는 두 구현 중 하나를 즉시 고르는 대신, 공통 기능을 식별하고 코드 구조를 정리해 통합 가능성을 높이자고 제안했다.
- 논의에서는 페이지 테이블 엔트리 수집, refault distance 계산, 통계 카운터, 파일 기반/익명 메모리 균형 등 핵심 휴리스틱 차이가 다뤄졌다.
- 참석자들은 벤치마크와 워크로드가 중요하지만 모든 reclaim 특성을 쉽게 측정할 수는 없다는 점에도 주목했다.
- 최종 목표는 가능하다면 하나의 reclaim 구현으로 수렴하는 것이지만, 우선 두 구현을 분리·정리해 이해 가능성과 공유 코드를 늘리는 방향에 대체로 공감대가 있었다.

글쓴이

Jonathan Corbet

2026년 5월 20일

LSFMM+BPF

"회수(reclaim)"는 현재 사용자가 쓰고 있는 메모리 중 빼앗아 시스템 안에서 더 나은 용도로 돌릴 수 있는 것을 찾아내는 작업이다. 이는 메모리 관리(memory management) 그림의 핵심 부분이다.[^p13n1] 

다세대 LRU

(MGLRU)는 그 이전의 "전통적인 LRU"보다 나은 reclaim 구현을 제공하려는 의도로 추가되었지만, 오히려 상황을 복잡하게 만들었다. 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

의 메모리 관리 트랙 세션 중 적어도 세 개가 MGLRU에 초점을 맞추었다. 목표는 MGLRU를 더 완전하게 통합하고, 성능을 개선하며, Android 시스템에서 마주친 몇 가지 문제를 해결하는 것이었다.

middle-ad

#### reclaim 코드 통합

[![[Shakeel Butt]](https://static.lwn.net/images/conf/2026/lsfmm/ShakeelButt2-sm.png)](https://lwn.net/Articles/1072877/) Shakeel Butt가 reclaim 중심의 논의를 [제안했을](https://lwn.net/ml/linux-mm/20260325210637.3704220-1-shakeel.butt@linux.dev/) 때, 그는 해당 코드의 현재 상태에 대한 자기 의견을 분명히 밝혔다.

> 커널의 메모리 reclaim은 엉망입니다. 우리는 전통적인 LRU와 MGLRU라는 완전히 별개의 축출(eviction) 알고리즘 두 개를 같은 파일 안에 담아 배포하고 있습니다. `mm/vmscan.c`는 8,000줄이 넘습니다. 그중 40%는 전통적인 경로에 이미 존재하는 기능을 중복 구현한 MGLRU 전용 코드입니다. 모든 버그 수정, 모든 최적화, 모든 기능을 두 번 해야 합니다. 그러지 않으면 사용자 절반에게만 동작합니다. 이는 지속 가능하지 않습니다. 멈춰야 합니다.

그 결과 열린 세션에서 그는 Emil Tsalapatis와 함께, 점점 더 나빠지고 있다고 그가 말한 문제에 대한 해답을 찾고자 했다. 그들은 커널의 두 reclaim 하위 시스템을 통합할 방법을 찾고 싶어 한다.

그가 제안한 방법론은 두 대안 중 승자를 고르는 것이 아니라, 가능한 한 두 구현을 통합할 방법을 찾는 것이다. 그러려면 두 구현을 모두 잘 이해해야 하는데, MGLRU 개발자가 사라졌고 실제로 아무도 그것을 제대로 이해하지 못한다는 사실 때문에 일이 복잡해진다고 그는 말했다. (이어진 논의에서는 MGLRU가 그가 생각했던 것보다는 더 잘 이해되고 있음이 분명해졌다.) 통합 작업에는 성능을 평가할 방법이 필요하다. 즉 특정 알고리즘의 강점과 약점을 드러낼 수 있는 좋은 워크로드 집합이 필요하다.

Lorenzo Stoakes는 유용한 첫 단계로 코드를 모듈화하자고 제안했다. 이는 두 구현 사이에 공유되는 코드의 양을 늘리는 좋은 방법일 수 있다. 그런 다음 Butt는 네 단계로 된 자신의 상위 수준 계획을 설명했다.

1. 두 코드베이스를 하나의 큰 파일에 함께 두는 대신, 각각 별도의 파일로 분리한다.
2. reclaim 패치를 평가하는 데 사용할 수 있는 워크로드를 정의한다.
3. 두 구현 사이의 공통 기능을 찾는다.
4. 각 기능의 구현을 비교한다.

한 참석자는 파일을 분리하려는 계획이 Git 이력을 혼란스럽게 만들 수 있다고 우려하며 문제를 제기했지만, 다른 사람들은 대체로 어떤 형태로든 정리가 필요하다고 보는 듯했다. Vlastimil Babka는 구현을 분리하면 그것들을 통합하는 작업이 더 복잡해질 수 있다고 생각했다. Johannes Weiner는 어차피 MGLRU에는 Git 이력이 많지 않다고 말했다. 그는 가능한 것은 분리해야 하지만, 서로 뒤섞인 코드가 많아 떼어내기 어려울 것이라고 했다. 그다음에는 양쪽이 사용하는 공통 코드로 기능을 구현할 방법을 찾아야 한다고 말했다.

Chris Li는 Kairui Song이 보류 중인 좋은 MGLRU 개선 작업을 여럿 가지고 있다고 언급했다([예](https://lwn.net/ml/all/20260428-mglru-reclaim-v7-0-02fabb92dc43@tencent.com/)). 코드를 흔들어 많은 충돌을 만들어 내는 것은 그 작업에 도움이 되지 않을 것이다. 그는 개선은 좋은 일이며, 그것들을 잃고 싶지 않다고 말했다. Butt도 동의했지만, 그 작업이 두 구현의 통합에 도움이 되는지를 기준으로 평가되어야 한다고도 말했다. Stoakes는 커널 개발에서는 충돌이 자주 일어나며, 충돌은 관리되는 것이지 다른 작업을 막도록 허용되는 것이 아니라고 말했다.

청중 한 명은 일부 기능이 벤치마크 집합으로 쉽게 측정되지 않는다고 우려했다. 그는 특히 MGLRU가 전통적인 LRU보다 훨씬 더 빨리 out-of-memory killer에 의존하게 된다는 점을 언급했다. 그는 이를 스래싱(thrashing)을 방지하는 좋은 기능으로 보았다.[^p13n2]

이 지점에서 Tsalapatis가 이어받아 계획을 더 자세히 논의했다. 그 계획은 두 구현을 깔끔하게 분리하여 각각의 구조를 더 잘 파악하고, 두 구현 사이의 공통점을 확인하는 것을 포함한다. 워크로드 수집은 완전한 집합을 만들려는 것이 아니다. 목적은 개선(또는 회귀)을 보여줄 수 있는 중요한 워크로드를 확보하는 것이다. 공통 기능의 정의는 이 작업에서 중요한 부분이다. 두 구현에는 공통 기능이 많지만, 그것들을 지칭하는 어휘가 다르다. 두 구현 모두 많은 휴리스틱에 의존한다. 양쪽 모두에 이식 가능한 휴리스틱이 있는지 염두에 두고, 그것들을 식별해야 한다. 예를 들어 두 구현은 파일 기반 페이지와 익명 페이지의 비율을 서로 다르게 계산하는데, 왜 그런지는 분명하지 않다. 마지막으로 통합 구현을 만들려면 각 기능에 대해 가능한 선택지 중 어느 것을 택할지 결정해야 한다.

[![[Emil Tsalapatis]](https://static.lwn.net/images/conf/2026/lsfmm/EmilTsalapatis-sm.png)](https://lwn.net/Articles/1072878/) 그는 페이지 테이블 엔트리 수집(page-table-entry harvesting)부터 시작해 여러 예를 다루었다. 이는 페이지 테이블에서 정보, 주로 "이 페이지가 접근되었다" 비트를 얻어내는 과정이다. 전통적인 LRU는 역매핑(reverse-mapping) 인프라를 사용해 엔트리를 순회하는 반면, MGLRU는 페이지 테이블 스캔을 사용한다. 이를 서로 바꿔 적용해 보고, 궁극적으로 이 구현을 일반화하는 것은 흥미로울 것이다.

refault distance 계산(본질적으로 한 페이지가 reclaim된 뒤 다시 fault되어 들어오기까지 얼마나 시간이 지나는지)은 두 구현에서 서로 다르며, 그는 그 이유를 알지 못한다. 전통적인 LRU에는 "실전 검증된(battle-tested)" 구현이 있다. 어쩌면 MGLRU가 그것을 사용하도록 전환할 수도 있다. 두 구현은 서로 다른 통계 카운터를 유지한다. 코드를 공유하려면 이들도 통합되어야 한다.

그는 MGLRU가 [`mmap()`](https://man7.org/linux/man-pages/man2/mmap.2.html)으로 매핑된 파일 기반 페이지에 우선순위를 부여한다고 말했다. 반면 전통적인 LRU는 실행 가능 페이지를 비활성화하지 않으려 한다. 이 두 휴리스틱은 동등할 수도 있지만, Tsalapatis는 확신하지 못했다. MGLRU는 빠르게 refault된 페이지를 표시한다. 전통적인 LRU는 대신 그것들을 곧바로 active list로 옮긴다. control group 안에서 reclaim할 시간이 오면, 전통적인 LRU는 하위 워터마크에 도달할 때까지 페이지를 축출하는 반면 MGLRU에는 더 복잡한 부하 분산 알고리즘이 있다.[^p13n3]

파일 기반 메모리와 익명 메모리 사이의 균형은 reclaim 알고리즘이 적용하는 핵심 휴리스틱 중 하나다. 전통적인 LRU는 몇 가지 특수 휴리스틱의 도움을 받아 [swappiness](https://docs.kernel.org/admin-guide/sysctl/vm.html#swappiness) 설정에 의해 구동된다. 반면 MGLRU는 그 결정을 이끌기 위해 [자신의 비례-적분-미분(PID) 제어기](https://docs.kernel.org/mm/multigen_lru.html#pid-controller)를 가지고 있지만, 여전히 swappiness도 고려한다. PID 제어기가 실제로 이로운지는 분명하지 않다.

이때 Song이 끼어들어, 이런 질문 중 다수에 대한 답은 자신의 패치 세트에서 찾을 수 있다고 말했다. 그는 자신이 제목을 잘못 골랐으며, 제목 어딘가에는 "unify"가 들어갔어야 했다고 말했다.

시간이 부족해지고 있었다. Tsalapatis는 진행 방식에 대해 합의가 이루어진 것처럼 들린다고 말했다. 하지만 John Hubbard는 그렇게 확신하지 못했다. 그는 커널 안에 단일 reclaim 구현이 있기를 바란다. 개발자들은 현재 두 구현의 장점을 모두 가진 하나를 고른 뒤 앞으로 나아가야 한다. 그는 둘을 분리하는 것이 그 목표에 도달하는 데 도움이 되지 않는다고 말했다. Butt는 궁극적인 목표가 커널 안에 단 하나의 reclaim 구현만 두는 것이라고 말했다. Stoakes는 결국 둘을 모두 유지해야 할 좋은 이유가 드러날 수도 있지만, 개발자들이 그것을 알기까지는 시간이 걸릴 것이라고 말했다. 그동안 둘을 같은 파일 안에 두는 것은 해를 끼치고 있다. 그는 정리에 대한 전반적인 합의가 있었다고 보았다.

[^p13n1]: 커널 reclaim은 단순히 "메모리를 비우는" 기능이 아니라, 파일 캐시·익명 메모리·스왑·cgroup 한계 사이의 우선순위를 정하는 정책 계층이다. 따라서 reclaim 경로의 중복은 성능 문제뿐 아니라 버그 수정과 정책 변경의 일관성 문제로 이어진다.
[^p13n2]: OOM killer로 더 빨리 넘어가는 정책은 과도한 reclaim 반복으로 시스템 전체가 느려지는 상황을 줄일 수 있지만, 워크로드에 따라서는 프로세스 종료라는 더 급격한 실패 모드로 나타날 수 있다. 그래서 평균 처리량 벤치마크만으로는 장단점을 판단하기 어렵다.
[^p13n3]: cgroup 단위 reclaim의 차이는 컨테이너 환경에서 특히 중요하다. 같은 전역 메모리 압박이라도 어떤 cgroup의 페이지를 먼저 축출할지에 따라 격리성, 지연시간, 서비스별 메모리 공정성이 달라질 수 있다.

---

### [MGLRU를 어떻게 해야 하는가?](https://lwn.net/Articles/1072866/) (계속 2부)

#### 요약

- 논의는 Kairui Song의 MGLRU 개선 계획으로 이어졌으며, 기존 LRU와 MGLRU 구현을 어떻게 통합·분리할지가 핵심 쟁점으로 남았다.
- MGLRU는 락 경합과 reverse-mapping 비용을 줄이는 등 많은 워크로드에서 효과적이지만, page cache 보호와 active/inactive 지표, writeback throttling에는 아직 개선 여지가 있다.
- Android에서는 MGLRU가 대규모 기기에 배포되어 있지만, 120Hz 렌더링 예산 안에서 reclaim이 끝나야 하므로 foreground 앱, file-backed page, direct reclaim 지연을 더 세밀히 제어해야 한다.
- 참석자들은 벤더별 해킹보다 MGLRU가 aging, reclaim 중단, 태스크 우선순위 인식 같은 일반 인터페이스를 제공하는 방향을 기대했다.

Suren Baghdasaryan은 전반적인 계획은 좋아 보이며, 주된 논쟁점은 두 구현을 분리하는 문제라고 말했다. 하지만 그는 그 분리가 그렇게 어렵지는 않을 것이며, 필요하다면 현재 작업이 병합된 뒤로 미룰 수도 있다고 보았다. Weiner도 이에 동의하며, 세션이 시스템의 상당 부분이 잘 이해되지 않았고 구현들을 통합해야 한다는 주장으로 시작되었다고 말했다. 그에 따르면 Song은 이미 그중 많은 부분을 해결했다. Song의 작업이 출발점이 되어야 하며, 그 뒤에 분리가 이루어질 수 있다. Li는 Song이 그 분리 작업을 할 수 있겠다고 제안했지만, Weiner는 그런 식으로 과제를 배정할 수는 없다고 말했다. 이 작업은 그룹 차원의 노력이 되어야 한다는 것이다.

#### MGLRU 개선 계획

[![[Kairui Song]](https://static.lwn.net/images/conf/2026/lsfmm/KairuiSong2-sm.png)](https://lwn.net/Articles/1072885/) 다음 날 Song은 자신이 MGLRU에서 수행한 작업과 앞으로 무엇이 필요하다고 생각하는지를 설명하기 위해 별도 세션을 진행했다. 그는 MGLRU가 완벽하지는 않지만 많은 워크로드에서 "놀라울 정도로 좋다"고 말했다. MGLRU는 전통적인 LRU보다 락 경합이 낮고, lazy-promotion 방식 덕분에 비교적 효율적이다. reverse-mapping 오버헤드도 더 낮으며, 내장된 bloom filter는 메모리의 hot 영역에 집중하는 데 도움이 된다. 한 참석자가 그 필터가 실제로 얼마나 도움이 되는지 물었고, Song은 측정하기 쉽다며 답은 꽤 많이 도움이 된다는 것이라고 말했다.[^p14n1]

Song의 목표는 MGLRU를 "더 좋고 더 똑똑하게" 만드는 것이다. 현재 MGLRU는 많은 워크로드에서 전통적인 LRU보다 더 나은 성능을 보인다. 여러 배포판이 이를 채택했다는 사실은 그 점에서 강한 신호다. MGLRU는 여러 실제 문제를 해결한다. 예를 들어 time-to-live(TTL) 휴리스틱은 thrashing을 방지하는 데 도움이 된다. working-set 감지도 더 좋아지고 있다. MGLRU에 빠져 있는 한 가지는 control group을 위한 writeback throttling이다. 이는 현재 수정되고 있지만, global writeback throttling은 여전히 빠져 있다.

MGLRU는 page fault에 대응해 생성된 folio와 그 밖의 folio를 구분한다. fault로 생성된 folio는 더 빨리 활성화된다. Song은 이 동작이 애플리케이션이 메모리 읽기에서 stall이 일어나지 않기를 기대한다는 가정에서 나온 것이라고 말했다. 하지만 `mmap()`으로 매핑한 파일에서 읽는 경우는 그 모델에 맞지 않는다. Barry Song이 이 상황을 고치려는 [패치](https://lwn.net/ml/all/20260418120233.7162-1-baohua@kernel.org/)를 내놓았다. 다만 그는 이 동작을 그냥 제거하는 편이 더 나을 수도 있다고 생각했다.

`/proc/meminfo`에는 active 및 inactive page 수에 관한 지표가 유지되지만, MGLRU는 이를 잘 관리하지 못하며 그 결과 숫자가 "튀는" 모습을 보인다. MGLRU는 가장 어린 두 세대의 page를 active로 간주하므로, 세대가 aging될 때 큰 변화가 생긴다. 이 문제를 고치기 위한 작업이 ["MGLRU-FG" 패치 세트](https://lwn.net/Articles/1070902/)에서 진행 중이다.

또 다른 문제는 MGLRU가 page cache를 충분히 보호하지 못한다는 점이라고 Song은 말했다. anonymous page가 많은 워크로드는 잘 동작하지만, page cache에 더 의존하는 워크로드는 성능이 퇴보할 수 있다. 그는 이것이 단순한 균형 조정의 문제가 아니라 working set을 제대로 식별하는 문제라고 말했다. PID controller가 이를 제대로 수행하지 못하고 있다는 것이다. MGLRU-FG 작업은 이 영역의 지표를 통합하고 working-set 감지를 개선하는 것을 목표로 하며, 그 결과 성능이 상당히 좋아진다.[^p14n2]

David Hildenbrand는 MGLRU가 병합될 때 계획은 이를 기본값으로 만드는 것이었다고 말하며, 왜 지금 사람들이 이를 쓰지 않기로 선택할 수 있는지 Song에게 물었다. Song은 많은 배포판이 전환했지만 page-cache 성능 회귀를 겪는 사용자들이 있다고 답했다. 그는 그 문제가 해결되고 나면 MGLRU를 그냥 사용하지 않을 이유가 없다고 본다고 말했다.

Hildenbrand는 이어 page-flag 사용에 대해 물었다. 이 비트들은 부족한 자원이며, MGLRU는 그중 여러 개를 사용한다. Song은 MGLRU-FG 시리즈가 그 사용량을 네 비트에서 세 비트로 줄인다고 말했다. Hildenbrand는 그것이 MGLRU를 이제 32비트 시스템(사용 가능한 page flag가 더 적은 시스템)에서도 사용할 수 있다는 뜻인지 물었다. 통합된 reclaim 구현은 "우리가 신경 쓰지 않는 모든 아키텍처"에서도 동작해야 한다는 것이다. Song은 약간의 성능 영향을 감수하면 flag 사용량을 두 비트로 줄일 수 있다고 말했다.

세션 말미에 Song이 자신이 작업해 온 다른 몇 가지를 언급하면서 진행 속도가 빨라졌다. 그는 두 구현 사이에서 refault distance 계산을 통합하려 하고 있다. 세대와 tier 수를 각각 둘로 줄이면 "traditional-LRU compatibility mode"를 구현할 수 있다. 또한 그는 세대 수(보통 네 개로 설정됨)를 늘리면서 관련 page flag 사용량은 줄이는 작업도 하고 있다. 궁극적으로는 64개 세대를 지원할 수 있어야 한다. Matthew Wilcox가 64개가 얼마나 더 나을지 물었지만, Song은 뚜렷한 답은 없다고 하면서도 그 실험을 돌리는 비용은 낮다고 말했다.

미래 아이디어 중 하나는 BPF를 사용해 MGLRU를 확장하는 것이다. 이를 통해 fault가 발생한 folio를 어느 세대에 넣을지 BPF 프로그램이 결정할 수 있는 hook을 제공할 수 있다. 또 다른 hook은 접근 시 folio를 다른 세대로 옮길 수 있게 할 수 있다. 그러면 관리자 제어 아래 여러 가지 reclaim 정책을 구현할 수 있다. 시간이 다 되어 갈 무렵, 한 참석자는 이것이 과도한 설계일 수도 있다고 제안했다.

#### Android에서의 MGLRU

[![[Zicheng Wang]](https://static.lwn.net/images/conf/2026/lsfmm/ZichengWang-sm.png)](https://lwn.net/Articles/1072879/) Zicheng Wang은 출하하는 모든 기기에서 MGLRU를 활성화하기로 한 스마트폰 제조사 HONOR에서 일한다. 전체적으로 약 7천만 대의 기기가 MGLRU를 실행하고 있다는 뜻이다. 그는 Android가 메모리를 심하게 overcommit하며, 좋은 성능을 내려면 공격적인 reclaim이 필요하다고 말했다. 하지만 그 reclaim 작업은 8.3ms 시간 예산 안에 들어와야 한다. 그보다 길어지면 초당 120프레임 화면에서 렌더링 stall을 일으킬 수 있다. reclaim이 critical path를 막도록 허용해서는 안 된다.[^p14n3]

그는 Android 앱 lifecycle이 launch에서 시작해 foreground, background, frozen 상태 사이의 전환으로 이어진다고 말했다. Android는 빠른 launch를 위해 초기 단계에서 많은 page를 preload하는 경향이 있으며, 필요하지 않은 메모리는 공격적인 reclaim으로 정리하는 데 의존한다. Wang은 MGLRU가 file-backed page를 너무 많이 reclaim해 일부 시나리오에서 성능을 떨어뜨린다고 말했다. 예를 들어 camera launch가 느려질 수 있다. 이 문제의 한 해법은 active aging이다. 앱이 background로 들어가면 그 앱의 page를 aging 대상으로 삼는다. 이는 anonymous page를 여러 세대에 걸쳐 분산하는 데 도움이 되며, CPU 사용량이 조금 늘어나는 대가로 상당한 개선을 가져온다.

MGLRU는 reclaim을 얼마나 수행할지 제어하기 어렵게 만든다. 목표 watermark에 도달한 뒤에도 page reclaim을 계속하기 때문이다. 무엇보다도 이는 reclaim이 맞춰야 하는 시간 예산을 깨뜨린다. HONOR는 MGLRU에 이제 그만둘 때임을 알리는 hook을 추가해 이 문제를 해결했다.

direct reclaim 중인 프로세스 throttling은 태스크를 잠재워 kswapd 커널 스레드가 더 많은 메모리를 해제하기를 기다리게 할 수 있다. 이로 인해 스레드가 너무 오래 stall되고 있다. 문제는 kswapd가 reclaim 가능한 메모리를 거의 내놓지 못할 control group을 스캔하느라 많은 시간을 낭비하는 데 있는 듯하다. 그는 이 문제에 대한 실질적인 해법은 없다고 했다.

foreground 앱의 file-backed page가 자주 reclaim되어, 다시 fault로 들여와야 하면서 latency가 증가할 수 있다. 그는 reclaim 중 foreground 앱을 건너뛰는 hook을 추가해 이를 해결했다. readahead 코드가 가져온 page를 자동으로 활성화하는 문제도 있다. 이로 인해 실제 앱이 필요로 하는 page를 희생하면서 결코 사용되지 않을 page가 활성화될 수 있다.

마무리로 Wang은 MGLRU가 어떤 형태의 일반 인터페이스를 제공하기를 바란다고 말했다. 그것이 현재의 벤더별 해킹보다 낫다는 것이다. 그는 aging을 제어하는 파라미터들이 노출되어야 한다고 말했다. 현재 debugfs에 있는 몇몇 knob은 아마도 sysfs로 옮겨 production system에서 사용할 수 있게 해야 할 것이다. 그리고 MGLRU에는 시스템에서 실행 중인 태스크들의 priority를 더 잘 인식하는 능력이 필요하다고 말했다.[^p14n4]

세션은 토론 없이 끝났다.

Wang은 이 세션의 [슬라이드](https://docs.google.com/presentation/d/1hUogz6InyLn13c8CjHuvEIzE4rT7saVRUV6xpWZoNfQ/edit?slide=id.g3ddb7916804_2_27#slide=id.g3ddb7916804_2_27)를 게시했다.

[댓글(게시된 것 없음)](https://lwn.net/Articles/1072866/#Comments)

[^p14n1]: MGLRU의 bloom filter와 lazy promotion은 reclaim 경로에서 모든 page를 같은 비용으로 다시 평가하지 않도록 해 준다. 이는 큰 메모리 시스템에서 스캔 비용과 락 경합을 낮추지만, hot/cold 판단이 틀리면 page cache 회귀처럼 특정 워크로드에 불리하게 작용할 수 있다.
[^p14n2]: page cache 보호가 약하면 파일 기반 워크로드는 anonymous memory가 압박을 만드는 상황에서 필요한 캐시를 잃고 refault를 반복할 수 있다. 실무적으로는 database, build workload, 앱 launch처럼 file-backed working set에 민감한 경우 MGLRU 전환 전후의 refault 및 latency 지표를 함께 봐야 한다.
[^p14n3]: Android 같은 latency-sensitive 시스템에서는 reclaim의 총 처리량보다 tail latency가 더 중요할 수 있다. direct reclaim이나 kswapd 스캔이 몇 ms만 길어져도 UI frame deadline을 놓칠 수 있으므로, reclaim 중단 조건과 foreground 보호 정책이 성능의 핵심이 된다.
[^p14n4]: debugfs knob을 sysfs 같은 production interface로 옮긴다는 것은 단순한 위치 변경이 아니라 ABI 안정성 약속에 가까워진다는 뜻이다. 따라서 aging 파라미터와 우선순위 인식 hook은 벤더 튜닝을 가능하게 하면서도 장기 유지보수 가능한 의미론을 가져야 한다.

---

### [더 빠른 this_cpu 연산을 찾아서](https://lwn.net/Articles/1073395/)

#### 요약

- 커널의 `this_cpu` 연산은 per-CPU 변수 접근을 빠르게 하기 위한 것이지만, x86이 아닌 일부 아키텍처에서는 여러 명령어와 선점 비활성화가 필요해 비용이 커진다.
- Yang Shi는 per-CPU 페이지 테이블을 사용해 모든 CPU에서 특정 per-CPU 변수가 같은 주소를 갖게 하는 방식을 제안했다.
- 이 방식은 선점 비활성화 필요성을 줄일 수 있지만, `per_cpu_ptr()` 호환성, TLB 관리, 주소 공간 사용량 같은 쟁점이 있다.
- 160코어 Arm 시스템의 벤치마크에서는 커널 빌드 시스템 시간이 13–18% 줄고 전체 경과 시간도 3–7% 감소했다.
- 참석자들은 속도 향상의 원인 분석과 restartable sequences 같은 대안 가능성도 논의했다.

글쓴이

Jonathan Corbet

2026년 5월 19일

LSFMM+BPF

커널의

this_cpu 연산(this_cpu operations)

은 per-CPU 변수에 대한 접근을 빠르게 하기 위한 것이다. 다만 일부 CPU에서는 다른 CPU보다 더 최적화되어 있다. 2026년

Linux Storage, Filesystem, Memory Management, and BPF Summit

의 메모리 관리 트랙 세션에서 Yang Shi는 더 넓은 범위의 아키텍처에서 더 나은 성능을 제공하기 위해, 이 연산들이 동작하는 방식을 근본적으로—그리고 다소 논쟁적으로—바꾸는 방안을 제안했다.

[![[Yang Shi]](https://static.lwn.net/images/conf/2026/lsfmm/YangShi-sm.png)](https://lwn.net/Articles/1073398/) per-CPU 변수는 CPU 번호로 인덱싱되는 배열 형태로 구성되며, 각 CPU의 데이터는 별도의 캐시 라인에 배치된다. 이를 통해 CPU들은 락 오버헤드나 다른 CPU와의 경합 없이 자신만의 사유 데이터에 접근할 수 있다. x86 아키텍처(x86)에서는 관련 명령어 앞에 세그먼트 레지스터 접두어를 붙이는 방식으로 per-CPU 접근이 구현되어, 원자적으로 실행되는 단일 명령어 연산이 만들어진다. Arm을 포함한 다른 아키텍처에는 세그먼트 레지스터가 없기 때문에 구현이 더 복잡하다. 특히 주소 계산과 그 주소 뒤에 있는 데이터 접근을 별도로 수행해야 하므로, per-CPU 접근은 여러 명령어로 이루어진 시퀀스가 된다.

이는 중대한 차이다. 여러 명령어로 된 시퀀스가 중간에 선점되면, 새로 실행되는 스레드가 같은 변수에 접근할 수 있고, 그 결과 온갖 달갑지 않은 동작이 발생할 수 있다. 스레드가 다른 CPU로 마이그레이션되면 cross-CPU 접근이 일어날 수 있는데, 이 역시 바람직하지 않다. 이러한 시나리오를 막기 위해 영향을 받는 아키텍처에서는 this_cpu 연산이 선점을 비활성화해야 하며, 이는 성능을 떨어뜨린다.[^p15n1]

Shi의 제안은 per-CPU 페이지 테이블을 사용하여, 어떤 특정 per-CPU 변수든 모든 CPU에서 같은 주소를 갖도록 per-CPU 변수를 다시 구현하는 것이다. 그렇게 하면 인덱스 계산이 사라지고 선점도 더 이상 문제가 되지 않는다. 이 방안의 유일한 문제는 모든 CPU에 걸쳐 데이터를 초기화하는 데 사용되는 `per_cpu_ptr()` 매크로가 깨진다는 점이다. 이 문제를 해결하기 위해 per-CPU 변수는 두 번 매핑된다. 기존 전역 매핑은 유지되어 초기화에 사용되고, 두 번째 매핑은 각 CPU에 특화된다.[^p15n2]

Jason Gunthorpe는 과거에 Linus Torvalds가 per-CPU 페이지 테이블을 이런 방식으로 사용하는 것에 강하게 반대해 왔다고 지적했다. Gunthorpe는 그의 우려가 해소되지 않는다면 이 작업은 멀리 가지 못할 것이라고 말했다. 그 반대는 해당 주소들과 연관된 변환 색인 버퍼(TLB) 항목을 올바르게 관리하기 어렵다는 점에 근거한 것으로 보인다. 최근 아키텍처 개정에서 그 상황이 개선되었는지를 두고 약간의 논의가 있었다. 또한 이 방식이 어떤 상황에서는 선점을 비활성화할 필요를 없애겠지만, 둘 이상의 명령어가 관련되는 어떤 종류의 갱신이든 여전히 선점을 비활성화한 상태에서 실행해야 한다는 점도 지적되었다.

Shi는 계속해서, 새 구현에는 더 높은 주소 공간 사용량이라는 비용이 있긴 하지만 그 비용은 작아 보인다고 말했다. per-CPU 페이지 테이블은 물리 메모리를 차지해야 한다. 그는 160코어 머신에서 그 비용이 약 2MB라고 말했다. per-CPU 변수의 할당과 해제에는 몇 가지 추가 페이지 테이블 연산이 필요하다. 전용 가상 주소 공간 범위를 할당해야 할 필요도 있을 수 있는데, 이는 32비트 머신에서 문제가 될 수 있다.[^p15n3]

성능 벤치마크는 160코어 Arm 시스템에서 수행되었다. 핵심 커널 빌드 벤치마크는 시스템 시간이 13–18% 감소했으며, 벽시계 기준 시간(wall-clock time)도 3–7% 적게 걸렸다. [stress-ng 벤치마크](https://wiki.ubuntu.com/Kernel/Reference/stress-ng)에서도 상당한 개선이 나타났다. Brendan Jackman은 그 수치가 이렇게 큰 데 놀라움을 표했다. 선점 비활성화를 피하는 것만으로는 그 차이를 설명하기에 충분해 보이지 않는다는 것이다. 그는 속도 향상의 원인에 대해 더 조사할 필요가 있다고 말했다.

시간이 다 되어 갈 무렵 Ryan Roberts는 Peter Zijlstra의 [커널 내부 restartable-sequences 작업](https://lwn.net/ml/all/20260223163843.GR1282955@noisy.programming.kicks-ass.net/)이 이 문제의 대안적 해결책이 될 수 있을지 물었다. Shi는 그 작업에 대해 충분히 알지 못해 답할 수 없다고 했다. Shi는 per-CPU 페이지 테이블이 앞으로 NUMA 노드 전반에 걸친 커널 텍스트 복제에도 사용되어, 시스템 전체에서 로컬 접근을 제공할 수 있을 것이라고 말했다. Jackman은 그것이 자신이 제안한 "mermap"(회의 앞부분에서 [논의된](https://lwn.net/Articles/1072367/) 바 있음)도 더 잘 동작하게 만들 수 있다고 말했다.

[댓글(3개 게시됨)](https://lwn.net/Articles/1073395/#Comments)

[^p15n1]: per-CPU 연산(per-CPU operations)이 여러 명령어로 분해되는 아키텍처에서는, 주소 계산 후 실제 접근 전에 CPU가 바뀌거나 다른 스레드가 끼어드는 순간 현재 CPU용 데이터라는 가정이 깨질 수 있다. 그래서 선점 비활성화가 정확성을 위한 방어막이 되지만, 빈번한 경로에서는 지연 시간과 스케줄링 유연성 비용을 만든다.

[^p15n2]: 모든 CPU에서 같은 가상 주소를 사용하도록 만들면 코드 생성과 접근 경로는 단순해질 수 있지만, CPU별로 다른 물리 페이지를 가리키도록 페이지 테이블을 유지해야 한다. 따라서 per-CPU 데이터 모델이 배열 인덱싱 문제에서 주소 변환 관리 문제로 일부 이동한다.

[^p15n3]: 64비트 시스템에서는 추가 가상 주소 공간 사용이 대체로 감당 가능하지만, 32비트 커널에서는 주소 공간 자체가 제한 자원이므로 전용 매핑 영역 확보가 실제 설계 제약이 될 수 있다.

---

### [제10회 OpenPGP 이메일 서밋](https://lwn.net/Articles/1072870/)

#### 요약

- 제10회 OpenPGP 이메일 서밋은 암호화 이메일 생태계의 프로젝트·서비스 제공자들이 모여 거버넌스, 키 형식, PQC(post-quantum cryptography) 전환을 논의한 자리였다.
- OpenPGP.org 도메인은 Phil Zimmermann 개인 소유에서 커뮤니티 중심 구조로 이전하는 방안이 검토되고 있으며, keys.openpgp.org(KOO) 이사회와 Wau Holland Foundation이 후보로 거론되었다.
- OpenPGP용 PQC 지원 IETF 초안은 최종 승인 단계에 있으며, Proton, Delta Chat, Thunderbird/RNP, Hockeypuck 등 여러 구현체가 배포 또는 통합을 준비하고 있다.
- v6 키 형식은 SHA2-256 지문을 사용하지만, 생태계 전환에는 시간이 걸리므로 기존 v4 키에도 ML-KEM-768+X25519 복합 하위키를 추가해 PQC 암호화를 지원할 수 있게 했다.
- FreePG(freepg.org)는 GnuPG 사용자가 OpenPGP IETF 표준에 더 가깝게 머물 수 있도록 하는 임시 가교 역할을 목표로 한다.

2026년 5월 20일

이 글은 Heiko Schäfer, Andrew Gallagher, David Runge가 기고했다.

[OpenPGP](https://www.openpgp.org/) 이메일 서밋은 암호화 이메일과 관련 주제를 다루는 이들이 매년 모이는 행사다. 이 회의의 [열 번째 행사](https://www.openpgp.org/community/email-summit/2026/)는 2026년 3월에 열렸고, 이제 [회의록](https://www.openpgp.org/community/email-summit/2026/minutes/)이 공개되었다. 늘 그렇듯 폭넓은 주제가 논의되었다. 주요 내용에는 올해 안에 여러 주체가 배포를 계획하고 있는 포스트 양자 암호(PQC, post-quantum cryptography) 지원, OpenPGP 서명 이메일을 기본값으로 삼는 계획과 함께 이메일 서명을 보편화하기 위한 유망한 새 접근법, OpenPGP에 신뢰할 수 있는 삭제(또는 "forward secrecy") 기능을 가져오는 새 초안, 그리고 OpenPGP.org 도메인의 소유권 이전 계획 등이 포함되었다.[^p16n1]

서밋 참석자들은 이 분야의 많은 프로젝트, 서비스 제공자, 기타 이해관계자를 대표했으며, 여기에는 [Delta Chat](https://delta.chat/), [FreePG](https://freepg.org/)(freepg.org), [Hagrid](https://gitlab.com/keys.openpgp.org/hagrid/), [Hockeypuck](https://github.com/hockeypuck/hockeypuck/#hockeypuck), [keys.openpgp.org (KOO)](https://gitlab.com/keys.openpgp.org/infrastructure#keysopenpgporg-infrastructure), [Proton](https://proton.me/), [Ripasso](https://github.com/cortex/ripasso#ripasso), [RNP](https://www.rnpgp.org/), [Sequoia-PGP](https://sequoia-pgp.org/), [Signstar](https://signstar.archlinux.page), [Thunderbird](https://thunderbird.net), [VOA](https://voa.archlinux.page) 등이 포함되었다.

#### 거버넌스와 openpgp.org 도메인

[Phil Zimmermann](https://en.wikipedia.org/wiki/Phil_Zimmermann)은 현재 [OpenPGP.org](https://openpgp.org) 도메인의 소유자다. 그는 서밋에 참석하지 않았지만, 이 디지털 자산을 커뮤니티에 넘기고 싶다는 뜻을 전했다. 커뮤니티는 어떤 개인도 개인적 책임을 떠안지 않아도 되는 구성을 찾는 쪽을 [선호한다](https://www.openpgp.org/community/email-summit/2026/minutes/#openpgporg-governance). [keys.openpgp.org (KOO) 이사회](https://gitlab.com/keys.openpgp.org/governance/#keysopenpgporg-governance)는 도메인을 인수할 수 있는 기존 거버넌스 기구 중 하나다. 현재 그 권한은 keys.openpgp.org 키 서버 운영에 좁게 초점을 맞추고 있다.

KOO 이사회는 [Wau Holland Foundation](https://en.wikipedia.org/wiki/Wau_Holland_Foundation)을 수탁자로 삼아 도메인에 대한 책임을 맡는 방안을 검토하고 있다. 이 재단은 [Chaos Computer Club](https://www.ccc.de/en/)(CCC)과 느슨하게 연결되어 있으며, 지난 10년 동안 OpenPGP 이메일 서밋의 후원자였다. 재단 구성원들은 OpenPGP 생태계의 확산에 깊이 관여하고 있다. 다음 단계로 KOO 이사회는 투표권자들에게 [정관 변경](https://gitlab.com/keys.openpgp.org/governance/-/merge_requests/54)을 제안했다.

#### OpenPGP의 PQC

PQC는 이번 서밋에서 [논의된 주제](https://www.openpgp.org/community/email-summit/2026/minutes/#pqc-migration) 중 하나였다. 업계 전반에서 사람들은 양자 컴퓨터가 언젠가 현재의 암호 알고리즘들을 깰 수 있게 될 가능성에 대비하고 있다. 그런 상황에서는 공격자가 충분히 강력한 양자 컴퓨터를 사용할 수 있게 된 뒤 나중에 복호화하려고, 오늘의 암호화된 메시지까지 수집할 수 있다. PQC 알고리즘은 앞으로 등장할 가능성이 있는 양자 컴퓨터로도 깨뜨릴 수 없도록 설계된다. [OpenPGP의 PQC 지원을 명시하는 IETF 초안](https://datatracker.ietf.org/doc/draft-ietf-openpgp-pqc)은 마지막 검토(last call)를 마쳤으며 저자들의 최종 승인을 기다리고 있다. RFC로서의 공식 비준은 앞으로 몇 달 안에 예상된다. 형식 자체는 약 1년 동안 안정된 상태였다.[^p16n2]

이 초안은 [암호화를 위한 두 가지 복합 알고리즘](https://www.ietf.org/archive/id/draft-ietf-openpgp-pqc-17.html#name-composite-encryption-scheme), [디지털 서명을 위한 두 가지 복합 알고리즘](https://www.ietf.org/archive/id/draft-ietf-openpgp-pqc-17.html#name-composite-signature-schemes-), 그리고 [디지털 서명용 PQC 전용 알고리즘 세 가지](https://www.ietf.org/archive/id/draft-ietf-openpgp-pqc-17.html#name-the-slh-dsa-algorithms)를 규정한다. 일곱 알고리즘은 모두 새 OpenPGP 키 형식([RFC 9580](https://www.rfc-editor.org/rfc/rfc9580.html)에 명시됨), 즉 흔히 "v6"라 부르는 형식에서 사용할 수 있다. 또한 복합 암호화 알고리즘 중 하나는 현재 널리 쓰이는 v4 키와 함께 사용하도록 지정되어 있다(자세한 내용은 아래 참조).

OpenPGP 암호화 메일 서비스를 제공하는 회사인 Proton은 서밋 당시 이미 자사 이메일 서비스용 PQC 지원의 완전한 구현을 갖추고 있었다. 이후 일반 공개가 [발표되었다](https://proton.me/blog/introducing-post-quantum-encryption). Proton의 PQC 구현 핵심 부분은 Proton이 사용하고 유지보수하는 두 OpenPGP 라이브러리, [GopenPGP](https://github.com/ProtonMail/gopenpgp#gopenpgp-v3)와 [OpenPGP.js](https://github.com/openpgpjs/openpgpjs/#openpgpjs-)의 기능 브랜치에서 자유 소프트웨어로 제공된다.

Delta Chat 보안 메시징 프로젝트는 PQC 지원을 위한 모든 구성 요소를 갖추고 있으며, 올해 말 프로덕션에 배포할 계획이다. Thunderbird는 v4 PQC 암호화 메시지를 보내고 받는 실험적 지원을 갖고 있다. 다만 이 기능을 안정 릴리스에서 제공하려면 아직 시간이 더 걸릴 것이다. Thunderbird는 [RNP OpenPGP 라이브러리](https://github.com/rnpgp/rnp/#rnp)를 사용한다. 이 라이브러리의 유지보수자들은 [독일 연방 정보보안청](https://www.bsi.bund.de/EN/Home/home_node.html)(BSI)의 자금 지원을 받은 [프로젝트의 일부](https://pkic.org/events/2023/pqc-conference-amsterdam-nl/pkic-pqcc_stephan-ehlen_bsi_post-quantum-policy-and-roadmap-of-the-bsi.pdf)로 개발된 [상당한 규모의 PQC 풀 리퀘스트를 통합](https://github.com/rnpgp/rnp/pull/2355)하는 작업을 하고 있다. Hockeypuck 키 서버도 [최신 베타 릴리스](https://infosec.exchange/@pgpkeys/116524105050914478)에서 복합 PQC 키 지원을 추가했다.

#### v4 키를 위한 PQC 암호화

v6 형식은 이전 형식("v4"라 불리며 [RFC 4880](https://www.rfc-editor.org/rfc/rfc4880.html)에 명시됨)을 대체한다. v6 키 형식 자체의 변화는 중간 정도다. 새 키 버전의 핵심은 v6 키의 지문이 SHA2-256 해시를 사용하는 반면, v4 키는 지문으로 SHA1 해시를 사용한다는 점이다. SHA1 해시 알고리즘에 대한 공격은 [충분히 심각해져](https://en.wikipedia.org/wiki/SHA-1#Attacks), v4 키에서 벗어나는 것이 신중한 장기 전략으로 보인다.[^p16n3]

하지만 생태계를 새 키 버전으로 전환하는 일은 장기 프로젝트다. 가능한 포스트 양자 공격으로부터 통신을 보호해야 할 긴급성이 커질수록, 사용자가 기존 v4 키를 매끄럽게 업그레이드해 PQC 암호화를 활성화할 수 있도록 하는 일이 더 중요한 문제가 된다. 이러한 필요를 충족하기 위해 PQC 초안은 ML-KEM-768+X25519 복합 알고리즘을 v4 하위키로 사용할 수 있도록 명시적으로 지정한다. 사용자는 상대방이 아직 초기 단계인 v6 키 형식을 지원하지 않아도, 이 알고리즘을 사용하는 포스트 양자 암호화 하위키를 기존 v4 키에 추가할 수 있다.[^p16n4]

Thunderbird는 해당 형식을 지원하는 RNP 릴리스를 전제로, 올해 말까지 추가 ML-KEM-768+X25519 암호화 하위키가 있는 v4 키에 대한 PQC 지원을 배포할 계획이다. v4와 v6 형식 모두에서 PQC를 사용할 수 있으면, 서로 다른 프로젝트의 필요와 우선순위에 따라 PQC 지원을 더 유연하게 배포할 수 있다. 현재 진행 중인 두 OpenPGP 현대화 노력, 즉 v6 키 지원과 PQC 지원은 따로 추진할 수도 있고 결합해서 추진할 수도 있다.

많은 라이브러리가 전체 형식 범위를 지원하므로, 프로젝트들이 서로 다른 일정으로 지원을 업그레이드하더라도 대체로 공통분모가 있을 것이다.

#### FreePG(freepg.org)와 PQC

[FreePG](https://freepg.org/)는 [GnuPG](https://www.gnupg.org/)의 패치된 버전으로, 더 큰 Linux 배포판들 중 다수가 부분적으로 또는 전면적으로 사용하고 있다. FreePG의 주요 목표는 OpenPGP IETF 표준을 준수하여, GnuPG 사용자가 업스트림의 점점 커지는 [OpenPGP 표준과의 괴리](https://lwn.net/Articles/953797/)에서 벗어날 수 있게 하는 것이다. 그러나 FreePG는 장기 포크가 아니라 임시 가교로 설계되어 있다.

[^p16n1]: 서명을 기본값으로 만들면 메시지 위·변조 탐지가 쉬워지지만, 서명의 보편화는 메타데이터 노출이나 키 관리 실패 같은 운영상의 위험도 함께 고려해야 한다.
[^p16n2]: "수집 후 나중에 복호화" 공격은 장기 기밀성이 필요한 이메일에 특히 중요하다. PQC 전환은 현재 전송되는 암호문이 미래의 양자 컴퓨터에 노출될 가능성을 줄이기 위한 선제 조치다.
[^p16n3]: SHA1 지문은 충돌 공격의 발전 때문에 장기 식별자로서 신뢰성이 약해졌다. 키 지문은 사용자가 키를 확인하는 근거이므로, 더 강한 해시로 이동하는 것은 단순한 형식 변경 이상의 보안 의미가 있다.
[^p16n4]: ML-KEM-768+X25519 같은 복합 방식은 기존 타원곡선 보안과 PQC 보안을 결합해, 한쪽 가정이 깨지더라도 전체 암호화 체계가 즉시 붕괴하지 않도록 위험을 분산한다.

---

### [제10회 OpenPGP 이메일 서밋](https://lwn.net/Articles/1072870/) (계속 2부)

**요약:** 이번 부분은 FreePG의 PQC 지원 한계, 눈에 띄지 않는 서명(unobtrusive signatures), Autocrypt v2 (AC2)의 시간 기반 키 회전과 신뢰 가능한 삭제, 그리고 HKPv2를 통한 현대적 키 서버 API 통합을 다룬다.

유지보수자들은 IETF PQC 초안 지원을 추가하는 일이 간단하지 않으며, 단기적으로 FreePG에서 이를 지원하기에는 이용 가능한 자원이 너무 제한적일 수 있다고 설명했다. 그룹은 FreePG가 v4 PQC 암호화 하위 키를 사용할 수 없더라도, 최소한 이를 문제없이 무시할 수는 있어야 한다는 데 동의했다. GnuPG 업스트림이 v6 키를 지원하지 않는 한, FreePG가 v6 PQC 키를 포함한 어떤 v6 형식도 지원하는 것은 현실적으로 가능하지 않다.

FreePG와는 별개로, 새로운 포스트 양자 암호화 알고리즘인 [Hamming Quasi-Cyclic](https://pqc-hqc.org/) (HQC)에 대해서도 짧게 논의했다. 관심은 있지만, OpenPGP에서 이 알고리즘의 사용을 규정하기 시작하기에는 아직 너무 이르다는 데에도 합의가 있었다.

#### 눈에 띄지 않는 서명

새 [IETF 초안](https://datatracker.ietf.org/doc/draft-ietf-mailmaint-unobtrusive-signatures/)에서 설명하는 눈에 띄지 않는 서명도 올해 [논의](https://www.openpgp.org/community/email-summit/2026/minutes/#unobtrusive-signatures-1)되었다. 이 아이디어는 [이전 제9회 이메일 서밋에서 처음 브레인스토밍되었다](https://www.openpgp.org/community/email-summit/2025/minutes/#cleartext-non-disturbing-signatures-in-headers-dkg). 기존 이메일 서명 방식(`multipart/signed` 구조를 사용)은 모든 이메일 소프트웨어에서 매끄럽게 처리되지 않는다. 그 결과 많은 사용자가 수신자에게 무해하지만 혼란스러운 오류가 표시되는 일을 피하려고 서명 생성을 꺼 둔다.[^p17n1]

눈에 띄지 않는 서명의 목표는, 서명을 지원하지 않는 클라이언트를 쓰는 수신자가 사용자에게 불만을 제기할 위험 없이, 발신 소프트웨어가 자신 있게 기본 서명을 활성화할 수 있게 하는 것이다. 눈에 띄지 않는 서명은 이를 지원하지 않는 소프트웨어에서 조용히 무시되므로 이런 기본값을 가능하게 한다. 이전에는 OpenPGP 서명이 일부 이메일 수신자를 혼란스럽게 하거나 심지어 걱정하게 만들어, 수신자가 발신자에게 불만을 제기하곤 했다. 따라서 이메일 소프트웨어 개발자는 서명 지원이 없는 수신자에게서 불만이 발생할 수 있다는 이유로 기본 서명 활성화를 꺼리는 경우가 있었다.

새 접근법은 OpenPGP 서명을 첨부 파일이 아니라 헤더로 포함한 `multipart/mixed` 래퍼를 사용한다. 이 구성은 눈에 띄지 않는 서명이 주된 목표, 즉 수신자를 혼란스럽게 하는 방식으로 절대 표시되지 않도록 하는 목표를 달성할 수 있게 한다. 서명을 이해하지 못하는 레거시 클라이언트도 서명에 관한 어떤 내용도 표시하지 않은 채 이메일의 나머지 부분을 정상적으로 렌더링한다. 반면 눈에 띄지 않는 서명을 지원하는 클라이언트는 서명을 검증하고 사용자에게 성공을 알릴 수 있다.

서밋 당시 이 방식의 구현은 Thunderbird의 [개발 버전](https://thunderbird.topicbox.com/groups/planning/Tfd5f9c444ef3d06c-M6cac45a5459adb7e58a7ac79)에서 사용할 수 있었고, 이미 실제 환경의 사용자들에게서 몇 차례 성공적인 테스트를 거쳤다. 개발을 추적하고 최신 기능을 포함하는 메일 클라이언트의 롤링 릴리스인 [Thunderbird Daily](https://support.mozilla.org/en-US/kb/thunderbird-daily)는 이미 눈에 띄지 않는 서명을 생성하고 소비할 수 있지만, 현재는 사용자가 숨겨진 환경설정을 활성화해야 한다. Thunderbird의 Kai Engert는 눈에 띄지 않는 서명의 생성이 올해 말 기본값이 되기 시작할 것으로 예상한다. Proton도 곧 수신되는 눈에 띄지 않는 서명에 대한 지원을 구현할 계획이다.

Proton의 Bart Butler는 Thunderbird와 Proton이 모두 눈에 띄지 않는 서명을 지원하게 되면 다른 클라이언트도 참여시키는 일이 간단해질 것이며, 이 노력이 서명된 이메일에 대한 투자 대비 효과가 가장 큰 개선 중 하나가 될 것이라고 보았다.

#### Autocrypt v2 (AC2): PQC와 신뢰 가능한 삭제의 결합

Delta Chat의 Holger Krekel은 Delta Chat 프로젝트 구성원들이 부분적으로 추진한 [명세](https://datatracker.ietf.org/doc/draft-autocrypt-openpgp-v2-cert/)인 [Autocrypt v2](https://autocrypt2.org) (AC2)를 발표했다([논의 회의록](https://www.openpgp.org/community/email-summit/2026/minutes/#autocrypt-v2)). AC2는 [Autocrypt v1](https://docs.autocrypt.org/level1.html)과는 별도의 관심사를 다룬다. v1이 이메일 피어 간 OpenPGP 키의 교환과 갱신을 처리하는 반면, AC2는 핵심적으로 시계 기반 키 자료 회전 방식을 도입한다. 이는 신원과 키 자료 사이의 결합 자체를 다루지는 않는다.

AC2 초안의 서문은 목표를 다음과 같이 요약한다.

> It offers defense against store-now-decrypt-later attacks from quantum computers through post-quantum hybrid cryptography. It also enables reliable deletion ("Forward Secrecy") of received messages even when adversaries capture encrypted messages in transit and later compromise the user's message archive and secret keys.

즉, 채팅의 모든 참여자가 복호화된 메시지 평문을 보관하지 않고, 이 방식이 규정하듯 오래된 개인 키 자료를 정기적으로 파기한다면, 시간이 지나면서 과거의 평문은 통신 상대나 공격자 어느 쪽도 근본적으로 복구할 수 없게 된다. Autocrypt v2는 이 시계 기반 키 회전 방식을 PQC 암호화와 결합한다.[^p17n2]

키 회전 방식은 영구적인 대체 키와 수명이 짧은 암호화 하위 키(예를 들어 10일 동안 유효)를 결합한다. 통신은 일반적으로 수명이 짧은 키에만 의존하지만, 예외적 상황(예를 들어 두 피어가 더 오랫동안 통신하지 않은 경우)에서는 장기 암호화 키로 폴백할 수 있다. 발신자는 새 하위 키를 정기적으로 배포한다. 수신자는 피어의 암호화 하위 키를 로컬에서 병합하면서, 만료된 오래된 하위 키를 제거한다.

이 방식에 내재한 절충에 대한 논의도 있었다. 신뢰 가능한 삭제는 오래된 메시지를 더 이상 누구도 읽을 수 없다는 뜻이다. 이 속성은 메시지가 흔히 무기한 저장되고(예: IMAP 서버에), 사용자가 장래에도 이를 복호화해 읽을 수 있으리라고 기대하는 전형적인 이메일의 기대와 충돌한다. 반대로 클라이언트가 자신의 복호화 하위 키를 삭제했지만 암호문이 서버에 남아 있다면, 사용자는 오래된 메일에 접근할 수 없게 된다. 가능한 완화책—메시지를 장기 키로 다시 암호화하거나, 세션 키를 별도로 저장하는 것—은 전방 보안 보장의 일부를 포기하는 대가를 치른다.[^p17n3]

결론은 나지 않았지만, 서로 다른 사용 사례가 존재하며 전방 보안이 모든 경우에 잘 맞는 것은 아니라는 점은 분명하다. AC2 프레임워크는 서로 다른 절충점 중 무엇을 선택하느냐에 따라 다양한 결과를 실현하는 데 적용할 수 있다.

제기되었지만 해결되지 않은 또 다른 질문은 Autocrypt v2 인증서를 명시적으로 그렇게 표시해야 하는지였다. 예를 들어 키 서버가 만료된 암호화 하위 키를 무기한 누적하기보다 가지치기하도록 유도하는 힌트로는 도움이 될 수 있다.

#### HKPv2: 현대화된 범용 키 서버 API

OpenPGP 생태계에는 현재 인증서 배포를 위한 다소 임시적인 기술이 세 가지 있다. Hockeypuck 서버는 "Legacy HTTP Keyserver Protocol"(HKPv1)을 구현한다. [keys.openpgp.org](https://keys.openpgp.org/)의 [Hagrid](https://gitlab.com/keys.openpgp.org/hagrid/#hagrid) 서버는 맞춤형 [Verifying Key Server](https://keys.openpgp.org/about/api/) (VKS) API를 사용하지만, HKPv1의 하위 집합도 구현한다. [Web Key Directory](https://datatracker.ietf.org/doc/draft-koch-openpgp-webkey-service/) (WKD)라는 세 번째 방식은 이메일 주소로 조회할 수 있도록 OpenPGP 키 자료를 정적으로 제공한다.

[HKPv2](https://datatracker.ietf.org/doc/draft-gallagher-openpgp-hkp/)는 [이번 서밋에서 논의](https://www.openpgp.org/community/email-summit/2026/minutes/#hkpv2)된 제안으로, 이 세 가지 키 배포 시스템의 모든 사용 사례를 하나의 통합 API로 포괄하는 것을 목표로 한다. 이는 검증형 및 비검증형 키 서버 사용 사례를 모두 다루고, (WKD와 유사하지만 서버에 특수 소프트웨어를 요구하지 않고) 단순한 정적 파일 집합에서 직접 인증서를 제공하는 경우도 지원하도록 설계되었다. 이 초안은 비교적 안정된 상태에 도달했으며, 생태계가 고전적인 v4 키에서 v6 및/또는 PQC 키로 이동하는 과정을 촉진하도록 특별히 설계되었다.[^p17n4]

2025년 keys.openpgp.org 이사회는 HKPv2 초안을 논의하고 작업했으며, keys.openpgp.org가 이 프로토콜 지원을 구현하겠다는 결정을 내렸다(제한된 개발 자원이 허용하는 즉시).

[^p17n1]: 서명이 사용자에게 보이는 오류나 이상한 첨부 파일로 나타나면, 암호학적으로는 유용해도 사용자는 이를 고장이나 피싱 징후로 오해할 수 있다. 눈에 띄지 않는 서명은 호환성 문제를 줄여 기본 서명 채택 가능성을 높인다.
[^p17n2]: PQC를 결합하는 목적은 오늘 수집한 암호문을 미래의 양자 컴퓨터로 해독하는 "store-now-decrypt-later" 위협을 줄이는 것이다. 다만 표준화와 구현 성숙도가 보안의 핵심 변수로 남는다.
[^p17n3]: 신뢰 가능한 삭제와 장기 보관은 서로 긴장 관계에 있다. 전방 보안을 강하게 적용하면 과거 메일 복구 능력이 줄고, 복구성을 높이면 키 유출 시 과거 메일 노출 위험이 커질 수 있다.
[^p17n4]: HKPv2 같은 통합 키 배포 API는 key migration 과정에서 클라이언트와 서버의 상호운용성을 높일 수 있지만, 키 검증 정책과 개인정보 노출 범위는 별도로 신중히 설계해야 한다.

---

### [제10회 OpenPGP 이메일 서밋](https://lwn.net/Articles/1072870/) (계속 3부)

요약: OpenPGP 생태계는 HKPv2, 키 마이그레이션(Key migration), v6/PQC 키 전환을 중심으로 상호운용성과 보안 자동화를 진전시키고 있다.

Hockeypuck 키 서버 소프트웨어는 이후 이 API에 대한 예비 지원을 추가했다. 2025년 keys.openpgp.org 이사회도 이 프로젝트가 API를 구현하기로 결정했지만, 아직 이 작업에 대한 명확한 일정은 없다. HKPv2 초안은 현재 IETF OpenPGP 워킹그룹의 채택을 기다리고 있다.

#### 키 마이그레이션(Key migration)과 키 교체 초안

요약: v4 키에서 v6 및/또는 PQC 키로의 전환을 사용자가 직접 검증해야 했던 기존 방식에서, 소프트웨어가 암호학적으로 검증된 선언을 바탕으로 자동 처리하는 방식으로 옮기려는 논의가 진행 중이다.[^p18n1]

OpenPGP v4 키에서 v6 키 및/또는 PQC 키로 업그레이드하는 문제는 [간단히 논의되었다](https://www.openpgp.org/community/email-summit/2026/minutes/#key-migration). 가까운 미래에는 많은 OpenPGP 사용자가 현재의 v4 키에서 새로운 v6 및/또는 PQC 키로 업그레이드하는 것을 고려하게 될 것이다. 역사적으로 OpenPGP에서 이러한 키 마이그레이션은 대체로 수동 절차였다. 키 보유자는 새 키를 만들고, 그 키들이 서로 연결되어 있음을 표시하기 위해 자신의 인증서들 사이에 여러 인증을 발행했다. 그들과 통신하는 상대방은 새 인증서가 신뢰하던 이전 인증서와 안정적으로 연결되어 있는지 수동으로 판단한 뒤, 자신의 OpenPGP 소프트웨어에서 새 인증서를 받아들여야 했다.

[키 교체 초안](https://datatracker.ietf.org/doc/draft-ietf-openpgp-replacementkey/)은 키 전환을 정형화하고, 소프트웨어가 사용자 대신(키 보유자와 그 통신 상대 모두에 대해) 이를 투명하게 처리할 수 있게 하는 메커니즘을 정의한다.

애플리케이션에서 충분히 지원된다면, 이 메커니즘은 키 전환을 거의 매끄럽게 만들 것이다. 동시에 키 보유자가 제공하는 암호학적 선언으로 엄격하게 보호된다. 이 초안은 OpenPGP 워킹그룹에 채택되었고, 수개월 동안 문구 측면에서는 대체로 안정된 상태였지만, "last call"에 들어가기 전 구현을 아직 기다리고 있다.

#### 전망

요약: Thunderbird, Proton, Delta Chat, Hockeypuck, keys.openpgp.org가 각자의 제품과 인프라에 서명, PQC, HKPv2 관련 기능을 도입할 계획을 밝혔다.

이번 서밋에서는 여러 구체적인 다음 단계가 발표되었다. Thunderbird와 Proton은 각자의 소프트웨어의 향후 릴리스에서 눈에 잘 띄지 않는 서명(unobtrusive signatures)을 제공할 계획을 발표했다. Thunderbird는 또한 향후 stable 릴리스에 완전한 v4 PQC 지원을 추가할 계획이다. Proton은 성공적인 내부 테스트 뒤 모든 사용자에게 v6 PQC 지원을 배포하려는 의사를 확인했다. Delta Chat은 2026년에 Autocrypt v2를 통해 v6 PQC와 "신뢰할 수 있는 삭제(reliable deletion)"를 사용자에게 배포할 계획이다. Hockeypuck 키 서버 소프트웨어의 HKPv2 지원은 PQC 키 지원과 함께 올해 마무리되어 관련 키 서버에 배포될 예정이다. keys.openpgp.org가 Hagrid 키 서버에 HKPv2 지원을 추가할 의향이라는 점도 확인되었지만, 구현을 위한 명확한 로드맵은 아직 제시되지 않았다.

여러 장기 과제도 활발히 개발되고 있다. 많은 참가자는 올해 서밋이 매우 생산적이었다고 말했다. OpenPGP 생태계는 다양하고 활력이 있어 보이며, 많은 장기 프로젝트가 현재 결실을 맺고 있다. 특히 OpenPGP의 PQC 지원 최종화(독일 BSI가 [2021년에 시작한](https://www.evergabe-online.de/tenderdetails.html?1&id=397181) 작업)와 곧 이어질 다수의 관련 배포는 시의적절해 보인다.[^p18n2]

후속 임시 회의는 2026년 10월 21일로 예정되어 있으며, 다음 대면 서밋은 잠정적으로 2027년 4월 말로 계획되어 있다. 참여에 관심 있는 사람은 [IETF Open Specification for Pretty Good Privacy](https://datatracker.ietf.org/wg/openpgp/about/) 그룹의 [메일링 리스트](https://mailman3.ietf.org/mailman3/lists/openpgp@ietf.org)를 구독할 수 있다. 참여는 누구에게나 열려 있다.

[댓글(11개 게시)](https://lwn.net/Articles/1072870/#Comments)

**페이지 편집자**: Joe Brockmeier

# 단신

## 커널 개발

### [커널 릴리스 상태(Kernel release status)](https://lwn.net/Articles/1073752/)

요약: 현재 개발 커널은 7.1-rc4이며, Linus Torvalds는 AI 기반 버그 보고가 보안 목록을 중복 보고로 압도하고 있어 공개적이고 책임 있는 보고 방식이 필요하다고 지적했다.[^p18n3]

현재 개발 커널은 7.1-rc4이며,

5월 17일에 릴리스되었다. Linus Torvalds는 이렇게 말했다.

> 문서 업데이트 중 일부는 강조할 만할지도 모른다. AI 보고서가 계속 쏟아지면서 보안 목록은 사실상 거의 관리 불가능한 상태가 되었고, 서로 다른 사람들이 같은 도구로 같은 문제를 찾아내면서 엄청난 중복이 생겼다. 사람들은 그저 모든 시간을 들여 내용을 올바른 사람에게 전달하거나, "그건 이미 일주일/한 달 전에 고쳐졌다"고 말하며 공개 논의를 가리키고 있다.
>
> 이는 전적으로 무의미한 소모적 활동이며, 우리는 AI가 감지한 버그는 거의 정의상 비밀이 아니고, 그것을 어떤 비공개 목록에서 다루는 것은 관련된 모든 사람의 시간 낭비라는 점을 분명히 하고 있다. 게다가 보고자들이 서로의 보고서를 볼 수도 없기 때문에 그 중복을 더 악화시킬 뿐이다.

(그는 Willy Tarreau의 패치가 포함된 [이 풀 요청](https://lwn.net/ml/all/87lddksslx.fsf@trenco.lwn.net/)을 언급하고 있다. 이 패치는 [무엇이 보안 버그에 해당하는지](https://lwn.net/ml/all/20260509094755.2838-3-w@1wt.eu/)와 [AI를 사용해 버그를 찾는 책임 있는 방식](https://lwn.net/ml/all/20260509094755.2838-4-w@1wt.eu/)을 정의한다.)

이번 개발 주기에는 2,217명의 개발자로부터 13,963개의 비병합 변경 집합이 들어왔으며, 이 중 417명은 처음으로 커널에 기여한 사람이다. 릴리스 이력은 다음과 같다.

> | RC | Date | Commits |  |
> | --- | --- | --- | --- |
> | **v7.1-rc1** | 2026-04-26 | 13963 | 13963 |
> | **v7.1-rc2** | 2026-05-03 | 475 | 475 |
> | **v7.1-rc3** | 2026-05-10 | 584 | 584 |
> | **v7.1-rc4** | 2026-05-17 | 428 | 428 |

훨씬 더 자세한 내용은 [LWN KSDB 7.1 페이지](https://lwn.net/ksdb/releases/v7.1/)를 참고하라.

**Stable updates**(stable kernels 업데이트)는 또다시 부족하지 않았다. [7.0.7](https://lwn.net/Articles/1072850/), [6.18.30](https://lwn.net/Articles/1072851/), [6.12.88](https://lwn.net/Articles/1072852/)은 5월 14일에, [7.0.8](https://lwn.net/Articles/1073061/), [6.18.31](https://lwn.net/Articles/1073062/), [6.12.89](https://lwn.net/Articles/1073063/), [6.6.139](https://lwn.net/Articles/1073064/), [6.1.173](https://lwn.net/Articles/1073065/), [5.15.207](https://lwn.net/Articles/1073066/), [5.10.256](https://lwn.net/Articles/1073067/)은 5월 15일에, [7.0.9](https://lwn.net/Articles/1073162/), [6.18.32](https://lwn.net/Articles/1073163/), [6.12.90](https://lwn.net/Articles/1073164/), [6.6.140](https://lwn.net/Articles/1073165/)은 5월 17일에 릴리스되었다.[^p18n4]

[댓글(게시 없음)](https://lwn.net/Articles/1073752/#Comments)

### [금주의 인용문](https://lwn.net/Articles/1073753/)

> Intel의 zero-day bot이 (a) 비공개 소스였고, (b) linux-kernel 메일링 리스트를 참조(cc)에 넣어 테스트 회귀 보고서를 보냈으며, 아무도 크게 불평하지 않았다는 점도 언급해야 한다. 그것이 매우 유용했기 때문이다. Intel이 자사 데이터센터의 매우 비싼 하드웨어를 사용해 보고서를 기여할 의향이 있었고, 그 보고서가 유용하며 거짓 양성(false-positive) 잡음이 충분히 낮은 한, 우리는 고마워하기로 했고 Intel의 zero-day bot이 비공개 소스라는 사실에 대해서는 (너무 많이) 걱정하지 않기로 했다. (물론 Plumbers의 술자리에서는 실제로 약간의 투덜거림이 있었다. :-)
>
> 내 의견으로는 Sashiko에 대해서도 같은 방식으로 해야 하며, 그것이 ext4 개발자들이 내린 결정이다 --- 적어도 ext4 패치에 대해서는 그렇다.

—

Ted Ts'o

[댓글(3개 게시)](https://lwn.net/Articles/1073753/)

## 배포판

### [배포판 금주의 인용문](https://lwn.net/Articles/1073099/)

> 별도 공지가 있을 때까지는 매일 긴급 #fedora 커널 보안 업데이트가 있을 것이라고 가정하는 편이 아마 좋을 것이다.

—

Adam Williamson

[댓글(게시 없음)](https://lwn.net/Articles/1073099/)

## 개발

### [Firefox 151.0 릴리스](https://lwn.net/Articles/1073579/)

요약: Firefox 151.0은 사생활 보호 브라우징 세션 재시작, 지문 추적 방어 개선, Firefox VPN 위치 제어 등을 포함한다.

Firefox 브라우저 버전 151.0이 릴리스되었다. 주요 변경 사항에는 사생활 보호 브라우징(private-browsing) 세션을 지우고 다시 시작하는 기능, 더 나은 지문 추적(fingerprinting) 보호, Firefox VPN 사용 시 표시되는 위치에 대한 제어 등이 포함된다.

[댓글(3개 게시)](https://lwn.net/Articles/1073579/)

[^p18n1]: 키 교체 메커니즘은 사용자가 새 키를 신뢰할지 직접 판단하는 부담을 줄이지만, 구현이 잘못되면 잘못된 키 전환을 자동으로 신뢰하게 만들 수 있으므로 클라이언트 간 상호운용성과 검증 절차가 중요하다.
[^p18n2]: PQC 지원은 장기적으로 양자컴퓨터 공격에 대비하기 위한 조치이지만, 실제 보안은 알고리즘 선택뿐 아니라 키 배포, 교체, 철회 절차가 함께 안전하게 동작할 때 확보된다.
[^p18n3]: 커널 보안 목록에서 AI 생성 보고를 비공개로 처리하면 중복과 업무량이 급증할 수 있다. 공개적으로 재현 가능한 문제는 공개 토론과 추적 체계가 더 효과적일 수 있다는 것이 이 논의의 핵심이다.
[^p18n4]: stable kernels 업데이트가 자주 나온다는 것은 중요한 수정이 빠르게 배포된다는 장점이 있지만, 운영자는 커널 ABI·드라이버·배포판 패키지와의 호환성을 확인하며 신속히 적용해야 한다.

---

### [pgBackRest는 계속된다](https://lwn.net/Articles/1073470/)

**요약:** PostgreSQL용 백업·복구 도구인 pgBackRest는 후원 부족으로 보관 처리되었으나, 여러 후원자가 새로 나서면서 유지보수와 개발이 계속될 예정이다.[^p19n3]

4월에 PostgreSQL용 인기 [pgBackRest](https://pgbackrest.org/) 백업·복구 프로젝트의 유지보수자인 David Steele은 후원 부족 때문에 [프로젝트를 보관 처리했다](https://github.com/pgbackrest/pgbackrest#notice-of-obsolescence)고 발표했으며, 더 이상 유지보수하지 않겠다고 밝혔다. 5월 18일 그는 여러 후원자가 나서서 프로젝트의 지속적인 개발을 보장하게 되었다고 [발표했다](https://pgbackrest.org/news.html#will-continue).

> 지난 몇 주 동안, 여러 후원자로 이루어진 연합이 지속적인 개발에 자금을 지원하기 위해 모였습니다. 이들의 지원 덕분에 프로젝트는 더 이상 단일 후원자에게 의존하지 않게 되었고, pgBackRest가 장기적으로 필요로 하는 안정성을 얻게 되었습니다.
>
> [...] 다시 작업에 복귀할 수 있게 되어 기대가 큽니다. 향후 릴리스에서 공유하고 싶은 기능과 최적화가 준비 중입니다. 이를 가능하게 해 준 후원자들께 감사드리며, 전환 기간 동안 인내와 지원을 보여 준 커뮤니티에도 감사드립니다.

제보해 준 Paul Wise에게 감사한다.

[댓글(1개 게시됨)](https://lwn.net/Articles/1073470/#Comments)

## 기타

### [Peter G. Neumann의 별세](https://lwn.net/Articles/1073186/)

**요약:** 수십 년 동안 RISKS Digest를 운영하는 등 컴퓨터 보안과 신뢰성 커뮤니티에 큰 영향을 준 Peter G. Neumann이 세상을 떠났다.

우리는 여러 업적 가운데에서도 수십 년 동안

RISKS Digest

를 운영했던 Peter G. Neumann이 세상을 떠났다는 소식을 전해 들었다. 그는 크게 그리워질 것이다.

**업데이트**: New York Times가 Neumann 박사의 [부고](https://www.nytimes.com/2026/05/17/obituaries/peter-g-neumann-dead.html)를 게재했다.

[댓글(52개 게시됨)](https://lwn.net/Articles/1073186/)

**페이지 편집자**: Daroc Alden

# 공지

## 뉴스레터

### 배포판 및 시스템 관리

DistroWatch Weekly

5월 18일

This week in F-Droid

5월 14일

openSUSE Tumbleweed Review of the Week

5월 15일

Ubuntu Weekly Newsletter

5월 18일

### 개발

Emacs News

5월 18일

What's cooking in git.git

5월 18일

What's cooking in git.git

5월 20일

This Week in GNOME

5월 15일

GNU Tools Weekly News

5월 17일

Golang Weekly

5월 15일

Last Week in Kubernetes Development

5월 14일

LLVM Weekly

5월 18일

This Week in Matrix

5월 15일

OCaml Weekly News

5월 19일

Perl Weekly

5월 18일

This Week in Plasma

5월 16일

PyCoder's Weekly

5월 19일

Weekly Rakudo News

5월 18일

Ruby Weekly News

5월 14일

This Week in Rust

5월 13일

Sourceware @ Conservancy Year Three

5월 16일

Wikimedia Tech News

5월 18일

### 회의록

Fedora FESCo meeting minutes

5월 19일

This week in the Perl Steering Committee

5월 19일

## 발표 모집(CFP)

### CFP 마감일: 2026년 5월 21일부터 2026년 7월 20일까지

**요약:** 이 표는 2026년 5월 말부터 7월 중순까지 마감되는 LWN.net CFP Calendar의 발표 제안서 접수 일정을 정리한다. DebConf 26, Netdev, PostgreSQL Conference Europe, Linux Foundation 유럽 행사 등 여러 오픈소스·인프라 행사의 제안서 마감일이 포함되어 있다.[^p19n1]

다음 CFP 마감 목록은

LWN.net CFP Calendar

에서 가져온 것이다.

| 마감일 | 행사 날짜 | 행사 | 장소 |
| --- | --- | --- | --- |
| 5월 25일 | 7월 20일–7월 25일 | [DebConf 26](https://debconf26.debconf.org/cfp/) | 아르헨티나 산타페 |
| 5월 31일 | 10월 1일 | [Open Tech Day \| Software-defined Storage](https://opentechday.de/propose/) | 독일 뉘른베르크 |
| 6월 1일 | 7월 13일–7월 16일 | [Netdev](https://www.netdevconf.info/0x1A/pages/submit-proposal.html#submissions-overview) | 이탈리아 로마 |
| 6월 1일 | 10월 20일–10월 23일 | [PostgreSQL Conference Europe](https://2026.pgconf.eu/call-for-papers/) | 스페인 발렌시아 |
| 6월 5일 | 7월 18일 | [AlmaLinux Day: Los Angeles](https://sessionize.com/almalinux-day-los-angeles) | 미국 CA 로스앤젤레스 |
| 6월 14일 | 6월 14일 | [Neocypherpunk Summit](https://luma.com/f47k4xnd) | 독일 베를린 |
| 6월 14일 | 9월 30일–10월 1일 | [All Systems Go! 2026](https://cfp.all-systems-go.io/all-systems-go-2026/cfp) | 독일 베를린 |
| 6월 24일 | 10월 7일–10월 9일 | [Embedded Linux Conference Europe](https://events.linuxfoundation.org/embedded-linux-conference-europe/program/cfp/) | 체코 프라하 |
| 6월 24일 | 10월 7일–10월 9일 | [Open Source Summit Europe](https://events.linuxfoundation.org/open-source-summit-europe/program/cfp/) | 체코 프라하 |
| 6월 28일 | 10월 8일 | [Linux Security Summit Europe](https://events.linuxfoundation.org/linux-security-summit-europe/program/cfp/) | 체코 프라하 |
| 6월 30일 | 11월 17일–11월 19일 | [Open Source Monitoring Conference](https://osmc.de/call-for-papers/) | 독일 뉘른베르크 |
| 7월 15일 | 7월 15일–7월 22일 | [BornHack 2026](https://bornhack.dk/bornhack-2026/program/call-for-participation/) | 덴마크 퓐 섬 |

행사의 CFP 마감일이 여기에 보이지 않으면 [알려 주십시오](https://lwn.net/Calendar/new/).

## 예정된 행사

### 행사: 2026년 5월 21일부터 2026년 7월 20일까지

**요약:** LWN.net Calendar에서 가져온 예정 행사 목록으로, 2026년 5월 말부터 7월 중순까지 유럽·북미·아시아에서 열리는 리눅스, 오픈소스, 보안, 언어 커뮤니티 행사를 날짜순으로 보여 준다.[^p19n2]

다음 행사 목록은

LWN.net Calendar

에서 가져온 것이다.

| 날짜 | 행사 | 장소 |
| --- | --- | --- |
| 5월 18일–5월 23일 | [RustWeek 2026](https://2026.rustweek.org/) | 네덜란드 위트레흐트 |
| 5월 21일–5월 22일 | [Linux Security Summit North America](https://events.linuxfoundation.org/linux-security-summit-north-america/) | 미국 미네소타주 미니애폴리스 |
| 5월 23일–5월 24일 | [Curl up](https://github.com/curl/curl-up/wiki/2026) | 체코 프라하 |
| 5월 26일 | [Media Summit](https://lwn.net/ml/all/92e24f36-d189-4ba8-ad0b-43277bc1aabd@kernel.org) | 프랑스 니스 |
| 5월 27일–5월 28일 | [Embedded Recipes](https://embedded-recipes.org/2026/) | 프랑스 니스 |
| 5월 29일 | [libcamera workshop](https://lwn.net/ml/all/20260315221126.GA520505@killaraus.ideasonboard.com) | 프랑스 니스 |
| 5월 29일 | [Yocto Project Developer Day](https://pretalx.com/yocto-embedded-recipes-2026/) | 프랑스 니스 |
| 5월 30일–5월 31일 | [Journées du Logiciel Libre 2026](https://jdll.org/) | 프랑스 리옹 |
| 6월 6일 | [Hong Kong Open Source Conference](https://hkoscon.org) | 홍콩 |
| 6월 6일–6월 7일 | [Technical Dutch Open Source Event](https://t-dose.org/) | 네덜란드 헬드롭(에인트호번 인근) |
| 6월 8일–6월 12일 | [RISC-V Summit Europe 2026](https://riscv-europe.org/summit/2026/) | 이탈리아 볼로냐 |
| 6월 12일–6월 14일 | [Southeast Linuxfest](https://southeastlinuxfest.org/) | 미국 NC 샬럿 |
| 6월 14일 | [Neocypherpunk Summit](https://s26ber.web3privacy.info/) | 독일 베를린 |
| 6월 14일–6월 16일 | [Flock to Fedora](https://fedoramagazine.org/flock-to-fedora-2026-prague/) | 체코 프라하 |
| 6월 16일–6월 17일 | [Open Source Summit India](https://events.linuxfoundation.org/open-source-summit-india/) | 인도 뭄바이 |
| 6월 18일–6월 20일 | [Linux Audio Conference](https://lac26.mucs.club/) | 아일랜드 메이누스 |
| 7월 13일–7월 19일 | [DebCamp 26](https://debconf26.debconf.org/) | 아르헨티나 산타페 |
| 7월 13일–7월 16일 | [Netdev](https://www.netdevconf.info/0x1A/) | 이탈리아 로마 |
| 7월 13일–7월 19일 | [EuroPython](https://ep2026.europython.eu/) | 폴란드 크라쿠프 |
| 7월 15일–7월 22일 | [BornHack 2026](https://bornhack.dk/bornhack-2026/) | 덴마크 퓐 섬 |
| 7월 16일–7월 19일 | [Electromagnetic Field](https://www.emfcamp.org/) | 영국 이스트너 |
| 7월 18일 | [AlmaLinux Day: Los Angeles](https://almalinux.org/almalinux-day-los-angeles-2026/) | 미국 CA 로스앤젤레스 |

행사가 여기에 보이지 않으면 [알려 주십시오](https://lwn.net/Calendar/new/).

## 보안 업데이트

[^p19n1]: CFP 일정은 프로젝트가 발표자와 주제를 조기에 확보할 수 있게 해 주며, 특히 배포판·커널·데이터베이스처럼 유지보수자가 분산된 분야에서는 로드맵 공유와 신규 기여자 유입의 중요한 통로가 된다.
[^p19n2]: 행사 목록은 커뮤니티 유지보수 관점에서 단순한 일정표 이상이다. 대면 회의와 워크숍은 장기 미해결 이슈를 조율하고, 신규 릴리스 정책이나 보안 대응 절차를 합의하는 데 자주 활용된다.
[^p19n3]: pgBackRest 사례는 핵심 오픈소스 인프라가 단일 후원자에 의존할 때 생기는 지속 가능성 위험을 보여 준다. 여러 후원자로 기반을 넓히면 프로젝트의 버스 팩터와 장기 유지보수 가능성을 개선할 수 있다.

---

### [2026년 5월 14일~5월 20일 보안 알림 요약](https://lwn.net/Articles/1073757/)
#### 요약

- 이 표는 2026년 5월 14일부터 20일까지 LWN이 집계한 배포판별 보안 업데이트를 정리한다.
- 배포판 이름, 권고 ID, 릴리스, 패키지명, 날짜와 링크는 운영자가 원문 권고를 추적할 수 있도록 그대로 보존했다.
- `kernel`, `chromium`, `firefox`, `nginx`, `ruby`, `postgresql`, `thunderbird` 등 서버·데스크톱 핵심 패키지 업데이트가 포함되어 패치 우선순위 검토에 유용하다.[^p20n1]
| 배포판 | ID | 릴리스 | 패키지 | 날짜 |
| --- | --- | --- | --- | --- |
| AlmaLinux | [ALSA-2026:16482](https://lwn.net/Articles/1073202/) | 9 | freerdp | 2026-05-16 |
| AlmaLinux | [ALSA-2026:16484](https://lwn.net/Articles/1072780/) | 9 | gimp | 2026-05-14 |
| AlmaLinux | [ALSA-2026:17533](https://lwn.net/Articles/1073203/) | 8 | gimp:2.8 | 2026-05-16 |
| AlmaLinux | [ALSA-2026:16692](https://lwn.net/Articles/1073204/) | 10 | jq | 2026-05-16 |
| AlmaLinux | [ALSA-2026:16693](https://lwn.net/Articles/1072781/) | 9 | jq | 2026-05-14 |
| AlmaLinux | [ALSA-2026:A010](https://lwn.net/Articles/1073207/) | 10 | kernel | 2026-05-16 |
| AlmaLinux | [ALSA-2026:16195](https://lwn.net/Articles/1073205/) | 8 | kernel | 2026-05-16 |
| AlmaLinux | [ALSA-2026:A008](https://lwn.net/Articles/1073208/) | 8 | kernel | 2026-05-16 |
| AlmaLinux | [ALSA-2026:A009](https://lwn.net/Articles/1073206/) | 9 | kernel | 2026-05-16 |
| AlmaLinux | [ALSA-2026:16206](https://lwn.net/Articles/1073628/) | 9 | kernel | 2026-05-20 |
| AlmaLinux | [ALSA-2026:18064](https://lwn.net/Articles/1073629/) | 10 | libpng | 2026-05-19 |
| AlmaLinux | [ALSA-2026:18028](https://lwn.net/Articles/1073476/) | 9 | libpng | 2026-05-18 |
| AlmaLinux | [ALSA-2026:18063](https://lwn.net/Articles/1073630/) | 10 | nginx | 2026-05-19 |
| AlmaLinux | [ALSA-2026:18029](https://lwn.net/Articles/1073477/) | 9 | nginx | 2026-05-18 |
| AlmaLinux | [ALSA-2026:18041](https://lwn.net/Articles/1073631/) | 8 | nginx:1.24 | 2026-05-19 |
| AlmaLinux | [ALSA-2026:17481](https://lwn.net/Articles/1073209/) | 8 | rsync | 2026-05-16 |
| AlmaLinux | [ALSA-2026:18065](https://lwn.net/Articles/1073633/) | 10 | ruby | 2026-05-19 |
| AlmaLinux | [ALSA-2026:18039](https://lwn.net/Articles/1073632/) | 9 | ruby | 2026-05-19 |
| AlmaLinux | [ALSA-2026:18030](https://lwn.net/Articles/1073634/) | 9 | ruby:3.3 | 2026-05-19 |
| AlmaLinux | [ALSA-2026:17075](https://lwn.net/Articles/1072782/) | 10 | yggdrasil | 2026-05-14 |
| Debian | [DSA-6273-1](https://lwn.net/Articles/1073210/) | stable | chromium | 2026-05-15 |
| Debian | [DLA-4590-1](https://lwn.net/Articles/1073478/) | LTS | erlang | 2026-05-18 |
| Debian | [DSA-6268-1](https://lwn.net/Articles/1072950/) | stable | ffmpeg | 2026-05-14 |
| Debian | [DSA-6276-1](https://lwn.net/Articles/1073211/) | stable | ffmpeg | 2026-05-15 |
| Debian | [DLA-4585-1](https://lwn.net/Articles/1073212/) | LTS | firewalld | 2026-05-15 |
| Debian | [DSA-6281-1](https://lwn.net/Articles/1073635/) | stable | gnutls28 | 2026-05-19 |
| Debian | [DSA-6271-1](https://lwn.net/Articles/1072951/) | stable | gsasl | 2026-05-14 |
| Debian | [DLA-4587-1](https://lwn.net/Articles/1073215/) | LTS | kernel | 2026-05-16 |
| Debian | [DSA-6274-1](https://lwn.net/Articles/1073213/) | stable | kernel | 2026-05-15 |
| Debian | [DSA-6275-1](https://lwn.net/Articles/1073214/) | stable | kernel | 2026-05-15 |
| Debian | [DLA-4588-1](https://lwn.net/Articles/1073636/) | LTS | linux-6.1 | 2026-05-19 |
| Debian | [DSA-6280-1](https://lwn.net/Articles/1073479/) | stable | netatalk | 2026-05-18 |
| Debian | [DLA-4581-1](https://lwn.net/Articles/1072784/) | LTS | nghttp2 | 2026-05-13 |
| Debian | [DSA-6266-1](https://lwn.net/Articles/1072783/) | stable | nghttp2 | 2026-05-14 |
| Debian | [DLA-4589-1](https://lwn.net/Articles/1073480/) | LTS | nginx | 2026-05-18 |
| Debian | [DSA-6278-1](https://lwn.net/Articles/1073216/) | stable | nginx | 2026-05-16 |
| Debian | [DSA-6272-1](https://lwn.net/Articles/1072952/) | stable | nodejs | 2026-05-14 |
| Debian | [DSA-6277-1](https://lwn.net/Articles/1073217/) | stable | openjpeg2 | 2026-05-15 |
| Debian | [DLA-4584-1](https://lwn.net/Articles/1073218/) | LTS | openssh | 2026-05-15 |
| Debian | [DLA-4586-1](https://lwn.net/Articles/1073219/) | LTS | php7.4 | 2026-05-16 |
| Debian | [DSA-6269-1](https://lwn.net/Articles/1072953/) | stable | postgresql-15 | 2026-05-14 |
| Debian | [DSA-6270-1](https://lwn.net/Articles/1072954/) | stable | postgresql-17 | 2026-05-14 |
| Debian | [DLA-4583-1](https://lwn.net/Articles/1072955/) | LTS | python3.9 | 2026-05-15 |
| Debian | [DSA-6279-1](https://lwn.net/Articles/1073220/) | stable | redis | 2026-05-17 |
| Debian | [DLA-4582-1](https://lwn.net/Articles/1072956/) | LTS | thunderbird | 2026-05-14 |
| Debian | [DSA-6267-1](https://lwn.net/Articles/1072785/) | stable | thunderbird | 2026-05-14 |
| Fedora | [FEDORA-2026-585a8768df](https://lwn.net/Articles/1072789/) | F42 | GitPython | 2026-05-14 |
| Fedora | [FEDORA-2026-ee7b1c75b6](https://lwn.net/Articles/1072960/) | F43 | GitPython | 2026-05-15 |
| Fedora | [FEDORA-2026-b4653c757d](https://lwn.net/Articles/1072961/) | F44 | GitPython | 2026-05-15 |
| Fedora | [FEDORA-2026-8ac58f5cf3](https://lwn.net/Articles/1073484/) | F42 | SDL2_image | 2026-05-19 |
| Fedora | [FEDORA-2026-f1f87b465a](https://lwn.net/Articles/1073483/) | F43 | SDL2_image | 2026-05-19 |
| Fedora | [FEDORA-2026-7fe0476df9](https://lwn.net/Articles/1072804/) | F44 | SDL2_image | 2026-05-13 |
| Fedora | [FEDORA-2026-db5621b65e](https://lwn.net/Articles/1073223/) | F42 | apptainer | 2026-05-18 |
| Fedora | [FEDORA-2026-6c547e9f64](https://lwn.net/Articles/1073222/) | F43 | apptainer | 2026-05-18 |
| Fedora | [FEDORA-2026-d516d12934](https://lwn.net/Articles/1073221/) | F44 | apptainer | 2026-05-18 |
| Fedora | [FEDORA-2026-67a2a7275d](https://lwn.net/Articles/1073224/) | F42 | chromium | 2026-05-15 |
| Fedora | [FEDORA-2026-1aa7b8b515](https://lwn.net/Articles/1072786/) | F44 | chromium | 2026-05-13 |
| Fedora | [FEDORA-2026-885a3f8c70](https://lwn.net/Articles/1073225/) | F44 | chromium | 2026-05-18 |
| Fedora | [FEDORA-2026-dfa8ea5809](https://lwn.net/Articles/1073228/) | F42 | coturn | 2026-05-18 |
| Fedora | [FEDORA-2026-f0fbd93125](https://lwn.net/Articles/1073227/) | F43 | coturn | 2026-05-18 |
| Fedora | [FEDORA-2026-3b3139882c](https://lwn.net/Articles/1073226/) | F44 | coturn | 2026-05-18 |
| Fedora | [FEDORA-2026-6384a3cf14](https://lwn.net/Articles/1073637/) | F43 | dnsmasq | 2026-05-20 |
| Fedora | [FEDORA-2026-ac5cceec13](https://lwn.net/Articles/1073229/) | F44 | dnsmasq | 2026-05-15 |
| Fedora | [FEDORA-2026-4ef690dc30](https://lwn.net/Articles/1072957/) | F44 | expat | 2026-05-15 |
| Fedora | [FEDORA-2026-c62259888c](https://lwn.net/Articles/1073230/) | F42 | firefox | 2026-05-15 |
| Fedora | [FEDORA-2026-4542b2d7aa](https://lwn.net/Articles/1072958/) | F43 | firefox | 2026-05-15 |
| Fedora | [FEDORA-2026-67917a57a3](https://lwn.net/Articles/1072787/) | F44 | firefox | 2026-05-14 |
| Fedora | [FEDORA-2026-dfde5fc92a](https://lwn.net/Articles/1072959/) | F43 | freerdp | 2026-05-15 |
| Fedora | [FEDORA-2026-1c8efcc330](https://lwn.net/Articles/1072788/) | F44 | freerdp | 2026-05-14 |
| Fedora | [FEDORA-2026-ec1c523fdb](https://lwn.net/Articles/1072790/) | F42 | kernel | 2026-05-14 |
| Fedora | [FEDORA-2026-8b4a8d18d2](https://lwn.net/Articles/1073233/) | F42 | kernel | 2026-05-15 |
| Fedora | [FEDORA-2026-db3618772b](https://lwn.net/Articles/1073640/) | F42 | kernel | 2026-05-19 |
| Fedora | [FEDORA-2026-cccb681166](https://lwn.net/Articles/1072792/) | F43 | kernel | 2026-05-14 |
| Fedora | [FEDORA-2026-5e5a0f9621](https://lwn.net/Articles/1072962/) | F43 | kernel | 2026-05-15 |
| Fedora | [FEDORA-2026-03be3dc34b](https://lwn.net/Articles/1073232/) | F43 | kernel | 2026-05-15 |
| Fedora | [FEDORA-2026-88a1fb9418](https://lwn.net/Articles/1073638/) | F43 | kernel | 2026-05-19 |
| Fedora | [FEDORA-2026-4462efc052](https://lwn.net/Articles/1072791/) | F44 | kernel | 2026-05-14 |
| Fedora | [FEDORA-2026-6b173ffc2a](https://lwn.net/Articles/1072963/) | F44 | kernel | 2026-05-15 |
| Fedora | [FEDORA-2026-2aeb7d033a](https://lwn.net/Articles/1073231/) | F44 | kernel | 2026-05-15 |
| Fedora | [FEDORA-2026-346fbec5d5](https://lwn.net/Articles/1073639/) | F44 | kernel | 2026-05-19 |
| Fedora | [FEDORA-2026-cccb681166](https://lwn.net/Articles/1072794/) | F43 | kernel-headers | 2026-05-14 |
| Fedora | [FEDORA-2026-4462efc052](https://lwn.net/Articles/1072793/) | F44 | kernel-headers | 2026-05-14 |
| Fedora | [FEDORA-2026-30a8b60b25](https://lwn.net/Articles/1073641/) | F43 | keylime-agent-rust | 2026-05-19 |
| Fedora | [FEDORA-2026-9002354692](https://lwn.net/Articles/1073642/) | F44 | keylime-agent-rust | 2026-05-19 |
| Fedora | [FEDORA-2026-6c99aaa6d3](https://lwn.net/Articles/1072795/) | F42 | krb5 | 2026-05-14 |

[^p20n1]: 보안 업데이트 표는 개별 취약점의 심각도까지 모두 설명하지 않지만, 운영 환경에서는 배포판 권고 ID와 패키지명을 기준으로 자산 목록·노출 서비스·재부팅 필요 여부를 대조하는 출발점이 된다. 특히 커널·브라우저·TLS/HTTP 스택은 원격 공격면이나 권한 상승과 직접 연결될 수 있어 변경 창(change window)과 롤백 계획을 함께 잡는 것이 좋다.

---

### [2026년 5월 14일~5월 20일 보안 알림 요약](https://lwn.net/Articles/1073757/) (continued part 2)
#### 요약

- 이 표는 2026년 5월 14일부터 20일까지 LWN이 집계한 배포판별 보안 업데이트를 정리한다.
- 배포판 이름, 권고 ID, 릴리스, 패키지명, 날짜와 링크는 운영자가 원문 권고를 추적할 수 있도록 그대로 보존했다.
- `kernel`, `chromium`, `firefox`, `nginx`, `ruby`, `postgresql`, `thunderbird` 등 서버·데스크톱 핵심 패키지 업데이트가 포함되어 패치 우선순위 검토에 유용하다.[^p21n1]
| Fedora | [FEDORA-2026-bb6bb5d1e4](https://lwn.net/Articles/1073235/) | F42 | libgit2_1.8 | 2026-05-17 |
| Fedora | [FEDORA-2026-7b1d032de7](https://lwn.net/Articles/1073234/) | F43 | libgit2_1.8 | 2026-05-17 |
| Fedora | [FEDORA-2026-a4d5162b52](https://lwn.net/Articles/1073236/) | F44 | libgit2_1.8 | 2026-05-17 |
| Fedora | [FEDORA-2026-c618807faa](https://lwn.net/Articles/1073237/) | F44 | libmetal | 2026-05-18 |
| Fedora | [FEDORA-2026-707b7050da](https://lwn.net/Articles/1073482/) | F43 | mod_md | 2026-05-19 |
| Fedora | [FEDORA-2026-c9b72de46a](https://lwn.net/Articles/1073481/) | F44 | mod_md | 2026-05-19 |
| Fedora | [FEDORA-2026-fbeaecb457](https://lwn.net/Articles/1072796/) | F42 | nano | 2026-05-13 |
| Fedora | [FEDORA-2026-38623b4fed](https://lwn.net/Articles/1073240/) | F42 | nginx | 2026-05-15 |
| Fedora | [FEDORA-2026-fb53cb4d67](https://lwn.net/Articles/1073239/) | F43 | nginx | 2026-05-15 |
| Fedora | [FEDORA-2026-094eb13bb1](https://lwn.net/Articles/1073238/) | F44 | nginx | 2026-05-15 |
| Fedora | [FEDORA-2026-38623b4fed](https://lwn.net/Articles/1073243/) | F42 | nginx-mod-brotli | 2026-05-15 |
| Fedora | [FEDORA-2026-fb53cb4d67](https://lwn.net/Articles/1073242/) | F43 | nginx-mod-brotli | 2026-05-15 |
| Fedora | [FEDORA-2026-094eb13bb1](https://lwn.net/Articles/1073241/) | F44 | nginx-mod-brotli | 2026-05-15 |
| Fedora | [FEDORA-2026-38623b4fed](https://lwn.net/Articles/1073246/) | F42 | nginx-mod-fancyindex | 2026-05-15 |
| Fedora | [FEDORA-2026-fb53cb4d67](https://lwn.net/Articles/1073245/) | F43 | nginx-mod-fancyindex | 2026-05-15 |
| Fedora | [FEDORA-2026-094eb13bb1](https://lwn.net/Articles/1073244/) | F44 | nginx-mod-fancyindex | 2026-05-15 |
| Fedora | [FEDORA-2026-38623b4fed](https://lwn.net/Articles/1073249/) | F42 | nginx-mod-headers-more | 2026-05-15 |
| Fedora | [FEDORA-2026-fb53cb4d67](https://lwn.net/Articles/1073248/) | F43 | nginx-mod-headers-more | 2026-05-15 |
| Fedora | [FEDORA-2026-094eb13bb1](https://lwn.net/Articles/1073247/) | F44 | nginx-mod-headers-more | 2026-05-15 |
| Fedora | [FEDORA-2026-094eb13bb1](https://lwn.net/Articles/1073250/) | F44 | nginx-mod-js-challenge | 2026-05-15 |
| Fedora | [FEDORA-2026-38623b4fed](https://lwn.net/Articles/1073253/) | F42 | nginx-mod-modsecurity | 2026-05-15 |
| Fedora | [FEDORA-2026-fb53cb4d67](https://lwn.net/Articles/1073252/) | F43 | nginx-mod-modsecurity | 2026-05-15 |
| Fedora | [FEDORA-2026-094eb13bb1](https://lwn.net/Articles/1073251/) | F44 | nginx-mod-modsecurity | 2026-05-15 |
| Fedora | [FEDORA-2026-38623b4fed](https://lwn.net/Articles/1073256/) | F42 | nginx-mod-naxsi | 2026-05-15 |
| Fedora | [FEDORA-2026-fb53cb4d67](https://lwn.net/Articles/1073255/) | F43 | nginx-mod-naxsi | 2026-05-15 |
| Fedora | [FEDORA-2026-094eb13bb1](https://lwn.net/Articles/1073254/) | F44 | nginx-mod-naxsi | 2026-05-15 |
| Fedora | [FEDORA-2026-38623b4fed](https://lwn.net/Articles/1073259/) | F42 | nginx-mod-vts | 2026-05-15 |
| Fedora | [FEDORA-2026-fb53cb4d67](https://lwn.net/Articles/1073258/) | F43 | nginx-mod-vts | 2026-05-15 |
| Fedora | [FEDORA-2026-094eb13bb1](https://lwn.net/Articles/1073257/) | F44 | nginx-mod-vts | 2026-05-15 |
| Fedora | [FEDORA-2026-3cfb30c1fb](https://lwn.net/Articles/1072797/) | F42 | nix | 2026-05-14 |
| Fedora | [FEDORA-2026-5dfbb9ed69](https://lwn.net/Articles/1072799/) | F43 | nix | 2026-05-14 |
| Fedora | [FEDORA-2026-65ce3da435](https://lwn.net/Articles/1072798/) | F44 | nix | 2026-05-14 |
| Fedora | [FEDORA-2026-0f43f09cd9](https://lwn.net/Articles/1072800/) | F42 | nodejs20 | 2026-05-13 |
| Fedora | [FEDORA-2026-c618807faa](https://lwn.net/Articles/1073260/) | F44 | open-amp | 2026-05-18 |
| Fedora | [FEDORA-2026-9e783d6aa1](https://lwn.net/Articles/1073643/) | F43 | perl-Net-CIDR-Lite | 2026-05-19 |
| Fedora | [FEDORA-2026-6f3d2d0d82](https://lwn.net/Articles/1073261/) | F44 | perl-Net-CIDR-Lite | 2026-05-15 |
| Fedora | [FEDORA-2026-cf2ba5b766](https://lwn.net/Articles/1073264/) | F42 | pgbouncer | 2026-05-18 |
| Fedora | [FEDORA-2026-fad57ac86d](https://lwn.net/Articles/1073263/) | F43 | pgbouncer | 2026-05-18 |
| Fedora | [FEDORA-2026-d3d959a176](https://lwn.net/Articles/1073262/) | F44 | pgbouncer | 2026-05-18 |
| Fedora | [FEDORA-2026-3a58db70ca](https://lwn.net/Articles/1072801/) | F42 | php | 2026-05-14 |
| Fedora | [FEDORA-2026-c4d1ca4f16](https://lwn.net/Articles/1072964/) | F43 | php | 2026-05-15 |
| Fedora | [FEDORA-2026-3505a95524](https://lwn.net/Articles/1073265/) | F43 | pypy | 2026-05-17 |
| Fedora | [FEDORA-2026-130f7539d3](https://lwn.net/Articles/1073266/) | F44 | pypy | 2026-05-17 |
| Fedora | [FEDORA-2026-599dafe4ae](https://lwn.net/Articles/1072802/) | F43 | python-click | 2026-05-14 |
| Fedora | [FEDORA-2026-b9548393aa](https://lwn.net/Articles/1072803/) | F42 | python-django5 | 2026-05-14 |
| Fedora | [FEDORA-2026-793b55138d](https://lwn.net/Articles/1073268/) | F42 | python-jupytext | 2026-05-17 |
| Fedora | [FEDORA-2026-85b819b928](https://lwn.net/Articles/1073267/) | F43 | python-jupytext | 2026-05-17 |
| Fedora | [FEDORA-2026-301cbbe347](https://lwn.net/Articles/1073269/) | F44 | python-jupytext | 2026-05-17 |
| Fedora | [FEDORA-2026-28858c383e](https://lwn.net/Articles/1073644/) | F44 | python-pysam | 2026-05-19 |
| Fedora | [FEDORA-2026-48989df336](https://lwn.net/Articles/1073645/) | F44 | python-urllib3 | 2026-05-19 |
| Fedora | [FEDORA-2026-8d8aee6aaf](https://lwn.net/Articles/1073272/) | F42 | python-uv-build | 2026-05-18 |
| Fedora | [FEDORA-2026-a8100094df](https://lwn.net/Articles/1073271/) | F43 | python-uv-build | 2026-05-18 |
| Fedora | [FEDORA-2026-7aacc8ea7d](https://lwn.net/Articles/1073270/) | F44 | python-uv-build | 2026-05-18 |
| Fedora | [FEDORA-2026-75599531db](https://lwn.net/Articles/1073273/) | F44 | rsync | 2026-05-15 |
| Fedora | [FEDORA-2026-8d8aee6aaf](https://lwn.net/Articles/1073276/) | F42 | rust-astral-tokio-tar | 2026-05-18 |
| Fedora | [FEDORA-2026-a8100094df](https://lwn.net/Articles/1073275/) | F43 | rust-astral-tokio-tar | 2026-05-18 |
| Fedora | [FEDORA-2026-7aacc8ea7d](https://lwn.net/Articles/1073274/) | F44 | rust-astral-tokio-tar | 2026-05-18 |
| Fedora | [FEDORA-2026-813872cbff](https://lwn.net/Articles/1073646/) | F43 | rust-cargo-vendor-filterer | 2026-05-19 |
| Fedora | [FEDORA-2026-b631ccd99a](https://lwn.net/Articles/1073647/) | F44 | rust-cargo-vendor-filterer | 2026-05-19 |
| Fedora | [FEDORA-2026-ba5710ebd0](https://lwn.net/Articles/1073648/) | F43 | rust-ingredients | 2026-05-19 |
| Fedora | [FEDORA-2026-6b01755e7d](https://lwn.net/Articles/1073649/) | F44 | rust-ingredients | 2026-05-19 |
| Fedora | [FEDORA-2026-9695dd338f](https://lwn.net/Articles/1073650/) | F43 | rust-oo7-cli | 2026-05-19 |
| Fedora | [FEDORA-2026-8e53f4aa95](https://lwn.net/Articles/1073651/) | F44 | rust-oo7-cli | 2026-05-19 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072965/) | F44 | rust-podman-sequoia | 2026-05-15 |
| Fedora | [FEDORA-2026-f55df93b17](https://lwn.net/Articles/1073652/) | F43 | rust-rpki | 2026-05-19 |
| Fedora | [FEDORA-2026-aac0adf7f7](https://lwn.net/Articles/1073653/) | F44 | rust-rpki | 2026-05-19 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072966/) | F44 | rust-rpm-sequoia | 2026-05-15 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072967/) | F44 | rust-sequoia-chameleon-gnupg | 2026-05-15 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072968/) | F44 | rust-sequoia-git | 2026-05-15 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072969/) | F44 | rust-sequoia-keystore-server | 2026-05-15 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072970/) | F44 | rust-sequoia-octopus-librnp | 2026-05-15 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072971/) | F44 | rust-sequoia-openpgp | 2026-05-15 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072972/) | F44 | rust-sequoia-sop | 2026-05-15 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072973/) | F44 | rust-sequoia-sq | 2026-05-15 |
| Fedora | [FEDORA-2026-5619c60e85](https://lwn.net/Articles/1072974/) | F44 | rust-sequoia-sqv | 2026-05-15 |
| Fedora | [FEDORA-2026-72a1f0b109](https://lwn.net/Articles/1073654/) | F43 | rust-sevctl | 2026-05-19 |
| Fedora | [FEDORA-2026-941244e8ee](https://lwn.net/Articles/1073655/) | F44 | rust-sevctl | 2026-05-19 |
| Fedora | [FEDORA-2026-95cc69e19a](https://lwn.net/Articles/1073656/) | F43 | rust-tealdeer | 2026-05-19 |

[^p21n1]: 보안 업데이트 표는 개별 취약점의 심각도까지 모두 설명하지 않지만, 운영 환경에서는 배포판 권고 ID와 패키지명을 기준으로 자산 목록·노출 서비스·재부팅 필요 여부를 대조하는 출발점이 된다. 특히 커널·브라우저·TLS/HTTP 스택은 원격 공격면이나 권한 상승과 직접 연결될 수 있어 변경 창(change window)과 롤백 계획을 함께 잡는 것이 좋다.

---

### [2026년 5월 14일~5월 20일 보안 알림 요약](https://lwn.net/Articles/1073757/) (continued part 3)
#### 요약

- 이 표는 2026년 5월 14일부터 20일까지 LWN이 집계한 배포판별 보안 업데이트를 정리한다.
- 배포판 이름, 권고 ID, 릴리스, 패키지명, 날짜와 링크는 운영자가 원문 권고를 추적할 수 있도록 그대로 보존했다.
- `kernel`, `chromium`, `firefox`, `nginx`, `ruby`, `postgresql`, `thunderbird` 등 서버·데스크톱 핵심 패키지 업데이트가 포함되어 패치 우선순위 검토에 유용하다.[^p22n1]
| Fedora | [FEDORA-2026-acda6951c6](https://lwn.net/Articles/1073657/) | F44 | rust-tealdeer | 2026-05-19 |
| Fedora | [FEDORA-2026-593d463bbf](https://lwn.net/Articles/1073277/) | F42 | uriparser | 2026-05-15 |
| Fedora | [FEDORA-2026-8d8aee6aaf](https://lwn.net/Articles/1073280/) | F42 | uv | 2026-05-18 |
| Fedora | [FEDORA-2026-a8100094df](https://lwn.net/Articles/1073279/) | F43 | uv | 2026-05-18 |
| Fedora | [FEDORA-2026-7aacc8ea7d](https://lwn.net/Articles/1073278/) | F44 | uv | 2026-05-18 |
| Fedora | [FEDORA-2026-114b1e5d3a](https://lwn.net/Articles/1073283/) | F42 | valkey | 2026-05-18 |
| Fedora | [FEDORA-2026-76cf27ea56](https://lwn.net/Articles/1073282/) | F43 | valkey | 2026-05-18 |
| Fedora | [FEDORA-2026-3e31dafe5c](https://lwn.net/Articles/1073281/) | F44 | valkey | 2026-05-18 |
| Fedora | [FEDORA-2026-0c9aff64a5](https://lwn.net/Articles/1072805/) | F42 | xen | 2026-05-14 |
| Fedora | [FEDORA-2026-7c3b91a2bc](https://lwn.net/Articles/1073284/) | F43 | yelp | 2026-05-17 |
| Fedora | [FEDORA-2026-ed4f450fa9](https://lwn.net/Articles/1073285/) | F44 | yelp | 2026-05-17 |
| Mageia | [MGASA-2026-0138](https://lwn.net/Articles/1072975/) | 9 | awstats | 2026-05-15 |
| Mageia | [MGASA-2026-0152](https://lwn.net/Articles/1073658/) | 9 | bind | 2026-05-19 |
| Mageia | [MGASA-2026-0135](https://lwn.net/Articles/1072806/) | 9 | dnsmasq | 2026-05-14 |
| Mageia | [MGASA-2026-0144](https://lwn.net/Articles/1073286/) | 9 | dpkg | 2026-05-16 |
| Mageia | [MGASA-2026-0145](https://lwn.net/Articles/1073287/) | 9 | firefox, thunderbird | 2026-05-16 |
| Mageia | [MGASA-2026-0133](https://lwn.net/Articles/1072807/) | 9 | flatpak | 2026-05-14 |
| Mageia | [MGASA-2026-0143](https://lwn.net/Articles/1073288/) | 9 | golang | 2026-05-16 |
| Mageia | [MGASA-2026-0146](https://lwn.net/Articles/1073289/) | 9 | haproxy | 2026-05-17 |
| Mageia | [MGASA-2026-0132](https://lwn.net/Articles/1072808/) | 9 | kernel, kmod-virtualbox | 2026-05-13 |
| Mageia | [MGASA-2026-0131](https://lwn.net/Articles/1072809/) | 9 | kernel-linus | 2026-05-13 |
| Mageia | [MGASA-2026-0141](https://lwn.net/Articles/1072976/) | 9 | libreoffice | 2026-05-15 |
| Mageia | [MGASA-2026-0140](https://lwn.net/Articles/1072977/) | 9 | perl-HTTP-Tiny | 2026-05-15 |
| Mageia | [MGASA-2026-0136](https://lwn.net/Articles/1072810/) | 9 | perl-Net-CIDR-Lite | 2026-05-14 |
| Mageia | [MGASA-2026-0149](https://lwn.net/Articles/1073486/) | 9 | perl-WWW-Mechanize-Cached, perl-File-XDG, perl-Path-Tiny | 2026-05-18 |
| Mageia | [MGASA-2026-0137](https://lwn.net/Articles/1072811/) | 9 | perl-XML-LibXML | 2026-05-14 |
| Mageia | [MGASA-2026-0148](https://lwn.net/Articles/1073487/) | 9 | perl-YAML-Syck | 2026-05-18 |
| Mageia | [MGASA-2026-0150](https://lwn.net/Articles/1073485/) | 9 | perl-libwww-perl, perl-HTTP-Message | 2026-05-19 |
| Mageia | [MGASA-2026-0151](https://lwn.net/Articles/1073488/) | 9 | postgresql15 | 2026-05-19 |
| Mageia | [MGASA-2026-0147](https://lwn.net/Articles/1073489/) | 9 | rclone | 2026-05-18 |
| Mageia | [MGASA-2026-0134](https://lwn.net/Articles/1072812/) | 9 | redis | 2026-05-14 |
| Mageia | [MGASA-2026-0142](https://lwn.net/Articles/1073290/) | 9 | samba | 2026-05-16 |
| Mageia | [MGASA-2026-0139](https://lwn.net/Articles/1072978/) | 9 | tomcat | 2026-05-15 |
| Oracle | [ELSA-2026-11371](https://lwn.net/Articles/1073659/) | OL7 | bind | 2026-05-19 |
| Oracle | [ELSA-2026-13644](https://lwn.net/Articles/1072979/) | OL10 | corosync | 2026-05-14 |
| Oracle | [ELSA-2026-13657](https://lwn.net/Articles/1072980/) | OL8 | corosync | 2026-05-14 |
| Oracle | [ELSA-2026-16014](https://lwn.net/Articles/1072981/) | OL10 | freerdp | 2026-05-14 |
| Oracle | [ELSA-2026-16019](https://lwn.net/Articles/1072983/) | OL8 | freerdp | 2026-05-14 |
| Oracle | [ELSA-2026-16482](https://lwn.net/Articles/1072982/) | OL9 | freerdp | 2026-05-14 |
| Oracle | [ELSA-2026-8883](https://lwn.net/Articles/1073660/) | OL7 | giflib | 2026-05-19 |
| Oracle | [ELSA-2026-16484](https://lwn.net/Articles/1072984/) | OL9 | gimp | 2026-05-14 |
| Oracle | [ELSA-2026-17533](https://lwn.net/Articles/1073661/) | OL8 | gimp:2.8 | 2026-05-19 |
| Oracle | [ELSA-2026-16875](https://lwn.net/Articles/1072985/) | OL8 | git-lfs | 2026-05-14 |
| Oracle | [ELSA-2026-15969](https://lwn.net/Articles/1072986/) | OL10 | glib2 | 2026-05-14 |
| Oracle | [ELSA-2026-15953](https://lwn.net/Articles/1072988/) | OL8 | glib2 | 2026-05-14 |
| Oracle | [ELSA-2026-15971](https://lwn.net/Articles/1072987/) | OL9 | glib2 | 2026-05-14 |
| Oracle | [ELSA-2026-16692](https://lwn.net/Articles/1072989/) | OL10 | jq | 2026-05-14 |
| Oracle | [ELSA-2026-16252](https://lwn.net/Articles/1072991/) | OL8 | jq | 2026-05-14 |
| Oracle | [ELSA-2026-16693](https://lwn.net/Articles/1072990/) | OL9 | jq | 2026-05-14 |
| Oracle | [ELSA-2026-16062](https://lwn.net/Articles/1072992/) | OL10 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50262](https://lwn.net/Articles/1072998/) | OL7 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50262](https://lwn.net/Articles/1072996/) | OL8 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50261](https://lwn.net/Articles/1072997/) | OL8 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50271](https://lwn.net/Articles/1073001/) | OL8 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50262](https://lwn.net/Articles/1073003/) | OL8 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-16195](https://lwn.net/Articles/1073662/) | OL8 | kernel | 2026-05-19 |
| Oracle | [ELSA-2026-50261](https://lwn.net/Articles/1072993/) | OL9 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50271](https://lwn.net/Articles/1072994/) | OL9 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-16206](https://lwn.net/Articles/1072995/) | OL9 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50271](https://lwn.net/Articles/1072999/) | OL9 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50260](https://lwn.net/Articles/1073000/) | OL9 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50270](https://lwn.net/Articles/1073002/) | OL9 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50261](https://lwn.net/Articles/1073004/) | OL9 | kernel | 2026-05-14 |
| Oracle | [ELSA-2026-16799](https://lwn.net/Articles/1073005/) | OL8 | krb5 | 2026-05-14 |
| Oracle | [ELSA-2026-18064](https://lwn.net/Articles/1073664/) | OL10 | libpng | 2026-05-19 |
| Oracle | [ELSA-2026-18028](https://lwn.net/Articles/1073663/) | OL9 | libpng | 2026-05-19 |
| Oracle | [ELSA-2026-15968](https://lwn.net/Articles/1073006/) | OL10 | libsoup3 | 2026-05-14 |
| Oracle | [ELSA-2026-16055](https://lwn.net/Articles/1073007/) | OL8 | libtiff | 2026-05-14 |
| Oracle | [ELSA-2026-15888](https://lwn.net/Articles/1073008/) | OL10 | openexr | 2026-05-14 |
| Oracle | [ELSA-2026-15887](https://lwn.net/Articles/1073009/) | OL9 | openexr | 2026-05-14 |
| Oracle | [ELSA-2026-17481](https://lwn.net/Articles/1073665/) | OL8 | rsync | 2026-05-19 |
| Oracle | [ELSA-2026-18065](https://lwn.net/Articles/1073666/) | OL10 | ruby | 2026-05-19 |
| Oracle | [ELSA-2026-15892](https://lwn.net/Articles/1073010/) | OL9 | thunderbird | 2026-05-14 |
| Oracle | [ELSA-2026-50270](https://lwn.net/Articles/1073011/) |  | uek-kernel | 2026-05-14 |
| Oracle | [ELSA-2026-50260](https://lwn.net/Articles/1073012/) |  | uek-kernel | 2026-05-14 |
| Oracle | [ELSA-2026-6617](https://lwn.net/Articles/1073667/) | OL7 | vim | 2026-05-19 |
| Oracle | [ELSA-2026-17075](https://lwn.net/Articles/1073013/) | OL10 | yggdrasil | 2026-05-14 |
| Red Hat | [RHSA-2026:17040-01](https://lwn.net/Articles/1072948/) | EL10.0 | podman | 2026-05-15 |
| Red Hat | [RHSA-2026:17287-01](https://lwn.net/Articles/1072947/) | EL9.6 | podman | 2026-05-15 |
| Red Hat | [RHSA-2026:16696-01](https://lwn.net/Articles/1072949/) | EL10.0 | skopeo | 2026-05-15 |
| Slackware | [SSA:2026-135-01](https://lwn.net/Articles/1073291/) |  | dnsmasq | 2026-05-15 |
| Slackware | [SSA:2026-139-01](https://lwn.net/Articles/1073668/) |  | haveged | 2026-05-19 |
| Slackware | [SSA:2026-135-02](https://lwn.net/Articles/1073292/) |  | kernel | 2026-05-15 |
| Slackware | [SSA:2026-139-03](https://lwn.net/Articles/1073670/) |  | mozilla | 2026-05-19 |
| Slackware | [SSA:2026-139-02](https://lwn.net/Articles/1073669/) |  | mozilla | 2026-05-19 |
| SUSE | [SUSE-SU-2026:2003-1](https://lwn.net/Articles/1073678/) | SLE15 oS15.6 | GraphicsMagick | 2026-05-19 |
| SUSE | [SUSE-SU-2026:2021-1](https://lwn.net/Articles/1073683/) | SLE12 | ImageMagick | 2026-05-20 |

[^p22n1]: 보안 업데이트 표는 개별 취약점의 심각도까지 모두 설명하지 않지만, 운영 환경에서는 배포판 권고 ID와 패키지명을 기준으로 자산 목록·노출 서비스·재부팅 필요 여부를 대조하는 출발점이 된다. 특히 커널·브라우저·TLS/HTTP 스택은 원격 공격면이나 권한 상승과 직접 연결될 수 있어 변경 창(change window)과 롤백 계획을 함께 잡는 것이 좋다.

---

### [2026년 5월 14일~5월 20일 보안 알림 요약](https://lwn.net/Articles/1073757/) (continued part 4)
#### 요약

- 이 표는 2026년 5월 14일부터 20일까지 LWN이 집계한 배포판별 보안 업데이트를 정리한다.
- 배포판 이름, 권고 ID, 릴리스, 패키지명, 날짜와 링크는 운영자가 원문 권고를 추적할 수 있도록 그대로 보존했다.
- `kernel`, `chromium`, `firefox`, `nginx`, `ruby`, `postgresql`, `thunderbird` 등 서버·데스크톱 핵심 패키지 업데이트가 포함되어 패치 우선순위 검토에 유용하다.[^p23n1]
| SUSE | [SUSE-SU-2026:2023-1](https://lwn.net/Articles/1073681/) | SLE15 | ImageMagick | 2026-05-20 |
| SUSE | [SUSE-SU-2026:2020-1](https://lwn.net/Articles/1073684/) | SLE15 oS15.4 | ImageMagick | 2026-05-20 |
| SUSE | [SUSE-SU-2026:2022-1](https://lwn.net/Articles/1073682/) | SLE15 oS15.6 | ImageMagick | 2026-05-20 |
| SUSE | [SUSE-SU-2026:21615-1](https://lwn.net/Articles/1073028/) | SLE16.0 | ImageMagick | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:10777-1](https://lwn.net/Articles/1073311/) | TW | ImageMagick | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1844-1](https://lwn.net/Articles/1072826/) | SLE12 | Mesa | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1845-1](https://lwn.net/Articles/1072825/) | SLE15 | Mesa | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1839-1](https://lwn.net/Articles/1072827/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | Mesa | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1835-1](https://lwn.net/Articles/1072828/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | Mesa | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1821-1](https://lwn.net/Articles/1072830/) | oS15.4 | NetworkManager | 2026-05-13 |
| SUSE | [openSUSE-SU-2026:10752-1](https://lwn.net/Articles/1072831/) | TW | OpenImageIO | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1619-2](https://lwn.net/Articles/1073515/) | SLE15 | PackageKit | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1939-1](https://lwn.net/Articles/1073337/) | SLE15 oS15.6 | PackageKit | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:20753-1](https://lwn.net/Articles/1073490/) | oS16.0 | agama | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:20752-1](https://lwn.net/Articles/1073491/) | oS16.0 | alloy | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:10765-1](https://lwn.net/Articles/1073014/) | TW | amazon-ssm-agent | 2026-05-14 |
| SUSE | [openSUSE-SU-2026:10784-1](https://lwn.net/Articles/1073293/) | TW | apache-commons-configuration2 | 2026-05-17 |
| SUSE | [openSUSE-SU-2026:10785-1](https://lwn.net/Articles/1073294/) | TW | apache2 | 2026-05-17 |
| SUSE | [openSUSE-SU-2026:20730-1](https://lwn.net/Articles/1073295/) | oS16.0 | apptainer | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21631-1](https://lwn.net/Articles/1073015/) | SLE-m6.1 | avahi | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21584-1](https://lwn.net/Articles/1073016/) | SLE-m6.2 | c-ares | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:0169-1](https://lwn.net/Articles/1073492/) | osB15 | cacti | 2026-05-18 |
| SUSE | [SUSE-SU-2026:21583-1](https://lwn.net/Articles/1073017/) | SLE-m6.2 | cairo | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:10786-1](https://lwn.net/Articles/1073296/) | TW | chromedriver | 2026-05-17 |
| SUSE | [SUSE-SU-2026:1980-1](https://lwn.net/Articles/1073493/) | MP4.3 SLE15 oS15.4 oS15.6 | cloud-init | 2026-05-18 |
| SUSE | [SUSE-SU-2026:2005-1](https://lwn.net/Articles/1073671/) | SLE5.3 SLE-m5.3 | cockpit | 2026-05-19 |
| SUSE | [SUSE-SU-2026:2019-1](https://lwn.net/Articles/1073672/) | SLE5.4 SLE-m5.4 | cockpit | 2026-05-20 |
| SUSE | [SUSE-SU-2026:21630-1](https://lwn.net/Articles/1073018/) | SLE-m6.1 | containerd | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21599-1](https://lwn.net/Articles/1073019/) | SLE16.0 | cpp-httplib | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1948-1](https://lwn.net/Articles/1073297/) | SLE15 oS15.6 | cups-filters | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1940-1](https://lwn.net/Articles/1073298/) | SLE15 oS15.6 | curl | 2026-05-18 |
| SUSE | [SUSE-SU-2026:21626-1](https://lwn.net/Articles/1073022/) | SLE-m6.0 | dnsmasq | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21677-1](https://lwn.net/Articles/1073673/) | SLE-m6.0 | dnsmasq | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21633-1](https://lwn.net/Articles/1073021/) | SLE-m6.1 | dnsmasq | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21640-1](https://lwn.net/Articles/1073020/) | SLE-m6.2 | dnsmasq | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1826-1](https://lwn.net/Articles/1072815/) | SLE12 | dnsmasq | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1934-1](https://lwn.net/Articles/1073299/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 | dnsmasq | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1827-1](https://lwn.net/Articles/1072813/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 oS15.6 | dnsmasq | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1828-1](https://lwn.net/Articles/1072814/) | SLE5.2 SLE-m5.2 | dnsmasq | 2026-05-13 |
| SUSE | [openSUSE-SU-2026:20748-1](https://lwn.net/Articles/1073494/) | oS16.0 | dnsmasq | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:10766-1](https://lwn.net/Articles/1073023/) | TW | dovecot24 | 2026-05-14 |
| SUSE | [openSUSE-SU-2026:20759-1](https://lwn.net/Articles/1073495/) | oS16.0 | emacs | 2026-05-19 |
| SUSE | [SUSE-SU-2026:2010-1](https://lwn.net/Articles/1073674/) | SLE15 oS15.3 | erlang26 | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:10787-1](https://lwn.net/Articles/1073300/) | TW | expat | 2026-05-17 |
| SUSE | [openSUSE-SU-2026:10767-1](https://lwn.net/Articles/1073024/) | TW | ffmpeg-4 | 2026-05-14 |
| SUSE | [openSUSE-SU-2026:20726-1](https://lwn.net/Articles/1073301/) | oS16.0 | ffmpeg-4 | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:10768-1](https://lwn.net/Articles/1073302/) | TW | ffmpeg-7 | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1868-1](https://lwn.net/Articles/1073303/) | SLE15 | firebird | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1830-1](https://lwn.net/Articles/1072816/) | SLE12 | firefox | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1829-1](https://lwn.net/Articles/1072817/) | SLE15 | firefox | 2026-05-13 |
| SUSE | [SUSE-SU-2026:21607-1](https://lwn.net/Articles/1073025/) | SLE16.0 | firefox | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20741-1](https://lwn.net/Articles/1073496/) | oS16.0 | firefox | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1872-1](https://lwn.net/Articles/1073304/) | SLE15 oS15.6 | firewalld | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:10769-1](https://lwn.net/Articles/1073305/) | TW | flux2-cli | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21680-1](https://lwn.net/Articles/1073675/) | SLE-m6.0 | freeipmi | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:0171-1](https://lwn.net/Articles/1073676/) | osB15 | git-bug | 2026-05-20 |
| SUSE | [SUSE-SU-2026:21682-1](https://lwn.net/Articles/1073677/) | SLE-m6.0 | glibc | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:10770-1](https://lwn.net/Articles/1073306/) | TW | glibc | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20764-1](https://lwn.net/Articles/1073497/) | oS16.0 | glibc | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1862-1](https://lwn.net/Articles/1073307/) | SLE15 | go1.25 | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20763-1](https://lwn.net/Articles/1073498/) | oS16.0 | go1.25 | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1861-1](https://lwn.net/Articles/1073308/) | SLE15 | go1.26 | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20762-1](https://lwn.net/Articles/1073499/) | oS16.0 | go1.26 | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1938-1](https://lwn.net/Articles/1073500/) | MP4.3 SLE15 | google-cloud-sap-agent | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1935-1](https://lwn.net/Articles/1073501/) | SLE12 | google-cloud-sap-agent | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:20761-1](https://lwn.net/Articles/1073502/) | oS16.0 | google-guest-agent | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:0167-1](https://lwn.net/Articles/1073309/) | osB15 | gosec | 2026-05-16 |
| SUSE | [SUSE-SU-2026:21621-1](https://lwn.net/Articles/1073310/) | SLE-m6.0 | grub2 | 2026-05-15 |
| SUSE | [SUSE-SU-2026:2008-1](https://lwn.net/Articles/1073680/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 | haveged | 2026-05-19 |
| SUSE | [SUSE-SU-2026:2009-1](https://lwn.net/Articles/1073679/) | SLE15 oS15.6 | haveged | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21628-1](https://lwn.net/Articles/1073027/) | SLE-m6.0 | helm | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21635-1](https://lwn.net/Articles/1073026/) | SLE-m6.1 | helm | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20750-1](https://lwn.net/Articles/1073503/) | oS16.0 | ibus-rime, librime | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:20747-1](https://lwn.net/Articles/1073504/) | oS16.0 | imagemagick | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21679-1](https://lwn.net/Articles/1073685/) | SLE-m6.0 | iproute2 | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21582-1](https://lwn.net/Articles/1073029/) | SLE-m6.2 | iproute2 | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:10788-1](https://lwn.net/Articles/1073312/) | TW | java-11-openj9 | 2026-05-17 |
| SUSE | [openSUSE-SU-2026:10789-1](https://lwn.net/Articles/1073313/) | TW | java-17-openj9 | 2026-05-17 |
| SUSE | [openSUSE-SU-2026:10790-1](https://lwn.net/Articles/1073314/) | TW | java-1_8_0-openj9 | 2026-05-17 |

[^p23n1]: 보안 업데이트 표는 개별 취약점의 심각도까지 모두 설명하지 않지만, 운영 환경에서는 배포판 권고 ID와 패키지명을 기준으로 자산 목록·노출 서비스·재부팅 필요 여부를 대조하는 출발점이 된다. 특히 커널·브라우저·TLS/HTTP 스택은 원격 공격면이나 권한 상승과 직접 연결될 수 있어 변경 창(change window)과 롤백 계획을 함께 잡는 것이 좋다.

---

### [2026년 5월 14일~5월 20일 보안 알림 요약](https://lwn.net/Articles/1073757/) (continued part 5)
#### 요약

- 이 표는 2026년 5월 14일부터 20일까지 LWN이 집계한 배포판별 보안 업데이트를 정리한다.
- 배포판 이름, 권고 ID, 릴리스, 패키지명, 날짜와 링크는 운영자가 원문 권고를 추적할 수 있도록 그대로 보존했다.
- `kernel`, `chromium`, `firefox`, `nginx`, `ruby`, `postgresql`, `thunderbird` 등 서버·데스크톱 핵심 패키지 업데이트가 포함되어 패치 우선순위 검토에 유용하다.[^p24n1]
| SUSE | [SUSE-SU-2026:1955-1](https://lwn.net/Articles/1073315/) | SLE15 | java-1_8_0-openjdk | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:10791-1](https://lwn.net/Articles/1073316/) | TW | java-21-openj9 | 2026-05-17 |
| SUSE | [openSUSE-SU-2026:10792-1](https://lwn.net/Articles/1073317/) | TW | java-25-openj9 | 2026-05-17 |
| SUSE | [openSUSE-SU-2026:10748-1](https://lwn.net/Articles/1072818/) | TW | jupyter-jupyterlab | 2026-05-13 |
| SUSE | [openSUSE-SU-2026:20723-1](https://lwn.net/Articles/1073318/) | oS16.0 | kdenlive | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1857-1](https://lwn.net/Articles/1073033/) | MP4.3 SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | kernel | 2026-05-14 |
| SUSE | [SUSE-SU-2026:1909-1](https://lwn.net/Articles/1073321/) | MP4.3 SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | kernel | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1904-1](https://lwn.net/Articles/1073324/) | SLE12 | kernel | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1825-1](https://lwn.net/Articles/1072820/) | SLE15 | kernel | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1959-1](https://lwn.net/Articles/1073505/) | SLE15 | kernel | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1978-1](https://lwn.net/Articles/1073506/) | SLE15 | kernel | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1900-1](https://lwn.net/Articles/1073325/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 | kernel | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1907-1](https://lwn.net/Articles/1073323/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | kernel | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1899-1](https://lwn.net/Articles/1073326/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | kernel | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1840-2](https://lwn.net/Articles/1072819/) | SLE15 oS15.6 | kernel | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1840-1](https://lwn.net/Articles/1072821/) | SLE15 oS15.6 | kernel | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1908-1](https://lwn.net/Articles/1073322/) | SLE15 oS15.6 | kernel | 2026-05-18 |
| SUSE | [SUSE-SU-2026:21610-1](https://lwn.net/Articles/1073030/) | SLE16.0 | kernel | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21616-1](https://lwn.net/Articles/1073320/) | SLE16.0 | kernel | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21594-1](https://lwn.net/Articles/1073031/) | SLE16.0 SLE-m6.2 | kernel | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21590-1](https://lwn.net/Articles/1073032/) | SLE16.0 SLE-m6.2 | kernel | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20758-1](https://lwn.net/Articles/1073508/) | SLE16.0 oS16.0 | kernel | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:20743-1](https://lwn.net/Articles/1073507/) | SLE16.0 oS16.0 | kernel | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21643-1](https://lwn.net/Articles/1073035/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21642-1](https://lwn.net/Articles/1073036/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21625-1](https://lwn.net/Articles/1073039/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21622-1](https://lwn.net/Articles/1073319/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21646-1](https://lwn.net/Articles/1073688/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21684-1](https://lwn.net/Articles/1073686/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21673-1](https://lwn.net/Articles/1073687/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21645-1](https://lwn.net/Articles/1073689/) | SLE6.0 SLE-m6.0 | kernel | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21644-1](https://lwn.net/Articles/1073034/) | SLE6.0 SLE-m6.0 SLE-m6.1 | kernel | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21636-1](https://lwn.net/Articles/1073037/) | SLE6.0 SLE-m6.0 SLE-m6.1 | kernel | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21632-1](https://lwn.net/Articles/1073038/) | SLE6.0 SLE-m6.0 SLE-m6.1 | kernel | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:10793-1](https://lwn.net/Articles/1073327/) | TW | kernel-devel | 2026-05-17 |
| SUSE | [openSUSE-SU-2026:10779-1](https://lwn.net/Articles/1073328/) | TW | keylime-config | 2026-05-16 |
| SUSE | [SUSE-SU-2026:21641-1](https://lwn.net/Articles/1073040/) | SLE-m6.0 | krb5 | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21618-1](https://lwn.net/Articles/1073329/) | SLE-m6.0 | krb5 | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21629-1](https://lwn.net/Articles/1073041/) | SLE-m6.1 | krb5 | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1816-1](https://lwn.net/Articles/1072822/) | SLE5.5 SLE-m5.5 oS15.5 | krb5 | 2026-05-13 |
| SUSE | [openSUSE-SU-2026:10772-1](https://lwn.net/Articles/1073330/) | TW | libIex-3_4-33 | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1969-1](https://lwn.net/Articles/1073509/) | SLE12 | libsndfile | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1968-1](https://lwn.net/Articles/1073510/) | SLE15 | libsndfile | 2026-05-18 |
| SUSE | [SUSE-SU-2026:21581-1](https://lwn.net/Articles/1073042/) | SLE-m6.2 | libtpms | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:10751-1](https://lwn.net/Articles/1072823/) | TW | libvinylapi3 | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1843-1](https://lwn.net/Articles/1072824/) | SLE15 | log4j | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1870-1](https://lwn.net/Articles/1073331/) | SLE15 oS15.6 | mozjs115 | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1817-1](https://lwn.net/Articles/1072829/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 | mozjs60 | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1956-1](https://lwn.net/Articles/1073332/) | SLE15 oS15.4 | mozjs78 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1953-1](https://lwn.net/Articles/1073333/) | SLE15 oS15.4 | nginx | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:10796-1](https://lwn.net/Articles/1073511/) | TW | nginx | 2026-05-18 |
| SUSE | [SUSE-SU-2026:21608-1](https://lwn.net/Articles/1073043/) | SLE16.0 | ongres-scram, ongres-stringprep, plexus-testing, maven, maven-doxia, mojo-parent, sisu | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20742-1](https://lwn.net/Articles/1073512/) | oS16.0 | ongres-scram, ongres-stringprep, plexus-testing, | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21637-1](https://lwn.net/Articles/1073045/) | SLE-m6.1 | openCryptoki | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21593-1](https://lwn.net/Articles/1073044/) | SLE-m6.2 | openCryptoki | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20755-1](https://lwn.net/Articles/1073513/) | oS16.0 | openexr | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21627-1](https://lwn.net/Articles/1073047/) | SLE-m6.0 | openssh | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21634-1](https://lwn.net/Articles/1073046/) | SLE-m6.1 | openssh | 2026-05-15 |
| SUSE | [SUSE-SU-2026:2025-1](https://lwn.net/Articles/1073691/) | SLE12 | openssh | 2026-05-20 |
| SUSE | [SUSE-SU-2026:2024-1](https://lwn.net/Articles/1073692/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.3 | openssh | 2026-05-20 |
| SUSE | [SUSE-SU-2026:1876-1](https://lwn.net/Articles/1073334/) | SLE15 oS15.6 | openssh | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:10804-1](https://lwn.net/Articles/1073690/) | TW | openssh | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:20757-1](https://lwn.net/Articles/1073514/) | oS16.0 | openssh | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1871-1](https://lwn.net/Articles/1073335/) | oS15.4 | openvswitch | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1952-1](https://lwn.net/Articles/1073336/) | SLE15 | ovmf | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1954-1](https://lwn.net/Articles/1073338/) | SLE15 | perl-Crypt-URandom | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:10773-1](https://lwn.net/Articles/1073339/) | TW | perl-CryptX | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:0170-1](https://lwn.net/Articles/1073693/) | osB15 | perl-CryptX | 2026-05-20 |
| SUSE | [openSUSE-SU-2026:10805-1](https://lwn.net/Articles/1073694/) | TW | perl-HTTP-Tiny | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:10780-1](https://lwn.net/Articles/1073341/) | TW | perl-Net-CIDR-Lite | 2026-05-16 |
| SUSE | [SUSE-SU-2026:1936-1](https://lwn.net/Articles/1073516/) | SLE15 | perl-Text-CSV_XS | 2026-05-18 |
| SUSE | [SUSE-SU-2026:21596-1](https://lwn.net/Articles/1073048/) | SLE16.0 | perl-Text-CSV_XS | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:10774-1](https://lwn.net/Articles/1073342/) | TW | perl-Text-CSV_XS | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:10781-1](https://lwn.net/Articles/1073340/) | TW | perl-libwww-perl | 2026-05-16 |
| SUSE | [SUSE-SU-2026:1970-1](https://lwn.net/Articles/1073517/) | SLE15 oS15.4 | php-composer2 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1958-1](https://lwn.net/Articles/1073518/) | SLE15 | php8 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1957-1](https://lwn.net/Articles/1073519/) | SLE15 oS15.6 | php8 | 2026-05-18 |

[^p24n1]: 보안 업데이트 표는 개별 취약점의 심각도까지 모두 설명하지 않지만, 운영 환경에서는 배포판 권고 ID와 패키지명을 기준으로 자산 목록·노출 서비스·재부팅 필요 여부를 대조하는 출발점이 된다. 특히 커널·브라우저·TLS/HTTP 스택은 원격 공격면이나 권한 상승과 직접 연결될 수 있어 변경 창(change window)과 롤백 계획을 함께 잡는 것이 좋다.

---

### [2026년 5월 14일~5월 20일 보안 알림 요약](https://lwn.net/Articles/1073757/) (continued part 6)
#### 요약

- 이 표는 2026년 5월 14일부터 20일까지 LWN이 집계한 배포판별 보안 업데이트를 정리한다.
- 배포판 이름, 권고 ID, 릴리스, 패키지명, 날짜와 링크는 운영자가 원문 권고를 추적할 수 있도록 그대로 보존했다.
- `kernel`, `chromium`, `firefox`, `nginx`, `ruby`, `postgresql`, `thunderbird` 등 서버·데스크톱 핵심 패키지 업데이트가 포함되어 패치 우선순위 검토에 유용하다.[^p25n1]
| SUSE | [SUSE-SU-2026:21612-1](https://lwn.net/Articles/1073049/) | SLE16.0 | php8 | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20745-1](https://lwn.net/Articles/1073520/) | oS16.0 | php8 | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1931-1](https://lwn.net/Articles/1073343/) | SLE15 SES7.1 oS15.3 | podman | 2026-05-18 |
| SUSE | [SUSE-SU-2026:2007-1](https://lwn.net/Articles/1073696/) | SLE15 | postgresql14 | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:10806-1](https://lwn.net/Articles/1073695/) | TW | postgresql14 | 2026-05-19 |
| SUSE | [SUSE-SU-2026:2000-1](https://lwn.net/Articles/1073697/) | SLE15 | postgresql15 | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1999-1](https://lwn.net/Articles/1073698/) | SLE15 oS15.6 | postgresql15 | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1942-1](https://lwn.net/Articles/1073521/) | SLE15 | postgresql16 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:2001-1](https://lwn.net/Articles/1073700/) | SLE15 oS15.6 | postgresql16 | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:10808-1](https://lwn.net/Articles/1073699/) | TW | postgresql16 | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1943-1](https://lwn.net/Articles/1073344/) | SLE15 oS15.6 | postgresql17 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1946-1](https://lwn.net/Articles/1073522/) | SLE12 | postgresql18 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1945-1](https://lwn.net/Articles/1073523/) | SLE15 | postgresql18 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1944-1](https://lwn.net/Articles/1073345/) | SLE15 oS15.6 | postgresql18 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1820-1](https://lwn.net/Articles/1072833/) | SLE15 | python-Mako | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1819-1](https://lwn.net/Articles/1072832/) | SLE15 oS15.6 | python-Mako | 2026-05-13 |
| SUSE | [SUSE-SU-2026:1842-1](https://lwn.net/Articles/1072834/) | SLE15 oS15.3 | python-Pillow | 2026-05-13 |
| SUSE | [SUSE-SU-2026:2004-1](https://lwn.net/Articles/1073701/) | SLE15 oS15.3 | python-Pillow | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:10759-1](https://lwn.net/Articles/1073052/) | TW | python-Twisted-doc | 2026-05-14 |
| SUSE | [SUSE-SU-2026:21587-1](https://lwn.net/Articles/1073051/) | SLE-m6.2 | python-lxml | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21603-1](https://lwn.net/Articles/1073050/) | SLE16.0 | python-lxml | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20737-1](https://lwn.net/Articles/1073524/) | oS16.0 | python-lxml | 2026-05-19 |
| SUSE | [SUSE-SU-2026:21619-1](https://lwn.net/Articles/1073346/) | SLE-m6.0 | python-pyOpenSSL | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21617-1](https://lwn.net/Articles/1073347/) | SLE-m6.0 SLE-m6.1 | python-pyOpenSSL | 2026-05-15 |
| SUSE | [SUSE-SU-2026:1961-1](https://lwn.net/Articles/1073525/) | oS15.6 | python-python-multipart | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1937-1](https://lwn.net/Articles/1073526/) | SLE12 | python3 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1947-1](https://lwn.net/Articles/1073348/) | SLE15 oS15.4 | python310 | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:10758-1](https://lwn.net/Articles/1073054/) | TW | python311-GitPython | 2026-05-14 |
| SUSE | [openSUSE-SU-2026:10760-1](https://lwn.net/Articles/1073053/) | TW | python311-click | 2026-05-14 |
| SUSE | [openSUSE-SU-2026:10798-1](https://lwn.net/Articles/1073527/) | TW | python311-urllib3 | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1818-1](https://lwn.net/Articles/1072835/) | SLE15 oS15.3 | python39 | 2026-05-13 |
| SUSE | [openSUSE-SU-2026:10762-1](https://lwn.net/Articles/1073055/) | TW | rclone | 2026-05-14 |
| SUSE | [openSUSE-SU-2026:10763-1](https://lwn.net/Articles/1073056/) | TW | regclient | 2026-05-14 |
| SUSE | [SUSE-SU-2026:1964-1](https://lwn.net/Articles/1073528/) | MP4.3 SLE15 oS15.4 | rmt-server | 2026-05-18 |
| SUSE | [SUSE-SU-2026:21676-1](https://lwn.net/Articles/1073703/) | SLE-m6.0 | rsync | 2026-05-19 |
| SUSE | [SUSE-SU-2026:2002-1](https://lwn.net/Articles/1073702/) | SLE12 | rsync | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:10775-1](https://lwn.net/Articles/1073349/) | TW | rsync | 2026-05-15 |
| SUSE | [openSUSE-SU-2026:20754-1](https://lwn.net/Articles/1073529/) | oS16.0 | rsync | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1941-1](https://lwn.net/Articles/1073350/) | SLE15 oS15.6 | sed | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:10764-1](https://lwn.net/Articles/1073057/) | TW | syncthing | 2026-05-14 |
| SUSE | [openSUSE-SU-2026:10776-1](https://lwn.net/Articles/1073351/) | TW | tekton-cli | 2026-05-15 |
| SUSE | [SUSE-SU-2026:21675-1](https://lwn.net/Articles/1073704/) | SLE-m6.0 | tiff | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1966-1](https://lwn.net/Articles/1073531/) | SLE12 | tiff | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1965-1](https://lwn.net/Articles/1073532/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 | tiff | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1967-1](https://lwn.net/Articles/1073530/) | SLE15 oS15.6 | tiff | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:10810-1](https://lwn.net/Articles/1073705/) | TW | traefik | 2026-05-19 |
| SUSE | [openSUSE-SU-2026:20749-1](https://lwn.net/Articles/1073533/) | oS16.0 | tree-sitter | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1962-1](https://lwn.net/Articles/1073534/) | SLE5.5 SLE-m5.5 oS15.5 | util-linux | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1949-1](https://lwn.net/Articles/1073353/) | SLE15 | valkey | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1950-1](https://lwn.net/Articles/1073352/) | SLE15 oS15.6 | valkey | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1998-1](https://lwn.net/Articles/1073536/) | SLE15 | xen | 2026-05-19 |
| SUSE | [SUSE-SU-2026:1933-1](https://lwn.net/Articles/1073354/) | SLE5.5 SLE-m5.5 oS15.5 | xen | 2026-05-18 |
| SUSE | [openSUSE-SU-2026:10800-1](https://lwn.net/Articles/1073535/) | TW | xen | 2026-05-18 |
| SUSE | [SUSE-SU-2026:1951-1](https://lwn.net/Articles/1073355/) | SLE15 | zypper-docker | 2026-05-18 |
| Ubuntu | [USN-8276-1](https://lwn.net/Articles/1073706/) | 16.04 18.04 20.04 | Highlight.js | 2026-05-19 |
| Ubuntu | [USN-8269-1](https://lwn.net/Articles/1073058/) | 14.04 16.04 18.04 20.04 22.04 24.04 25.10 26.04 | avahi | 2026-05-14 |
| Ubuntu | [USN-8268-1](https://lwn.net/Articles/1072836/) | 14.04 16.04 18.04 20.04 22.04 24.04 25.10 26.04 | dnsmasq | 2026-05-13 |
| Ubuntu | [USN-8279-1](https://lwn.net/Articles/1073707/) | 20.04 22.04 | linux, linux-aws, linux-aws-5.15, linux-aws-fips, linux-fips, linux-gcp, linux-gcp-fips, linux-gke, linux-gkeop, linux-hwe-5.15, linux-ibm, linux-ibm-5.15, linux-intel-iotg, linux-intel-iotg-5.15, linux-kvm, linux-nvidia, linux-nvidia-tegra, linux-nvidia-tegra-5.15, linux-oracle, linux-raspi, linux-realtime | 2026-05-19 |
| Ubuntu | [USN-8273-1](https://lwn.net/Articles/1073537/) | 18.04 20.04 | linux, linux-aws, linux-aws-5.4, linux-aws-fips, linux-azure, linux-azure-5.4, linux-azure-fips, linux-bluefield, linux-fips, linux-gcp, linux-gcp-5.4, linux-gcp-fips, linux-hwe-5.4, linux-ibm, linux-ibm-5.4, linux-iot, linux-kvm, linux-oracle, linux-oracle-5.4, linux-xilinx-zynqmp | 2026-05-19 |
| Ubuntu | [USN-8280-1](https://lwn.net/Articles/1073708/) | 18.04 20.04 | linux, linux-aws, linux-aws-fips, linux-bluefield, linux-fips, linux-gcp, linux-gcp-5.4, linux-gcp-fips, linux-ibm, linux-ibm-5.4, linux-kvm, linux-oracle, linux-oracle-5.4, linux-xilinx-zynqmp | 2026-05-19 |
| Ubuntu | [USN-8281-1](https://lwn.net/Articles/1073709/) | 18.04 | linux, linux-aws, linux-aws-fips, linux-fips, linux-gcp-4.15, linux-gcp-fips, linux-kvm, linux-oracle | 2026-05-19 |
| Ubuntu | [USN-8278-1](https://lwn.net/Articles/1073710/) | 22.04 24.04 | linux, linux-aws, linux-aws-fips, linux-gcp, linux-gcp-fips, linux-gke, linux-gkeop, linux-ibm, linux-ibm-6.8, linux-lowlatency, linux-lowlatency-hwe-6.8, linux-raspi, linux-raspi-realtime, linux-realtime, linux-realtime-6.8 | 2026-05-19 |
| Ubuntu | [USN-8277-1](https://lwn.net/Articles/1073711/) | 24.04 25.10 | linux, linux-aws, linux-hwe-6.17, linux-oem-6.17, linux-oracle, linux-raspi, linux-realtime, linux-realtime-6.17 | 2026-05-19 |
| Ubuntu | [USN-8274-1](https://lwn.net/Articles/1073538/) | 14.04 16.04 | linux, linux-aws, linux-kvm, linux-lts-xenial | 2026-05-19 |
| Ubuntu | [USN-8254-3](https://lwn.net/Articles/1073539/) | 24.04 | linux-nvidia-tegra | 2026-05-19 |
| Ubuntu | [USN-8255-3](https://lwn.net/Articles/1073540/) | 20.04 22.04 | linux-nvidia-tegra-5.15, linux-raspi | 2026-05-19 |
| Ubuntu | [USN-8275-1](https://lwn.net/Articles/1073541/) | 22.04 | linux-xilinx-zynqmp | 2026-05-19 |
| Ubuntu | [USN-8271-1](https://lwn.net/Articles/1072837/) | 22.04 24.04 25.10 26.04 | nginx | 2026-05-14 |

[^p25n1]: 보안 업데이트 표는 개별 취약점의 심각도까지 모두 설명하지 않지만, 운영 환경에서는 배포판 권고 ID와 패키지명을 기준으로 자산 목록·노출 서비스·재부팅 필요 여부를 대조하는 출발점이 된다. 특히 커널·브라우저·TLS/HTTP 스택은 원격 공격면이나 권한 상승과 직접 연결될 수 있어 변경 창(change window)과 롤백 계획을 함께 잡는 것이 좋다.

---

### [2026년 5월 14일부터 2026년 5월 20일까지의 보안 경보 요약](https://lwn.net/Articles/1073757/) (계속, 7부)

**요약:** 이 부분은 Ubuntu 16.04의 smarty3 보안 업데이트를 마무리하고, 7.1-rc4 및 여러 안정 커널 릴리스와 함께 아키텍처, 빌드 시스템, 코어 커널, 개발 도구 영역의 주목할 만한 커널 패치 흐름을 정리한다.[^p26n1]

| Ubuntu | [USN-8272-1](https://lwn.net/Articles/1073712/) | 16.04 | smarty3 | 2026-05-19 |

전체 기사

(

댓글: 없음

)

## 관심을 끄는 커널 패치

### 커널 릴리스

Linus Torvalds

Linux 7.1-rc4

5월 17일

Greg Kroah-Hartman

Linux 7.0.9

5월 17일

Greg Kroah-Hartman

Linux 7.0.8

5월 15일

Greg Kroah-Hartman

Linux 7.0.7

5월 14일

Greg Kroah-Hartman

Linux 6.18.32

5월 17일

Greg Kroah-Hartman

Linux 6.18.31

5월 15일

Greg Kroah-Hartman

Linux 6.18.30

5월 14일

Greg Kroah-Hartman

Linux 6.12.90

5월 17일

Greg Kroah-Hartman

Linux 6.12.89

5월 15일

Daniel Wagner

v6.12.89-rt18

5월 16일

Greg Kroah-Hartman

Linux 6.12.88

5월 14일

Greg Kroah-Hartman

Linux 6.6.140

5월 17일

Greg Kroah-Hartman

Linux 6.6.139

5월 15일

Greg Kroah-Hartman

Linux 6.1.173

5월 15일

Greg Kroah-Hartman

Linux 5.15.207

5월 15일

Greg Kroah-Hartman

Linux 5.10.256

5월 15일

### 아키텍처별

Magnus Lindholm

alpha: generic entry 인프라 활성화

5월 17일

Ruidong Tian

arm64: ARCH_HAS_COPY_MC 지원 추가

5월 18일

Dylan Hatch

unwind, arm64: 커널용 sframe unwinder 추가

5월 19일

Ard Biesheuvel

arm64: 커널 data/bss의 선형 alias 매핑 해제

5월 19일

Bibo Mao

LoongArch: KVM: 인터럽트 주입 관련 소규모 개선

5월 14일

Mukesh Kumar Chaurasiya (IBM)

powerpc용 Rust 지원

5월 20일

Milan Tripkovic

riscv: lib: 최적화한 memcmp() 추가 및 KUnit 테스트 확장

5월 14일

Himanshu Chauhan

riscv: 하드웨어 break/watchpoint 지원 도입

5월 18일

Heiko Carstens

s390: idle time accounting 개선

5월 13일

Jan Polensky

s390: Rust 지원 활성화 및 필요한 arch glue 추가

5월 19일

Heiko Carstens

s390: this_cpu 연산 개선

5월 20일

Farhan Ali

s390x의 vfio-pci 장치 오류 복구

5월 14일

Chao Gao

런타임 TDX 모듈 업데이트 지원

5월 13일

Mario Limonciello

CPPC HighestFreq 지원 추가

5월 14일

Sean Christopherson

x86: PV clock과 TSC의 관계 정리 시도

5월 15일

Ross Philipson

x86: Intel TXT용 Secure Launch 지원

5월 15일

Richard Patel

사용자 모드 Indirect Branch Tracking

5월 17일

Ashish Kalra

RMPOPT 지원 추가.

5월 18일

### 빌드 시스템

James Clark

tools/build: 모든 LLVM 도구의 버전 지정 허용

5월 14일

Julian Braha

kconfirm 추가

5월 16일

Nathan Chancellor

커널 빌드에 필요한 최소 LLVM 버전을 17.0.1로 상향

5월 17일

### 코어 커널

David Woodhouse

timekeeping: vmclock을 통한 feed-forward clock discipline 추가

5월 13일

Tim Chen

캐시 인식 스케줄링 개선

5월 13일

Li Pengfei

trace: ftrace ring buffer를 위한 stack trace 중복 제거

5월 14일

Pasha Tatashin

liveupdate: 파일과 세션 수 제한 제거

5월 14일

Shrikanth Hegde

sched: cpu_preferred_mask와 steal-driven vCPU backoff 도입

5월 14일

Waiman Long

cgroup/cpuset: cpuset_*attach()를 위한 여러 source/destination cpuset 지원

5월 14일

Qais Yousef

sched/tick: sched_tick()을 HZ에서 분리

5월 17일

Tejun Heo

bpf/arena: 커널 측 직접 접근

5월 17일

Tejun Heo

sched_ext: cmask 개선

5월 17일

André Almeida

sched: 긴 task name 지원 추가

5월 17일

Thomas Gleixner

/proc/interrupts 추가 개선

5월 17일

David Woodhouse

timekeeping: draft tracking 정밀도 수정 및 vmclock을 통한 feed-forward discipline 추가

5월 17일

Clément Léger

io_uring/zcrx: CQE 기반 알림 및 통계 보고 추가

5월 18일

Leonardo Bras

Per-CPU Work helper 도입(이전 명칭 QPW)

5월 18일

Steven Rostedt

tracing/probes: BTF 이름을 사용한 포인터 역참조 허용

5월 18일

Martin KaFai Lau

bpf: struct_ops를 cgroup에 붙이는 공통 방식

5월 19일

### 개발 도구

Albert Esteve

kunit: 경고 backtrace 억제 지원 추가

5월 14일

Allison Henderson

selftests: rds: rds selftests에 ROCE 지원 추가

5월 13일

Gabriele Monaco

rv: tools에 selftests 및 KUnit tests 추가

5월 14일

Wei-Lin Chang

KVM: arm64: selftests: 기본 nested guest 지원

5월 16일

Ritesh Harjani (IBM)

KVM: selftests: powerpc 지원 추가

5월 15일

Alex Williamson

selftests/vfio: igb: 82576 하드웨어 호환성

5월 15일

Aaron Tomlin

blk-mq: tag starvation observability 도입

5월 17일

Albert Esteve

cgroup: dmem: selftest helper, coverage, VM runner 추가

5월 19일

Yosry Ahmed

KVM: selftests: save+restore와 #PF 스트레스 테스트(ft. nested)

5월 18일

[^p26n1]: LWN의 “Kernel patches of interest” 항목은 머지 여부가 확정된 변경 목록이라기보다, 해당 주에 커널 메일링 리스트에서 주목할 만한 패치 시리즈를 분야별로 추린 것이다.
[^p26n2]: `-rt`가 붙은 릴리스는 PREEMPT_RT 실시간 커널 계열을 가리키며, 일반 안정 커널과 별도의 지연시간 관련 패치 흐름을 따른다.

---

### 장치 드라이버

요약: 이번 장치 드라이버 묶음은 네트워크, 미디어, DRM/GPU, PHY/clock/reset, IIO, 펌웨어, IOMMU/VFIO 등 여러 커널 하위 시스템에 걸쳐 새 하드웨어 지원과 기존 드라이버의 관리·디버그·오프로딩 기능을 넓힌 패치들을 모은 것이다.[^p27n1] 특히 DPLL/PTP, SR-IOV/VFIO, DMA-BUF, PCIe/USB4, SMMUv3 관련 작업은 장치 드라이버가 시간 동기화, 가상화, 메모리 매핑, 플랫폼별 전원·리셋 제어와 더 긴밀하게 결합되고 있음을 보여준다.[^p27n2]

Alexander Usyskin

ISSEI 드라이버

5월 13일

Ivan Vecera

dpll: NCO 핀 유형과 zl3073x 지원 추가

5월 13일

Taniya Das

Eliza의 Video, Camera, Graphics clock controller 지원 추가

5월 13일

Jai Luthra

media: Sony IMX678용 bindings 및 드라이버 추가

5월 13일

Satish Kharat

enic: SR-IOV V2 admin channel 및 MBOX 프로토콜

5월 13일

Konrad Dybcio

non-PCIe NHI/TBT 호스트를 위한 사전 작업

5월 13일

Boris Brezillon

drm/panthor: guards 사용

5월 13일

Dmitry Baryshkov

drm/msm/hdmi & phy: generic PHY framework 사용

5월 13일

Ioana Ciornei

phy: ti: TI DS125DF111 Dual-Channel Retimer용 드라이버 추가

5월 13일

Caleb James DeLisle

EcoNet EN7528 및 EN751221 PCIe 지원 추가.

5월 13일

Erikas Bitovtas

media: qcom: venus: MSM8939 지원 추가

5월 14일

Long Li

net: mana: vPort별 EQ 및 MSI-X 인터럽트 관리

5월 13일

Derek J. Clark

MSI Claw HID Configuration Driver 추가

5월 13일

Ratheesh Kannoth

octeontx2-af: npc: 개선 사항.

5월 14일

tze.yee.ng@altera.com

firmware: stratix10-rsu: 펌웨어에서 QSPI 플래시 크기와 erase size 노출

5월 14일

Junhui Liu

clk/reset: anlogic: DR1V90 SoC 지원 추가

5월 14일

Thangaraj Samynathan

net: lan743x: PCI11x1x용 SFP 지원 추가

5월 14일

Changhuang Liang

JHB100 SoC용 기본 pinctrl 드라이버 추가

5월 14일

dongxuyang@eswincomputing.com

ESWIN EIC7700 HSP clock and reset generator용 드라이버 지원 추가

5월 14일

Tomi Valkeinen

drm/rcar-du: DSC가 있는 DSI 파이프라인 지원 추가

5월 14일

Xuan Zhuo

eea: Alibaba Elastic Ethernet Adaptor용 기본 드라이버 프레임워크 추가

5월 14일

Ahsan Atta

crypto: qat - QAT 장치용 sysfs PCI reset 지원 추가

5월 13일

Rob Clark

drm/msm: PERFCNTR_CONFIG ioctl 추가

5월 14일

Shivendra Pratap

PSCI reset을 위한 PSCI reboot mode 드라이버 구현

5월 14일

Liviu Stan

iio: temperature: ltc2983: ADT7604 지원 추가

5월 14일

Srinivas Kandagatla

soc: qcom: apr: RX 처리 개선

5월 14일

Harshitha Ramamurthy

gve: PTP gettimex64 지원 추가

5월 14일

Grzegorz Nitka

dpll/ice: E825용 generic DPLL 유형 및 전체 TX reference clock 제어 추가

5월 15일

David E. Box

Intel PMC용 ACPI 기반 PMT discovery 지원 추가

5월 14일

Jia Wang via B4 Relay

riscv: ultrarisc: DP1000 SoC DT 및 pinctrl 지원 추가

5월 15일

Alexander Koskovich

Adreno 810 GPU 지원 추가

5월 15일

Amit Sunil Dhamne via B4 Relay

Battery Status AMS 지원 추가

5월 15일

Alexandre Courbot

gpu: nova-core: unbinding 시 unload sequence 실행

5월 15일

Hal Feng

OpenCores PTC PWM 지원 추가

5월 15일

Chen-Yu Tsai

arm64: mediatek: Chromebook에 M.2 E-key 슬롯 추가

5월 15일

Tudor Ambarus

firmware: samsung: acpm: TMU 지원 및 정리

5월 15일

Billy Tsai

pinctrl: aspeed: AST2700 SoC1 지원 추가

5월 15일

Kaustabh Chakraborty

Samsung S2MU005 PMIC 및 그 하위 장치 지원

5월 15일

Vishnu Reddy

media: iris: glymur 플랫폼 지원 추가

5월 15일

Dmitry Baryshkov

media: iris: AR50LT core 지원 추가 및 Agatti 플랫폼 활성화

5월 15일

Atanas Filipov

Subject: [PATCH 0/3] media: qcom: Qualcomm JPEG encoder 드라이버 추가

5월 15일

ZongYu Wu

crypto: hisilicon - backlog 처리 개선

5월 15일

Miguel Vadillo

media: i2c: cvs: Intel CVS 드라이버 추가

5월 14일

Sriharsha Basavapatna

RDMA/bnxt_re: QP uapi 확장 지원

5월 14일

Radu Sabau via B4 Relay

iio: adc: ad4691: AD4691 multichannel SAR ADC family용 드라이버 추가

5월 15일

Hans Zhang

PCI: cadence: LTSSM debugfs 추가

5월 15일

Sven Püschel

media: platform: rga: RGA3 지원 추가

5월 15일

Wadim Mueller

counter: GPIO 기반 quadrature encoder 드라이버 추가

5월 15일

Adrian Hunter

i3c: mipi-i3c-hci: DMA abort, recovery 및 관련 개선

5월 15일

Oleksij Rempel

mfd: NXP MC33978/MC34978 MSDI 지원 추가

5월 15일

Nikhil P. Rao

pds_core용 PLDM Firmware Update 지원

5월 16일

Julian Orth

misc/syncobj: /dev/syncobj 장치 추가

5월 16일

Caleb James DeLisle

clocksource/timer-econet-en751221: timer별 irq 번호 지원

5월 16일

Niklas Söderlund

media: Dreamchip RPPX1 ISP를 사용하는 R-Car ISP 지원 추가

5월 16일

Joshua Crofts

iio: light: veml3328: 새 sensor 지원 추가

5월 16일

Rodrigo Alencar via B4 Relay

ADF41513/ADF41510 PLL frequency synthesizers

5월 17일

Muralidhara M K

platform/x86/amd/hsmp: Family 1Ah, Model 50h-5Fh 지원 추가

5월 17일

Jagadeesh Kona

Glymur 플랫폼의 camera clock controller 지원 추가

5월 17일

Rodrigo Alencar via B4 Relay

AD9910 Direct Digital Synthesizer

5월 17일

Tony Nguyen

iXD 드라이버 도입

5월 15일

Arthur Kiyanovski

ptp: PHC timestamp quality attributes 추가

5월 15일

Jason Gunthorpe

VFIO self test를 위한 mlx5 지원

5월 15일

Linus Walleij

net: dsa: microchip: KSZ8995XA/KS8995XA 지원 추가

5월 16일

Lorenzo Bianconi

net: airoha: 동일한 GDM port에 연결된 여러 net_devices 지원

5월 16일

Chris Morgan

Invensense ICM42607 추가

5월 15일

Chris Morgan

Anbernic RG Vita-Pro 추가

5월 15일

Alessio Ferri

b43: N-PHY rev 8 + radio 2057 rev 8 지원 완성

5월 18일

Tariq Toukan

net/mlx5: satellite PF 지원을 위해 eswitch 인프라 준비

5월 18일

Sumit Garg

firmware: qcom: OP-TEE PAS service 지원 추가

5월 18일

Marco Scardovi (scardracs)

gpiolib: acpi: ACPI GPIO 지원 리팩터링, 강화 및 모듈화

5월 18일

Xingyu Wu

StarFive SAR-ADC 드라이버 추가

5월 18일

Jijie Shao

net: hns3: tc flow offload 지원 강화

5월 18일

Svyatoslav Ryhel

mfd: Asus Transformer embedded controller 지원 추가

5월 18일

Paul Kocialkowski

media: sun6i-csi/isp MC-centric 지원 및 정리

5월 18일

Konrad Dybcio

X1E에서 QMMPHY용 USB4 mode programming

5월 18일

Ahmed Tiba

ACPI: APEI: GHES CPER helper 공유 및 DT FFH provider 추가

5월 18일

Adrian Hunter

i3c: Hot-Join 개선 및 MIPI HCI Hot-Join 지원

5월 18일

Jens Emil Schulz Østergaard

net: dsa: LAN9645x switch chip family용 DSA 지원 추가

5월 18일

Boshi Yu

RDMA/erdma: DMA-BUF memory registration 추가

5월 18일

Philip Radford

SCMIv4.0 Powercap Extensions 지원 추가

5월 18일

Caleb James DeLisle

EcoNet USB PHY 지원 추가

5월 18일

ZongYu Wu

crypto: hisilicon/qm - function reset 및 VF isolation 지원

5월 18일

Manivannan Sadhasivam via B4 Relay

PCI: 플랫폼별 방식으로 Root Ports를 reset하는 지원 추가

5월 18일

Arun Menon

tpm_crb: command 및 response buffer chunking 지원 추가

5월 18일

Marcelo Schmitt

iio: adc: LTC2378 및 유사 ADC 지원 추가

5월 18일

Prabhakar

RZ/V2H(P) SoC용 PCIe 지원 추가

5월 18일

palash.kambar@oss.qualcomm.com

Hawi UFS PHY 및 Controller 지원 추가

5월 18일

Jonas Karlman

drm: bridge: dw_hdmi: 기타 enable/disable, CEC 및 EDID 정리

5월 18일

Joel Fernandes

nova-core mm prerequisites 도입

5월 18일

Joel Fernandes

page table types, vmm 및 bar1 mapping 지원 도입

5월 18일

Rik van Riel

iova: linear search를 피하기 위해 augmented rbtree로 전환

5월 18일

Piyush Patle

iio: adc: AVIA HX710B ADC 지원 추가

5월 19일

Edelweise Escala

LTC3220 18 Channel LED Driver 지원 추가

5월 19일

Nicolin Chen

iommu/arm-smmu-v3: ATC invalidation timeout 시 장치를 quarantine

5월 18일

Luiz Angelo Daros de Luca

net: dsa: realtek: rtl8365mb: bridge offloading 및 VLAN 지원

5월 19일

Qiang Yu

phy: qcom: qmp-pcie: Glymur Gen5x8 PHY용 link-mode 기반 지원 추가

5월 18일

Joey Lu

drm/verisilicon: Nuvoton MA35D1 DCU Lite 지원 추가

5월 19일

Ekansh Gupta via B4 Relay

accel/qda: Qualcomm DSP Accelerator 드라이버

5월 19일

Otto Pflüger

regulator: Unisoc SC2730 PMIC regulators 지원 추가

5월 19일

Srinivas Kandagatla

ASoC: qcom: qdsp6: push/pull module 지원 추가

5월 19일

Bartosz Golaszewski

crypto/dmaengine: qce: BAM locking 도입 및 register I/O에 DMA 사용

5월 19일

syyang@lontium.com

Lontium LT7911EXC eDP to MIPI DSI bridge 추가

5월 19일

Honglei Huang

drm/amdgpu: drm_gpusvm 기반 SVM 구현

5월 19일

Honglei Huang

drm/amdgpu: SVM용 xnack off 지원 추가

5월 19일

Jason Gunthorpe

iommupt가 사용할 수 있도록 SMMUv3 invalidation flow 구성

5월 18일

Laurentiu Palcu

i.MX8MQ용 Cadence MHDP8501(HDMI/DP) 초기 지원

5월 19일

Thomas Richard (TI)

firmware: ti_sci: Jacinto family용 BOARDCFG_MANAGED mode 도입

5월 19일

Daniel Golle

net: dsa: mxl862xx: SerDes ports 및 stats

5월 19일

Vignesh Viswanathan

MPS MP8899 PMIC용 regulator 드라이버 추가

5월 19일

Vignesh Viswanathan

CDSP Power Manangement Driver 추가

5월 20일

Lothar Rubusch

crypto: atmel - 공유 i2c core client 관리 및 capability 기반 selection framework 도입

5월 19일

Christian Marangi

airoha: an7581: USB 지원

5월 20일

Christian Marangi

thermal/drivers: airoha: AN7583 지원 추가

5월 20일

Omar Elghoul

vfio-pci/zdev: 개선된 zPCI Function Measurement 지원

5월 19일

javen

r8169: RTL8127용 RSS 지원 추가

5월 20일

illusion.wang

Nebulamatrix NICs용 nbl 드라이버

5월 20일

Qinxin Xia

ARM SMMUv3용 debugfs 지원 추가

5월 20일

Jinseob Kim

iio: Open Sensor Fusion UART 드라이버 추가

5월 20일

Daniel Machon

net: lan966x: PCIe FDMA 지원 추가

5월 20일

Fidelio Lawson

ksz87xx: low-loss cable equalizer errata 지원 추가

5월 20일

Maciej W. Rozycki

ethernet: 3c509: 드라이버를 되살리고 몇 가지 수정 수행

5월 20일

Rishikesh Donadkar

media: cadence,ti: CSI2RX Multistream 지원

5월 20일

Himanshu Bhavani

media: i2c: imx576 camera sensor 드라이버 추가

5월 20일

Markus Stockhausen

mdio: realtek-rtl9300: 다중 SOC 지원을 위한 기반 작업

5월 19일

Pooja Katiyar

usb: typec: ucsi: SET_PDOS command 지원 추가

5월 19일

Zhiping Zhang

vfio/dma-buf: peer-to-peer access용 TPH 지원 추가

5월 19일

Mallesh Koujalagi

cold reset recovery method 도입

5월 20일

[^p27n1]: 새 드라이버와 바인딩이 추가되면 해당 하드웨어는 일반 커널 API를 통해 노출되므로, 보드별 out-of-tree 코드 의존을 줄이고 배포판 커널에서의 장치 지원 범위를 넓힐 수 있다.
[^p27n2]: SR-IOV, VFIO, DMA-BUF, IOMMU 관련 변경은 드라이버가 가상화·격리·장치 간 버퍼 공유를 안전하게 처리해야 함을 뜻하며, 성능 개선과 함께 ABI 안정성 검토도 더 중요해진다.

---

### 장치 드라이버 인프라

> 요약: RDMA cgroup 계측, 드라이버 코어 정리, DRM 핫플러그 처리, Rust 런타임 PM, virtio 절전 콜백, 범용 RDMA 버퍼 인프라 등 드라이버 하부 구조 개선이 모였다.

Tao Cui

cgroup/rdma: rdma.peak 및 rdma.events[.local] 추가

5월 14일

Bartosz Golaszewski

driver core: 장치 해제 시 플랫폼 장치에서 software node 제거

5월 13일

Dmitry Baryshkov

drm: IRQ_HPD 이벤트를 올바르게 처리

5월 13일

Beata Michalska

Rust: 런타임 PM 지원 추가

5월 14일

Sungho Bae

virtio: virtio-mmio용 noirq 시스템 sleep PM 콜백 추가

5월 16일

Danilo Krummrich

rust: device: 장치 드라이버를 위한 Higher-Ranked Lifetime Types

5월 17일

Jiri Pirko

RDMA: umem을 위한 범용 버퍼 디스크립터 인프라 도입

5월 17일

David Jeffery

장치들을 비동기적으로 종료

5월 18일

Luca Ceresoli

drm bridge 핫플러그

5월 19일

### 파일시스템과 블록 계층

> 요약: 블록 장치의 RWF_DONTCACHE, ext4 fast commit, dm-inlinecrypt 하드웨어 래핑 키, ocfs2 검증 강화, btrfs 압축 지연, XFS fs-verity, 컨테이너화된 ext4 서버의 빠른 IO 등이 포함된다.[^p28n1]

Tal Zussman

block: 블록 장치에서 RWF_DONTCACHE 활성화

5월 14일

Li Chen

ext4: fast commit: FC 로그를 위해 inode 상태 스냅샷 생성

5월 15일

Linlin Zhang

dm-inlinecrypt: hardware-wrapped key 지원 추가

5월 16일

Michael Bommarito

ocfs2: 위조된 메타데이터에 대해 inode 검증기 강화

5월 17일

Jori Koolstra

vfs: open*(2)에 O_CREAT|O_DIRECTORY 추가

5월 17일

Qu Wenruo

btrfs: 압축을 bbio 제출 시점까지 지연

5월 16일

Christoph Hellwig

struct xfs_inode.i_ino 제거

5월 15일

Namjae Jeon

exfat: iomap으로 변환

5월 18일

David Howells

netfs: 분할된 bio_vec[] 체인에서 folio 추적 유지

5월 18일

David Howells

cifs: [WIP] 메시지 처리 전면 개편 및 네트워크 전송 개선

5월 19일

Andrey Albershteyn

EOF 이후 merkle tree를 사용하는 XFS용 fs-verity 지원

5월 20일

Darrick J. Wong

fuse/libfuse/e2fsprogs: 컨테이너화된 ext4 서버를 위한 더 빠른 파일 IO

5월 19일

Keith Busch

block: 진입한 컨텍스트에서 queue limit에 대해 bio 검증

5월 19일

### 메모리 관리

> 요약: 복구 불가능한 페이지 panic 옵션, ioremap/vmalloc/vmap 최적화, virtio-balloon 통계와 push mode, DAMON 확장, swap_ops 재구성, shmem folio 배치, file THP 확대, userfaultfd 지원 등이 다뤄진다.[^p28n2]

Breno Leitao

mm/memory-failure: 복구 불가능한 페이지에 대한 panic 옵션 추가

5월 13일

Wen Jiang

mm/vmalloc: 연속 메모리로 ioremap, vmalloc, vmap 가속

5월 14일

Gregory Price

virtio-balloon: 확장 통계 및 push mode

5월 13일

SeongJae Park

mm/damon: 데이터 속성 모니터링 도입

5월 14일

Kairui Song via B4 Relay

mm, swap: swap table phase IV: 할당 통합 및 정적 메타데이터 축소

5월 15일

Baoquan He

[PATCH v7 0/3] mm/swap: swap_ops를 사용해 swap 장치의 메서드 등록

5월 15일

Li Zhe

mm: ZONE_DEVICE memmap 초기화 가속

5월 15일

Zhen Ni

mm/page_owner: print_mode 및 NUMA 필터링을 위한 per-fd 필터 인프라 추가

5월 15일

Chi Zhiling

mm/shmem: folio 배치로 읽기 성능 최적화

5월 15일

Christoph Hellwig

RFC: 더 나은 block swap 배치 처리와 swap_ops에 대한 다른 접근

5월 15일

Alban Crequy

mm/process_vm_access: process_vm_readv/writev를 위한 pidfd 및 nowait 지원

5월 15일

Zi Yan

CONFIG_READ_ONLY_THP_FOR_FS 제거 및 쓰기 가능 파일에 대한 file THP 활성화

5월 17일

Harry Yoo (Oracle)

mm/slab: 런타임 sheaves 튜닝 활성화

5월 16일

Ravi Jonnalagadda

mm/damon: 하드웨어 샘플링 접근 보고 + AMD IBS Op 예제

5월 16일

Ackerley Tng via B4 Relay

더 범용적인 사용을 위해 HugeTLB 할당 루틴 공개

5월 18일

Shivam Kalra via B4 Relay

mm/vmalloc: vrealloc() 축소 시 사용하지 않는 페이지 해제

5월 19일

Eric Chanudet

cgroup/dmem: dmem 할당을 memcg에 이중 과금할 수 있도록 허용

5월 19일

Yuan Liu

mm/memory_hotplug: pfn 범위 변경 시 zone 연속성 검사 최적화

5월 20일

Stanislav Kinsburskii

mm/hmm: userfaultfd 기반 매핑을 위한 mmap lock-drop 지원 추가

5월 20일

### 네트워킹

> 요약: openvswitch 레거시 터널 포트 제거, devmem/netkit 연동, TLS 1.3 하드웨어 오프로딩, BPF kfunc, rtnetlink 병목 완화, netlink 오류 이벤트, IPsec 오프로딩 등이 포함된다.

Ilya Maximets

openvswitch: 레거시 터널 포트 지원 제거

5월 13일

Bobby Eshleman

net: devmem: netkit 장치에서 devmem 지원

5월 14일

Rishikesh Jethwani

tls: TLS 1.3 하드웨어 오프로딩 지원 추가

5월 15일

Mahe Tardy

bpf: icmp_send kfunc 추가

5월 15일

Kuniyuki Iwashima

udp_tunnel: UDP 터널 장치 소멸 가속(Part II)

5월 18일

Eric Dumazet

rtnetlink: rtnl_getlink()에서 RTNL 회피

5월 18일

Riana Tauro

drm_ras netlink 오류 이벤트 지원 추가

5월 18일

Chuck Lever

net/handshake: 고정된 file 참조에 request 수명 고정

5월 18일

Jihong Min

bonding: 복제된 SA를 사용한 LAG IPsec offload 지원

5월 20일

### 보안 관련

> 요약: landlock의 RENAME_WHITEOUT 제한, seccomp unotify 주입 개선, per-function short-circuit 완화 원시 기능, splice() 차단 경로, 세분화된 LSM mount hook 전환이 보안 경계를 조정한다.[^p28n3]

Günther Noack

landlock: RENAME_WHITEOUT을 사용하는 renameat2 제한

5월 13일

Cong Wang

seccomp: race-free unotify를 위한 SECCOMP_IOCTL_NOTIF_INJECT

5월 14일

Sasha Levin

killswitch: per-function short-circuit 완화 primitive 추가

5월 17일

Pedro Falcato

fs/splice: 읽기 전용 파일에서 splice()를 차단할 방법 허용

5월 16일

Song Liu

lsm: security_sb_mount를 세분화된 mount hook으로 대체

5월 15일

### 가상화와 컨테이너

> 요약: mshv 메모리 영역 관리, KVM x86 에뮬레이터와 AMD CPUID 동작 가상화, KVM riscv dirty logging 성능, liveupdate의 Guest_memfd 보존을 다룬다.[^p28n3]

Stanislav Kinsburskii

mshv: pin 되지 않은 영역의 메모리 소비 감소

5월 13일

Stanislav Kinsburskii

mshv: 메모리 영역 관리 리팩터링 및 생성 시 페이지 매핑

5월 13일

Jim Mattson

KVM: x86: AMD의 "usermode에서 CPUID 비활성화"를 가상화

5월 13일

Sean Christopherson

KVM: x86: 에뮬레이터의 #DB 처리 개선

5월 15일

Jinyu Tang

KVM: riscv: dirty logging write fault 가속

5월 17일

Tarun Sahu

liveupdate: kvm: Guest_memfd 보존

5월 18일

### 기타

> 요약: perf/libunwind 원격 지원, perf test harness, BPF resizable hash map, SPDX SBOM 생성, util-linux와 stalld 릴리스, rv 및 perf tools 업데이트가 포함된다.

Ian Rogers

perf libunwind 다중 원격 지원

5월 13일

Ian Rogers

perf test: harness 개선

5월 13일

Mykyta Yatsenko

bpf: 크기 조정 가능한 hash map 도입

5월 13일

Luis

SPDX SBOM 생성 스크립트 추가

5월 18일

Karel Zak

util-linux v2.42.1

5월 18일

Nam Cao

rv: rtapp monitor update

5월 19일

Ian Rogers

perf tools: inject --aslr 기능, early maps loading, decoupling 수정 추가

5월 19일

Clark Williams

stalld v1.27.1 released

5월 18일

**페이지 편집자**: Joe Brockmeier

[^p28n1]: 파일시스템과 블록 계층 변경은 디스크 캐시 우회, inline encryption 키 관리, Merkle tree 기반 무결성 검증, bio 검증 시점처럼 데이터 지속성과 I/O 지연 시간에 직접 영향을 주는 경로를 바꿀 수 있다.
[^p28n2]: 메모리 관리 변경은 swap 메타데이터, folio 배치, THP, vmalloc 재배치, memory hotplug처럼 NUMA 대형 시스템과 가상화 호스트에서 성능과 장애 격리의 균형에 영향을 준다.
[^p28n3]: 보안 및 가상화 변경은 사용자 공간 알림 경합, 파일 splice 우회, LSM mount 정책, 게스트 메모리 보존 및 CPU 동작 노출 같은 컨테이너/VM 격리 경계를 더 명확히 하거나 재정의한다.
