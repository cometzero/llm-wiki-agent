# LWN.net Weekly Edition for June 25, 2026 한국어 번역

- 원문: https://lwn.net/Articles/1078380/bigpage
- 선택 기준: 최신 Weekly Edition인 2026-07-02호(article_id 1079457)는 최신/유료 가능성이 있어 건너뛰고, 직전 무료 공개판으로 접근 확인된 2026-06-25호(article_id 1078380)를 번역했습니다.
- 생성시각: 2026-07-03T10:06:18+09:00
- 원문 SHA-256: `8d9ee2c39d8749e6f1ed2427f11ef7b0d9f91c82ce702138eeb782fa3a3e106d`
- 번역 경로: Codex CLI 인증 토큰 만료로 `$tech-translate` 경로가 실패하여, 공개 bigpage를 추출한 뒤 Hermes chunk 번역과 보안표 보존 fallback으로 생성했습니다.

## 전체 요약

- 이번 호는 free-threaded Python의 현재 상태, Arch User Repository(AUR) 연쇄 공격, Fedora 2FA 정책 논쟁처럼 언어 런타임·패키지 생태계·프로젝트 보안의 운영 리스크를 집중적으로 다룹니다.
- 커널 쪽에서는 Linux 7.2 merge window 전반부, BPF arena helper library, BPF coroutine/suspend-resume, JIT-compiled BPF용 KASAN, 단일 홉 block replication 등 성능·검증·스토리지 안정성 이슈가 이어집니다.
- OSPM 2026 리포트는 CPU idle, scheduler, thermal pressure, sched_ext, latency nice, hybrid-core scheduling 등 전력 관리와 스케줄링의 실제 설계 쟁점을 폭넓게 정리합니다.
- 단신과 공지에서는 Tor 0.4.8 sunset, Fedora/Arch 보안 이슈, Systemd v261, Mastodon 4.6, Xfce Wayland compositor preview, 배포판별 보안 업데이트와 커널 패치 목록을 제공합니다.
- 보안 업데이트 표와 패치 목록은 검색성과 추적 가능성을 위해 공지 ID, 패키지명, 링크, 버전 문자열을 원문 중심으로 보존했습니다.


### [2026년 6월 25일 LWN.net Weekly Edition에 오신 것을 환영합니다](https://lwn.net/Articles/1079405/)

#### 요약

- 이번 호는 Python의 global interpreter lock (GIL)[^lwn1078380-p01-gil] 제거 노력과 향후 계획을 다룹니다.
- Arch User Repository (AUR) 패키지 침해, Fedora의 2FA 강화 시도 등 보안 이슈를 소개합니다.
- Linux 7.2 merge window 전반부의 주요 커널 변경 사항을 살펴봅니다.
- 2026 Linux Storage, Filesystem, Memory Management, and BPF Summit의 BPF[^lwn1078380-p01-bpf] 관련 세션 보도를 이어갑니다.
- 클라우드 블록 복제, OSPM Summit 2026 1일 차와 2일 차 보고서도 포함합니다.

이번 호에는 다음 특집 콘텐츠가 포함되어 있습니다.

- [Free-threaded Python: 과거,
  현재, 그리고 미래](https://lwn.net/Articles/1078367/): Python의
  global interpreter lock (GIL)을 제거하려는 노력과 앞으로의 일을 살펴봅니다.
- [AURpocalypse now: 최근 AUR 공격
  살펴보기](https://lwn.net/Articles/1077619/): Arch가 지금까지 겪은 AUR
  패키지 침해 중 최악의 공세에 직면했습니다.
- [Fedora: 2FA냐, 아니냐, 그것이
  문제로다](https://lwn.net/Articles/1078964/): Fedora의 보안을 개선하려는 시도입니다.
- [7.2 merge window의 전반부](https://lwn.net/Articles/1078068/): 다음 커널 릴리스에 들어올 중요한 변경 사항입니다.
- [2026 Linux Storage, Filesystem, Memory Management, and BPF Summit](https://lwn.net/Articles/lsfmmbpf2026/)의 추가 보도:

- [BPF arenas를 위한 helper library](https://lwn.net/Articles/1078526/): libarena 라이브러리와 그 향후 방향을 살펴봅니다.
- [BPF programs 일시 중단과 재개](https://lwn.net/Articles/1076210/): BPF에 coroutines를 도입하려는 계획입니다.
- [JIT-compiled BPF code를 위한 KASAN](https://lwn.net/Articles/1077740/): kernel address sanitizer[^lwn1078380-p01-kasan]가 BPF의 JIT compiler에서 버그를 감지하는 방법을 배우고 있습니다.

- [RMR와 BRMR을 이용한 single-hop block replication](https://lwn.net/Articles/1074291/): 클라우드 제공자가 가능한 한 적은 오버헤드로 durable block devices를 노출하는 방법입니다.
- [OSPM 2026 첫째 날 보고서](https://lwn.net/Articles/1077759/): Linux Kernel의 Power Management and Scheduling (OSPM) Summit 첫째 날 세션들입니다.
- [OSPM 2026 둘째 날 보고서](https://lwn.net/Articles/1078696/): OSPM Summit 둘째 날의 보고서입니다.

이번 주 호에는 다음 내부 페이지도 포함되어 있습니다.

- [간단한 소식](https://lwn.net/Articles/1078382/): 커뮤니티 전반의 간단한 뉴스 항목입니다.- [공지](https://lwn.net/Articles/1078383/): 뉴스레터, 컨퍼런스, 보안 업데이트, 패치 등입니다.

이번 주 호도 즐겁게 읽어 주시기 바라며, 언제나처럼 LWN.net을
후원해 주셔서 감사합니다.

[댓글(아직 없음)](https://lwn.net/Articles/1079405/#Comments)

[^lwn1078380-p01-gil]: global interpreter lock (GIL)은 CPython에서 한 시점에 하나의 스레드만 Python bytecode를 실행하도록 제한해 내부 상태를 보호하는 런타임 메커니즘입니다.
[^lwn1078380-p01-bpf]: BPF는 Linux 커널 안에서 검증된 작은 프로그램을 실행해 네트워킹, 추적(tracing), 보안 정책 등을 확장하는 기술입니다.
[^lwn1078380-p01-kasan]: KASAN(Kernel Address Sanitizer)은 커널 코드의 out-of-bounds 접근이나 use-after-free 같은 메모리 오류를 탐지하는 디버깅 도구입니다.

### [자유 스레드 Python: 과거, 현재, 미래](https://lwn.net/Articles/1078367/)

글: **Jake Edge**  
2026년 6월 22일

---

[PyCon US](https://lwn.net/Archives/ConferenceByYear/#2026-PyCon)

#### 요약

- Thomas Wouters는 PyCon US 2026에서 GIL 제거와 자유 스레드(free-threaded) CPython의 동기, 역사, 현황을 설명했다.
- GIL은 CPython 객체와 참조 횟수(reference count)를 보호하지만, 멀티코어 시대에는 Python 스레드의 병렬 실행을 제한한다.
- 과거 GIL 제거 시도들은 단일 스레드 성능 저하나 기존 생태계와의 호환성 문제로 일반 해법이 되지 못했다.
- Sam Gross의 No-GIL 포크와 PEP 703은 편향 참조 카운팅(biased reference counting), 지연 참조 카운팅, 낙관적 접근, 세밀한 잠금 등을 결합했다.
- 현재의 자유 스레드 구현은 리스트와 딕셔너리 같은 핵심 타입을 빠르게 유지하면서도 여러 스레드가 동시에 인터프리터에서 실행될 수 있게 하는 방향으로 발전하고 있다.

아마도 지난 5년 남짓 동안 Python에서 가장 큰 변화는 언어의 “자유 스레드(free-threaded)” 버전이 등장한 것이다. 이 버전은 전역 인터프리터 락(GIL)을 제거하고, 인터프리터 안에서 여러 스레드가 병렬로 실행될 수 있게 한다.[^lwn1078380-p02-gil] 5월 중순 캘리포니아 롱비치에서 열린 [PyCon US 2026](https://us.pycon.org/2026/)에서, 오랫동안 CPython 핵심 개발자로 활동해 왔고 현재는 운영 위원회(steering council) 위원이기도 한 Thomas Wouters가 이 기능에 대해 발표했다. 그는 GIL 제거 노력의 동기, 일부 역사, 자유 스레드 인터프리터의 현재 상태를 살펴보고, 이 모든 것이 어디로 이어질지에 대한 예측도 제시했다.

그는 자신이 이제 약 25년 동안 CPython 핵심 개발을 해 왔으며, 지난 6년 중 5년 동안 운영 위원회에 있었다고 언급하며 발표를 시작했다. 운영 위원회는 자유 스레딩(free threading)을 포함한 언어 기능의 향후 방향을 결정하는 기구다. 그 밖에도 그는 Meta에서 자유 스레드 인터프리터와 다른 일들을 하고 있다. 발표와 완전히 관련 있는 내용은 아니었지만, 그는 고양이 세 마리를 키우고 있다고 말하며 고양이들을 보여 주는 슬라이드를 띄웠다. 그는 웃음과 박수 속에서 “다른 우주 어딘가에는 제가 고양이들을 슬라이드로 쓰는 버전의 이 발표가 있을 겁니다”라고 말했다.

#### 동기

하지만 이것은 그런 발표가 아니라고 그는 말했다. “이것은 지루한 발표입니다.” 그는 청중 대부분이 이미 알고 있을 것이라고 언급하면서도, 스레드를 간단히 소개했다. 스레드는 하나의 프로세스와 그 주소 공간 안에서 별도의 “제어 스레드(threads of control)”를 사용해 여러 일을 동시에 실행하는 방법을 제공한다. 스레드가 존재하는 주된 이유는 성능이다. 메모리 접근은 느리기 때문에, 스레드는 CPU가 메모리를 기다리는 동안 다른 일을 할 수 있게 해 주는 방법이다.

[![[Thomas Wouters]](https://static.lwn.net/images/2026/pycon-wouters2-sm.png "Thomas Wouters")](https://lwn.net/Articles/1078544/)

여러 프로세스를 사용해도 같은 이점을 얻을 수 있지만, 오버헤드가 더 크고 주소 공간이 공유되지 않는다. Python 같은 언어에 스레드가 필요한 이유는 성능 외에도 몇 가지가 더 있다. 예를 들어 블로킹 API를 호출하는 동안 주 프로그램의 실행을 계속하거나, 스레드를 사용해야 접근할 수 있는 서드파티 라이브러리와 상호작용하는 경우가 그렇다. 그는 그런 라이브러리로 “흔히 데이터베이스”를 들었다.

GIL은 오래전에 “CPython이 스레드를 지원하기로 결정한 방식”이며, 그가 이 언어에 관여하기 전부터 있었다. GIL은 Python 객체와 객체가 아직 사용 중인지 판단하는 데 쓰이는 참조 횟수를 보호한다. 또한 CPython 내부 구조도 보호하며, “CPython이 스레드를 지원할 수 있는 가장 효율적인 방법”이다. GIL은 사용자의 Python 코드를 보호하지 않는다. 사용자는 인터프리터가 언제 GIL을 해제하고 다시 획득할지 제어할 수 없기 때문이다. GIL은 C 및 C++ 확장도 “대체로 보호하지 않는다”. 확장 호출이 언제 GIL을 해제할 수 있는지는 더 명확하더라도, “여전히 의도치 않게 GIL에 의존해 결국 안전하지 않게 되기는 매우 쉽다”.

Wouters는 “근본적으로 스레드는 어렵다”고 말했다. 스레드는 복잡하며, GIL이 때로는 그렇지 않은 것처럼 보이게 하더라도 스레드를 더 쉽게 만들어 주지는 않는다. 그러나 GIL은 스레드를 덜 유용하게 만들기도 하며, 그래서 수년 동안 Python에서 GIL을 제거하려는 노력이 있었다. GIL이 처음 추가되었을 때는 다중 CPU 시스템이 드물었지만, 이제 그의 휴대전화에는 코어가 여덟 개 있다.

오랫동안 대안은 프로그램 일부를 C로 다시 작성하는 것이었다. 다만 지난 몇 년 사이에는 그 대상이 Rust로 바뀌었고, 이는 더 낫다. 하지만 그 답이 항상 통하지는 않는다. 코드만 새 언어로 바꾸는 것이 아니라, 데이터도 그 언어의 영역(domain)으로 옮기기 위해 애플리케이션의 많은 부분을 다시 작업해야 하기 때문이다.

여러 프로세스를 사용하는 등 다른 선택지도 있지만, 일반적으로 더 많은 메모리가 필요하고 프로세스 사이에서 데이터를 복사해야 한다. [서브인터프리터(Subinterpreters)](https://lwn.net/Articles/941090/)는 하나의 프로세스가 각각 자체 GIL을 가진 여러 인터프리터를 갖고, 이를 별도 스레드에서 실행할 수 있게 해 줄 것이다. 하지만 그 접근법에는 몇 가지 문제가 있다. 서드파티 라이브러리, 특히 Python을 염두에 두고 작성되지 않은 라이브러리와의 상호작용은 “아직 거기까지 이르지 못했으며”, 지금까지는 서브인터프리터 사이에서 데이터를 복사할 좋은 방법도 없다. [asyncio](https://docs.python.org/3/library/asyncio.html)도 있는데, 이는 사실상 [그린 스레드(green threads)](https://en.wikipedia.org/wiki/Green_thread)와 같은 발상이다. 그는 asyncio의 열렬한 지지자이며, “스레드는 쉽게 잘못된 길로 이끌 수 있는” 네트워크 I/O에는 asyncio가 최선의 방법이라고 생각한다.

하지만 때로는 그런 해법들이 필요한 성능을 제공하지 못한다고 그는 말했다. “GIL이 없다면, 그런 문제들에 대한 멀티스레드 해법은 더 높은 처리량, 더 낮은 메모리 사용량, 더 낮은 지연 시간을 제공할 수 있습니다.” 그러나 앞서 언급했듯이 스레드는 어렵다. 데이터를 공유하기가 어렵기 때문이다. CPU와 컴파일러는 속도를 위해 최적화하며, 메모리 접근이 느리기 때문에 캐싱, 데이터 프리페치(prefetching), 메모리 접근 재정렬 같은 여러 일을 한다.

그런 기법들과 스레드의 상호작용은 “극도로 복잡하다”. 한 스레드가 값을 쓰면, 다른 스레드는 그것을 언제 보게 되며, 쓰인 값의 절반만이 아니라 전체 값을 보게 되는가? 한 스레드가 두 가지를 쓰면, 다른 스레드는 그것들을 어떤 순서로 보게 되는가? 이런 문제를 처리하려면 메모리 펜스(memory fence), 원자적 연산(atomic operation), 메모리 모델(memory model) 같은 것이 필요하지만, 그는 이를 다루지는 않겠다고 했다. 그의 결론은 이렇다. “스레드에서 공유되고 변경 가능한 데이터는 나쁘다.”

Python의 문제는 모든 것이 객체이고, 모든 것이 공유된다는 점이다. 모든 객체에는 참조 횟수가 있으며, 이는 모든 객체 안에 있는 작은 변경 가능한 데이터 조각이다. 따라서 Python에서는 “모든 것이 공유된 변경 가능한 데이터”다. Wouters는 CPython C API가 여러 방식으로 GIL에 의존한다고 말했다. 예를 들어 [PyDict\_GetItem()](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem)은 딕셔너리 안의 항목에 대한 [빌린 참조(borrowed reference)](https://docs.python.org/3/glossary.html#term-borrowed-reference)를 반환한다.[^lwn1078380-p02-borrowed] GIL이 객체가 바뀌지 않도록 보장하는 상황이라면, 예컨대 코드가 자신의 (빌린 것이 아닌) 참조를 갖기 위해 참조 횟수를 증가시키는 동안에는 문제가 되지 않는다. GIL이 없으면 객체는 언제든 바뀔 수 있다. 실제로 문제가 자주 일어나지는 않겠지만, 참조 횟수를 바꾸는 코드는 올바름(correctness)을 위해 GIL에 의존하고 있다.

이런 종류의 문제를 피하려면 잠금을 사용할 수 있지만, 잠금은 비용이 크고 곳곳에서 사용해야 한다. Python에는 리스트, 딕셔너리, 튜플, 코드 객체 등 “어디에나 있으며, 전체 프로세스가 이것들로 가득 차 있다”. 참조 카운팅을 잠금으로 대체하는 것은 “극도로 비용이 클” 것이다. PyDict\_GetItem()에 잠금을 사용하게 만드는 것만으로도 비용이 크며, 스레드를 사용하지 않는 Python 코드에도 그 잠금들이 모두 존재하게 된다. “여러 스레드가 동시에 실행되는 것을 그만큼 빠르게 만들기 위해 인터프리터를 50% 느리게 만들 수는 없습니다.” 특히 “그럴 수 없기 때문에” 여러 스레드로 Python 워크로드를 실행하는 사용자가 아직 없다는 점을 고려하면 더욱 그렇다.

#### 역사

GIL을 제거하려는 노력은 [Greg Stein의 1996년 Python 1.4용 패치](https://dabeaz.blogspot.com/2011/08/inside-look-at-gil-removal-patch-of.html)까지 거슬러 올라간다. 그 패치는 참조 카운팅을 세밀한 잠금(fine-grained lock)으로 대체하고, CPython의 여러 부분에 다른 잠금들을 추가했다. 하지만 단일 스레드 성능 손실을 받아들일 수 없었기 때문에 성공하지 못했다.

2013년에 Trent Nelson은 [PyParellel](https://pyparallel.org/)을 시작했다. 이는 운영체제 스레드를 사용하지 않는 완전히 다른 모델이었다. Python 안에서 여러 작업을 수행할 스레드를 만들기 위한 별도 API를 갖고 있었고, 그 스레드들이 끝날 때까지 참조 카운팅과 가비지 컬렉션(garbage collection)을 지연시켰다. 이미 운영체제 스레드를 사용하는 어떤 것과도 함께 동작하지 않았기 때문에 일반적인 해법은 아니었다.

2015년에 Larry Hastings는 [Gilectomy 프로젝트](https://lwn.net/Articles/689548/)를 시작했고, 그는 이를 [몇 년 동안](https://lwn.net/Articles/754577/) [작업했다](https://lwn.net/Articles/723514/). 그는 특히 참조 횟수를 다루는 새로운 접근법을 살펴보았고, GIL을 언어에서 제거하려면 그 밖에 무엇이 필요할지도 조사했다. Wouters에 따르면 그가 탐색하고 싶어 했던 다른 길들이 몇 가지 있었지만, 그는 “거의 포기했다”.

몇 년 전, “Meta에서 일하는 Sam Gross는 자신이 그 문제들의 대부분을 해결할 *수 있다*고 생각했고 실제로 그렇게 했다.” 그는 [CPython 3.9의 No-GIL 포크](https://lwn.net/Articles/872869/)에서 이를 해냈다. “그것이 지금 우리가 가진 것과 대체로 같습니다.” Gross는 [PEP 703](https://peps.python.org/pep-0703/)(“Making the Global Interpreter Lock Optional in CPython”)을 작성했는데, 이는 자유 스레딩을 지원하고 GIL을 제거하기 위해 CPython에 필요한 여러 기법을 설명했다.

예를 들어 이제 Python의 객체는 [“소유자(owner)” 스레드](https://peps.python.org/pep-0703/#biased-reference-counting)를 가진다. 이는 단순히 해당 스레드가 객체와 그 참조 횟수에 빠르게 접근할 수 있다는 뜻이다. 다른 스레드도 여전히 객체에 접근할 수 있지만, 별도의 공유 참조 횟수에 원자적 연산을 사용하는 더 느린 경로를 거쳐야 한다. 또한 [일부 참조 횟수 연산은 지연되어](https://peps.python.org/pep-0703/#deferred-reference-counting) 가비지 컬렉션 시점까지 미뤄졌다가 여러 연산이 한꺼번에 처리된다. 그러나 이는 의미론적 변화(semantic change)를 구성한다. 참조 횟수가 0에 도달했을 때 즉시 회수되었을 객체가 다음 가비지 컬렉션 실행까지 지연되기 때문이다. “작은 차이이고, 아마 받아들일 만합니다.”

[list와 dictionary 멤버에 접근할 때](https://peps.python.org/pep-0703/#optimistic-avoiding-locking-in-dict-and-list-accesses)도 추측적 참조 횟수 연산(speculative reference-count operation)이 있다. 항목 객체의 참조 횟수를 증가시킨 다음, CPython은 그것이 여전히 리스트나 딕셔너리에 있는지 확인한다. 그는 그것이 “정말 이상하게 들리며”, 객체가 이미 파괴되었을 수도 있으므로 어쩌면 위험해 보인다고 말했다. 보호 장치들이 있으며 통제된 상황에서 수행된다. 일반적인 용도로 쓰는 것이 아니라 “인터프리터 자체 안의 마법”이다.

“정지 상태 기반 회수(Quiescent-state-based reclamation)”는 객체가 다른 스레드 밑에서 갑자기 사라지지 않도록 보장하는 데 사용된다.[^lwn1078380-p02-qsbr] 리스트와 딕셔너리가 해제될 때, 그 메모리는 즉시 재사용되지 않는다. 그래야 [다른 스레드가 여전히 객체의 참조 횟수에 접근할 수 있기](https://peps.python.org/pep-0703/#optimistic-dict-and-list-access-summary) 때문이다. 언어가 그렇게 해도 안전하다는 것을 알 때에만 메모리가 정리되며, 일반적으로는 가비지 컬렉션이 수행될 때가 그 시점이다. 그때 모든 스레드가 정지 상태(quiescent state)에 도달했기 때문이다.

[![[Thomas Wouters]](https://static.lwn.net/images/2026/pycon-wouters-sm.png "Thomas Wouters")](https://lwn.net/Articles/1078543/)

세밀한 잠금도 추가되었다. “어떤 것들은 그냥 잠금이 필요하다.” 기존 가비지 컬렉터가 복잡했기 때문에 [새로운 가비지 컬렉터](https://peps.python.org/pep-0703/#garbage-collection-cycle-collection)가 추가되었다. 메모리 할당자는 [mimalloc으로 전환되었는데](https://peps.python.org/pep-0703/#memory-management), 이는 스레드 안전(thread-safe) 할당자이며 정지 상태 기반 회수에 필요한 훅(hook)도 제공한다.

이 모든 것을 종합하면 잠금 없는(lock-free) 리스트, 딕셔너리, 그리고 “다른 중요한 타입들”이 만들어진다고 그는 말했다. 이는 특히 소유 스레드에게 접근을 빠르게 해 주며, 다른 스레드에서의 접근도 여전히 “꽤 빠르다”. 객체의 타입을 바꾸는 것과 같은 작업을 수행할 때는 그것이 올바르게 이루어지도록 모든 스레드를 멈출 필요가 있다. “우리는 세상을 멈추고, 변경을 한 다음, 모두를 다시 실행합니다.”

[^lwn1078380-p02-gil]: 전역 인터프리터 락(GIL)은 CPython에서 한 번에 하나의 스레드만 Python 바이트코드를 실행하도록 제한해 내부 자료구조를 단순하게 보호하는 잠금이다.
[^lwn1078380-p02-borrowed]: 빌린 참조(borrowed reference)는 C API 호출자가 객체의 소유권을 얻지 않는 참조다. 호출자가 오래 보관하려면 보통 참조 횟수를 증가시켜 자신의 참조를 만들어야 한다.
[^lwn1078380-p02-qsbr]: 정지 상태 기반 회수(QSBR)는 모든 참여 스레드가 안전한 지점에 도달했음을 확인한 뒤에야 메모리를 실제로 재사용하는 동시성 메모리 회수 기법이다.

객체별 잠금(per-object locks)도 있어 [임계 구역(critical sections)](https://peps.python.org/pep-0703/#python-critical-sections)을 제공한다.[^lwn1078380-p03-critical] 이것들은 일반적인 잠금이 아니라, “교착 상태(deadlock)가 없는 특수한 종류의 잠금”이다. 그는 잠금을 다뤄본 사람이라면 그 표현이 모순어법처럼 느껴질 것이라고 지적했다. 하지만 CPython에서는 임계 구역 안에서 GIL의 의미론이 재현되기 때문에 동작한다. GIL을 획득하고 해제하던 기존 호출은 어떤 스레드가 작업 중에 블로킹되지 않는지를 추적하는 용도로 재활용되어, “stop the world” 작업이 완료될 수 있게 한다. 블로킹하려는 스레드는 이미 그 전에 GIL을 해제하고 있어야 한다.

최종 결과는 “자유 스레딩(free-threaded) Python에서 스레드 의미론은 GIL이 있는 Python과 *거의* 같다”는 것이다. 이는 “무시무시한 메모리 모델, 원자적 연산(atomics), 메모리 순서(memory-order) 문제, 메모리 펜스(memory fences) 같은 것들이 없고, 그 어느 것도 중요하지 않으며, Python은 그저 Python처럼 동작한다”는 상황을 만들어 준다.

Wouters는 “free threaded”라는 용어가 Gross가 아니라 운영 위원회(steering council)에서 나온 것이라고 말했다. 이전에는 “No-GIL” Python이라고 불렸지만, 위원회는 사람들이 결국 “No No-GIL Python”에 대해 이야기하게 되는 상황을 원하지 않았다. Wouters는 “free threading”이 업계 용어가 아니라, 단순히 GIL이 제거되었음을 뜻하는 Python 용어라고 말했다. 또한 이는 어느 정도 잘못된 명칭이기도 한데, Python의 자유 스레딩은 C나 C++에서처럼 제한 없이 메모리 곳곳에 쓸 수 있는 경우보다 훨씬 덜 자유롭고, 심지어 그 점에서는 더 나은 Rust조차도 Python보다 더 자유로운 스레딩을 제공하기 때문이다.

#### 상태

2024년 10월에 릴리스된 Python 3.13에는 실험적 자유 스레딩 지원이 들어 있었다. 그것은 “상대적으로 느려서, 단일 스레드 작업부하(single-threaded workloads)에서 20~40%의 성능 저하”가 있었다. 스레드 안전성(thread-safety) 문제가 있었고, 스레드를 더 추가하면 오히려 더 느려질 수 있는 확장성 문제도 있었다. “하지만 그것은 이 방식이 동작한다는 것을 증명했다.”

2025년 10월의 3.14에서는 자유 스레딩 Python이 “훨씬 더 안전해졌고” “훨씬 더 빨라졌으며”, 단일 스레드 작업부하에서 성능 저하는 0~10% 수준이었다. “개인적으로는 아직도 우리가 0% 성능 저하에 도달했다는 사실이 충격적입니다. 그것은 Arm 하드웨어에서의 결과인데, 거기에는 어떤 마법이 일어나고 있습니다. 그게 무엇인지는 모르겠지만, 정말 놀랍습니다.” Linux에서 GCC를 사용할 때는 보통 약 5% 수준이지만, 특히 오래된 컴파일러에서는 10%까지 올라갈 수 있다.

그는 자신이 공동 저자로 참여한 [PEP 779](https://peps.python.org/pep-0779/)(“자유 스레딩 Python의 지원 상태 기준”)를 3.14용으로 승인한 운영 위원회의 일원은 아니었다. 이 PEP는 자유 스레딩 빌드에서 “실험적”이라는 꼬리표를 제거하고 그것을 언어의 지원 기능으로 전환하기 위해 무엇이 필요한지를 설명했다. [PEP 승인 발표](https://discuss.python.org/t/pep-779-criteria-for-supported-status-for-free-threaded-python/84319/123)는 실험적 지정을 제거하고, 앞으로 자유 스레딩 개발자들이 무엇을 해야 하는지 설명했다.

올해 10월에 나올 Python 3.15에는 인터프리터의 GIL 버전과 자유 스레딩 버전 모두를 위한 단일하고 안정적인 ABI가 포함될 예정이다.[^lwn1078380-p03-abi] 이는 확장 개발자들이 코드를 한 번만 빌드하면, GIL을 사용하든 자유 스레딩을 사용하든 Python 3.15 이상에서 그 코드가 로드되어 실행된다는 뜻이다. 3.15에는 자유 스레딩을 위한 많은 확장성 개선도 들어올 예정이다.

확장 개발자들은 자유 스레딩 지원을 추가해야 한다는 전망에 위축될 수 있지만, Quansight의 개발자들은 [Python 자유 스레딩 가이드](https://py-free-threading.github.io/)를 마련해 두었다. 여기에는 [확장을 자유 스레딩 인터프리터로 포팅하는 방법](https://py-free-threading.github.io/porting-extensions/)에 대한 정보가 포함되어 있다. “그렇게 어렵지 않습니다.”

C 전역 변수들은 GIL이 더 이상 보호해 주지 않기 때문에—애초에 실제로 보호해 주고 있었다면 말이지만—보호되어야 한다. “그냥 C 전역 변수를 없애버릴 수도 있습니다. 나쁜 생각이 아닙니다.” 임계 구역은 Python 객체 안의 가변 데이터(mutable data)를 보호하는 데 사용할 수 있다. 많은 스레드가 한 객체에 동시에 접근할 예정이라면 다른 종류의 잠금이 바람직할 수도 있지만, 그것은 나중의 최적화로 남겨둘 수 있다.

또한 확장 모듈은 자신들이 자유 스레딩을 지원한다고 선언해야 한다. 이를 수행하는 방법은 여러 가지가 있으며, “가이드를 확인하라”. 확장 안에 있는 기존의 GIL 관련 호출을 제거하지 않는 것이 중요하다. 자유 스레딩 인터프리터가 그것들을 사용하기 때문이다. Wouters는 다중 스레드 테스트를 일부 추가하는 것도 좋은 생각이라고 말했다. “스레딩 버그가 있다면, 더 이상 GIL이 우연히 어느 정도 보호해 주지 않기 때문에 그 버그들이 드러날 것입니다.”

일반 Python 코드의 경우에는 해야 할 일이 많지 않거나, 아예 없을 가능성이 크다. 다만 코드에 이미 다중 스레딩 버그가 있다면 예외인데, 자유 스레딩 버전에서는 그런 버그가 발생할 가능성이 더 커지기 때문이다. 다시 말해, 간단한 테스트를 조금 추가하는 것만으로도 그런 버그를 “훨씬 더 빨리 드러나게” 할 가능성이 크다. 자유 스레딩 인터프리터는 그런 종류의 버그를 찾기 쉽게 만든다.

하지만 자유 스레딩은 Python에서 스레드를 사용하는 일을 더 매력적으로 만들 것이고, 그 역시 기존 코드의 버그를 드러낼 수 있다. Python 코드가 잘 확장되게 만들려면 더 광범위한 변경이 필요할 수도 있다. 많은 스레드가 같은 객체에 접근하는 것은 Python이 직접 해결할 수 없는 문제다. “스레드 간에 객체를 공유하는 것은 성능 측면에서 여전히 문제가 됩니다.” [ft\_utils](https://github.com/facebookincubator/ft_utils#welcome-to-ft_utils) 패키지처럼 몇 가지 가능한 해결책이 있는데, 이 패키지에는 확장 가능한 컨테이너 타입들이 들어 있다.

#### 미래

Wouters는 자유 스레딩 Python에는 아직 할 일이 남아 있다고 말했다. 인터프리터와 이미 자유 스레딩을 지원하는 서드파티 패키지에서 성능 및 확장성 개선이 필요하다. 그 밖에도 더 많은 서드파티 패키지에서 자유 스레딩을 지원하도록 하는 작업이 필요하지만, 그것이 자유 스레딩 Python을 성공으로 간주하기 위한 필수 조건은 아니다. [상위 360개 바이너리 휠(binary wheels)의 50% 이상](https://hugovk.dev/free-threaded-wheels/)이 [Python Package Index](https://pypi.org/)(PyPI)에서 이를 지원하고 있으므로 “이미 성공”이라는 것이다. 그 공로의 상당 부분은 Meta와 Quansight에 돌아간다. 이들은 그 지원 작업을 했을 뿐 아니라 패키지 작성자들을 교육하는 데도 도움을 주었다. 물론 그 노력에는 다른 기여자들도 있었다고 그는 말했다.

그는 운영 위원회에 속해 있기는 하지만, “이 말을 어떤 권위로 하는 것은 전혀 아닙니다”라고 했다. 그는 자유 스레딩 버전이 향후 릴리스에서 기본 Python이 될 것이라고 믿고 있다. 그는 Python 프로젝트가 Red Hat과 Debian 같은 Linux 배포판, 그리고 Meta 같은 대기업들보다 뒤처질 것이라고 의심한다. 이들은 이미 자유 스레딩을 기본값으로 활성화해 두었을 것이다. 그의 예측은 그것이 3.16(2027년 10월 예정) 이후, 3.20(2031년 10월) 이전 어느 시점에 일어나리라는 것이다.

그 이후 어느 시점에는 GIL 기반 버전이 완전히 사라질 것이라고 그는 생각한다. “이것은 먼 미래의 일입니다. 제가 예상하기로는 다음 10년대의 일입니다. 하지만, 알다시피, 제가 놀라게 될 수도 있겠죠.” 이것으로 그의 발표는 끝났지만, 질문을 받을 시간이 몇 분 남아 있었다.

그 질문 중 하나는 자유 스레딩을 지원하는 모듈과 지원하지 않는 모듈을 섞어 쓰는 문제에 관한 것이었다. Wouters는 자유 스레딩을 지원하지 않는 모듈은 현재 인터프리터가 경고를 내고 GIL을 다시 활성화하게 만든다고 말했다. GIL을 항상 비활성화하는 플래그로 이를 우회할 수는 있지만, “그것은 불장난이므로 아마 테스트용으로만 하고 싶을 것입니다.”

Hastings는 “Larry Hastings가 왜 Gilectomy를 포기했는지”를 보충 설명하려고 앞으로 나섰고, 이는 폭넓은 웃음을 자아냈다. 그는 Gross가 결국 택한 길과 어느 정도 비슷하다고도 할 수 있는 기법들을 사용하려고 했지만, Hastings가 해결 불가능하다고 판단한 엄청난 확장성 및 성능 문제에 부딪혔다. 그는 Hastings가 Gilectomy 작업을 하던 당시에는 자유 스레딩 인터프리터에서 참조 카운트(reference counts)에 사용된 기법이 “아직 발명되지 않았다”고 Gross가 친절히 알려주었다고 말했다—그러자 또 웃음이 터졌다. Wouters는 그 일화를 발표에 넣을까 생각했지만, Hastings가 그것을 스스로 발명할 만큼 똑똑하지 않았다는 뜻으로 비칠까 봐 그러지 않았다고 덧붙이며 마지막 말을 했다.

[ PyCon US 참석을 위해 Long Beach로 가는 제 여행에 도움을 준 LWN의 여행 후원사 Linux Foundation에 감사드립니다. ]

[댓글(3개 게시됨)](https://lwn.net/Articles/1078367/#Comments)

[^lwn1078380-p03-critical]: 임계 구역(critical section)은 동시에 실행되는 스레드가 공유 데이터에 접근할 때 경쟁 조건(race condition)을 피하려고 한 번에 제한된 실행 흐름만 들어가게 하는 코드 구간이다.
[^lwn1078380-p03-abi]: ABI(Application Binary Interface)는 컴파일된 확장 모듈과 인터프리터 사이의 바이너리 수준 약속으로, 호출 규약·자료 구조 배치·심볼 호환성 등을 포함한다.

### [AURpocalypse now: 최근 AUR 공격 살펴보기](https://lwn.net/Articles/1077619/)

글쓴이: **Joe Brockmeier**  
2026년 6월 19일

#### 요약

- Arch User Repository(AUR)가 고아(orphaned) 패키지를 노린 지속적인 악성 업데이트 공격을 받았다.
- 공격자는 새 계정을 만들어 패키지를 인수한 뒤 npm 또는 Bun을 통해 악성 패키지를 설치하도록 PKGBUILD를 바꿨다.
- AUR의 개방적인 협업 모델은 편리하지만, 공식 검토 없이 패키지 생성과 인수가 가능해 공급망 공격에 취약하다.
- Arch 프로젝트는 대응 과정에서 신규 사용자 등록을 중단했지만, 장기적인 방어책은 아직 분명하지 않다.

[Arch User Repository](https://aur.archlinux.org/)(AUR)는 최근 지속적인 공격을 받았다. 공격자 또는 공격자들은 일련의 새 계정을 만든 뒤, 이를 이용해 고아(orphaned) 패키지를 인수하고 사용자의 시스템에 악성코드를 설치하는 악성 업데이트를 밀어 넣었다.[^lwn1078380-p04-1] 이 공격으로 얼마나 많은 사용자가 침해되었는지는 분명하지 않지만, 유지관리자들은 며칠 동안 새로 침해된 각 패키지에 대응하느라 두더지 잡기(Whac-A-Mole)를 해야 했다. 프로젝트는 현재 [AUR의 신규 사용자 등록을 꺼 둔 상태](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/4JRS73YVTE7JUYHHE3ZDUIHXYHXZ3YQQ/)지만, 장기적인 대응이 무엇이 될지, 또는 기존 협업 모델을 크게 바꾸지 않고 AUR을 안전하게 만들 수 있을지는 불분명하다.

#### AUR이 특히 취약한 이유

Arch Linux는 core와 extras 같은 소프트웨어 [공식 저장소](https://wiki.archlinux.org/title/Official_repositories)를 제공하며, 이는 [Arch Linux Developers](https://archlinux.org/people/developers/)와 [Package Maintainers](https://wiki.archlinux.org/title/Package_Maintainers)가 감독한다(계층 구조에 대해서는 [공식 기여자](https://wiki.archlinux.org/title/DeveloperWiki:Governance_And_Decision_Making#Categories_of_official_contributors) 범주를 참고하라). 이 패키지들은 유지관리자의 검토를 거치며, [pacman](https://wiki.archlinux.org/title/Pacman) 패키지 관리자를 통해 바이너리 형식으로 내려받을 수 있다.

반면 AUR은 아직 공식 저장소에 들어가지 않았고 앞으로도 들어가지 않을 수 있는 소프트웨어를 위한 저장소다. Pacman은 AUR 저장소를 직접 사용하지 않으므로, 사용자는 보통 AUR에서 소프트웨어를 검색하고, [PKGBUILD](https://wiki.archlinux.org/title/PKGBUILD) 파일을 내려받고, 의존성을 해결하며, 소프트웨어를 컴파일·설치·업데이트하기 위해 [paru](https://github.com/morganamilo/paru#paru)나 [yay](https://jguer.github.io/yay/) 같은 별도의 [AUR helper](https://wiki.archlinux.org/title/AUR_helpers) 애플리케이션을 사용한다.[^lwn1078380-p04-2]

AUR은 Arch의 Package Maintainers가 관리한다. 예를 들어 이들은 패키지를 고아로 만들거나 삭제해 달라는 요청에 대응하고, [패키지를 AUR에서 공식 extras 저장소로 옮길](https://wiki.archlinux.org/title/Package_Maintainer_guidelines#Moving_packages_from_the_AUR_to_extra) 수도 있다. 하지만 패키지가 AUR에 들어가거나 업데이트되는 과정에는 공식적인 검토 절차가 없다. AUR에는 소스에서 소프트웨어를 컴파일하는 데 필요한 사용자 기여 PKGBUILD 파일이 들어 있으며, 바이너리 빌드는 제공되지 않는다. 현재 AUR에는 107,000개가 넘는 패키지가 있고, 그중 현재 [고아 상태](https://wiki.archlinux.org/title/AUR_submission_guidelines#Orphan)로 누구나 가져갈 수 있는 패키지가 [거의 14,000개](https://aur.archlinux.org/packages?O=0&SeB=nd&K=&outdated=&SB=p&SO=d&PP=50&submit=Orphans)에 이른다.

AUR 사용자 등록은 보통 가입하려는 누구에게나 활짝 열려 있으며, 현재 등록 사용자는 141,000명을 넘는다. AUR에 등록된 사용자 계정이 있는 사람은 누구나 고아 패키지를 인수하고 변경할 수 있다. 사용자가 [새 패키지를 게시](https://wiki.archlinux.org/title/AUR_submission_guidelines#Publishing_new_package_content)하거나 고아 패키지를 인수하려 할 때 거치는 검토나 심사 절차는 없다. 등록 사용자는 고아 패키지 페이지에서 "Adopt Package"를 클릭하기만 하면 자동으로 패키지 소유권을 부여받는다.

#### 자기 책임으로 사용하기

Arch 사용자는 AUR의 패키지를 다룰 때 주의를 기울여야 한다. 이들은 AUR PKGBUILD 파일이 "완전히 비공식적이며 철저한 검토를 거치지 않았다. 제공된 파일의 사용은 전적으로 자신의 책임"이라는 경고를 받는다. 이론적으로 사용자는 소프트웨어를 빌드하거나 설치하기 전에 PKGBUILD 파일을 검토할 것이다. 하지만 실제로, 특히 이미 설치한 패키지를 업데이트하는 경우에는 그럴 가능성이 낮다.

Arch Linux는 AUR 패키지에 대한 빌드를 제공하지 않지만, 다른 위치에서 미리 빌드된 바이너리를 내려받는 데 쓰이는 "-bin" PKGBUILD 파일은 허용한다. 예를 들어 사용자는 Firefox의 포크인 [LibreWolf](https://librewolf.net/)를 소스에서 빌드하지 않고 AUR의 [librewolf-bin](https://aur.archlinux.org/packages/librewolf-bin) 패키지로 설치할 수 있다. 이는 빌드 시간이 긴 오픈소스 소프트웨어에 편리할 뿐 아니라, AUR 정책은 독점 소프트웨어도 허용하는데, 이런 소프트웨어는 소스 형태로 배포될 가능성이 낮다. 물론 이는 사용자가 AUR 패키지 유지관리자가 바이너리에 악성 요소를 넣지 않았다고 신뢰해야 한다는 뜻이기도 하다.

Arch만 "자기 책임으로 사용"하는, 검토되지 않은 사용자 제출 콘텐츠를 제공하는 서비스를 가진 배포판은 아니다. Fedora에는 [Copr](https://copr.fedorainfracloud.org/coprs/)가 있고, openSUSE 프로젝트에는 [Open Build Service](https://openbuildservice.org/)(OBS)가 있으며, Ubuntu에는 [Personal Package Archives](https://launchpad.net/ubuntu/+ppas)(PPAs)가 있다. 이들 서비스는 각각 어떤 사람이든 별도의 검토 절차 없이 가입해 배포판의 다른 사용자가 내려받을 수 있는 패키지를 빌드할 수 있게 한다.

그러나 이들 서비스와 AUR 사이에는 중요한 차이가 있다. 이 서비스들은 공식 배포판 패키지에 쓰이는 것과 비슷한 빌드 환경을 제공하며, 미리 빌드된 바이너리나 독점 소프트웨어를 허용하지 않는다. Copr, OBS, PPA의 모델은 사용자가 자기 사용자 네임스페이스 아래에 프로젝트를 만드는 방식이다. 사용자는 이들 서비스 중 하나에서 각 저장소를 별도로 추가해야 한다.

예를 들어 [niri](https://lwn.net/Articles/1025866/) 제작자 Ivan Molodetskikh는 타일링 Wayland 컴포지터를 실행하려는 Fedora 사용자를 위해 [Copr 저장소](https://copr.fedorainfracloud.org/coprs/yalter/niri/)를 유지관리한다. Copr에서 niri를 설치하려면 사용자가 해당 저장소를 명시적으로 활성화해야 한다. 다른 Copr 사용자가 자기 네임스페이스 아래에 비슷한 프로젝트를 만드는 것은 가능하지만, Molodetskikh의 인증 정보가 침해되지 않는 한 다른 사용자가 그의 저장소를 탈취하는 것은 불가능하다. 공격을 시도하는 사람은 Copr에 악성 포크를 만들고 Fedora 사용자를 유인해 그 패키지 저장소를 시스템에 추가하게 할 수는 있지만, 이미 추가한 사용자들을 침해하기 위해 단순히 고아 Copr 저장소를 주워 갈 수는 없다.

반면 AUR은 소유권에 관해 훨씬 느슨하다. PKGBUILD 파일은 모두 AUR 네임스페이스 아래에서 유지관리된다. [규칙](https://wiki.archlinux.org/title/AUR_submission_guidelines#Rules_of_submission)에 따르면 새 유지관리자가 AUR 패키지를 넘겨받을 때는 자신의 정보를 유지관리자로 추가한 뒤 이전 유지관리자들을 기여자로 나열해야 한다. 그러나 이는 신뢰에 맡겨져 있으며, 현재 공격에서 보았듯 쉽게 악용될 수 있다.

#### 공격

AUR은 수년 동안 고아 패키지를 이용한 여러 공격을 받아 왔다. 2018년에는 [세 패키지가 변경](https://sensorstechforum.com/arch-linux-aur-repository-found-contain-malware/)되어 데이터 수집 악성코드를 포함하게 되었다. 지난해에는 두 차례 공격이 있었다. 7월 18일 Quentin Michaud는 웹 브라우저용 "-bin" 패키지 세 개가 원격 접근 트로이목마(remote-access trojan, RAT) 악성코드와 함께 업로드되었다는 [권고문](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/7EZTJXLIAQLARQNTMEW2HBWZYE626IFJ/)을 보냈다. 7월 말에는 또 다른 [시도](https://linuxiac.com/arch-aur-under-fire-once-more-as-malware-resurfaces/)가 있었고, 이는 빠르게 탐지되었다. "google-chrome-stable" 패키지가 또 다른 RAT와 함께 업로드된 것이다.

각 공격은 규모가 작았다. 가장 최근 공격은 그렇지 않았다. 이 공격은 5월 27일 시작된 것으로 보이며(그리고 그날 탐지되었다), Fabio Loli는 "[plex-media-player](https://aur.archlinux.org/packages/plex-media-player)" 패키지가 악성 npm 패키지 "[crypto-javascript](https://socket.dev/npm/package/crypto-javascript/overview/4.3.6)"를 설치하도록 업데이트되었다고 [보고했다](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/BAWHLX4VFTT7JMQTTYTMG2URQFEZJV7Y/). 해당 PKGBUILD는 고아가 된 뒤 완전히 새 계정에 의해 인수되었다. 비슷한 이름의 새 패키지 여러 개도 새 계정들에 의해 업로드되었으며, 모두 사용자를 유인해 악성 npm 패키지를 설치하게 하려는 같은 시도를 담고 있었다.

6월 11일 Mark Wagie는 새 유지관리자가 "[gnome-randr-rust](https://aur.archlinux.org/packages/gnome-randr-rust)" 패키지를 인수하고 [PKGBUILD 파일을 변경](https://aur.archlinux.org/cgit/aur.git/commit/?h=gnome-randr-rust&id=da9f4cf2d470bd603968ef605736285a2e0c8880)해 npm 의존성을 추가한 다음, 이를 이용해 "[atomic-lockfile](https://socket.dev/npm/package/atomic-lockfile)"이라는 악성 패키지를 설치하게 했다고 [보고했다](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/L2JXQNYBGWOQQQXDEPEAICBHKFEFANUC/). 공격자는 PKGBUILD의 Contributor 스탠자(stanza)도 바꾸어 이전 유지관리자의 이메일 주소를 교체했지만, 이름은 그대로 두었다. Sonatype 블로그에는 이 패키지에 대한 [분석](https://www.sonatype.com/blog/atomic-arch-npm-campaign-adds-malicious-dependency)이 있다. 이 패키지에는 GitHub 인증 정보, SSH 정보, 브라우저 쿠키, Slack·Discord 같은 채팅 애플리케이션의 데이터 저장소 등 사용자 기계에서 광범위한 정보를 유출하려 시도하는 eBPF 프로그램이 포함되어 있었다.

공격자(들)는 지난해 공격처럼 일부 선별된 패키지가 아니라 [수백 개의 고아 패키지](https://md.archlinux.org/s/SxbqukK6IA)를 노렸다. Arch의 Package Maintainers 중 한 명인 Jonathan Grotelüschen은 6월 11일 사람들이 침해된 패키지를 보고할 수 있도록 [스레드](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/thread/FGXPCB3ZVCJIV7FX323SBAX2JHYB7ZS4/#7QNBBIEMDZRVCITJ4P2QPKCVYIQZIEQ7)를 시작했다.

필자는 Grotelüschen에게 이메일로 연락해 공격에 대해 물었다. 그는 공격자가 계정을 만들어 몇 개의 패키지를 인수한 뒤 비슷한 방식으로 침해하고 있었다고 말했다. 신규 사용자 등록은 6월 11일 중단되었고, 이후 프로젝트가 공격자의 대량 계정 등록을 막기 위해 [Anubis](https://lwn.net/Articles/1028558/)를 추가한 뒤 다시 활성화되었다. 그러나 이는 효과가 없었고, 등록은 6월 12일 다시 비활성화되었다.

6월 13일에는 등록이 중단되기 전에 만들어진 네 계정으로 또 다른 공격 물결이 있었다. 공격자는 악성 패키지를 설치하려고 npm 대신 [Bun](https://bun.com/docs) 패키지 관리자를 사용하는 방식으로 전환했고, 이후 "npm"이나 "bun" 문자열이 있는지 PKGBUILD 파일을 스캔하도록 만든 스크립트를 피하기 위해 "bun install" 명령을 난독화하려 했다.

```
    # post_install() {
    #   $'\x63'"d" "/"'t'"m"'p' && "b"'u''n' 'a'"d"'d' 
    $'\141\x6e''s'"i""-"$'\143''o''l''o''r'$'\x73' 
    'n'"e"'x'"t""f"'i''l''e''-''j''s'
    # }
```

난독화 시도는 설치 명령을 찾는 스크립트를 피할 수 있었겠지만, 실제로 PKGBUILD 파일을 검토하는 사용자는 그것을 수상하게 여겼기를 바랄 수밖에 없다.

#### 대응

전체적으로 1,500개가 넘는 패키지가 영향을 받은 것으로 알려져 있다. Grotelüschen은 새로 만들어진 패키지는 약 20개뿐이고, 나머지는 공격자가 인수한 고아 패키지였다고 말했다. 이 글을 쓰는 시점에도 등록은 여전히 비활성화되어 있다. Grotelüschen은 유지관리자들이 "우리가 할 수 있는 한 AUR을 깨끗하게 유지하지만, AUR의 규모를 고려하면 절대적으로 모든 것을 잡아낼 가능성은 매우 작다"고 말했다.

[^lwn1078380-p04-1]: AUR의 "고아" 패키지는 현재 책임지는 유지관리자가 없어 다른 등록 사용자가 인수할 수 있는 패키지를 뜻한다.
[^lwn1078380-p04-2]: AUR helper는 pacman 자체가 직접 처리하지 않는 AUR 검색, PKGBUILD 다운로드, 빌드, 설치, 업데이트 절차를 자동화하는 보조 도구다.

그는 이어 "공격은 사용자 관리 콘텐츠에만 영향을 미쳤으며,
공식 저장소는 영향을 받지 않았다"고 덧붙였다. 게다가 AUR
패키지에는 "자신의 책임하에 사용"한다는 면책 문구가 붙어 있다. 그로텔뤼셴은
사용자가 PKGBUILD를 읽고 그 콘텐츠를 사용해도 안전한지 스스로 판단할
책임이 있다고 말했다.[^lwn1078380-p05-pkgbuild]

하지만 그 정책은 현실의 사용자 관행과는 맞지 않는 듯하다. 많은 사용자가
AUR을 그저 또 하나의 패키지 저장소로 취급하고, 패키지를 설치하거나
업데이트하기 전에 PKGBUILD 파일을 읽는 일은 거의 없을 가능성이 크다.
신중하고 보안 의식이 있는 사람들조차 PKGBUILD의 모든 업데이트를 하나하나
검토할 가능성은 낮으며, 공격자는 단 한 번만 운이 좋으면 된다. AUR의 정책은
오늘날의 보안 위협에 충분하지 않을 수 있다.

그는 프로젝트가 새 계정을 만들기 더 어렵게 하는 작업을 하고 있지만,
"AUR이 실명이나 정부 발급 신분증 확인까지 요구하지는 않을 것"이라고 말했다.
그는 비슷한 공격을 막거나 탐지할 방법을 두고 AUR 메일링 리스트에서 논의가
진행 중이지만, 그 아이디어들은 Arch 관리자와 개발자가 아니라 사용자들에게서
나오고 있다고 언급했다.

2026년이므로, 여러 아이디어는 당연히 LLM 사용을 중심에 두고 있다. 예를 들어 Thomas
Stromberg는 "최근 공격과 위협 피드를 바탕으로 계속 재훈련되는 작은 로컬 결정론적
AI 모델"을 사용하는, 자신이 작업 중인 [Atomdrift](https://atomdrift.org/)라는 프로젝트를
사용하자는 [제안](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/ASQP7CC4EOMEG7GASDHJBZEINBEQKD65/)을 했다.
Andreas Reichel은 Claude, Codex, 또는 로컬 LLM을 사용할 수 있는
[aurscan](https://github.com/manticore-projects/aurscan#%EF%B8%8F-aurscan)이라는 비슷한 것을 만들었다고
[말했다](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/2RTSLW7AH3LB7DRV5VCMIPUHXZH2HBJJ/).

Lukas Grumlik은 고아 패키지를 처리하는 방식을 바꾸는 것이 도움이 될 수 있다고
[생각했다](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/YWSB5N3NQMDHQZDJN2FHX6J2HEA4BYYN/). 누구나 고아 패키지를 입양할 수 있게 하는 대신,
그는 그런 패키지를 잠그고 읽기 전용 상태로 설정하자고 제안했다. 사용자는 여전히
PKGBUILD를 내려받을 수 있지만, 입양에는 "왜 업데이트가 필요한지 설명하는
적절한 인수 요청"이 필요하게 되어, 봇이 대량으로 인수하는 일을 방해할 수 있다는 것이다.[^lwn1078380-p05-orphan]
Reichel은 그런 전략이 선의로 패키지를 고치려는 사람들의 의욕을 꺾겠지만,
"최소 2만 달러의 넉넉한 자금을 가진 국가 후원 범죄 조직"과 LLM 접근 권한은
막지 못할 것이라고 [답했다](https://lists.archlinux.org/archives/list/aur-general@lists.archlinux.org/message/CW67LA2WWRQD235AJPWPNNRS5QN3XZ2S/). 그 이유는 "내 LLM Agent에게는 필요한 시간이 모두 있고,
어차피 더 나은 설명을 써낼 것이기 때문"이라는 것이다.

또 다른 접근법은 AUR 자체가 아니라 AUR 유틸리티에 방어책을 구축하는 것이다.
Fidel Ramos는 고아가 되었다가 입양된 패키지를 설치하거나 업그레이드할 때 paru가
"요란한 경고"를 표시하자고 [제안했다](https://github.com/Morganamilo/paru/issues/1565#issue-4654851404). 그러려면 필요한 정보를
노출하기 위해 AUR의 [RPC 인터페이스](https://wiki.archlinux.org/title/Aurweb_RPC_interface#Query_types)를 변경해야 할 가능성이 크다.
Josephine Pfeiffer는 그 정보를 제공할 [머지 요청을 열었다](https://gitlab.archlinux.org/archlinux/aurweb/-/merge_requests/904).

yay의 관리자 Jo Guerreiro는 "npm install yyy" 검색, 시간 지연 업데이트, 또는
관리자 변경 추적 같은 방향의 변경을 요구하는 기능 요청이 많았다고
[말했다](https://jguer.space/blog/2026-06-15-yay-v13#aurpocalypse). 그러나 그는 다음 악성코드의 물결은 전술을 바꿔,
"모든 탐지 스캐닝을 '탐지되지 않을 때까지 반복'하는 생성 주기에 먹여 넣을 것"이라고
주장했다. yay가 공격자를 따라잡을 방법은 없었고, 그는 "보안 연극"을 피하고 싶어 했다.[^lwn1078380-p05-security-theater]

하지만 그는 yay의 최신 릴리스가 이제 PKGBUILD의 마지막 수정 시각을 표시하게 될 것이라고도
언급했다. 최근 수정이 있었다고 해서 사용자가 그 패키지를 신뢰하지 말아야 한다는 뜻은
아니지만, 더 주의하고 패키지를 검토해야 한다는 뜻이다. 오래된 패키지가 반드시 더
신뢰할 만한 것은 아니라고 그는 말했지만, "커뮤니티가 검토해 왔다는 점에서 더 확신할
이유"는 된다고 했다.

#### 밖에서는 조심하자

AUR에서 제출과 변경에 대한 개방 정책을 생각하면, 공격자가 이 정도 규모의 캠페인을
벌이기까지 이렇게 오래 걸렸다는 사실이 오히려 거의 놀랍다. 하지만 좋은 것은 영원하지
않으며, 이번 공격의 배후에 있는 사람이든 사람들이든 손을 떼기로 하더라도 모방범은
거의 틀림없이 나타날 것이다.

새 가입을 늦추는 것은 어느 정도 도움이 될 수 있지만, 악의적 행위자들은 PKGBUILD
파일을 검토하는 데 방심한 AUR 사용자들을 이용할 방법을 계속 찾을 것이다. AUR은
커뮤니티 협업의 인상적인 사례다. 신뢰 위에 구축된 어떤 시스템이든 악용하려는 사람이
항상 있다는 점은 안타까운 일이다.

[댓글 (32개 게시됨)](https://lwn.net/Articles/1077619/#Comments)

[^lwn1078380-p05-pkgbuild]: PKGBUILD는 Arch Linux 패키지를 빌드하는 데 필요한 메타데이터와 스크립트를 담은 파일이다.
[^lwn1078380-p05-orphan]: AUR에서 "고아" 패키지는 현재 관리자가 없는 패키지를 가리킨다.
[^lwn1078380-p05-security-theater]: "보안 연극"은 실제 위험을 크게 줄이지 못하면서 보안 조치처럼 보이는 행위를 뜻한다.

### [Fedora: 2FA를 할 것인가, 말 것인가, 그것이 문제로다](https://lwn.net/Articles/1078964/)

By **Joe Brockmeier**  
2026년 6월 24일

#### 요약

- Fedora는 의심되는 계정 탈취 사건 이후, 먼저 provenpackager 그룹에 약 3개월 안에 2FA를 요구하는 방안을 추진하고 있다.
- 2FA 의무화는 공급망 공격 위험을 줄일 수 있지만, Kerberos, GNOME online accounts, SSH 접근, 계정 복구 등 인프라와 사용성 문제가 남아 있다.
- 일부 기여자들은 “완벽히 준비될 때까지” 기다리면 개선이 지연된다며, 의무화를 먼저 해야 한다고 주장했다.
- FESCo는 2024년에 모든 패키저 대상 2FA 의무화를 완화해 provenpackager에게 “SHOULD” 수준으로 권고한 바 있다.
- 2026년 6월 논의에서는 provenpackager 114명 중 59명이 2FA를 활성화하지 않은 것으로 확인되었고, FESCo가 다시 정책 결정을 논의했다.

탈취된 계정은 공격자가 오픈소스 공급망에 악성코드를 몰래 끼워 넣는 가장 흔한 경로 중 하나다. 계정 탈취를 줄이는 한 가지 방법은 프로젝트가 이중 인증(2FA) 또는 다중 인증(MFA)을 요구하는 것이지만[^lwn1078380-p06-1], 말처럼 쉽지는 않다. 다만 Fedora는 현재 2FA 요구 사항을 곧 도입하는 방안을 논의하고 있다. 이는 [의심되는 계정 탈취](https://lwn.net/Articles/1077035/) 이후 AI 에이전트가 프로젝트에 여러 문제를 일으킨 사건에 뒤이은 것이다. 논의 끝에 Fedora는 먼저 "[provenpackager](https://docs.fedoraproject.org/en-US/fesco/Provenpackager_policy/)" 그룹의 패키저들에게 앞으로 약 3개월 안에 2FA를 활성화하도록 요구하는 것부터 시작할 예정이다.

#### "상당히 난처한 일"

Fedora는 5월에 그 에이전트의 활동을 알아차렸지만, 실제 접근 권한은 그보다 훨씬 이전부터 있었던 것으로 보인다. 얼마나 이전인지는 불분명하다. 그 기여 내용은 도움이 되지는 않았더라도 악의적이지는 않았던 것으로 보이지만, 또 다른 계정이 탈취될 경우 Fedora의 행운이 계속되리라고 기대할 이유는 없다. 6월 11일, Daniel P. Berrangé는 감독받지 않은 AI 에이전트에 관한 Fedora 개발 메일링 리스트 스레드에 [답장을 보냈다](https://lwn.net/ml/all/aip6Lcn5LV3xv3xR@redhat.com/). 그는 Fedora가 [XZ 백도어](https://lwn.net/Articles/967866/) 이후 2년 전 2FA 의무화를 검토했지만 아직 그렇게 하지 않았다고 지적했다. 이번 사건이 정말로 비밀번호 탈취로 인한 계정 장악 사례라면, "그렇다면 이는 Fedora로서는 상당히 난처한 상황"이라는 것이다.

물론 Fedora만 그런 것은 아니다. 커뮤니티 기여자를 두고 있는 다른 주요 Linux 배포판들 중 2FA 요구 사항을 둔 곳은 없으며, 이를 널리 지원하는 인프라도 없어 보인다. 내가 알기로 Debian의 협업 플랫폼 [Salsa](https://salsa.debian.org/)는 2FA 활성화를 지원하지 않으며, openSUSE의 [Open Build Service](https://build.opensuse.org/) (OBS)도 마찬가지다. [Launchpad](https://launchpad.net/) 협업 플랫폼에 사용되는 Ubuntu의 싱글 사인온 서비스는 사용자가 2FA를 활성화할 수 있게 하지만, Ubuntu 기여자에게 실제로 그렇게 하도록 요구하는지는 불분명하다. 다만 Debian과 Ubuntu는 업로드 전에 OpenPGP 서명으로 패키지에 서명할 것을 요구한다. (**업데이트**: Salsa는 분명히 2FA를 지원한다. 오류에 대해 사과한다.)

Michael Catanzaro는 Fedora 계정이 공격자에게 큰 가치가 있을 텐데도, 자신은 "기본적으로 Fedora를 \*제외한\* 모든 것"에 2FA를 사용한다고 [말했다](https://lwn.net/ml/all/464111a9-0d15-4ca2-8c24-0e4fcdf69c98@app.fastmail.com/). "Fedora 패키저 하나를 탈취하면 사용자에게 악성코드를 거의 직접 밀어 넣을 수 있다." 그러나 그는 Fedora가 아직 2FA를 도입할 준비가 되어 있지 않다고 주장했다.

그의 불만은 GNOME의 [online accounts](https://help.gnome.org/gnome-help/accounts.html) 기능이 Kerberos 티켓 갱신을 지원하기 전까지는 2FA를 쓰고 싶지 않다는 것이었다. Fedora는 [koji 빌드 시스템](https://koji.fedoraproject.org/koji/) 같은 일부 인프라에 [Kerberos 인증](https://fedoraproject.org/wiki/Infrastructure/Kerberos)을 사용한다. Catanzaro는 [후속 글](https://lwn.net/ml/all/ed688f75-5758-45e0-aa59-3b0c1c009ce0@app.fastmail.com)에서, 아마도 몇 년 전에 같은 이의를 제기했던 것이 꽤 확실하지만 그 이후 아무 진전도 없었다고 말했다. "안타깝게도 우리는 모두 평소 업무로 바쁘고, 아무도 이 문제들을 우선순위에 올리지 않았다. 그러니까, 기본적으로 오픈소스 프로젝트에서 일이 어떻게 돌아가는지에 대한 흔한 설명이다."

GNOME의 online accounts 기능에서 Kerberos 2FA를 지원하는 코드는 몇 년 전에 구현된 것으로 보이지만, 아직 받아들여지지 않았다. Alexander Bokovoy는 MFA Kerberos 인증을 활성화하기 위한 [merge request](https://gitlab.gnome.org/GNOME/gnome-online-accounts/-/merge_requests/250)를 제출했지만 GNOME 쪽에서 막혀 있다고 [말했다](https://lwn.net/ml/all/ajpCiHI43BuuSh4I@redhat.com). 이 기능은 2024년 6월에 제출되었고 이후 광범위하게 검토되었지만 아직 병합되지 않았다. Catanzaro는 그 요청의 상태가 여전히 "Draft"로 설정되어 있다고 [지적했다](https://lwn.net/ml/all/7e562b6d-c5cd-4ed7-9e38-909a3a6ac2e1@app.fastmail.com). 어쩌면 Bokovoy가 적절한 버튼을 클릭하면 곧 빛을 보게 될지도 모른다.

#### 먼저 의무화하라

Fedora가 2FA를 완전히 준비할 때까지 기다리는 것의 문제는, 2FA 사용이 의무가 아니기 때문에 아무도 2FA 개선을 우선시할 동기가 없다는 점이라고 Berrangé는 [말했다](https://lwn.net/ml/all/aiq_QUl_9V0XBvbk@redhat.com). 의무가 된다면 누군가는 남은 문제를 고치는 일을 우선순위에 올릴 것이다. "아니면 또 다른 Fedora 계정의 자격 증명이 탈취되어 Fedora의 평판에 상당한 피해를 주는 더 큰 손상을 일으킬 때까지 이 문제를 계속 무시할 수도 있다."

Stephen Smoogen은 그렇게 해서 문제가 해결된다면 자신도 매우 좋겠지만 현실은 더 복잡하다고 [답했다](https://lwn.net/ml/all/4ad6e7c3-9abd-457f-8abd-faf93aa25e1b@app.fastmail.com/).

> 빌드를 늦추거나 이미 복잡한 시스템을 더 나쁘게 만드는 것은 무엇이든, 더 높은 우선순위 항목들 뒤로 밀려난다. 거의 매번 "이번에는 다를 것이고, 다른 항목보다 이 일을 최우선으로 처리해야 한다"고 말해 놓고도, 일주일 뒤에는 "우리가 그렇게 말한 건 알지만, X라는 이유로 이 compose가 반드시 나가도록 해야 하니 지금 하던 일을 내려놓고 도와달라"는 식이 된다.

그는 Fedora 인프라 팀이 2009년부터 Nagios 모니터링을 "다른 무엇이든"으로 교체하려 해 왔고, 다른 핵심 인프라 역시 거의 그만큼 오래 교체하려 했지만, 그런 프로젝트들의 우선순위가 Fedora의 연 2회 릴리스용 빌드를 만들어 내는 일보다 앞서지는 못한다고 지적했다.

Adam Williamson은 일부가 즉시 작동하지 않더라도 Fedora가 사람들에게 2FA를 사용하게 해야 한다고 [생각했다](https://lwn.net/ml/all/d92e6aada6dc0f5722108f71878d2eb1dd66bd9a.camel@fedoraproject.org). 계정 탈취를 이용하는 실제 공격이 널리 벌어지고 있다는 점이 사용자 경험보다 더 중요하다는 것이다. 또한 그는 사람들에게 오픈소스 프로젝트를 사용하게 하는 것이 그 프로젝트가 나아지도록 보장하는 한 방법이라고 주장했다. "우리는 몇 년 동안 '그래, 의무 2FA가 좋긴 하겠지만 먼저 누군가가 <긴 위시리스트>를 고쳐야 해'라고 말하며 손을 놓고 있었다. 그것은 분명히 효과가 없다. 우리는 다른 일을 해야 한다." 그는 자신이 Fedora 작업에 수년 동안 2FA를 사용해 왔고 괜찮다고 생각한다고 덧붙였다. Fedora 위키의 [Kerberos 인증 지침](https://fedoraproject.org/wiki/Infrastructure/Kerberos#How_to_use_kerberos_auth_with_Fedora_Infrastructure)은 2FA 사용 방법을 다룬다.

최소한 그는 Fedora의 provenpackager 그룹 구성원에게는 2FA 사용을 의무화하고 싶어 했다. 그 그룹의 누구든 자신이 소유한 패키지뿐 아니라 모든 패키지에 변경 사항을 커밋할 수 있기 때문이다[^lwn1078380-p06-2]. 따라서 그 그룹 구성원의 계정이 탈취되면 막대한 피해를 줄 수 있다. 그는 Fedora가 또한 프로젝트의 [Forgejo](https://forgejo.org/) 기반 협업 플랫폼인 [Fedora Forge](https://forge.fedoraproject.org/)에 SSH 인증을 활성화하고, proven packager에게 SSH 키 사용을 요구한 다음, 그 요구 사항을 모든 패키저로 확대해야 한다고 말했다.

그 forge는 OpenShift 인스턴스에서 호스팅되며, 현재 이 플랫폼의 Git 저장소에는 SSH로 접근할 수 없다. OpenShift 클러스터가 [인터넷에 직접 연결되지 않은 프록시 뒤에 있기](https://forge.fedoraproject.org/forge/forge/issues/27#issuecomment-256286) 때문이다. 6월 13일 Kevin Fenzi는 SSH 접근을 활성화하는 작업을 "백그라운드에서 천천히" 진행해 왔고 어느 정도 진전은 있었지만 아직 해야 할 일이 더 남아 있다고 [말했다](https://forge.fedoraproject.org/forge/forge/issues/27#issuecomment-821849).

Simo Sorce는 일부 사람들이 비밀번호용 애플리케이션과 2FA 토큰 생성용 애플리케이션을 같은 것으로 사용할 것이라는 이유로 2FA 요구에 [반대했다](https://lwn.net/ml/all/8bef612104064eeb95116ab7c1b6f14f36b6aee7.camel@redhat.com). "슬프게도 보안을 개선할 때마다, 그것을 더 잘 스스로 무력화하는 사람을 발견하게 된다." 그래도 Williamson은 주저하지 않았다. 그는 여러 상황에서 2FA가 여전히 유용할 수 있다고 [답했다](https://lwn.net/ml/all/ba3cddb61968fd751427d40d09966a7150a00c4b.camel@fedoraproject.org).

#### 설득됨

6월 12일 Catanzaro는 Fedora가 2FA를 요구할 때가 되었다는 점에 자신이 설득되었다고 [말했다](https://lwn.net/ml/all/19fae001-ee6c-4da5-b38c-b8ad05a7f8fc@app.fastmail.com). Gary Buhrmaster는 2FA를 요구 사항으로 만들기 위한 절차가 무엇인지 [궁금해했다](https://lwn.net/ml/all/CAMfXtQxcp0SkmCai34bjx+HxtJepw1=rLSwpugn+D91LLuan6A@mail.gmail.com). Berrangé는 지난번 제안 때는 [Fedora Engineering Steering Committee](https://docs.fedoraproject.org/en-US/fesco/) (FESCo)에 제출되었다고 [말했다](https://lwn.net/ml/all/ai-2kIDLZhEf-gSv@redhat.com)[^lwn1078380-p06-3].

그때는 2024년 3월로, Miroslav Suchý가 모든 Fedora 패키저에게 2FA를 의무화하자는 [제안](https://pagure.io/fesco/issue/3186)을 제출했다. FESCo는 그 제안을 [수락했지만](https://pagure.io/fesco/issue/3186#comment-908335), 내용을 완화했다. 모든 패키저에게 2FA 활성화를 요구하는 대신, FESCo는 provenpackagers 그룹 구성원이 2FA에 등록해야 한다("SHOULD")고 정책을 바꾸었다. 2FA의 사용자 경험이 개선되면 정책을 "MUST"로 바꾸는 것을 검토하겠다는 것이다.

그 이후 2FA 경험을 개선하는 데에는 거의 변화가 없었다. Williamson은 6월 15일 현재 스레드에 [후속 글](https://lwn.net/ml/all/11d52bbd41f66fb4843253e35d14ef2cfe8513b6.camel@fedoraproject.org/)을 올렸다. 그는 [Flock](https://fedoraproject.org/flock/2026/)에서 Fenzi와 이야기를 나누었고, 현재로서는 "이를 실제로 구현하는 것이 기술적으로 어렵다"는 말을 들었다고 했다. Fedora의 [DistGit](https://github.com/release-engineering/dist-git#distgit) 시스템에 대한 커밋 같은 작업이 2FA를 사용했는지 감시하는 방식으로 2FA 사용을 강제하는 것은 가능할 것이다. "그러면 규칙을 따르지 않은 사람들에게 가서 호통칠 수 있다."

그는 Fedora의 provenpackagers 그룹처럼 큰 집단에는 그런 방식이 잘 확장되지 않을 것이라고 말했다. "그래서 그 이유로 아직 티켓을 제출하지 않았다. 앞으로 나아갈 방법이 무엇일지 Kevin과 더 이야기해 보겠다." 하지만 FESCo 구성원 "Maxwell G"는 proven packager에게 2FA를 요구하는 [티켓](https://pagure.io/fesco/issue/3618)을 FESCo에 제출했다고 [말했다](https://lwn.net/ml/all/ea0b7973-12f3-43ee-b3d7-3044241b7df5@gtmx.me/). 그는 그 티켓에서 이를 어떻게 구현할지는 아직 열린 질문이라고 인정했으므로, 아직 모든 패키저에게 2FA 사용을 요구하자고 제안한 것은 아니었다.

그 제안의 논의에서 Fenzi는 해당 그룹에 114명이 있으며, 그중 59명은 2FA를 활성화하지 않았다고 [언급했다](https://pagure.io/fesco/issue/3618#comment-1019057). Maxwell G는 새 사람을 그룹에 추가할 때 2FA 등록 여부를 확인하고, 지정된 기준일까지 2FA에 등록하지 않은 사람을 그룹에서 제거할 날짜를 정할 수 있을 것이라고 [말했다](https://pagure.io/fesco/issue/3618#comment-1019358).

#### FESCo 결정

이 주제는 6월 23일 FESCo 회의에서 논의되었다([요약](https://lwn.net/ml/all/CAB-QmhTyNJ+QMV6+MeOK3yohFrc=LXiq2_D0N=MZx7egpfD3GQ@mail.gmail.com), [로그](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-06-23/fesco.2026-06-23-17.00.log.html)). 논의 중 걸림돌 하나는 사용자가 2FA에 사용하던 장치를 잃어버렸을 때 Fedora에 복구 메커니즘이 없다는 점이었다. 많은 서비스는 사용자가 일회용 비밀번호(OTP) 애플리케이션이나 하드웨어에 접근할 수 없을 때 사용할 수 있는 백업 코드를 제공한다.

[^lwn1078380-p06-1]: 2FA는 비밀번호 외에 일회용 코드나 보안 키 같은 두 번째 요소를 요구하는 방식이며, MFA는 둘 이상의 인증 요소를 조합하는 더 넓은 개념이다.
[^lwn1078380-p06-2]: Fedora의 provenpackager는 특정 패키지 소유권을 넘어 광범위한 패키지에 변경을 적용할 수 있는 신뢰 그룹이다.
[^lwn1078380-p06-3]: FESCo는 Fedora의 엔지니어링 정책과 기술 결정을 다루는 운영 위원회다.

[Neal
Gompa](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-06-23/fesco.2026-06-23-17.00.log.html#:~:text=I%20have%20MFA%20on%20for%20everything)와 [Michel
Lind](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-06-23/fesco.2026-06-23-17.00.log.html#:~:text=I%20don%27t%20have%20it%20turned%20on%20for%20fedora)는 모두 다른 서비스에서는 2FA[^lwn1078380-p07-1]를 사용하고 있지만, 백업 복구 방법이 없어서 Fedora에서는 이를 피하고 있다고 말했다. Fenzi는 다른 모든 방법이 실패하더라도 OTP[^lwn1078380-p07-2] 장치에 대한 접근 권한을 잃은 사람이 Fedora 관리자 그룹에 이메일을 보내 그런 방식으로 계정을 복구할 수 있다고 말했다. 이상적인 해결책은 아니지만, 그런 일이 자주 필요하지 않기를 바랄 뿐이다.

논의 끝에 FESCo는 provenpackager 그룹[^lwn1078380-p07-3] 구성원에게 2FA 활성화를 요구하기로 [결정했다](https://pagure.io/fesco/issue/3618#comment-1019455). 표결 결과는 찬성 7표, 반대 0표였고, Gompa는 현재의 2FA 복구 지원에 대한 불만을 표시하기 위해 ["+0" 표를 던졌다](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-06-23/fesco.2026-06-23-17.00.log.html#:~:text=14-,%2B0). ""더 적극적으로 지지할 수 있으면 좋겠지만, 우리가 사람들을 실패하도록 몰아가고 있다고 느낀다"".

새 요구 사항을 알리기 위해 Fedora 개발 목록으로 이메일([초안](https://pagure.io/fesco/issue/3618#comment-1019469))이 발송되고, 그룹 구성원들에게도 직접 이메일이 보내질 예정이다. 요구 사항이 시행되기 전까지 3개월의 유예 기간이 주어진다. 그 이후에는 2FA가 활성화되어 있지 않은 사용자는 그룹에서 제거된다. 2FA를 활성화한 뒤에는 다시 그룹에 추가되기 위해 인프라 팀에 요청을 제출해야 한다.

Fedora의 114명 proven packager에게 2FA를 추가하는 것은 프로젝트에 보안 계층을 더하는 작은 조치이지만, 그럼에도 진전이다. 완벽함이 좋은 것을 가로막지 않도록 결정함으로써, 프로젝트는 앞으로 자신과 사용자들이 겪을 골칫거리를 줄일 수 있을지도 모른다. 또한 프로젝트가 거친 부분을 다듬고, 결국 모든 packager에게 2FA를 요구할 수 있게 하는 데도 도움이 될 수 있다.

[댓글(38개 게시됨)](https://lwn.net/Articles/1078964/#Comments)

[^lwn1078380-p07-1]: 2FA는 two-factor authentication, 즉 2단계 인증을 뜻한다.
[^lwn1078380-p07-2]: OTP는 one-time password, 즉 일회용 비밀번호를 뜻한다.
[^lwn1078380-p07-3]: provenpackager는 Fedora에서 여러 패키지에 대한 광범위한 수정 권한을 가진 신뢰된 패키지 관리자 그룹을 가리킨다.

### [7.2 병합 창의 전반부](https://lwn.net/Articles/1078068/)

By **Jonathan Corbet**  
2026년 6월 18일

#### 요약

- 7.2 병합 창 초반에 이미 7,000개가 넘는 비병합 변경 집합이 메인라인에 들어갔다.
- i486 관련 코드 제거, s390 Rust 지원, arm64 하드닝 작업 등 아키텍처별 변화가 두드러진다.
- BPF에는 fault 허용 tracepoint 프로그램, 공통 속성, 더 많은 함수 인자, 크기 조절 가능한 hash map 등이 추가됐다.
- 파일시스템과 블록 I/O 쪽에서는 `openat2()`의 새 플래그, XFS zoned storage의 비실험 전환, Btrfs large folio 기본 사용 등이 포함됐다.
- 네트워킹, 보안, 하드웨어 지원 전반에서도 오래된 기능 제거와 새 장치 지원이 함께 진행됐다.

7.2 병합 창은 6월 14일 [7.1 커널 릴리스](https://lwn.net/ml/all/CAHk-=wi4BF4bMhZNZ1tqs+FFV4OuZRe3ZqdWB+LxRLmRweUzQw@mail.gmail.com/)와 함께 시작되었다. 이 글을 쓰는 시점에는 다음 커널 릴리스를 위해 7,000개가 조금 넘는 비병합 변경 집합이 메인라인에 pull되었다. 핵심 하위 시스템 다수가 이 시점에 이미 pull되었으므로, 7.2에서 기대할 수 있는 변경 사항 대부분의 윤곽이 이제 드러난 셈이다.

지금까지 병합된 가장 중요한 변경 사항은 다음과 같다.

#### 아키텍처별

- 커널에서 i486 전용 지원이 더 제거되었다. 그중에는 부동소수점 장치가 없는 프로세서에서 이를 에뮬레이션하는 데 필요했던 13,000줄이 넘는 코드 제거도 포함된다.
- [OLPC XO-1](https://en.wikipedia.org/wiki/OLPC_XO) 컴퓨터에 사용된 AMD Geode 프로세서는 [고아 상태로 표시되었다](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=4af2468b82bd).
- Intel [Trusted Domain Extensions (TDX)](https://www.intel.com/content/www/us/en/developer/tools/trust-domain-extensions/overview.html) 기능은 플래시 메모리에서 로드되는 특수 소프트웨어 모듈로 구현된다. 7.2의 변경 사항에는 이 모듈을 관리하기 위한 새 장치 유형 도입과, 실행 중인 시스템에서 모듈을 교체할 수 있는 기능(예를 들어 보안 업데이트 설치)이 포함된다. [이 문서 패치](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=2b9ad7a6154e)에 더 많은 정보가 있다.
- s390 아키텍처에 Rust 지원이 추가되었다.
- arm64 커널은 하드닝 전략의 하나로 데이터 영역을 전체 메모리 선형 매핑에서 제거하도록 변경되고 있다. 필요한 작업은 완료되었지만, 실제 제거를 적용하는 변경은 KVM 회귀 문제에 대한 해결책이 나올 때까지 현재 [되돌려졌다](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=f102131c842d).
- PowerPC는 커널에서 하드웨어 최적화 MD5 해시 구현을 가진 유일한 아키텍처였다. MD5 전반의 취약성을 고려하면 이 코드는 별 의미가 없으며 [제거되었다](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=cf52058dcdd9).

#### BPF

- tracepoint에 연결된 BPF 프로그램이 이제 fault를 일으킬 수 있게 되어, 사용자 공간 메모리에 안정적으로 접근할 수 있다.
- [bpf()](https://man7.org/linux/man-pages/man2/bpf.2.html) 시스템 호출에는 "공통 속성" 지원이 확장되었다. 처음에는 이 기능이 여러 BPF 하위 명령의 로깅을 제어하는 데 사용된다. (일부) 자세한 내용은 [이 병합 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=6318f11d53a3)을 보라.
- BPF 함수와 kfunc에 적용되던 5개 매개변수 제한은, 추가 매개변수를 스택에 배치할 수 있게 하면서 해제되었다. 자세한 내용은 [이 병합 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=cd59fa185a03)을 보라.
- 이제 커널 코드가 page fault를 걱정하지 않고 [BPF arena](https://lwn.net/Articles/961941/)에 안전하게 접근할 수 있다. 자세한 내용은 [이 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=dc11a4dba246)을 보라.
- BPF hash map은 생성 시 고정된 수의 bucket을 가진다. 새롭게 추가된 크기 조절 가능한 hash map 유형은 이 제한을 없앤다. 자세한 내용은 [이 병합 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=87d119abc42f)을 보라.
- 이제 같은 BPF 프로그램을 여러 tracepoint에 빠르게 연결할 수 있다. 이 기능에 대한 문서는 없지만, [패치 시리즈](https://lwn.net/ml/bpf/20260603110554.29590-1-jolsa@kernel.org/)에는 이 기능을 어떻게 사용할 수 있는지 보여주는 여러 self test가 포함되어 있다.

#### 핵심 커널

- `/proc/interrupts` 구현은 더 나은 성능을 위해 재작업되었다. 자세한 내용은 [이 병합 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=13e1a6d6a17e)을 보라. "`/proc/interrupts`는 오랫동안 마이크로 최적화의 대상이었지만, 쉽게 얻을 수 있는 성과 대부분은 그대로 남아 있었다."
- [cache-aware load-balancing](https://lwn.net/Articles/1018334/) 패치 시리즈가 병합되었다. 이 변경으로 스케줄러는 자원을 공유하는 프로세스들을 같은 cache domain으로 묶으려 하며, 이를 통해 성능이 향상되기를 기대한다.
- `sched_ext`에서 [sub-scheduler](https://lwn.net/Articles/1056014/) 지원을 추가하는 작업은 계속되고 있다. 현재 상태는 [이 병합 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=5b33fc6492a7)을 보라.

#### 파일시스템과 블록 I/O

- 파일시스템은 이제 [file_getattr() 시스템 호출](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=662416578541)을 통해 대소문자 구분 여부에 관한 정보를 제공할 수 있다. 두 개의 새 플래그가 구현되었다. `FS_XFLAG_CASEFOLD`는 파일 이름 조회가 대소문자를 구분하지 않음을 나타내며, `FS_XFLAG_CASENONPRESERVING`은 새 파일 이름의 구체적인 대소문자 형태가 보존되지 않음을 나타낸다. 무엇보다 이 기능은 대소문자를 구분하지 않는 동작을 기대하는 Windows NFS 클라이언트를 지원한다.
- [openat2()](https://man7.org/linux/man-pages/man2/openat2.2.html) 시스템 호출은 `O_EMPTYPATH`라는 새 플래그를 지원한다. 이 플래그에는 특정한 목적이 있다. 프로세스가 `O_PATH` 파일 디스크립터를 다시 열어 그 뒤에 있는 파일에 접근할 수 있게 하는 것이다. `O_EMPTYPATH`를 사용하면 빈 경로 이름을 `openat2()`에 전달할 수 있고, 주어진 파일 디스크립터가 (다시) 열 파일을 찾는 데 사용된다.
- `openat2()`에 새로 추가된 또 다른 것은 `OPENAT2_REGULAR` 플래그로, 대상이 일반 파일이 아니면 open이 실패하게 만든다. 실패 시 반환 코드는 Linux에는 새로운 `EFTYPE`이다. 이 플래그는 프로그램이 특수 파일을 열도록 조작되는 일을 막기 위한 하드닝 기능이다.
- XFS 파일시스템은 6.15 릴리스부터 [zoned storage device 지원](https://lwn.net/Articles/1001751/)을 제공해 왔다. 7.2에서는 이 기능이 [더 이상 실험적 기능으로 표시되지 않는다](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=610c08cbe79b).
- Btrfs 파일시스템은 이제 기본적으로 large folio를 사용한다. "huge" folio(최대 2MB) 지원은 실험적 옵션으로 추가되었다.
- 새 `dm-inlinecrypt` device-mapper target은 inline-encryption 기능이 있는 블록 장치를 지원할 수 있다. 문서는 [Documentation/admin-guide/device-mapper/dm-inlinecrypt.rst](https://docs.kernel.org/next/admin-guide/device-mapper/dm-inlinecrypt.html)에서 볼 수 있다.

#### 하드웨어 지원

- **GPIO와 pin control**: Waveshare DSI-panel GPIO 컨트롤러.
- **그래픽**: Focaltech OTA7290B 패널, Novatek NT35532 기반 DSI video mode 패널, CHIPWEALTH CH13726A 기반 DSI 패널. 한편, 유서 깊은 Hercules ISA 그래픽 카드 드라이버는 아마 수십 년 동안 동작하지 않았을 것이므로 [제거되었다](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=37a91b995952).
- **하드웨어 모니터링**: MPS MP2985 dual loop digital multi-phase 컨트롤러, Luxshare LX1308 DC/DC 전원 모듈, Analog Devices MAX20830 step-down DC-DC switching regulator, Analog Devices MAX20860A step-down converter, Analog Devices LTC4283 negative voltage hot swap controller, Delta E50SN12051 전원 모듈, ARCTIC fan controller, Murata D1U74T 전원 공급 장치, Microchip Technology EMC181X/33 multichannel low-voltage remote diode sensor.
- **기타**: ASPEED AST2700 interrupt controller, Qualcomm IPQ6018 pulse-width modulator, Loongson-2 Fast Speed I2C adapter, SG Micro SGM3804 voltage regulator, Spacemit K1 SPI controller, Qualcomm Gunyah watchdog timer, Andes ATCWDT200 watchdog timer.
- **네트워킹**: Alibaba Elastic Ethernet adapter, NXP NETC Ethernet switch, Airoha AN8801 Gigabit PHY, Realtek 8922AU USB wireless network adapter.
- **사운드**: Texas Instruments TAS675x quad-channel audio amplifier, Everest Semi ES9356 codec, Cirrus Logic CS42448/CS42888 codec.

#### 기타

- [Event probe(eprobe)](https://docs.kernel.org/trace/eprobetrace.html)는 이제 커널의 BTF 정보를 사용해 구조체 포인터를 더 쉽게 역참조할 수 있다. 자세한 내용은 [이 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=69efd863a785)을 보라.

#### 네트워킹

- 6.7 릴리스를 위해 [커널에 추가된](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=7fe0e38bb669) [TCP authentication option](https://datatracker.ietf.org/doc/html/rfc5925) 구현은 새 [libcrypto](https://origin.kernel.org/doc/html/next/crypto/libcrypto.html) 라이브러리를 사용하도록 변경되어 코드가 더 단순하고 효율적이 되었다. 사용되지 않는 것으로 보이는 여러 알고리즘에 대한 지원은 제거되었다. 자세한 내용은 [이 병합 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=fdd2c9a1d082)과 [이 문서 패치](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=34d67417c8cf)를 보라.
- multi-path TCP 연결에 지원되는 subflow 수가 8개에서 64개로 늘었다.
- `rtnl_lock`("큰 네트워킹 잠금") 사용을 줄여 네트워킹 스택의 확장성을 개선하는 작업은 계속되고 있다.
- 네트워크 하위 시스템에서 제거된 것에는 ISA 및 PCMCIA 기반 ARCnet 인터페이스 지원, PCMCIA 기반 Bluetooth adapter, Chelsea inline TLS accelerator, 더 많은 ATM 지원(자세한 내용은 [이 병합 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=e1f544466b2c)을 보라), 그리고 AppleTalk 프로토콜이 포함된다.

#### 보안 관련

- slab allocator에는 Clang [allocation token](https://clang.llvm.org/docs/AllocToken.html)을 사용해 서로 다른 유형의 할당 객체 배치를 분리하는 기능이 추가되었다. 이로써 한 유형의 객체에 대한 buffer overflow를 악용해 다른 유형의 객체를 손상시키기가 더 어려워진다. 자세한 내용은 [이 커밋](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=feb662d9168b)을 보라.[^lwn1078380-p08-1]
- 커널의 암호화 계층이 작업을 특수 목적 하드웨어로 offload할 수 있게 해주는 `AF_ALG` 메커니즘은 최근 여러 보안 문제에 연루되었다. 애초에 이 기능을 사용할 이유가 드문 만큼, 향후 제거를 염두에 두고 [사용 중단 처리되었다](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=a67afb1884ba). 동시에 하드웨어 accelerator 지원은 [제거되어](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=7524070f26d8), 소프트웨어 구현만 사용할 수 있게 되었다. 오래된 `rng_alg` 프레임워크를 사용하는 난수 생성기 드라이버 여러 개도 제거되었다.[^lwn1078380-p08-2]

#### 내부 커널 변경 사항

[^lwn1078380-p08-1]: allocation token은 할당 지점이나 객체 종류에 따라 메모리 배치를 구분해, 동일한 slab 안에서 서로 다른 민감도의 객체가 섞이는 상황을 줄이려는 하드닝 기법이다.
[^lwn1078380-p08-2]: `AF_ALG`는 사용자 공간에서 커널 암호화 API를 소켓 인터페이스처럼 사용할 수 있게 하는 기능이다.

- I/O를 위해 buffer head를 제출하는 새로운 `bh_submit()` 함수가 생겼고, `b_end_io` 콜백 포인터는 제거되었다. 이 변경은 성능과 보안을 모두 개선한다. 자세한 내용은 [이 merge message](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=f0d857543e4d)를 보라.[^lwn1078380-p09-1]
- [iomap](https://docs.kernel.org/filesystems/iomap/index.html) 계층이 [fs-verity](https://docs.kernel.org/filesystems/fsverity.html)를 지원하게 되었다. 이 기능은 함께 따라와야 할 문서 갱신 없이 추가되었는데, 그 문서도 틀림없이 곧 나올 것이다.
- 파일시스템 개발자를 꿈꾸는 이들을 위한 새 문서도 있다. [Documentation/filesystems/adding-new-filesystems.rst](https://docs.kernel.org/next/filesystems/adding-new-filesystems.html)는 커널에 새 파일시스템을 추가할 때 고려해야 할 사항과 요구 조건을 제시한다.
- 커널을 빌드하는 데 필요한 LLVM의 최소 버전은 이제 17.0.1이다.
- 새로 생긴, 철저히 문서화되지 않은 `kconfig-sym-check` 빌드 대상은 Kconfig 파일에서 한 번도 정의되지 않은 심벌을 참조하는지 검사한다.
- Rust의 ["zerocopy" crate](https://docs.rs/zerocopy/latest/zerocopy/)가 커널 소스에 들어왔다. 이 crate는 unsafe 코드를 격리하려는 의도로 저비용 메모리 조작 프리미티브를 제공한다. 자세한 내용은 [이 merge commit](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=98cc68794c00)을 보라.[^lwn1078380-p09-2]
- Rust 코드용 새 “higher-ranked lifetime types”는 드라이버의 수명과 그것이 바인딩되는 장치 사이의 연결을 더 잘 캡슐화한다. 자세한 내용은 [이 merge commit](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=2c7c65933600)을 보라.
- [nolibc library](https://lwn.net/Articles/920158/)는 이제 OpenRISC 및 32-bit PA-RISC 아키텍처를 지원한다. 또한 `alloca()`, `assert()`, `creat()`, `ftruncate()` 구현도 추가되었다.
- block-layer 수준에서 테스트하기 위한 새 error-injection framework가 생겼다. 조금 더 자세한 정보는 [Documentation/block/error-injection.rst](https://docs.kernel.org/next/block/error-injection.html)를 보라.[^lwn1078380-p09-3]

7.2 merge window는 6월 28일까지 열린 상태로 유지될 것으로 예상된다. linux-next에는 6,000개를 조금 넘는 changeset이 들어 있어, mainline으로 이동하기를 기다리는 코드가 아직 상당히 많다는 뜻이다. 늘 그렇듯, LWN은 merge window가 닫힌 뒤 그 코드에 무엇이 담겨 있는지 요약을 게시할 것이다.

[Comments (none posted)](https://lwn.net/Articles/1078068/#Comments)

[^lwn1078380-p09-1]: `buffer head`는 블록 I/O에서 버퍼를 설명하는 커널 내부 자료구조를 가리키는 용어이므로 원문 용어를 유지했다.
[^lwn1078380-p09-2]: Rust의 `crate`와 `unsafe`는 해당 생태계의 고유 용어라 번역하지 않았다.
[^lwn1078380-p09-3]: `block-layer`와 `error-injection framework`는 커널 하위 계층 및 시험 기능을 가리키는 기술 용어로 원문 형태를 살렸다.

### [BPF 아레나를 위한 헬퍼 라이브러리](https://lwn.net/Articles/1078526/)

글쓴이: **Daroc Alden**  
2026년 6월 24일

#### 요약

- Emil Tsalapatis는 BPF arenas에서 재사용할 수 있는 범용 유틸리티 라이브러리인 libarena 작업을 2026 LSFMM+BPF Summit에서 소개했다.
- libarena는 표준 BPF C 코드로 빌드·링크되는 선택적 라이브러리로, 커널 트리에 포함되어 verifier와 함께 테스트되는 것을 목표로 한다.
- 초기 버전은 7.2 커널에서 실험적으로 제공되며, buddy allocator와 ASAN 연동용 훅을 포함하지만 아직 본격적인 자료구조 구현은 없다.
- 향후에는 mimalloc 스타일 할당기, red-black tree, B-tree, bitmap, Lev-Chase queue 같은 공통 자료구조가 추가될 수 있다.
- 참석자들은 커널 버전 간 호환성과 디버깅, verifier와의 상호작용에 대해 질문했으며, libarena의 범위는 우선 핵심 기능에 집중하기로 했다.

---

[LSFMM+BPF](https://lwn.net/Articles/lsfmmbpf2026/)

[BPF arenas](https://lwn.net/Articles/961941/)는 프로그램이 verifier의 경계 검사에 얽매이지 않고 자체 자료구조를 자유롭게 만들 수 있는 메모리 영역(잠재적으로 사용자 공간과 공유될 수도 있음)이다.[^lwn1078380-p10-1] 그러한 자료구조 가운데 상당수는 여러 프로그램에서 사용할 수 있을 가능성이 있다. Emil Tsalapatis는 BPF arenas에서 사용할 범용 유틸리티를 담은 라이브러리인 libarena 작업을 2026년 [Linux Storage, Filesystem, Memory-Management, and BPF Summit](https://events.linuxfoundation.org/lsfmmbpf/)에 가져왔다. 이 라이브러리는 이미 커널의 일부로 제공되고 있지만, 아직 초기 단계이며 그는 더 많은 작업을 계획하고 있다.

Tsalapatis는 sched\_ext 작업을 하고 있는데, 이 프로젝트에서 그는 재사용될 수 있다고 보는 BPF arenas 기반 구성 요소를 여러 개 작성해 왔다. 특히 그는 arenas를 위한 보편적으로 합의된 메모리 할당기와, 그것을 사용하는 공통 자료구조 집합이 있을 가능성을 본다. 또한 arenas에 더 나은 디버깅 기능을 추가하는 방안도 살펴보고 싶어 한다. arenas는 verifier와 씨름할 필요를 없애 줄 수 있지만, 이는 동시에 커널에 대한 위협은 아니더라도 여전히 찾아서 고쳐야 하는 일반적인 메모리 안전성 문제가 생길 수 있음을 뜻한다.

[![[Emil Tsalapatis]](https://static.lwn.net/images/2026/emil-tsalapatis-lsfmmbpf-small.png "Emil Tsalapatis")](https://lwn.net/Articles/1078966)

Tsalapatis는 모든 것에 arenas를 사용하는 데 단점이 있다는 점을 인정했다. BPF 프로그램은 언제든 검사 없이 arenas에 쓸 수 있으므로, verifier는 arena에 저장된 커널 객체 포인터가 계속 유효하다고 신뢰할 수 없다. 따라서 verifier는 커널 객체에 대한 포인터를 arenas에 저장하는 것을 아예 금지한다. 그런 포인터들은 여전히 다른 종류의 BPF map에 저장해야 한다. 그런 단서에도 불구하고, 그는 arenas에 집중하는 것이 번거로움을 감수할 가치가 있다고 본다. 그가 말하길 최종 목표는 BPF C를 일반 C만큼 쉽게 작성할 수 있게 만드는 것이며, arenas는 그 목표의 큰 부분을 차지한다.

그는 libarena가 BPF 프로그램을 위한 표준 라이브러리를 제공하는 모습을 구상하고 있다. 이는 유지해야 할 추가 커널 인터페이스가 아니라, 일반적인 방식으로 BPF 프로그램에 컴파일되고 링크되는 순수 C 코드가 될 것이다. 이는 또한 선택 사항이라는 뜻이기도 하다. 작은 BPF 프로그램은 해당 기능을 사용하지 않는 한 libarena에 링크할 필요가 없다. 라이브러리 소스 코드는 커널 트리 안에 직접 들어가며, 제공하는 알고리즘과 자료구조가 실제로 검증을 통과하는지 확인하기 위해 verifier를 상대로 테스트될 것이다. libarena는 커널 버전에 대응하므로, 최신 verifier 기능도 걱정 없이 사용할 수 있다.

청중 한 명은 libarena가 커널 버전 간 프로그램 마이그레이션을 어떻게 지원할지 물었다. 커널 인터페이스를 사용하는 BPF 프로그램은 그 목적으로 "compile once — run everywhere"(CO-RE) relocation을 사용할 수 있지만, BPF 프로그램에 실제로 링크되는 코드에는 이것이 동작하지 않을 것이다. Tsalapatis는 libarena가 도입 이전의 커널 버전에서는 지원되지 않겠지만, 약간 주의를 기울이면 forward-compatible하게 만들 수 있어서 사람들이 목표로 삼으려는 가장 오래된 커널 버전의 libarena를 기준으로 빌드할 수 있고 CO-RE relocation은 필요하지 않게 할 수 있다고 말했다.[^lwn1078380-p10-2]

질문자는 회의적이었다. 그들은 현재 어떤 프로그램이 6.9 커널에서는 검증을 통과하지만 6.19 커널에서는 통과하지 못하는 문제를 고치려 하고 있으므로, forward compatibility는 실제 문제다. Tsalapatis는 아마도 프로그램이 사용 중인 커널 버전에 대응하는 libarena 버전을 링크할 수도 있을 것이라고 제안했다. 서로 다른 커널에 서로 다른 버전을 링크해도 문제가 생기지 않을 만큼 충분히 안정적인 인터페이스를 갖추는 것이 바람이다.

그는 이어서 프로그래머들이 이 라이브러리를 어떻게 활용할 것으로 생각하는지 설명했다. 소스는 커널 트리에 있지만, 사용자가 libbpf가 동작하는 방식과 똑같이 자체 포함형 Git submodule로 추가할 수 있도록 별도의 Git 저장소로 주기적으로 내보내고 싶어 한다. 빌드 시스템은 libarena의 makefile을 호출해 libarena.bpf.o를 생성한다. 주 BPF 프로그램은 libarena의 헤더를 포함하고 그 객체에 링크된다.

다른 청중은 이것이 BPF의 continuous-integration 테스트에 오래된 커널들을 추가해야 한다는 의미인지 물었지만, Tsalapatis는 backward compatibility가 우선순위가 아니라고 거듭 말했다. Alexei Starovoitov는 libarena가 개발 초기 단계임을 언급하며, 그 문제는 7.5 커널 때 걱정하자고 제안했다.

7.2 커널 기준으로 libarena는 실험적 사용이 가능해질 예정이다. 여기에는 buddy allocator와 향후 작업을 위한 일부 기본 scaffolding이 들어 있지만, 아직 실제 자료구조 구현은 없다. 또한 Clang의 address sanitizer인 ASAN과 함께 동작하는 데 필요한 훅도 갖고 있지만, 개발 중인 Clang 버전에서만 가능하다. 이 할당기는 사용 가능하며 모든 크기의 할당을 처리하지만, 아직 특별히 빠르지는 않다. Tsalapatis는 이 할당기를 작성하는 일이 arenas에 대한 좋은 사례 연구였으며, 해결해야 할 많은 edge case를 드러냈다고 보았다.

향후 libarena의 할당기는 단순한 buddy allocator 대신 [mimalloc](https://github.com/microsoft/mimalloc#mimalloc)의 설계를 사용하게 될 수도 있다. Mimalloc은 함수형 언어 런타임에서 사용하도록 설계되었고, multithreading과 수명이 짧은 할당에서 좋은 성능을 보인다. 이 두 특성은 Tsalapatis가 미래의 BPF 프로그램 성능에 중요할 것으로 예상하는 기능이다. 그는 또한 이것이 단순하고 효율적인 설계라고 말했다.

이전에 그는 fragmentation을 줄이기 위해 slab allocator를 사용하는 실험을 했지만, 임의의 프로그램에는 다루기 번거롭다는 것을 알게 되었다. sched\_ext에서는 필요한 구조체가 ""like three types""뿐이었기 때문에 잘 동작했지만, 일반적인 프로그램에서는 그렇지 않다.

향후 Tsalapatis는 최소한 red-black tree, B-tree, bitmap, 그리고 [Lev-Chase queue](https://www.dre.vanderbilt.edu/~schmidt/PDF/work-stealing-dequeue.pdf)(Chase-Lev queue라고도 알려짐)를 libarena의 일부로 제공하고 싶어 한다. 사람들이 BPF 프로그램을 작성하는 데 large language model을 쓰기 시작하더라도, verifier와 함께 동작하는 수작업 코딩 자료구조를 libarena에 두는 데 가치가 있다고 그는 생각했다. ""내 경험상, 좋은 코드로 에이전트에 seed를 주면 어려운 문제를 one-shot으로 풀 수 있게 해 준다는 것을 알게 됐다.""

그는 이어서 ASAN 훅이 무엇을 하는지 설명했다. arena가 생성될 때 페이지는 lazily하게 매핑된다. 새 페이지에 접근하면 page fault가 발생한다. BPF 프로그램은 이러한 이벤트를 수신하고, 이를 사용해 어느 메모리 영역에 접근해도 되는지에 대한 ASAN의 정보를 담는 metadata 영역도 채울 수 있다. 메모리 구간을 할당하면 8바이트 granularity로 안전하다고 표시되고, 이를 해제하면 그 표시가 제거된다. 컴파일러는 값을 로드하거나 저장하기 전에 metadata의 상태를 확인하도록 pointer dereference를 보강한다. 이 작업에는 개발 중인 Clang 버전이 필요한데, 이전 컴파일러는 metadata 메모리가 항상 address space zero에 있다고 가정했지만 BPF arenas는 address space one을 사용하기 때문이다. 그래서 Tsalapatis는 이를 위한 플래그를 추가해야 했다. (Clang은 사용 가능한 address space에 번호를 매기지만, GCC는 [이름을 붙인다](https://gcc.gnu.org/onlinedocs/gcc/Named-Address-Spaces.html).)[^lwn1078380-p10-3]

청중 한 명은 올바르게 탐색하기 어려운 일부 커널 자료구조를 탐색하는 코드를 libarena에 포함하는 방안을 Tsalapatis가 고려했는지 물었다. 그는 고려해 보았다고 말했지만, 지금으로서는 libarena의 범위를 작게 유지하고 모든 프로그램이 필요로 할 핵심 요소를 제공하는 데 집중하는 편이 더 낫다고 생각했다. 그 시점에서 세션 시간이 끝났지만, 강연 이후에도 libarena 작업은 [계속되었으며](https://lwn.net/ml/all/20260618085626.19633-1-emil@etsalapatis.com/), 계획된 자료구조 중 일부는 이제 사용할 수 있게 되었다.

[Comments (4 posted)](https://lwn.net/Articles/1078526/#Comments)

[^lwn1078380-p10-1]: 여기서 verifier는 BPF 프로그램이 커널에서 안전하게 실행될 수 있는지 검사하는 커널 내 검증기를 뜻한다.
[^lwn1078380-p10-2]: CO-RE는 BPF 프로그램을 여러 커널 버전에서 재컴파일 없이 실행할 수 있게 돕는 relocation 메커니즘이다.
[^lwn1078380-p10-3]: ASAN(Address Sanitizer)은 메모리 접근 오류를 탐지하기 위한 컴파일러 기반 검사 도구다.

### [BPF 프로그램 일시 중지와 재개](https://lwn.net/Articles/1076210/)

글쓴이: **Daroc Alden**  
2026년 6월 19일

#### 요약

- Kumar Kartikeya Dwivedi는 BPF 프로그램을 코루틴으로 표현해 실행을 일시 중지하고 나중에 재개할 수 있게 하는 작업을 소개했다.
- 이 기능은 스택 추적 수집이나 사용자 공간 네트워킹처럼 하나의 논리적 작업이 여러 시점과 위치에 나뉘어 실행되는 경우를 더 쉽게 다루게 해준다.
- 제안된 설계는 Rust 비동기 함수나 C++ 코루틴과 비슷한 스택 없는 코루틴을 기반으로 하며, verifier가 확인해야 할 새로운 안전 조건을 추가한다.
- verifier는 resume() 및 destroy() 함수 포인터 보호, 유효한 상태 인덱스, 잠금 해제, 중단 상태에서의 안전한 파괴와 재개 등을 보장해야 한다.
- Dwivedi의 프로토타입은 아직 BTF 정보 확장, aggregate return types 지원, Rust 지원 등 추가 작업이 필요하다.
- 장기적으로는 사용자 공간과 커널 공간을 오가는 중단 가능한 계산도 구상되고 있지만, 실제 구현까지는 시간이 오래 걸릴 전망이다.

---

[LSFMM+BPF](https://lwn.net/Articles/lsfmmbpf2026/)

BPF 프로그램은 Linux 커널의 많은 측면을 확장하는 데 사용할 수 있지만,
BPF 프로그램은 시작한 것과 같은 컨텍스트에서 끝까지 실행되어야 한다.
Kumar Kartikeya Dwivedi는 BPF 프로그램을 코루틴으로 표현할 수 있게 함으로써
이를 바꾸는 작업을 진행하고 있다.[^lwn1078380-p11-1] 그는 2026년
[Linux Storage, Filesystem, Memory-Management and BPF Summit](https://events.linuxfoundation.org/lsfmmbpf/)에서
이 작업에 대해 발표했다. 아직 실험 단계이지만, 이 변화는 오래 실행되는 BPF 작업을
훨씬 쉽게 작성할 수 있게 해줄 것으로 기대된다.

그는 하나의 논리적 작업이 공간과 시간 양쪽에 걸쳐 퍼져 있는 일이 흔하다고 설명했다.
실행은 여러 위치 사이를 오가고, 계산은 일시 중지될 수 있으며, 그 밖의 일도 벌어진다.
이를 BPF로 표현할 수 있다면 커널 기능에 대한 어떤 종류의 확장은 훨씬 더 쓰기 쉬워질
것이다. 예를 들어 스택 추적을 수집하는 작업을 생각해보자. 커널에는 커널 코드와
사용자 공간 코드의 결합된 스택 추적을 모으는 추적 기능이 있다. 커널이 사용자 공간으로
컨텍스트 스위치를 되돌리기 직전에 스택 추적의 사용자 공간 부분을 수집하는 것이 더
효율적이다. 스택 추적이 요청되면 커널 부분은 즉시 실행되고, 이어서 계산은 일시
중지되며, 사용자 공간 부분의 수집은 나중에 실행된다. 이 작업 흐름에 BPF를 추가하려면
하나의 논리적 연산을 여러 개의 독립적인 함수로 쪼개야 한다. 현재는 실행 중인 BPF
프로그램을 일시 중지할 방법이 없기 때문이다.

사용자 공간 네트워킹을 구현할 때도 비슷한 문제가 나타난다. [sendmsg()](https://man7.org/linux/man-pages/man2/sendmsg.2.html)로
패킷을 보내려고 하면 결국 [qdisc\_run()](https://elixir.bootlin.com/linux/v7.0.12/source/include/net/pkt_sched.h#L117)을
호출하게 되는데, 이 함수는 다른 스레드가 큐에 넣어둔 것을 보내는 등 그 스레드들을 위한
작업도 수행할 수 있다. 이는 후속 작업이 주된 작업과는 다른 시간과 장소에서 수행되는
또 다른 사례다. Dwivedi는 사람들이 전체 애플리케이션을 BPF로 작성하는 실험을 해왔고,
그 과정에서 같은 종류의 문제가 더 많이 드러난다고 말했다.

[![[Kumar Kartikeya Dwivedi]](https://static.lwn.net/images/2026/kumar-dwivedi-lsfmmbpf-small.png "Kumar Kartikeya Dwivedi")](https://lwn.net/Articles/1077738)

역사적으로 BPF 프로그램은 hook과 callback을 사용해왔다. 그 접근법에 문제가 있는 것은
아니다. 커널 개발자에게 필요한 모든 의미론을 표현할 수 있다. 하지만 그 방식은
프로그래머가 맞춤형 suspend/resume 로직을 작성하고 프로그램을 여러 함수로 나누도록
강제한다. Dwivedi의 해법은 BPF에 코루틴을 도입하는 것이다. 즉, 일시 중지되고, 제어를
커널로 되돌린 뒤, 나중에 재개될 수 있는 함수들이다. 그는 이어서 커널 안에서의 BPF
코루틴 설계를 설명했다.

그는 최선의 해법은 Rust의 asynchronous functions나 C++의 coroutines와 유사한 스택 없는
코루틴이라고 말했다.[^lwn1078380-p11-2] 이런 언어들에서는 컴파일러가 직선형 코드를
일시 중지하고 재개할 수 있는 형태로 다시 작성하는 일을 맡는다. 장점은 BPF verifier의
관점에서 크게 바뀔 것이 별로 없다는 점이다. 코루틴을 재개하는 것은 일반적인 간접 함수
호출처럼 보일 것이고, 컴파일러가 중간 값을 저장하고 불러오는 세부 사항을 처리할 것이다.
verifier는 여전히 전체 프로그램의 제어 흐름이 유효한지 확인해야 하며, 커널 컨텍스트에
걸쳐 나뉜 코드를 처리하려면 일부 변경이 필요할 수 있다.

Dwivedi는 verifier가 보게 될 인터페이스를 설명하기 위해 C++가 코루틴을 구현하는 방식을
조금 자세히 다루었다. 간단히 말해, C++는 코루틴을 resume()하거나 destroy()하는 데 사용할
수 있는 두 개의 함수 포인터를 담은 구조체를 만든다고 그는 말했다. resume()은 같은
구조체에 저장된, 코루틴이 마지막으로 일시 중지된 위치를 기록하는 인덱스를 사용해 switch
문으로 어떤 코드를 실행할지 선택한다. 일시 중지 지점을 넘어 보존되어야 하는 변수는 같은
구조체에 저장된다. 일시 중지 지점을 넘어 보존될 필요가 없는 변수는 스택에 남아 있으며,
작업이 일시 중지될 때 암묵적으로 폐기된다. 커널 리소스가 단순히 잊혀지는 것이 아니라
해제되는지 확인하는 verifier의 일반적인 검사는 BPF 프로그램이 어떤 잠금이나 참조 계수
구조체에 대해서도 그런 일을 하지 못하게 막는다. 두 함수 포인터는 항상 코루틴 구조체의
처음 두 요소이므로, 범용 코드는 코루틴 프레임의 크기나 배치를 알 필요가 없다.

이는 Rust가 asynchronous functions를 컴파일하는 방식과 꽤 비슷하지만, Rust는 resume() 및
destroy() callback을 전달하는 데 자체 타입 시스템을 사용한다는 점이 다르다. 하지만 Rust
컴파일러가 C++와 같은 layout의 구조체를 만들도록 하는 것은 어렵지 않으므로, verifier는
아마 그 하나의 layout만 처리하면 될 것이다. BPF 값의 타입을 추적한다는 관점에서 보면,
코루틴에 연결된 구조체는 스택과 같은 방식으로 처리할 수 있다. 값은 그곳으로 spill되고
그곳에서 load되지만, 특별한 처리는 필요하지 않다.

verifier가 모든 BPF 코드에 적용되는 제약을 검증하는 것 외에 코루틴이 안전한지 확인하기
위해 해야 할 일에는 resume() 및 destroy() 함수 포인터가 덮어써지지 않도록 하는 것,
인덱스가 유효한 값만 갖도록 하는 것, 코루틴이 일시 중지되어 있을 때 destroy()를 호출해도
항상 합법적임을 보장하는 것이 포함된다. verifier는 또한 잠금이 일시 중지 지점을 넘어
유지되지 않는지 확인해야 하지만, 그 검사는 함수가 반환되기 전에 잠금이 해제되는지
판정하는 verifier의 로직을 재사용할 수 있다. 같은 논리로, verifier는 타입에 따라 일시
중지 지점을 넘어 유지되는 map 값들을 무효화해야 할 수도 있다.

Andrii Nakryiko는 verifier가 코루틴이 무한 루프에 들어가지 않도록, 예를 들어 인덱스를
이전 값으로 되돌리는 식의 동작을 하지 않도록 어떻게 보장해야 하는지 물었다. Dwivedi는
코루틴 본문은 여전히 검증되고, 모든 일시 중지 지점에서 verifier가 resume() 호출을
검사하므로, verifier가 기존 루프를 찾아내는 것과 같은 방식으로 어떤 루프든 식별할 수
있다고 말했다. Nakryiko는 더 미묘한 루프에 대해서도 물었지만, Dwivedi는 두 개의 BPF
프로그램이 서로의 타이머를 arm하도록 하는 것은 이미 가능하며, 그런 무한 루프도 커널을
사용 불가능하게 만들지 않는 한 실제 문제를 일으키지 않는다고 지적했다. 더구나 verifier가
BPF 프로그램을 검증된 명령어 100만 개 미만으로 제한하더라도, 사용자가 비용이 큰 kfunc
호출을 많이 수행하는 999,999개 명령어짜리 BPF 프로그램을 사용 가능한 모든 커널 hook에
붙여 시스템을 거의 멈추다시피 느리게 만드는 것을 막을 방법은 없다. 이 제한의 목적은
교착 상태를 일으킬 수 있는 무한 루프를 막아 시스템이 계속 전진할 수 있게 하는 것이지,
BPF 프로그램이 CPU 시간을 낭비하는 것을 막는 것이 아니다.

verifier가 모든 일시 중지 상태에서 BPF 프로그램을 destroy()하는 것(언로드되는 경우)과
resume()하는 것이 항상 유효하다고 확인하기만 하면, 그 프로그램은 BPF의 안전 보장을
우회할 수 없다. 무한 루프를 설정하는 교묘한 방법이 있더라도, 코루틴이 일시 중지될 때마다
잡고 있던 모든 잠금을 해제하고 제어를 커널에 돌려줘야 하므로 커널을 deadlock에 빠뜨릴
수는 없다.

Dwivedi는 진행 중인 프로토타입 구현을 갖고 있지만, 아직 해야 할 일이 더 남아 있다. 예를
들어 그는 코루틴을 사용하는 프로그램을 위한 BTF 디버깅 정보를 확장하고 싶어 한다. 그의
프로토타입은 테스트용 C++ 프로그램이 올바르게 동작하도록 함수의 aggregate return types도
활성화해야 했으므로, 이를 위한 verifier 지원도 필요하다. Rust 지원을 추가하는 것은 그보다
훨씬 더 어렵지는 않을 것이다.

미래를 위한 더 실험적인 아이디어는 일시 중지된 계산이 사용자 공간과 커널 공간 사이를
전환할 수 있게 하는 것이다.[^lwn1078380-p11-3] Dwivedi는 그의 학생 한 명에게 그
프로토타입 작업을 맡겼지만, 그것은 아직 전혀 준비되지 않았다. 언젠가 그것이 실제로
동작하게 된다면, 애플리케이션은 사용자 공간에서 설정 작업을 수행한 뒤 커널로 전환해
네이티브 BPF 기능을 사용하고, 이후 다시 사용자 공간으로 돌아갈 수도 있게 될 것이다. 그런
종류의 인터페이스는 사용자 공간과 커널 사이의 구분을 흐리게 만들겠지만, 설령 실현된다
하더라도 현실이 되기까지는 오랜 시간이 걸릴 것이다.

보다 가까운 시점에서 Dwivedi는 현재 작업을 다듬어 커널에 넣을 준비를 하려 한다. BPF에
코루틴을 통합한다고 해서 기술적으로 새로운 무언가가 가능해지는 것은 아니지만, 그는 이
기능이 하나의 hook이나 callback으로 쉽게 단순화될 수 없는 커널 영역에 BPF 프로그램을 더
쉽게 통합하도록 해주기를 바라고 있다.

[댓글 (9개 게시됨)](https://lwn.net/Articles/1076210/#Comments)

[^lwn1078380-p11-1]: 코루틴은 실행 도중 상태를 보존한 채 제어권을 넘겼다가 이후 같은 지점에서 실행을 이어갈 수 있는 함수 형태를 말한다.
[^lwn1078380-p11-2]: 스택 없는 코루틴은 각 코루틴마다 별도 호출 스택을 유지하기보다 필요한 상태를 컴파일러가 생성한 프레임에 저장하는 방식이다.
[^lwn1078380-p11-3]: 여기서 사용자 공간과 커널 공간 사이를 전환한다는 것은 하나의 논리적 계산이 두 실행 영역을 오가며 이어질 수 있다는 뜻이다.

### [JIT 컴파일된 BPF 코드를 위한 KASAN](https://lwn.net/Articles/1077740/)

글쓴이: **Daroc Alden**  
2026년 6월 23일

---

#### 요약

- Alexis Lothoré는 JIT 컴파일된 BPF 코드에 커널 메모리 접근 검사기인 [KASAN](https://docs.kernel.org/dev-tools/kasan.html) 지원을 추가하는 작업을 소개했다.
- 현재 BPF JIT는 포인터 역참조를 직접 내보내므로, KASAN의 `__asan*()` 검사 호출을 적절한 위치에 삽입하도록 JIT를 수정해야 한다.
- 초기 패치는 x86에서 LDX/STX 같은 기본 load/store 명령에 집중하며, 아직 스택 접근과 다른 메모리 접근 명령은 다루지 않는다.
- 가장 큰 과제는 레지스터 저장·복원으로 인한 오버헤드이며, 인라이닝이나 구현 단순화가 개선 방향으로 논의되었다.
- 참석자들은 제한적인 초기 범위에도 불구하고 이 작업에 전반적으로 긍정적이었으며, 향후 BPF 코드에서도 KASAN을 사용할 수 있을 가능성이 커졌다.

[LSFMM+BPF](https://lwn.net/Articles/lsfmmbpf2026/)

Alexis Lothoré는 커널의 메모리 접근 검사기인
[KASAN](https://docs.kernel.org/dev-tools/kasan.html)을 just-in-time 컴파일된 BPF 코드에 지원하도록 추가하는 작업을 해왔다. 그는 그 작업에 대해 2026년
[Linux Storage, Filesystem, Memory-Management, and BPF Summit](https://events.linuxfoundation.org/lsfmmbpf/)에서 발표했다.
그는 BPF just-in-time (JIT) 컴파일러의 버그를 잡는 데 도움이 되도록 KASAN 지원이 필요하다고 말했다. KASAN은 커널의 메모리 관리 문제를 잡아내는 훌륭한 도구지만, 그것이 감시할 수 있는 코드에서만 그렇다.[^lwn1078380-p12-1]

KASAN은 하드웨어가 무엇을 지원하느냐에 따라 소프트웨어 또는 하드웨어 메모리 태깅을 사용해 use-after-free 버그와 out-of-bounds 접근을 모두 식별할 수 있다고 Lothoré는 말했다. 일반적인 소프트웨어 구현은 메인 메모리의 각 바이트에 대한 접근이 허용되는지를 추적하는 비트맵 역할을 할 메모리 영역을 예약한다. 빌드 시점에 컴파일러는 커널의 모든 포인터 역참조에, 참조된 메모리가 올바른 상태인지 검사하는 특수 `__asan*()` 함수 호출을 추가한다. 커널의 여러 할당자는 비트맵 상태를 갱신하고, 버퍼 오버런을 더 쉽게 잡아내도록 할당 영역 앞뒤에 “red zone”을 삽입하도록 연결되어 있다.

[![[Alexis Lothoré]](https://static.lwn.net/images/2026/alexis-lothoré-lsfmbpf-small.png "Alexis Lothoré")](https://lwn.net/Articles/1078524)

이전에는 BPF JIT가 적절한 `__asan*()` 함수 호출 없이 포인터 역참조를 직접 내보냈다. 따라서 KASAN 지원을 추가하는 일은 적절한 위치에 그런 호출을 내보내도록 JIT를 패치하는 것만큼 단순해야 한다. 이 그림은 BPF 프로그램이 BPF map, arena, 전역 변수, 스택 메모리 등 메인 커널 코드와는 다른 메모리 영역에 접근할 수 있다는 사실 때문에 약간 복잡해진다. 특히 현재 BPF 스택은 하나의 큰 메모리 영역으로 취급되지만, KASAN이 잘못된 접근을 더 세밀하게 감지하도록 돕기 위해 각 변수 사이에 red zone을 두는 식으로 수정될 가능성도 있다고 Lothoré는 말했다.

그는 올해 초부터, 우선 x86에서 JIT 코드에 KASAN 지원을 추가하는
[패치](https://lwn.net/ml/bpf/20260604-kasan-v2-0-c066e627fda8@bootlin.com/)를 작업해왔다. 현재로서는 기본적인 load와 store에 해당하는 LDX 및 STX BPF 명령에 집중해왔는데, 메모리에 접근할 수 있는 다른 명령들도 있기는 하다. 그의 코드는 또한 당분간 스택을 대상으로 하는 load와 store를 무시한다. 이 두 명령만 대상으로 해도 오버헤드는 여전히 상당히 심하다. 그의 패치는 본질적으로 명령 하나를 열두 개로 바꾼다. 하지만 Lothoré는 약간의 노력으로 이를 단순화할 수 있다고 믿고 있다.

오버헤드의 대부분은 레지스터를 저장하고 복원하는 데서 오는데, José Marchesi는 `__asan*()` 함수를 인라인할 수 있다면 이것이 필요하지 않을 수도 있다고 지적했다. Lothoré는 원칙적으로 도움이 될 수 있다는 데 동의했지만, 컴파일러는 그의 코드보다 훨씬 똑똑하며 순진한 인라이닝은 더 나쁠 것이라고 지적했다. 청중 중 한 명은 왜 Lothoré가 컴파일러나 verifier에 KASAN instrumentation을 추가하는 대신 JIT에서 이 작업을 하고 있는지 물었다. 그는 그렇게 하려면 안정적인 KASAN API를 노출해야 하며, KASAN을 활성화한 커널용으로 BPF 프로그램을 다르게 컴파일해야 하게 되므로, KASAN으로 테스트를 설정할 때 추가적인 골칫거리가 될 것이라고 설명했다.[^lwn1078380-p12-2]

다른 사람은 BPF JIT와 함께 KASAN을 사용해 지금까지 어떤 버그가 드러났는지 알고 싶어 했다. 아직은 아니라고 Lothoré는 말했다. 다만 그것은 주로 그의 패치가 아직 들어가지 않았고, 따라서 커널이 KASAN으로 테스트되는 많은 환경에서 아직 실행되지 않았기 때문이다. 그래도 instrumentation은 동작한다. KASAN이 BPF 코드를 포함하는 보고서를 생성할 수 있기 때문이다.

또 다른 사람은 KASAN 보고서를 그것을 유발한 BPF 프로그램과 어떻게 연결할 수 있는지 알고 싶어 했다. KASAN 오류 메시지에는 BPF 함수 이름이 포함될 것이라고 Lothoré는 말했다. Alexei Starovoitov는 프로그램이 BTF로 컴파일되었다면 파일 이름, 줄 번호 등도 볼 수 있을 것이라고 덧붙였다. Cupertino Miranda는 `__asan*()` 함수가 어디에 정의되어 있는지 물었다. Lothoré는 그것들이 컴파일러의 user-space address sanitizer 일부가 아니라 커널의 일부라고 설명했다.

다음 단계에는 그의 코드가 처리하는 BPF 명령의 수를 늘리는 일이 포함되며, 특히 atomic 명령이 중요하다. 그는 그것들이 KASAN load, store, 또는 새로운 종류의 연산으로 간주되어야 하는지 확신하지 못했다. Starovoitov는 atomic이 verifier 버그를 감추는 방식으로 사용될 가능성은 낮으며, 기본 load와 store에 대한 커버리지를 확보하는 것과 비교하면 모든 경우를 완전히 포괄하는 것은 그만한 가치가 없을 가능성이 높다고 의견을 밝혔다.
현재 패치 세트의 범위가 제한적임에도, Lothoré의 작업은 모인 개발자들로부터 전반적인 승인을 받았다. BPF 코드에서도 KASAN을 사용할 수 있게 되기까지 그리 오래 걸리지 않을지도 모른다.[^lwn1078380-p12-3]

[댓글(아직 없음)](https://lwn.net/Articles/1077740/#Comments)

[^lwn1078380-p12-1]: KASAN은 Kernel Address Sanitizer의 약자로, 커널 코드에서 잘못된 메모리 접근을 탐지하는 디버깅 기능이다.
[^lwn1078380-p12-2]: BPF verifier는 BPF 프로그램이 커널에서 안전하게 실행될 수 있는지 실행 전에 검사하는 구성요소다.
[^lwn1078380-p12-3]: 여기서 “coverage”는 테스트 커버리지라기보다 KASAN 검사가 적용되는 BPF 메모리 접근 범위를 뜻한다.

### [RMR과 BRMR을 이용한 단일 홉 블록 복제](https://lwn.net/Articles/1074291/)

2026년 6월 18일

이 글은 Haris Iqbal이 기고했습니다

#### 요약

- 클라우드 환경에서 RDMA 기반 스토리지 패브릭 위에 내구성 있는 가상 블록 장치를 효율적으로 제공하기 위한 RMR/BRMR 설계를 소개한다.
- RMR은 RTRS 위에서 신뢰성 있는 멀티캐스트 복제를 제공하고, BRMR은 이를 블록 장치로 노출하는 얇은 어댑터 역할을 한다.
- 더티 맵과 `map_ver`를 이용해 장애 동안 누락된 I/O를 추적하고, 복구 트래픽을 컴퓨트 호스트가 아닌 스토리지 노드 간 단일 홉으로 처리한다.
- 네트워크 장애, 스토리지 노드 재부팅, 유지보수 모드, 컴퓨트 클라이언트의 중간 쓰기 중단 등 여러 장애 복구 흐름을 다룬다.
- 기존 DRBD나 MD-RAID 1이 이 요구사항을 만족하기 어려운 이유와, 새 모듈이 필요한 배경을 설명한다.

클라우드 제공자는 내구성 있는 가상 블록 장치를 어떻게 효율적으로 제공할 수 있을까? Remote Direct Memory Access (RDMA)[^lwn1078380-p13-rdma]는 클러스터의 서버들이 메모리 조각을 공유할 방법을 제공하지만, 블록 장치에 기대되는 보장을 제공하려면 여전히 RDMA 위에서 동작하는 프로토콜이 필요하다. 커널의 RDMA transport library (RTRS)는 RDMA를 통해 메시지를 보낼 방법을 제공한다. 나는 2026년 [Linux Storage, Filesystem, Memory Management and BPF Summit](https://events.linuxfoundation.org/lsfmmbpf/)에서 RTRS 위에 구축한 두 가지 새 구성 요소, Reliable Multicast over RTRS (RMR)와 Block device over RMR (BRMR)에 대해 [발표](https://lwn.net/images/2026/RMR_BRMR.pdf)했다. Jia Li와 함께 작업 중인 이 모듈들은 클라우드 제공자가 가능한 한 적은 오버헤드로 내구성 있는 블록 장치를 노출하는 방법이 될 수 있다. 하지만 이를 이루려면 모듈을 업스트림으로 보내기 전에 커뮤니티의 논의와 피드백이 필요하다.

#### 문제

이 패치들은 일반적으로 컴퓨트 계층과, RDMA 패브릭으로 연결된 별도의 스토리지 계층을 가진 클라우드 제공자를 겨냥한다. 서비스를 안정적으로 유지하려면 컴퓨트 호스트의 블록 장치는 보통 최소 두 개의 스토리지 노드에 동기식으로 복제되어야 하며, 좋은 성능을 보장하기 위해 각 복제에는 가급적 단일 네트워크 홉만 사용해야 한다. 일반적으로 발생할 수 있는 모든 종류의 장애(네트워크 중단, 디스크 교체, 스토리지 노드 재부팅, 컴퓨트 클라이언트의 완전한 크래시)는 운영자 개입 없이 복구되어야 한다. 물론 이 패치들은 이런 종류의 견고한 블록 수준 복제를 필요로 하는 비(非)클라우드 제공자 조직에도 유용하다.

컴퓨트 호스트의 CPU와 RAM은 수익을 만들어내는 자원이다. 복제나 재동기화에 쓰이는 모든 사이클은 고객에게 판매할 수 없는 사이클이다. 그래서 우리가 따르는 설계 제약은 다음과 같다. 컴퓨트 호스트를 재동기화 데이터 경로에서 제외하라.

트리에 이미 들어 있는 두 가지 기존 선택지는 각각 이러한 제약 중 하나를 만족하지 못한다. [Distributed Replicated Block Device](https://docs.kernel.org/admin-guide/blockdev/drbd/index.html) (DRBD)의 전통적인 구성은 지정된 primary를 통해 쓰기가 지나가도록 한다. 즉, 2홉 쓰기 경로다. 네트워크 블록 장치 위에 MD-RAID 1(커널의 multiple-device RAID level 1)을 올리면 단일 홉 쓰기가 가능하지만, 성능이 저하된 leg를 재동기화하려면 컴퓨트 호스트에서 정상 leg를 읽고 그 데이터를 복구 중인 leg에 써야 한다. 여기서 "leg"는 쓰기가 팬아웃되는 복제본 사본을 뜻하며, 복제 집합 안의 각 스토리지 노드마다 하나씩 존재한다. 이는 다시 2홉이고, 재동기화 대역폭은 컴퓨트 호스트의 예산 일부를 소모한다.

#### 두 모듈로 이루어진 아키텍처

RMR은 전송 계층이다. 클라이언트 쪽 API는 scatter-gather list와, 그 목록의 데이터를 어떤 leg들로 보낼지를 지정하는 연결 풀을 받는다. RMR은 이를 사용하는 클라이언트, 여기서는 블록 장치에 대해 아무것도 알지 못한다. BRMR은 그 위의 얇은 블록 장치 어댑터다. 커널의 block multi-queue (blk-mq) 계층을 통해 /dev/brmrX를 노출하고, 디스크상의 풀 메타데이터를 소유한다. RMR에는 자체적인 온디스크 형식이 없다.

각 모듈은 클라이언트/서버로 나뉜다. 컴퓨트 호스트는 RMR 및 BRMR 클라이언트를 실행한다. 각 스토리지 노드는 RMR 서버, BRMR 서버, 그리고 스토리지 피어에 연결된 RMR 클라이언트를 실행한다. 스토리지 서버에 상주하는 그 RMR 클라이언트 덕분에 복구 트래픽은 컴퓨트 호스트를 건드리지 않고 전용 RTRS 세션에서 스토리지-대-스토리지로 단일 홉 흐름을 가질 수 있다.

풀(pool)은 복제의 단위다. 하나의 BRMR 장치는 하나의 RMR 풀에 매핑되며, 그 풀에는 스토리지 노드당 하나씩 N개의 클라이언트-서버 세션이 있다. 각 스토리지 노드는 풀 안에서 member ID로 식별된다. 세션은 sysfs를 통해 런타임에 추가, 제거, 분해(disassemble), 교체될 수 있다. 세션 상태는 NORMAL(정상이라는 뜻), FAILED, 또는 RECONNECTING인지 나타낸다. "primary" leg는 없다. 정상 상태(steady state)에서는 모든 NORMAL 세션이 라운드 로빈으로 읽기를 처리하고, 클라이언트의 멀티캐스트 팬아웃을 통해 쓰기를 받아들인다.

#### 더티 맵

네트워크 장애나 실패 때문에 놓친 I/O 작업을 추적하기 위해 RMR은 풀 안의 모든 스토리지 멤버에 대한 엔트리를 담은 더티 맵을 사용한다. 각 스토리지 멤버는 더티 맵 사본을 보유한다. 어떤 스토리지 멤버가 놓친 I/O 작업은 다른 사용 가능한 스토리지 멤버들이 가진 더티 맵에 기록된다. 스토리지 멤버가 어떤 종류의 장애에서든 돌아오면, 재연결 과정의 일부로 다른 스토리지 멤버들로부터 최신 더티 맵을 받는다. 그러면 무엇을 재동기화해야 하는지 파악할 수 있다.

RMR의 더티 맵은 2단계 페이지 테이블을 포함한다. first-level page (FLP)는 second-level page (SLP)를 가리키는 포인터 배열이다. 각 SLP는 한 페이지이며 4096개의 1바이트 엔트리를 담는다. 그 바이트 중 한 비트는 더티 비트, 하나는 "syncing" 필터 비트이고, 여섯 비트는 향후 플래그를 위해 예약되어 있다.

청크당 1바이트 레이아웃은 스토리지 백엔드가 교체되는 경우처럼 특별한 상황에서 클라이언트 모듈이 추가하는 맵 엔트리를 추적해야 하기 때문에 선택되었다. 현재 백엔드 교체 기능은 좀 더 작업이 필요해 비활성화되어 있다. 이 기능이 활성화되면 청크당 1바이트가 필요한지 다시 검토해야 한다. 나중에는 청크당 1비트 설계로 이동할 수도 있다.

각각 512개 엔트리를 가진 최대 256개의 FLP가 4096바이트 SLP를 가리킬 수 있으며, 이를 통해 맵은 5억 개가 조금 넘는 청크를 추적할 수 있다. 최대 청크 크기인 1MB에서는 풀당 512TB에 해당한다. 맵이 완전히 채워지면 이 메타데이터에 512MB의 메모리를 사용한다. 청크 크기는 128KB부터 1MB까지의 2의 거듭제곱이므로, 풀당 용량은 64TB에서 512TB까지이며 어떤 주소가 어느 청크에 속하는지는 한 번의 시프트로 계산할 수 있다.

이 맵은 단순한 비트맵 이상이다. 더티 비트와 나란히, 멤버별 맵은 현재 처리 중인 각 더티 청크마다 하나의 엔트리를 가진 활성 동기화 엔트리의 [XArray](https://docs.kernel.org/core-api/xarray.html)도 담고 있다. 각 엔트리는 참조 카운트와 대기 목록을 가진다. 어떤 청크에 대한 동기화가 진행 중일 때 그 청크에 도착한 I/O 작업은 대기 목록에 머물고, 동기화가 완료되면 깨어난다. 이 설계는 전역 락이나 노드 간 동시성 조정 없이, I/O 작업을 처리하면서 청크를 재동기화할 수 있게 한다.

세션이 NORMAL에서 FAILED로 전환될 때마다 64비트 단조 증가 버전 번호인 map\_ver가 증가한다. 진행 중인 I/O 작업은 이 버전 번호를 지니므로, 복구 중에는 가장 높은 map\_ver를 가진 생존 노드가 권위 있는 소스가 된다. 동률이 있으면 두 노드는 같은 맵을 가져야 하므로 하나를 임의로 선택한다. 현재 코드는 백엔드 교체 기능을 위해 map\_ver의 상위 비트를 "replace" 플래그로 취급한다.

#### 데이터 경로

컴퓨트 클라이언트의 쓰기는 NORMAL 상태인 모든 세션에 병렬로 발행된다. I/O 작업은 모든 세션이 성공이든 실패든 이를 확인(acknowledge)한 뒤에만 상위 계층에 확인된다. 한 멤버에서 쓰기가 실패하면, 풀의 모든 생존 멤버가 그 멤버의 맵에 있는 영향받은 청크를 각자의 사본에서 dirty로 설정한다. 이것이 map\_add 프로토콜 작업이다.

세션 하나가 non-NORMAL이 되면, 이후 남아 있는 사용 가능한 멤버들로 향하는 모든 쓰기는 데이터 페이로드와 함께 실패한 멤버의 ID를 싣고 간다. 쓰기를 받는 멤버들은 이 정보를 자기 더티 맵 사본에 추가한다. 이것이 map\_add 피기백이다. 명시적인 map\_add remote procedure call (RPC)은 세션이 실패했을 때 이미 wire 위에 있던 진행 중 I/O 작업에 대해서만 필요하다.

읽기는 NORMAL 세션들 사이에서 라운드 로빈 방식으로 처리되므로, 정상 상태의 읽기 처리량은 복제본 수에 따라 확장된다. 서버 쪽에서는 들어오는 I/O 작업이 대상 청크에 대한 로컬 더티 맵을 확인한다. 청크가 깨끗하면 I/O 작업은 곧장 backing store로 간다.

더티한 경우는 더 복잡하다. 서버는 해당 청크를 syncing으로 표시하고 스토리지 쪽 RMR 클라이언트를 통해 피어에서 동기식 읽기를 발행한다. 같은 청크에 대한 동시 I/O 작업은 대기 목록에 머물며 동기화가 완료되면 깨어난다.

복구 중인 서버 풀의 백그라운드 동기화 스레드도 같은 일을 대량으로 수행한다. 이 스레드가 수행하는 병렬 작업 수는 sync\_queue\_depth라는 모듈 매개변수로 제한되며, 기본값은 32이고 풀의 RTRS permit count(세션당 RTRS가 미리 할당하는 진행 중 RDMA 작업 수, 기본값은 512)로 상한이 정해진다.

#### 장애 복구

발표에서는 네 가지 장애 사례를 다루었다. 처음 세 가지는 하나의 흐름의 변형이다. 네트워크 또는 로컬 I/O 장애는 영향받은 세션을 FAILED로 이동시킨다. 더티 비트는 map\_add 피기백을 통해 전파된다. 네트워크가 복구되면 링크 이벤트가 생성되고, 이로 인해 세션이 재연결되며(RECONNECTING 상태로 전환된다). 그런 다음 복구 워커는 세션을 검사해 저장소가 여전히 I/O 작업을 처리할 수 있는지 확인하고, 성공하면 해당 세션은 NORMAL 피어로부터 더티 맵을 다시 채우는 맵 업데이트 과정을 거친 뒤 NORMAL로 돌아간다.

스토리지 노드 크래시 뒤 재부팅되는 경우도 위와 같은 흐름이다. 스토리지 노드가 다시 올라오면 RMR 메타데이터가 backing store에 존재하므로 join/rejoin 메시지를 기대한다. 그런 다음 NORMAL 상태로 돌아가기 전에 맵 업데이트 과정을 거친다. maintenance-mode 진입은 같은 경로의 운영자 주도 버전이며, 말 그대로 유지보수 목적으로 사용하도록 의도되어 있다.

네 번째 사례는 컴퓨트 클라이언트가 쓰기 도중 크래시하는 경우다. 클라이언트가 죽으면 어떤 leg들은 특정 쓰기를 받았을 수 있고 다른 leg들은 받지 못했을 수 있으며, 클라이언트 자신은 더 이상 생존 노드들에게 어떤 청크가 진행 중이었는지 알려줄 수 없다. 그대로 두면 쓰기를 받아 backing store에 쓴 스토리지 노드들은 이 쓰기를 받지 못한 노드들과 다른 데이터를 보유하게 된다. 여기서 last\_io가 등장한다.

각 스토리지 노드는 queue\_depth 길이의 last\_io 배열을 유지하며, 이 배열은 I/O 요청의 mem\_id(요청이 큐에서 가진 슬롯 인덱스, 범위 [0, queue\_depth-1])로 인덱싱된다. 성공한 모든 쓰기는 해당 슬롯에 그 청크 ID를 기록하므로, 어느 순간이든 각 스토리지 노드는 자신이 확인한 가장 최근 queue\_depth개 청크의 기록을 보유한다. 같은 청크가 여러 노드의 last\_io에 나타나면, 먼저 처리한 노드만 이긴다. 나머지 노드들은 그 청크가 이미 dirty임을 발견하고 건너뛴다.

여기에는 한 가지 약점이 있다. 컴퓨트 클라이언트가 쓰기 도중 크래시하고 복구가 완료되기 전에 스토리지 노드도 크래시하면, 그 스토리지 노드의 메모리 내 last\_io가 사라지고 불일치를 더 이상 감지할 수 없다. 이는 last\_io가 기록되지 않았던 경우와 같은 상황이다. 완화책은 last\_io를 backing store에 쓰는 것이다. BRMR의 영속화 경로는 코드에 존재하지만, 적절한 일관성 보장을 찾는 일은 아직 할 일 목록에 있다.

열린 질문은 last\_io를 데이터 쓰기와 원자적으로 써야 하는지, 아니면 뒤따르는 메타데이터 쓰기로 써야 하는지다. 이 선택은 실제 성능에 영향을 준다. 한 청중은 그 답이 RMR/BRMR이 그 위 계층에 제공하는 크래시 일관성 계약에 달려 있다고 지적했다.[^lwn1078380-p13-consistency]

#### 왜 새 모듈인가?

왜 그냥 DRBD를 확장하거나 MD-RAID 1을 사용하지 않는가? 이는 [LSFMM 제안](https://lwn.net/ml/all/CAJpMwyiVqqbR3ni%2BURv0uPnE0Bgt_%2Bd%2B-_%2B_t6E3wzfiUOT-cg%40mail.gmail.com/)이 나갔을 때 메일링 리스트에서 처음 제기된 질문이었다. DRBD의 리소스 및 역할 모델은 writer가 데이터 사본 중 하나이고, 하나의 peer가 직렬화 담당자(serializer)라고 가정한다. 이러한 가정은 DRBD의 요청 경로, 상태 머신, 온디스크 형식 깊숙이 자리 잡고 있다. 네트워크 블록 장치 위의 MD-RAID 1은 단일 홉 쓰기를 제공하지만, 그 대가로 컴퓨트 호스트를 거치는 2홉 재동기화를 치른다.

[^lwn1078380-p13-rdma]: RDMA는 CPU 개입을 줄여 원격 메모리에 직접 접근하도록 하는 네트워크 기술로, 스토리지 클러스터에서 낮은 지연시간과 높은 처리량을 얻기 위해 자주 사용된다.
[^lwn1078380-p13-consistency]: 크래시 일관성 계약은 장애 이후 상위 계층이 어떤 데이터 상태를 관찰할 수 있는지에 대한 보장을 뜻한다.

멀티캐스트 전송 계층인 RMR 자체는 블록 스토리지 밖에서도 재사용할 수 있다.[^lwn1078380-p14-1]
같은 fabric 위의 key-value store나 S3 스타일 object store도 같은 전달 보장을 원할 것이다.
RMR을 블록 계층의 가정에서 자유롭게 유지하면 그런 선택지를 보존할 수 있다.

#### DRBD 9: 컨퍼런스 중 드러난 변수

메일링 리스트에서 Philipp Reisner는 DRBD 9가 이미 RMR과 매우 비슷해 보이는 구성을
지원한다고 [지적했다](https://lwn.net/ml/all/afm2PewS5Gi5QU61@ryzen9/).
DRBD의 용어로 말하면, 이는 여러 스토리지 노드에 연결된 diskless primary이며,
네트워킹은 플러그형 전송 모듈로 추상화된다. TCP, load-balanced multipath TCP,
그리고 RDMA가 그것이다. diskless primary는 mesh 위에서 스토리지 피어들에게 병렬로
쓰기 작업을 뿌리며, 이는 쓰기 경로에서 한 hop이다. DRBD 9의 mesh 연결은 복구 경로에서
primary를 우회해, 한 secondary가 다른 secondary로부터 직접 재동기화할 수도 있게 한다.[^lwn1078380-p14-2]

따라서 RMR이 보장하는 두 속성, 즉 로컬 복사본이 없는 writer에서 출발하는 single-hop 쓰기와
writer를 루프에 포함하지 않는 peer-to-peer 재동기화는 모두 DRBD 9에서 사용할 수 있어 보인다.
DRBD 9의 diskless-primary 모드와 비교 실행을 후속 작업으로 계획하고 있다. 이 구성은
컨퍼런스 중 메일링 리스트에서야 드러났고, 관련 코드는 [LINBIT](https://linbit.com/)의
개발자들이 공유하지 않았다. 발표 전 평가는 불가능했다.

RMR을 별도로 유지해야 하는지, 아니면 DRBD 9의 장치를 더 많이 끌어올려 그 on-disk format을
채택하는 것이 옳은 방향인지는 그 비교가 답해야 할 질문이다. 완전히 DRBD 9로 옮기는
선택지도 있지만, 그것은 DRBD 9의 성능이 네트워크 블록 장치 위의 MD-RAID 1과
오늘날 RMR/BRMR이 제공하는 수준에 맞먹을 때에만 가능하다.

#### 전송 계층을 통하지 말고, 그 위에서

Leon Romanovsky는 컨퍼런스 중 나에게 두 가지 아키텍처상의 논점을 제기했고, 나중에
그 내용을 [메일링 리스트에 정리했다](https://lwn.net/ml/all/20260512103424.GR15586@unreal/).
첫 번째는 계층화에 관한 지적이었다. 복제와 dirty-tracking은 RDMA에만 해당하는 관심사가
아니다. 블록 계층은 MD-RAID, device-mapper mirror(DM-mirror), DRBD에서 수십 년 동안
그것들을 갖고 있었다. 따라서 새 복제 엔진은 RDMA를 가능한 하부 기반 중 하나로 두고,
전송 계층 위에 있어야 한다. 사용자는 복제 로직을 다시 쓰지 않고도 RTRS를 TCP,
nvme-tcp, 또는 다른 무엇으로든 바꿀 수 있어야 한다. RMR은 RDMA stack 안에 있기 때문에,
코드 자체가 블록 계층의 가정을 피하고 있더라도 전송 계층에 결합되어 있는 것처럼 보인다.

현재 코드는 그 분리의 일부를 지키고 있다. RMR 본체에는 블록에 관한 지식이 없고,
BRMR이 blk-mq와 on-disk format을 처리하는 계층이다. 하지만 dirty map, state machine,
recovery worker는 모두 RMR client 안에 있으며, 오직 그것을 통해서만 접근할 수 있다.

Dirty-tracking과 multi-leg state machine을 전송 계층 위로 밀어 올리는 방법은 여러 가지가
있을 수 있다.[^lwn1078380-p14-3] 가장 단순한 방법은 그 부분들을 블록 계층의 데이터 복제
모듈로 끌어올리고, RTRS 바인딩은 그 주변의 얇은 shim으로 남겨두는 것이다.

두 번째 지적은 커널 리뷰 절차에 관한 것이었다. in-tree consumer가 하나뿐인 커널 모듈은
설득하기 어렵다. RMR은 적어도 하나의 다른 장래 in-kernel 사용자를 제시할 수 있어야 하며,
이상적으로는 처음부터 그것을 수용할 수 있어야 한다. Li와 나는 이 작업이 Linux 커뮤니티와
업계의 관심을 끌고, 누군가 다른 쓰임새를 찾아내기를 바라고 있다.

RMR-as-transport의 원래 설계 의도는 같은 reliable multicast 계층을 같은 fabric 위의
key-value store나 object store 아래에서도 사용할 수 있게 하는 것이었다. 하지만 우리가
아는 한 어디에서도 두 번째 consumer가 개발되고 있지는 않다.

#### 앞으로의 작업 방향

열려 있는 주제가 몇 가지 있다. 우리는 last\_io 지속성 문제를 다루고, Romanovsky가 제안한
계층화 리팩터링을 추진하며, DRBD 9의 diskless-primary 모드와 비교를 수행하고자 한다.
그 결과는 후속으로 메일링 리스트에 올릴 예정이다.

코드는 GPL-2.0-or-later이며 활발히 개발 중이다. 이 프로젝트에 관심이 있다면 한번
시도해보라. 더 쉬운 VM 기반 설정 방법은 곧
[문서 사이트](https://ionos-cloud.github.io/rmr.io/)에 게시될 예정이다. 기여를 환영한다.
BRMR/RMR에 관해 생각이나 질문이 있거나 단지 더 알아보고 싶다면
haris.iqbal@ionos.com 및 jia.li@ionos.com 으로 자유롭게 연락해도 된다.

[댓글 (2개 게시됨)](https://lwn.net/Articles/1074291/#Comments)

[^lwn1078380-p14-1]: RMR은 이 기사에서 다루는 reliable multicast 기반 전송 계층을 가리키며, BRMR은 이를 블록 복제 용도로 사용하는 계층이다.
[^lwn1078380-p14-2]: DRBD에서 primary와 secondary는 각각 쓰기를 받아들이는 주 노드와 복제본을 유지하는 보조 노드를 뜻한다.
[^lwn1078380-p14-3]: “multi-leg”는 하나의 복제 작업이 여러 네트워크 경로나 대상 노드로 동시에 뻗어 나가는 구조를 가리킨다.

### [OSPM 2026 첫째 날 보고](https://lwn.net/Articles/1077759/)

글쓴이: **Jonathan Corbet**  
2026년 6월 22일

---

[OSPM](https://lwn.net/Archives/ConferenceIndex/#OS-Directed_Power-Management_Summit-2026)

[Linux Kernel의 전력 관리와 스케줄링 서밋](https://retis.santannapisa.it/ospm-summit/)은 역사적인 약어인 OSPM이라는 이름을 여전히 사용하며, 4월 중순 영국 케임브리지에서 열렸다. 이제 전통이 된 것처럼, 이 행사 발표자들은 이후 각 세션의 요약을 작성했고, 이 글은 LWN에 게재할 수 있도록 제공되었다. 첫째 날 세션에서는 idle-state 선택, sched\_ext를 사용한 사용자 공간 스케줄러, 락 보유자 선점 등 매우 다양한 주제를 다루었다.

(함께 보기: [둘째 날](https://lwn.net/Articles/1078696/) 및 [셋째 날](https://lwn.net/Articles/1078697/) 보도.)

#### 요약

- OSPM 2026 첫째 날에는 CPU 유휴 상태 선택, Intel 프로세서의 에너지 효율 스케줄링, fair scheduler의 작업 순환, sched\_ext의 남은 과제 등이 논의되었다.
- cpuidle governor가 “얕은” idle state 쪽으로 보수적으로 판단하는 것이 항상 안전하지 않을 수 있으며, 일부 전력 제약 시스템에서는 성능까지 악화될 수 있다는 문제가 제기되었다.
- Intel hybrid processor에서는 EAS의 대안으로 E-core에 더 높은 배치 우선순위를 주는 asymmetric packing 방식이 소개되었지만, 별도 메커니즘을 추가하기보다 EAS를 확장해야 한다는 반론도 나왔다.
- fair scheduler에서 CPU 간 작업의 실제 전진 정도를 더 공정하게 맞추려는 rotating task scheduler 접근은 특정 HMP 사례에는 효과가 있었지만 upstream에 넣기에는 한계가 크다고 평가되었다.
- sched\_ext는 BPF 프로그램으로 CPU scheduler를 런타임에 교체할 수 있게 해 주며 빠르게 성숙했지만, 아키텍처와 통합 측면의 과제는 계속 논의 중이다.

#### CPU idle state 선택의 성공 기준 — Rafael J. Wysocki

컨퍼런스 첫 세션에서 cpuidle subsystem maintainer인 Rafael Wysocki는 cpuidle governor가 내리는 결정의 품질을 측정하는 문제를 논의했다.

그는 먼저 Linux kernel의 CPU idle time management 코드의 설계와 목적을 되짚으며 시작했다. 이 코드의 목적은 “아무것도 하지 않는 일을 효율적으로 하는 것”이다. 이는 논리 CPU, 즉 symmetric multi-threading(SMT) thread이거나 SMT가 활성화되어 있지 않을 때의 core가 idle 상태가 되면(다시 말해 그 위에서 실행할 task가 없으면) 이를 멈출 기회가 생긴다는 관찰에 기반한다. 그렇게 하면 processor의 전력 소비가 줄어들고, 일반적으로 어느 정도 에너지를 절약할 수 있다. 물론 이를 위해서는 hardware 지원이 필요하지만, 현대 processor 대부분은 이를 제공한다.

CPU scheduler는 idle CPU가 idle loop라고 불리는 특별한 코드를 실행하도록 지시한다. 이 코드의 역할은 가능하다면 processor 기능을 활용해 전력을 줄이는 것이다. 이를 위해 idle loop는 매 반복마다 cpuidle subsystem을 호출한다. 이 subsystem은 세 부분으로 구성된다. 동작을 조율하고 user space에 interface를 제공하는 core, 주어진 CPU를 멈추고 processor 전력을 줄이기 위해 processor interface(대부분의 경우 platform-specific interface)를 사용하는 driver, 그리고 driver가 processor 전력 절감을 어느 정도까지 진행할 수 있는지를 결정하는 governor이다.

idle loop의 각 반복은 먼저 CPU에 여전히 실행할 task가 없는지 확인하고, 그렇다면 cpuidle governor를 호출해 결정을 내리게 한다. 이 결정에는 해당 CPU가 불필요하게 깨어나는 것을 막기 위해 scheduler tick을 멈출지 여부도 포함된다. 다음으로 governor가 내린 결정에 따라 processor 상태를 바꾸도록 driver를 호출한다. 이 코드를 실행 중인 CPU는 scheduler 관점에서는 idle 상태이며, 멈추고 processor 전력을 줄일 수 있다. 결국 CPU는 wakeup event(예를 들어 interrupt)를 받고 scheduler로 돌아가거나 idle loop의 다음 반복에 들어간다.

cpuidle governor의 결정은 processor 기능에 대한 정보를 바탕으로 한다. 이 정보는 cpuidle driver가 이른바 “idle state” 목록 형태로 제공한다. 각 state는 주어진 CPU를 멈춘 뒤 processor가 들어갈 수 있는, 전력이 낮아진 configuration을 나타낸다. state는 두 매개변수로 특징지어진다. target residency(해당 idle state를 선택하는 것이 의미 있으려면 그 state에서 보내야 하는 최소 시간)와 exit latency(CPU가 다시 instruction을 실행할 수 있게 되기까지 processor에 걸리는 최악의 시간)이다. driver가 제공하는 idle state 목록은 target residency와 exit latency가 모두 증가하는 순서로 정렬된다. 이 매개변수 값이 낮은 idle state를 “shallower”라고 부르며, 목록에서 그 뒤에 오는 idle state를 “deeper”라고 부른다.[^lwn1078380-p15-1]

문제는 governor가 CPU가 실제로 얼마나 오래 idle 상태일지를 알지 못한다는 데 있다. 그럼에도 governor는 앞으로 올 CPU idle 기간, 즉 idle duration에 맞는 idle state를 선택해야 한다. 매번 이를 정확하게 하려면 수정 구슬이 필요하지만, 그런 물건의 공급은 상당히 제한되어 있다. 따라서 governor는 통계에 의존해야 하고, 기존 governor들이 대부분의 경우 정확한 결정을 내리려고 노력하더라도 그 결정은 결코 완벽할 수 없다. 그렇다면 문제는 “shallower” 쪽과 “deeper” 쪽 중 어느 쪽으로 틀리는 편이 더 나은가이다.

분명히, 선택된 idle state의 target residency가 idle duration을 초과하면(즉 지나치게 deep한 idle state가 선택되면) energy efficiency와 performance가 모두 나빠진다. shallower idle state를 사용했다면 더 많은 에너지를 절약할 수 있었고 workload에 도입되는 latency도 더 낮았을 것이기 때문이다. 반대로 선택된 idle state의 target residency가 너무 짧으면, 역시 energy efficiency가 나빠진다. deeper idle state를 선택했다면 더 많은 에너지를 절약할 수 있었기 때문이다. 하지만 performance는 손상되지 않는다. 이론적으로는 shallower state를 고르는 것이 performance를 향상시키기까지 해야 한다. shallower idle state의 exit latency가 deeper state의 exit latency보다 낮기 때문이다.

이는 shallower 쪽으로 틀리는 것이 약간 더 낫다는 점을 시사하는 듯하며, Wysocki에 따르면 이 주제가 OSPM Summit에서 [마지막으로 논의되었던](https://lwn.net/Articles/793372/) 2019년의 합의도 그러했다. 그러나 더 최근에는 지나치게 shallow한 idle state를 선택하는 것 역시 performance를 해치는 system들이 있다는 사실이 드러났다.

문제가 된 system들(이국적인 x86 SoC 기반 Chromebook)에서 그런 결과가 나타나는 정확한 mechanism은 아직 명확히 식별되지 않았다. 다만 이들 system에서 deep idle state를 사용하면 shallow idle state를 사용할 때보다 non-idle CPU의 frequency가 더 높아질 수 있으며, 바쁜 CPU들은 전력 제약을 받는다는 점이 관찰되었다. 이는 idle state로 인한 전력 절감이 실제로 system 전체의 energy usage를 낮추는 것이 아니라, idle CPU가 아낀 에너지를 아직 instruction을 실행 중인 CPU의 frequency를 끌어올리는 데 쓰게 해 준다는 뜻일 가능성이 크다. 다시 말해 energy-efficiency optimization으로 설계된 것이 전혀 예상되지 않았던 power-distribution mechanism이 된 것이다.

돌이켜보면 이는 예상했어야 했던 일일지도 모른다. 전력 제약을 받는 system이 매우 많기 때문이다. 실제로 오늘날 출하되는 client platform의 압도적 다수는 주로 열적으로 까다로운 form factor 때문에 전력 제약을 받는다. 따라서 이 문제는 겉으로 보이는 것보다 실제로 더 널리 퍼져 있을 수 있다.

이는 Linux의 CPU idle time management에 도전 과제를 제기하는 것으로 보인다. Wysocki는 현재로서는 이를 어떻게 다루어야 할지 잘 모르겠다고 인정했다. 그럼에도 그는 이 문제를 모두에게 알리는 것이 유용할 것이라고 생각했다.

**Video:**
[CPU idle state 선택의 성공 기준 - Rafael J. Wysocki (OSPM26)](https://youtu.be/0oE9TXescUc)

#### Intel processor에서 energy-efficient scheduling을 위한 asymmetric packing — Ricardo Neri

OSPM 2025에서 Wysocki는 Intel hybrid processor를 위한 energy-aware-scheduling(EAS) 구현을 [발표했다](https://lwn.net/Articles/1020596/#eas). 그의 energy model은 E-core(energy efficiency에 초점을 둔 더 느린 CPU)가 power-performance curve의 넓은 구간에서 P-core(더 빠르고 performance 지향적인 CPU)보다 효율적이라는 관찰에 기반한다. 근본적인 제한은 현재 형태의 EAS가 wakeup 시점에 prospective operating-point 계산을 수행해야 한다는 점이다. 이는 Intel platform에서 지배적인 frequency scaling mechanism인 hardware-controlled performance scaling과 호환되지 않는다.[^lwn1078380-p15-2]

발표된 대안 접근법은 wakeup마다 드는 비용 계산을 피하고 대신 load balancer에서 동작한다. 이 방식은 asymmetric task packing을 사용해 E-core에 더 높은 배치 우선순위를 부여하는 한편, 무거운 task는 P-core에 남기기 위해 기존 capacity-aware scheduling에 의존한다. [schbench](https://lwn.net/Articles/725238/#schbench) 결과는 EAS와 비슷한 energy consumption을 보이면서 99th percentile latency는 상당히 낮았다.

Vincent Guittot는 EAS latency가 그 packing behavior에서 비롯되며 scheduler slice time을 조정해 완화할 수 있다고 지적했다.

Peter Zijlstra는 병렬적인 energy-efficiency mechanism을 도입하는 데 반대하며, 대신 EAS를 확장해야 한다고 주장했다. 그는 hardware-controlled performance scaling과의 비호환성을 제거하고, packing으로 유발되는 latency를 해결하며, CPU 수가 많은 system으로 확장할 것을 제안했다.

**Video:**
[Intel processor에서 energy-efficient scheduling을 위한 asymmetric packing - Ricardo Neri (OSPM26)](https://youtu.be/zNd63UJX0gM)

#### Linux fair scheduling class의 rotating task scheduler — Pierre Gondois

일부 workload는 platform에 있는 CPU 수만큼 많은 thread로 작업을 나눈다. workload는 모든 thread가 완료되어야만 끝난다. 그러나 work partitioning이 static, 즉 각 thread가 실행할 작업량이 같고 platform이 asymmetric(heterogeneous multi-processing 또는 HMP라고도 함)라면, big CPU에서 실행되는 thread는 little CPU에서 실행되는 thread보다 일찍 끝난다. 더 똑똑한 load distribution이 있다면 어느 정도 performance improvement를 얻을 수 있다.

이는 Linux fair scheduler의 더 일반적인 문제를 드러낸다. CPU 간 forward progress가 모니터링되지 않는다는 점이다. 비슷한 문제는 SMP system에도 존재한다. 두 CPU에서 세 개의 long-running task가 실행될 때, 한 CPU를 공유하는 두 task는 다른 CPU에서 단독으로 실행되는 세 번째 task보다 더 느리게 전진한다.

load balancer는 CPU 사이에서 fair task를 균형 배치한다. long-running task의 경우 load는 task의 nice value와 유사하다. 그 값이 낮을수록 load는 높고, task는 더 많은 running time을 받아야 한다. CPU 사이에서 load를 균형 있게 맞추면 task는 자신에게 합당한 forward progress 양을 대략 받게 된다.

위 예들(HMP의 long-running task, 그리고 두 SMP CPU 위의 세 long-running task)에서 load balancer는 imbalance를 감지하지 못하고 해결할 수도 없다. 실제로 balancing은 task 관점이 아니라 CPU 관점에서 수행되기 때문이다.

task 사이에 forward progress를 공정하게 분배하는 가장 정확한 방법은 global virtual run time을 사용하는 것이다. 하지만 이 solution은 scale하지 않는다. platform의 모든 CPU가 동시에 접근하는 global [red-black tree](https://lwn.net/Articles/184495/)가 필요하기 때문이다.

발표된 접근법은 초기의 contribution-scaled [per-entity load tracking](https://lwn.net/Articles/531853/)(PELT) 구현을 되살리는 것이었다. 현재의 scale-invariant PELT 구현은 추정을 수행하는 CPU의 capacity와 무관하게 task의 크기를 균일하게 추정할 수 있게 한다. 반면 예전의 contribution-scaled PELT는 각 task가 받은 instruction throughput의 양을 측정한다.[^lwn1078380-p15-3]

예전의 throughput-based PELT 구현에 의존해 forward-progress metric을 추정하고, 같은 속도로 전진하지 않는 long-running task들을 swap하는 또 다른 balancing mechanism을 추가함으로써 HMP-specific case가 개선되었다. 절약된 시간의 양은 platform마다 다르다. 안타깝게도 필요한 추가 logic, 제시된 solution의 HMP-specific 성격, 그리고 대부분의 multi-threaded workload가 dynamic partitioning을 사용한다는 사실 때문에 이 solution은 upstream에 적합하지 않다. Scientific workload는 static partitioning에 더 적합한 후보지만, HMP에서 실행될 가능성은 낮다.

**Video:**
[Linux Fair scheduler class의 rotating task scheduler - Pierre Gondois (OSPM26)](https://youtu.be/fdRLLqlrQp0)

#### sched\_ext에는 무엇이 빠져 있는가? — Andrea Righi

Sched\_ext(SCX)는 CPU scheduler를 BPF program으로 런타임에 교체할 수 있게 해 주는 Linux kernel framework이다. SCX는 빠르게 성숙했고 이제 널리 배포할 수 있는 상태가 되었지만, 여러 architecture 및 integration 과제가 여전히 활발히 논의되고 있다.

[^lwn1078380-p15-1]: “shallower/deeper”는 idle state 목록에서 target residency와 exit latency가 더 낮거나 높은 상태를 구분하는 용어다.
[^lwn1078380-p15-2]: 여기서 EAS는 energy-aware scheduling을, E-core/P-core는 Intel hybrid processor의 효율 중심/성능 중심 core를 가리킨다.
[^lwn1078380-p15-3]: PELT는 Linux scheduler가 task와 CPU load를 시간에 따라 추적하기 위해 사용하는 메커니즘이다.

오랫동안 문제가 있었고 7.1 커널 릴리스 전까지 고장 나 있던 ops.dequeue() 콜백이 마침내 수정되어, 코어 스케줄러가 태스크를 BPF 스케줄러의 제어에서 제거하는 시점을 BPF 스케줄러가 안정적으로 볼 수 있게 되었다. 이 변화는 사용자 정의 태스크 큐를 유지하거나 BPF에서 자체 회계 메커니즘을 구현하는 스케줄러에 특히 중요하다.

또 하나의 주요 개선은 SCX 태스크를 위한 전용 데드라인 서버[^lwn1078380-p16-1]의 도입이다. 이전에는 공격적인 SCHED\_FIFO/SCHED\_RR 또는 부하가 큰 fair-class 워크로드가 SCX를 완전히 굶길 수 있었고, 이로 인해 BPF 스케줄러 자체의 문제로 간주되는 워치독 실패가 자주 발생했다. 새 메커니즘은 SCX 태스크를 위해 CPU 대역폭을 예약하며, SCX와 fair 스케줄러 태스크가 정적 파티셔닝 없이 같은 CPU에서 안전하게 공존할 수 있는 “부분 모드”도 가능하게 한다.

데드라인 서버 인프라 자체와 관련해서는 아직 일부 정리 작업이 필요하다. 특히 현재 커널은 부팅 시 정적으로 설정되는 대역폭 예약에 의존한다. 다음 단계는 SCX 스케줄러가 활성화되거나 비활성화될 때 이러한 예약을 자동으로 등록하고 해제하는 것이다. 논의에서는 여러 데드라인 서버의 실행 시간과 주기 값을 설정하는 데 쓰이는 debugfs 인터페이스를 sysfs로 옮기는 문제도 다루어졌다(보안 부팅이나 커널 lockdown이 적용된 시스템에서는 debugfs를 사용할 수 없을 수 있기 때문이다). Zijlstra는 FIFO control-group 재작업이 더 명확히 정의되기 전에는 안정적인 ABI에 확정적으로 묶이기에는 너무 이르다고 주장했다.

논의는 계층적 스케줄링을 둘러싼 향후 작업도 다루었다. [컨트롤 그룹별 하위 스케줄러에 대한 초기 지원](https://lwn.net/Articles/1056014/)은 7.1 릴리스에 포함되어, 컨테이너나 워크로드 전반에서 서로 다른 스케줄링 정책이 공존할 수 있게 했다. 이 계층 구조가 애초에 커널 안에 있어야 하는지에 대한 질문도 제기되었는데, 서로 다른 지연 시간과 대역폭 제약을 가진 여러 스케줄러를 조율하려면 결국 하나의 전역 스케줄링 모델이 필요할 수 있다는 우려가 있었다.

[proxy execution](https://lwn.net/Articles/953438/)과의 통합도 아직 끝나지 않았다. 다음 단계는 남아 있는 설정 충돌을 해결하여, 배포판 커널이 proxy execution과 sched\_ext 지원을 동시에 활성화한 상태로 빌드될 수 있게 하고, 현재의 상호 배제 제약을 제거하는 것이다.

또 다른 미해결 문제는 평가다. SCX에는 이제 점점 더 많은 스케줄러가 함께 제공되지만, 개발자들에게는 특정 워크로드에서 한 스케줄러가 다른 스케줄러보다 왜 더 나은 성능을 내는지 설명해 줄 좋은 도구나 벤치마크가 여전히 부족하다. 이 서브시스템이 실험 단계를 넘어 더 넓은 배포로 이동함에 따라, 그 질문은 남아 있는 커널 작업 자체만큼이나 중요해질 수 있다.

**동영상:**
[What's missing in sched\_ext? -
Andrea Righi (OSPM26)](https://youtu.be/gftTDoV2Nuc)

#### Sched\_ext 오버헤드와 주의점 — Christian Loehle

Loehle는 스케줄러 개발자의 관점에서 sched\_ext를 소개하며 sched\_ext\_ops 콜백, 로컬 및 전역 디스패치 큐(DSQ), 사용자 정의 DSQ를 설명했다. 로컬 및 전역 DSQ 같은 터미널 DSQ[^lwn1078380-p16-2]는 제어권을 코어 sched\_ext 기계 장치로 돌려주는 반면, 사용자 정의 DSQ는 BPF 스케줄러가 순서 지정과 배치 제어를 유지할 수 있게 한다. 실제 정책의 상당 부분은 ops.dispatch()에 들어가는 경우가 많고, select\_cpu()와 enqueue() 같은 wakeup 쪽 콜백은 비용이 낮게 유지되어야 한다.

그런 다음 Loehle는 오버헤드 측정 결과를 다루었다. 간단한 futex wait/wake 테스트는 콜백 구조가 매우 중요하다는 점을 보여주었다. select\_cpu()에서 태스크를 로컬 DSQ에 직접 삽입하면 그 마이크로벤치마크에서는 fair 스케줄러를 이길 수 있었지만, 항상 select\_cpu()와 enqueue()를 모두 거치도록 하면 훨씬 느렸다. 기본적인 빈 sched\_ext 경로는 그보다도 훨씬 더 빨랐는데, 이는 정책이 아니라 BPF 콜백의 비용을 보여준다. 추가 측정은 PELT와 유사한 회계를 위해 태스크 상태를 추적하는 비용을 살펴보았다. runnable 및 quiescent 상태 추적은 hackbench와 CPU-bound 테스트에서 눈에 띄었고, run-time 콜백은 그보다 약간의 비용만 더했으며, tick() 콜백은 특히 1000Hz에서 더 비쌌다.

강연의 후반부는 현재 인터페이스가 여전히 사용하기 불편한 지점에 관한 것이었다. PELT, capacity-aware scheduling, EAS를 구현하려면 runnable, running, sleeping, migrating, stolen-time 상태를 정확히 알아야 하는데, 태스크가 터미널 DSQ, 특히 전역 DSQ 안으로 사라지면 이것이 어려워진다. misfit migration은 scx\_bpf\_reenqueue\_local() 같은 메커니즘으로, 또는 tick()에서 태스크의 slice를 만료시키는 방식으로 근사할 수 있지만, 이러한 접근법은 레이스와 장부 관리 문제를 추가한다. core scheduling과 gang scheduling도 사용자 정의 DSQ, 쿠키, 인터프로세서 인터럽트, 락킹으로 표현할 수 있지만, 형제 CPU를 조율하거나 gang을 원자적으로 전환하는 일은 여전히 어색하다. paired enqueue/dequeue 콜백과 SCX\_ENQ\_IMMED 같은 7.1의 새 기능이 도움이 되지만 모든 문제를 해결하지는 않는다.

논의는 짧았고, 대체로 이러한 주의점의 실질적 결과에 관한 것이었다. 한 가지 주제는 공유 DSQ에서의 캐시 라인 바운싱이었는데, 예를 들어 클러스터 도메인마다 하나의 큐를 사용하는 식으로 DSQ의 세분성이 스케줄러 설계의 일부가 된다. 또 다른 주제는 가장 빠른 벤치마크가 실제 정책을 나타내는지 여부였고, 이는 본질적으로 전역 DSQ를 사용하는 기본 빈 sched\_ext 스케줄러라고 설명되었다. EAS 논의에서는 오래된 per-CPU 회계 정보, 로컬 큐를 다시 enqueue할 때의 레이스, 로컬 DSQ를 순회하는 것이 더 나을지 여부가 다루어졌다. 마지막 논의 주제는 스케줄러 테스트였다. sched\_ext는 fair 스케줄러 전용 코드를 직접 테스트할 수는 없지만, PELT, core scheduling, 또는 proxy execution 같은 향후 메커니즘을 비롯한 공유 인프라에 대해 결정론적인 시나리오를 만들 수 있다.

**동영상:**
[Sched\_ext overheads and caveats - Christian Loehle](https://youtu.be/Wdx8TZwak9o?si=kgeBkM1demXiMokS)

#### FlexGuard 대 time-slice extension: lock holder preemption 처리 — Victor Laforet

[FlexGuard
(SOSP'25)](https://dl.acm.org/doi/10.1145/3731569.3764852)는 eBPF를 사용해 컨텍스트 스위치를 감시하고 critical-section preemption을 탐지하는 비휴리스틱 동기화 기법이다. lock holder가 선점되면 FlexGuard는 대기 중인 스레드를 spinning에서 blocking으로 선제적으로 전환하여, 선점된 critical section이 빠르게 재개될 수 있도록 CPU 자원을 확보한다. 정적 임계값이 아니라 실제 실행 이벤트에 반응함으로써, FlexGuard는 POSIX mutex에 비해 성능을 최대 여섯 배까지 향상할 수 있다.

Linux 커뮤니티에서 자주 논의되는 [time-slice extension](https://lwn.net/Articles/1038235/) 접근법은 이와 달리 태스크에 critical section을 완료할 약간의 CPU 시간을 주어 lock-holder preemption 자체를 방지하는 것을 목표로 한다. Linux 7.0부터 스레드는 락을 보유하고 있을 때 [rseq()](https://manpages.opensuse.org/Tumbleweed/librseq-devel/rseq.2.en.html)를 사용해 커널에 효율적으로 알릴 수 있다. 스케줄러는 그런 스레드를 선점하는 대신 락이 해제될 때까지(기본적으로 최대 5µs, 또는 최대 50µs까지) 실행되도록 허용하여 전진 진행을 보존한다. 데이터베이스 인덱스, LevelDB, 기타 벤치마크에서 두 해법을 비교 평가한 결과, 두 접근법은 서로 다른 병목을 다루며, 서로를 대체하기보다 보완한다는 점을 확인했다.

Realtime 태스크와 livelock 가능성에 대한 논의가 있었다. 그러나 spinlock은 realtime 태스크와 함께 사용해서는 안 된다. 또한 time-slice extension은 어차피 PREEMPT\_RT에서는 사용할 수 없다. 또 다른 논의는 spinlock이 많은 수의 스레드에서 사용되어서는 안 된다는 사실에 관한 것이었다. spinlock은 대신 세분화되어야 한다. 이렇게 하면 FIFO 방식이며 다음 대기자가 선점될 때 문제가 생기는 queue lock 대신 기본 spinlock을 사용할 수 있다. time-slice extension 기능은 세분화된 락을 중심으로 설계되었다. 그러나 널리 사용되는 일부 소프트웨어는 여전히 넓은 범위의 락을 사용하며, queue 기반 spinlock의 처리량 증가로 이득을 본다.

**동영상:** [FlexGuard
vs. Time-Slice Extension: Handling Lock Holder Preemption - Victor
Laforet](https://youtu.be/aBNSTS9XH_4?si=QjlDCS0CBSO1zrI2)

[댓글(아직 없음)](https://lwn.net/Articles/1077759/#Comments)

[^lwn1078380-p16-1]: 데드라인 서버는 특정 스케줄링 클래스나 작업 집합에 CPU 실행 시간을 예약해 주는 커널 스케줄링 메커니즘을 가리킨다.
[^lwn1078380-p16-2]: DSQ(dispatch queue)는 sched\_ext에서 태스크를 보관하고 전달하는 큐이며, “터미널” DSQ는 최종적으로 코어 sched\_ext 경로에 제어를 넘기는 큐를 뜻한다.

### [OSPM 2026 둘째 날 보고](https://lwn.net/Articles/1078696/)

글쓴이: **Jonathan Corbet**  
2026년 6월 24일

#### 요약

- OSPM 2026 둘째 날 세션은 uncore DVFS, CPUFreq 전력 절감, EEVDF 기반 CPU 선택, Arm64 서버 스케줄링 도메인 등 커널 전력 관리와 스케줄링 주제를 폭넓게 다뤘다.
- uncore DVFS 발표는 기존 `devfreq` 프레임워크 위에서 L3 캐시·인터커넥트·메모리 컨트롤러의 전력 소모를 줄이는 접근과 PI governor의 가능성을 소개했다.
- AMU/PMU 카운터를 CPUFreq에 활용하면 CPU 주파수를 높여도 성능 향상이 크지 않은 상황을 식별해 거의 같은 성능으로 에너지 효율을 높일 수 있다는 결과가 제시됐다.
- EEVDF slice duration을 CPU 선택에 활용하는 연구는 짧은 작업의 지연 시간을 줄이기 위한 여러 corner case 수정과 남은 과제를 설명했다.
- Arm64 서버에서는 평평한 mesh 기반 하드웨어와 비균일 캐시/메시 지연 특성을 스케줄러 토폴로지가 충분히 반영하지 못한다는 문제가 논의됐다.

[Linux Kernel Summit의 Power Management and Scheduling](https://retis.santannapisa.it/ospm-summit/)은 역사적 약자인 OSPM[^lwn1078380-p17-1]으로 여전히 불리며, 4월 중순 영국 케임브리지에서 열렸다. 관례가 되었듯이 이 행사 발표자들은 이후 각 세션의 요약을 작성했고, 이 글들은 친절하게도 LWN에 게재할 수 있도록 제공되었다. 둘째 날 세션은 device frequency scaling, time-slice duration을 이용한 CPU 선택, multi-cluster Arm 시스템의 scheduling domain, LAVD scheduler 등 다양한 주제를 다뤘다.

(함께 보기: [첫째 날](https://lwn.net/Articles/1077759/) 및 [셋째 날](https://lwn.net/Articles/1078697/) 보도).

#### uncore DVFS를 위한 Devfreq — Jie Zhan

이 발표는 커널의 기존 [devfreq](https://docs.kernel.org/driver-api/devfreq.html) 프레임워크 위에 [uncore](https://en.wikipedia.org/wiki/Uncore) dynamic voltage and frequency scaling(DVFS)[^lwn1078380-p17-2]을 구축하는 작업을 다뤘다. 여기서 uncore는 L3 캐시, 인터커넥트, 메모리 컨트롤러를 포함하지만 I/O와 GPU는 제외한다. 동기는 구체적이다. 연구 대상 칩에서 uncore는 idle 상태일 때 SoC 전력 소비의 약 41%, CPU-bound workload에서는 약 17%를 차지한다. uncore DVFS를 활성화한 SPECpower 실행에서는 측정 가능한 throughput 손실 없이 0–50% load 구간에서 SoC 전력을 7–35% 절감했다. 목표는 특히 generic upstream solution이 없는 server SoC에서 성능 영향은 작게 유지하면서 전력을 줄이는 것이다.

devfreq의 구조와 기존 다섯 가지 governor를 검토한 뒤, 논의는 두 가지 과제에 집중됐다. 첫째는 frequency-scaling strategy다. 실험에서 simple\_ondemand governor는 minimum frequency와 maximum frequency 사이를 심하게 ping-pong했다. 너무 공격적으로 scale down하고, 보고되는 “load” 자체도 frequency에 따라 변하기 때문이다. 제안된 것은 조정된 proportional/integral(PI) governor였다. 빠른 upscaling에는 proportional term을, 부드러운 downscaling에는 integral term을 사용해 throughput 손실 없이 frequency를 약 900 MHz 부근에 안정화했다. 둘째는 governor-driver 결합 문제다. devfreq는 device registration 시 governor-specific data 한 종류만 전달하므로, 새 dynamic governor를 추가하거나 전환하는 일이 사실상 지원되지 않는다. maintainer의 조언은 간단했다. patch를 보내고 mailing list에서 논의하라는 것이다.

청중도 적극적으로 참여했다. 여러 참석자는 PI가 아니라 완전한 [PID controller](https://en.wikipedia.org/wiki/PID_controller)를 시도해 보자고 주장했다. derivative term이 spike를 예측할 수 있다는 이유였지만, tuning이 어렵기로 악명 높고 workload에 의존한다는 점도 인정됐다. 한 참석자는 “good result”라는 주장에 의문을 제기했다. load가 60–80%까지 치솟는 동안 frequency가 약 900 MHz에 고정되어 있다면, governor가 hardware가 peak throughput에 도달하는 것을 막고 있을 수 있다는 것이다. SPECpower는 자체 load를 조정할 수 있지만, 다른 application이나 benchmark는 같은 설정에서 피해를 볼 수 있다.

반복해서 나온 제안은 CPU frequency와 연계된 bandwidth 및 quality-of-service hint와 함께 기존 interconnect framework를 사용하는 것이었다. 이 framework는 CPU, display, image signal processor 전반의 constraint를 aggregate할 수 있기 때문이다. 반론은 이 interconnect가 오늘날에는 대체로 static이며, reactive load detection은 항상 뒤처진다는 것이었다. task enqueue 시점의 scheduler-level hint(그리고 다음 날 참고된 forthcoming latency-based QoS proposal)가 L3/uncore에는 더 적합할 수 있다. 또 다른 질문은 per-scheduling-entity tracking에 관한 것이었다. 답변에서는 related-CPU topology가 이미 uncore device에 붙어 있으므로, scheduler utilization을 거기서 가져올 수 있다고 설명했다.

발표는 세 가지 열린 질문으로 마무리됐다. governor가 per-driver가 되지 않도록 common uncore event description을 정의하는 것, CPU 또는 I/O device에서 hint(scheduler utilization, enqueue-time signal)를 가져오는 것, tuning parameter를 단일 governor에서 분리하도록 governor-driver data interface를 재구성하는 것이다.

**Video:**
[uncore DVFS를 위한 Devfreq - Jie Zhan (OSPM26)](https://youtu.be/6TBt7TXKa7o?si=KqB5xGCjr9xc4dXr)

#### AMU/PMU를 사용해 CPUFreq의 쓸모없는 전력 소비 줄이기 — Hongyan Xia

Hongyan Xia는 실제 CPU capacity가 frequency에 항상 선형적으로 비례해 scale하지는 않는다는 점을 설명했다. workload에 따라 병목은 CPU capacity가 아니라 시스템의 다른 부분, 주로 cache와 DRAM contention에 있을 수 있다. 하지만 [schedutil](https://docs.kernel.org/scheduler/schedutil.html)은 이러한 요인을 인식하지 못하고, 성능을 높이기 위해 CPU frequency만 올리려 한다.

Xia는 CPU power가 병목이 아니고 CPU frequency를 높여도 유용하지 않은 때를 CPU-frequency governor에 알려 주기 위해 Arm64 activity monitoring unit(AMU)와 performance monitoring unit(PMU)의 counter를 사용하려고 했다. 발표에는 이런 scenario에서 가장 도움이 되는 AMU/PMU counter를 식별하는 방법과, 적절한 counter로 linear-regression model을 사용해 CPU frequency를 제한함으로써 거의 같은 performance level을 달성하면서 energy efficiency를 개선하는 방법이 포함됐다.

**Video:** [AMU/PMU를 사용해 CPUFreq의 쓸모없는 전력 소비 줄이기 — Hongyan Xia](https://youtu.be/4Gx6QSd3Dso?si=lO0gOSOFcb1IjOVx)

#### fair task의 slice duration을 CPU 선택에 사용하기 — Vincent Guittot

Vincent Guittot는 fairness를 깨지 않으면서 task scheduling 순서를 정하기 위해 [EEVDF](https://lwn.net/Articles/969062/) slice duration[^lwn1078380-p17-3]을 사용하는 것에 관한 몇 가지 결과를 발표했다. custom-slice 기능은 이론적으로 짧은 slice를 가진 task를 먼저 실행하는 데 사용할 수 있지만, 그림들은 현재 scheduler가 여전히 상당한 latency outlier를 겪고 있음을 보여준다.

테스트에서 Guittot는 짧게 실행되는 task의 scheduling latency를 평가하기 위해 [cyclictest](https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/cyclictest/start) benchmark를 사용했고, 시스템에 overload를 주기 위해 [hackbench](https://wiki.linuxfoundation.org/realtime/documentation/howto/tools/hackbench) 또는 [rt-app](https://github.com/scheduler-tools/rt-app)을 사용했다. Cyclictest는 8ms slice를 설정하고, hackbench와 rt-app은 short interactive task와 background activity를 모사하기 위해 20ms slice를 사용한다. idle system에서는 latency가 허용 가능한 수준을 유지하지만, hackbench가 만드는 것과 같은 stressed condition에서는 성능이 저하된다. 이러한 workload에는 wakeup, sleep, migration이 높은 빈도로 포함된다. overloaded scenario에서 Cyclictest benchmark가 시뮬레이션한 short-running task의 maximum latency는 우선순위가 높아야 함에도 약 9ms(거의 전체 slice duration)에 이를 수 있으며, latency의 99.9th percentile은 종종 4ms를 넘는다.

이는 현재 EEVDF 구현이 여러 corner case에서 running task를 preempt하지 못함을 시사한다.

- Negative lag preservation: task는 CPU time의 초과 소비분(“negative lag”로 측정)을 갚기 위해 queued state에 머무르는 경우가 많다. 하지만 이 기간에 새 task가 enqueue되면 기존 task의 negative lag가 실제로 증가할 수 있다. 제안된 수정은 task가 re-enqueue될 때 negative lag가 sleep에 들어갔을 때의 값 이하가 되도록 보장해, 비활성 상태인 동안 발생한 system activity 때문에 부당하게 불이익을 받지 않게 한다.
- Next-buddy shortcut: scheduler는 때때로 특정 task나 group을 우대하기 위해 buddy mechanism을 사용하는데, 이는 EEVDF가 가장 eligible한 task를 선택하는 과정을 우회한다. EEVDF가 다른 task를 골랐을 상황이라면 buddy를 clear함으로써, scheduler는 더 짧은 slice를 가진 task에 대해 preemption이 일관되게 유지되도록 한다.
- Delayed-dequeue bias: run queue에서 eligible해지기를 기다리는 delayed-dequeue task는 deadline이 짧은 경우가 많고, 다음에 실행될 대상으로 쉽게 선택될 수 있다. 따라서 이들은 더 짧은 slice를 가진 task가 current task를 preempt하지 못하게 할 수 있다. 이 문제를 해결하기 위해 wakeup preemption을 확인할 때 그런 delayed-dequeue task를 실제로 dequeue한다.

이러한 corner case를 수정하면 한 경우를 제외하고 latency의 99.9th percentile이 700µs 아래로 내려가지만, 일부 case는 여전히 추가 연구가 필요하다.

- Newly enqueued entities: preemption check와 next entity 선택 사이에 새 task가 enqueue될 수 있고, 이로 인해 average vruntime이 이동해 preempting task가 더 이상 eligible하지 않게 될 수 있다. preemption을 trigger한 task를 강제로 선택하기 위해 next buddy를 사용하는 방안은 추가 연구가 필요하다.
- Permanent positive lag: negative lag는 delayed dequeue로 decay될 수 있지만, positive lag는 영원히 지속되어 불공정한 advantage를 준다. sleep duration에 따라 positive lag를 decay하는 방안이 검토 중이다. CPU의 uncontended time을 추적해 모든 lag를 reset하는 것도 평가할 또 다른 선택지다.
- Disabling run to parity는 scheduler가 더 공격적으로 task를 switch하고 모든 task에 대한 minimum lag를 유지할 수 있게 해 maximum scheduling latency를 개선하지만, system throughput을 희생한다. 또한 0.7ms(fair scheduler의 default base time-slice value)보다 오래 실행되어야 하는 task는 작업을 끝내기 전에 preempt되어, 짧지만 0.7ms보다 긴 computation의 완료 시간이 지연된다.

이전의 모든 변경에 더해, CPU selection logic은 다음 순서를 따라야 한다.

1. Idle CPU Search: idle CPU는 즉시 실행을 제공하고 preemption overhead를 피하므로 여전히 최선의 target이다.
2. Minimum slice comparison: idle core가 없다면 scheduler는 target CPU에 enqueue된 모든 task의 minimum slice duration을 비교한다. 목표는 waking task의 slice가 minimum보다 짧은 core에 배치해, current task를 preempt할 가능성을 극대화하는 것이다.
3. Energy-aware scheduling(EAS): mobile platform에서 scheduler는 이러한 latency gain을 특정 power domain을 깨우거나 더 비용이 큰 core로 옮기는 energy cost와 저울질해야 한다.
4. A push callback mechanism: CPU 선택과 task가 실제로 enqueue되는 사이의 window는 atomic하지 않으므로, 그 사이 새 task가 도착해 waking task의 eligibility를 빼앗을 수 있다. push callback은 fallback으로 동작한다. task가 CPU에 도착했을 때 더 이상 첫 번째로 실행될 task가 아니라고 판단되면, 즉시 더 나은 core로 push될 list에 배치된다.

**Video**: [fair task의 slice duration을 CPU 선택에 사용하기 — Vincent Guittot](https://youtu.be/fsOy3M_HkVM?si=0UiKwa4T_DIV9UBH)

#### Arm64 서버를 위한 multi-cluster scheduling domain 재고 — Dietmar Eggemann

논의는 현재 Linux scheduler topology가 현대적인 64-bit Arm server system에 얼마나 잘 맞는지에 초점을 맞췄다. 이러한 platform은 x86 system과 동일한 Linux task scheduler kernel code를 공유하지만, hardware의 모습은 상당히 다르다. 많은 Arm64 server는 scheduler가 전통적으로 기대해 온 hierarchical layout이 아니라, 많은 수의 CPU와 분산된 non-uniform cache system을 갖춘 평평한 mesh 기반 설계를 사용한다.

주요 우려 중 하나는 이러한 Arm64 system이 흔히 하나의 큰 scheduling domain만 노출한다는 점이다. 이는 scheduler가 효과적인 wakeup 및 placement decision을 내리는 능력을 제한한다. system이 완전한 cache-coherent 구조라고 해도 mesh 전반의 latency는 균일하지 않으며, 이 정보는 현재 scheduler에 보이지 않는다. 그 결과 잠재적인 locality benefit이 활용되지 못하고 있다.

초기 실험은 scheduling-domain size가 performance에 영향을 줄 수 있으며, idle CPU를 찾는 overhead와 placement decision의 품질 사이에 tradeoff가 있음을 시사한다. 그 영향은 workload에 크게 의존하고, task-wakeup function의 early exit condition은 이러한 효과를 관찰하고 추론하기 어렵게 만든다.

[^lwn1078380-p17-1]: OSPM은 이 행사의 현재 이름과는 다르게 남아 있는 역사적 약자다.
[^lwn1078380-p17-2]: DVFS는 workload에 맞춰 전압과 frequency를 동적으로 조절해 전력과 성능을 균형 있게 맞추는 기법이다.
[^lwn1078380-p17-3]: EEVDF는 Linux fair scheduler의 task 선택 방식과 관련된 알고리즘으로, 여기서는 task별 slice duration이 latency에 미치는 영향이 논의됐다.

여러 가능한 방향이 논의되었는데, 큰 도메인을 더 작은 클러스터로 나누는 것, 펌웨어가 제공하는 토폴로지 정보를 더 잘 활용하는 것, CPU 사이 또는 메시의 메모리 사이 지연시간 측정값에서 구조를 도출하는 방법을 탐색하는 것 등이 포함되었다. 이들 각각에는 특히 복잡성, 안정성, 그리고 서로 다른 워크로드 전반에서 회귀를 피하는 문제와 관련해 고유한 어려움이 따른다.

전반적으로, 대형 Arm64 시스템에서 노출되고 사용 가능한 토폴로지가 부족하다는 점이 오늘날 스케줄러의 한계라는 데 의견이 모였다. 이 주제에 대한 진행 중인 작업은 위에서 언급한 접근법들을 더 탐색하여, 하드웨어·펌웨어·OS 팀 간의 조율을 필요로 하는 견고하고 일반적으로 적용 가능한 해법을 찾으려 할 것이다.

**비디오**: [Rethinking
multi-cluster scheduling domains for Arm64 servers — Dietmar Eggemann](https://youtu.be/sOVX5WJOvR8?si=acD1gJykeWwR0P3O)

#### Evolving sched\_ext: resource control, topology awareness, and energy efficiency for modern systems — Changwoo Min and Gavin Guo

Changwoo Min과 Gavin Guo는 sched\_ext 위에 구축된 Latency-criticality Aware Virtual Deadline 스케줄러인 [scx\_lavd](https://github.com/sched-ext/scx/tree/main/scheds/rust/scx_lavd#scx_lavd)의 두 가지 개선 사항을 다루는 공동 발표를 했다. Min이 처음 [OSPM 2025에서 scx\_lavd를 발표했을 때](https://lwn.net/Articles/1021332/#lavd), 그것은 SteamOS를 통해 Linux에서 실행되는 Windows 게임을 개선하는 데 초점을 둔 게임 지향 스케줄러였고, 태스크 긴급도의 주요 힌트로 waker/wakee 빈도를 사용했다. 1년 뒤 이 프로젝트의 범위는 더 넓어져, scx\_lavd를 잠재적인 기본 플릿 스케줄러로 확장하고 있으며, 그 확장은 스케줄링 문제의 두 부분을 부각시켰다. 첫 번째는 control-group-v2 CPU 대역폭 제어 — [cpu.max](https://docs.kernel.org/admin-guide/cgroup-v2.html#:~:text=cpu%2Emax) 인터페이스 — 에 대한 지원으로, 멀티테넌트 시스템(컨테이너, VM, 클라우드 워크로드)이 엄격한 CPU 할당량을 강제하기 위해 필요로 하는 것이다. 두 번째는 태스크 크기의 이질성과 CPU 용량의 이질성을 모두 이해하는 로드 밸런서다.

Sched\_ext cpu.max — 작업을 크리티컬 경로 밖으로 옮기기

Min은 cpu.max가 해야 하는 일을 간단히 요약하며 시작했다. cpu.max는 관리자가 제어 그룹마다 (quota, period, burst) 튜플을 지정할 수 있게 하며, 할당량을 초과한 그룹의 태스크는 스로틀링된다. 즉 다음 period 경계까지 디큐되어 대기 상태로 놓인다. 그는 성능 개선을 향한 자신의 접근법에 동기를 부여한, 커널의 기존 구현 설계 측면 세 가지를 빠르게 검토했다.

첫 번째는 태스크 선택이다. 커널은 제어 그룹 계층을 중첩된 [red-black tree](https://lwn.net/Articles/184495/)로 반영하므로, 다음에 실행할 태스크를 고르는 일은 그 중첩 트리를 따라 내려가는 과정이 된다. Min의 설명처럼, 태스크 선택 비용은 계층 깊이에 비례해 선형적으로 증가한다.

두 번째는 스로틀 감지다. 현재 커널 구현은 Min이 "동기식 pull 모델"이라고 부른 방식을 사용한다. 각 CPU는 중앙의 제어 그룹별 할당량 풀에서 5ms 슬라이스를 빌려와 로컬에서 소비하고, 다 쓰면 더 가져온다. 로컬 예산이 소진되고 그룹 자체에도 더 이상 할당량이 없으면, CPU는 예산의 출처를 찾기 위해 제어 그룹 계층을 거슬러 올라가야 한다. 그 결과 매 디스패치마다 수행되는 스로틀 검사는 비싸고, 전역 메모리에 접근하며, 역시 계층 깊이에 따라 비용이 증가한다.

세 번째는 보충이다. 커널은 그룹마다 두 개의 타이머를 사용한다. period\_timer는 매 period마다 할당량을 다시 채우고, slack\_timer는 사용되지 않은 로컬 예산을 비동기적으로 전역 풀에 돌려준다. 따라서 시스템의 총 타이머 수는 그룹 수에 비례해 선형적으로 증가한다. Min이 만든 sched\_ext cpu.max 라이브러리는 이 세 가지 문제를 하나의 원칙을 중심으로 재구성한다. 비용이 큰 작업을 디스패치 경로 밖으로 빼내는 것이다. 이 라이브러리는 lib/cgroup\_bw로 노출되며 어떤 sched\_ext 스케줄러에도 링크될 수 있다. scx\_lavd가 그 첫 번째 사용자다.

태스크 선택을 위해 라이브러리는 스로틀되지 않은 모든 태스크를 일반 디스패치 큐(DSQ)에 유지한다. 스로틀된 태스크만 따로 옮겨져 제어 그룹별 backlog task queue(BTQ)에 들어간다. 따라서 스로틀되지 않은 DSQ에서의 태스크 선택은 O(log N)으로 유지되고, 중첩 red-black tree는 완전히 사라진다. 핫 패스의 스로틀 검사는 단일 플래그 읽기로 바뀐다. 락도, atomic도, 계층 순회도 없다.[^lwn1078380-p18-1]

마지막 단순화가 가능한 것은, 라이브러리가 커널의 정확하고 즉각적인 단일 period 강제 모델을 Min이 여러 period에 걸친 최종적 대역폭 제어라고 부른 방식과 맞바꾸기 때문이다. 제어 그룹은 최대 한 회계 구간 동안 초과 사용이 허용된다. 초과 사용분은 부채로 기록되고 다음 period의 예산에서 정확히 차감된다. Min은 장기 평균 사용량이 여전히 설정된 할당량에 정확히 수렴한다고 조심스럽게 강조했다.

감지 지연시간을 작게 유지하기 위해, 라이브러리는 적응형 회계 타이머를 설정한다. 각 제어 그룹은 소비율의 지수 가중 이동 평균을 유지한다. 타이머는 그룹이 한도에 도달할 시점을 예측하고, 그룹이 스로틀되기 충분히 이른 시점에 실행된다.

마지막으로, 라이브러리는 모든 제어 그룹의 period를 고정된 100ms 창으로 정규화한다. 모든 그룹이 같은 시간 단위를 사용하면, 단일 보충 타이머가 전체 시스템을 처리할 수 있다. 총 타이머 수는 그룹당 두 개에서 전체 머신에 두 개로 줄어든다.

Min은 2소켓, 96코어 AMD EPYC 머신(192개 CPU)에서 stress-ng --cpu를 실행한 결과를 보여주었다. 그는 순수 사용자 공간 워크로드 동안의 커널 시간 CPU 사이클로 측정한 스케줄러 오버헤드를 설명했다. 제어 그룹 깊이가 1에서 32로 증가하자, EEVDF의 오버헤드는 대략 CPU 두 개분에서 다섯 개분으로 늘어난 반면, scx\_lavd는 약 두 개분으로 평탄하게 유지되었다. 제어 그룹 깊이 32에서 부하를 변화시켰을 때, 125% 부하에서 EEVDF 오버헤드는 CPU 열 개분을 넘어 급등했지만 scx\_lavd는 두 개분 근처에 머물렀다.[^lwn1078380-p18-2]

첫 번째 질문은 Andrea Righi에게서 나왔다. 그는 BTQ가 현재 arena task queue 위에 구축되어 있고, 이는 다시 BPF arena 위에 구축되어 있다고 지적했다. arena 지원이 없는 오래된 커널에서는 이것이 이식성 문제가 된다. Righi는 같은 메커니즘을 DSQ 위에 구축할 수 있는지 물었다. Min은 원칙적으로는 가능할 것이라고 답했지만, 현재 DSQ에는 태스크를 한 DSQ에서 다른 DSQ로 직접 옮기는 API가 없다고 말했다. 기존의 유일한 전송 경로는 실행을 위해 BPF DSQ에서 로컬 DSQ로 가는 것이다. DSQ들을 순회하는 방식은 동작하겠지만 비용이 크다고 그는 말했다. sched\_ext에 직접적인 DSQ-to-DSQ 태스크 이동 kfunc를 추가하면 BTQ가 arena 의존성을 없앨 수 있을 것이다.

한 청중은 이러한 아이디어 중 일부를 커널에 되돌려 기여할 수 있는지 물었다. Min은 그 논의에 열려 있지만, 먼저 설계가 의도대로 동작한다는 것을 확인하고 싶었다고 답했다. 오버헤드와 정확도 수치가 예상대로 움직인다는 몇 달간의 증거가 있는 만큼, 커널의 cpu.max 구현을 개선하는 데 관심 있는 협력자들을 환영한다고 그는 말했다.

또 다른 청중은 그 비교가 재작업 이후의 EEVDF를 대상으로 실행된 것인지 물었다. 2025년 9월 무렵, 커널의 cpu.max 스로틀링은 스로틀링을 사용자 공간 복귀 경계까지 지연하도록 재작업되었고, 부채 이월은 이미 커널 쪽에 구현되어 있었다. Min은 자신의 기준선이 그 재작업 이전의 것임을 인정했고, 현재 커널을 대상으로 하면 EEVDF 오버헤드 수치가 더 낮아질 것이라는 데 동의했다. 스로틀 감지의 깊이 독립성과 그룹별 타이머 제거는 그와 무관하게 여전히 이점으로 남겠지만, 구체적인 오버헤드 차이는 다시 측정해야 할 것이다.

또 다른 청중은 계층형 회계가 본질적인 것인지, 아니면 평탄한 모델이 bottom-up 및 top-down 트리 순회를 모두 피할 수 있는지 물었다. Min의 답은 제어 그룹 인터페이스가 계층적이므로 회계도 그래야 한다는 것이었다. 다만 계층 관련 작업은 디스패치 핫 패스가 아니라 백그라운드 회계 타이머에서만 실행된다.

scx\_lavd의 태스크 크기 인식 로드 밸런싱

이어서 Guo가 두 번째 개선 사항인 scx\_lavd용 새 로드 밸런서를 설명했다. 그는 scx\_lavd가 도메인 DSQ 스케줄러라는 점을 청중에게 상기시키며 시작했다. 각 last-level-cache(LLC) 도메인은 그 도메인의 모든 CPU가 공유하는 단일 DSQ를 가지며, 도메인들은 시스템 평균 대비 큐에 쌓인 부하를 기준으로 10ms마다 "stealer" 또는 "stealee" 역할을 배정받는다. CPU의 로컬 런 큐가 비면, ops.dispatch()는 먼저 원격 stealee로부터 CPU 시간을 훔치려 시도하고, 그다음 로컬 도메인의 DSQ에서 태스크를 가져오며, 마지막으로 근처의 아무 DSQ에서나 강제 steal하는 방식으로 폴백한다.

현재 밸런서에는 세 가지 약점이 있다. 부하 지표가 utilization과 스케일된 큐 길이의 합인데, Guo는 이것이 명백히 문제가 있다고 말했다. 짧게 사는 태스크 열 개가 있는 도메인이 장시간 실행되는 태스크 두 개가 있는 도메인보다 더 바빠 보이지만, 실제로는 후자가 더 많은 일을 하고 있을 수 있기 때문이다. 마이그레이션 예산이 없어서 많은 CPU가 한 라운드에서 같은 과부하 도메인을 비우려고 경쟁하며, 그 결과 생기는 thundering herd를 제한하는 것은 확률적 게이팅뿐이다. 그리고 마이그레이션은 태스크 유형을 고려하지 않는다. 큰 태스크가 작은 코어에 배치될 수 있다.

새 설계는 부하 지표를 queued\_load\_invr + util\_invr로 대체한다. 여기서 queued\_load\_invr는 태스크 수가 아니라 도메인 내 태스크 크기의 합이고, util\_invr는 도메인의 CPU들이 현재 얼마나 바쁜지를 포착한다. 이질적 시스템에서는 "invariant"라는 한정어가 중요하다. 실행 시간이 CPU 용량과 주파수에 따라 스케일되므로, P-core, E-core, LP-E-core의 부하를 직접 비교할 수 있다. 그런 다음 각 도메인에는 용량에 비례하는 공정 몫이 주어진다. 예를 들어 시스템 용량의 40%를 가진 도메인은 전체 큐 부하의 40%를 부담할 것으로 기대된다. big-core 도메인은 계산 용량이 더 크므로 자연스럽게 더 많은 부하를 떠안는다.

마이그레이션은 대칭적인 50% 예산으로 제한된다. stealee는 공정 몫을 초과하는 부하의 절반을 밖으로 이동시키도록 허용하고, stealer는 공정 몫에 못 미치는 부족분의 절반을 받아들인다. 한 라운드에서 격차의 절반만 줄이면 전체 불균형을 한 번에 바로잡을 때 발생할 thundering herd 문제를 피할 수 있다. 전체를 한 번에 바로잡으면 stealee가 곧바로 다음 stealer가 될 뿐이다.

Guo는 두 대의 머신에서 각각 여섯 번 실행한 schbench-wakeup-latency 결과를 보여주었다. 이질적인 14-CPU Meteor Lake 시스템에서는 p99가 5,867µs(scx\_lavd main)에서 5,613µs(−4.3%)로, p99.9가 9,899µs에서 9,195µs(−7.1%)로 낮아졌다. 동질적인 192-CPU AMD EPYC 9R14에서는 p99가 5,867µs에서 5,741µs(−2.1%)로, p99.9가 7,297µs에서 6,777µs(−7.1%)로 낮아졌다. 예상대로 설계의 용량 인식 측면은 이질적 플랫폼에서 더 큰 도움이 되지만, 마이그레이션 예산 설정과 태스크 크기 지표는 독립적인 개선 사항이므로 동질적 사례에도 깔끔하게 적용된다.

한 청중은 SMT 시스템에서 용량이 어떻게 계산되는지에 대해 추가로 질문했다. 그가 지적했듯 Meteor Lake 박스는 EAS가 목표로 하는 순수한 용량 비대칭 모델이 아니다. 그것은 SMT 시스템이기도 하며, scx\_lavd는 현재 P-core 도메인의 네 개 논리 CPU를 완전히 독립적인 것으로 취급한다. 그는 이들이 같은 용량을 가지며 독립적이라고 가정하는 것이 타당한지 물었다. 답은 독립적이지 않다는 것이었다. SMT sibling들은 서로 영향을 준다. 물리 코어의 두 sibling이 모두 바빠지면 각각의 유효 용량이 떨어지며, 그 관계는 워크로드에 따라 달라진다(계산 집약적인 sibling 두 개는 계산 집약적인 하나와 메모리 집약적인 하나보다 더 많이 간섭한다). Guo는 현재 모델이 과다 계산이라는 데 동의했고, 앞으로 이를 개선하고 싶다고 말했다. 하지만 도메인 기반 스케줄러에서는 로드 밸런싱이 CPU 용량이 아니라 도메인 용량을 기반으로 하므로, 이 문제는 성능 오버헤드보다 덜 중요하다.[^lwn1078380-p18-3]

[^lwn1078380-p18-1]: DSQ(dispatch queue)는 sched\_ext에서 태스크를 담는 디스패치 큐이며, BTQ(backlog task queue)는 여기서 스로틀된 태스크를 따로 보관하기 위해 언급된 큐다.
[^lwn1078380-p18-2]: EEVDF(Earliest Eligible Virtual Deadline First)는 Linux CFS 계열에서 사용되는 스케줄링 알고리즘이다.
[^lwn1078380-p18-3]: SMT(simultaneous multithreading)는 한 물리 코어가 여러 논리 CPU를 제공하는 기술로, sibling 스레드들이 코어 자원을 공유한다.

그런 다음 Ricardo Neri는 EAS 스타일 스케줄러가 같은 문제를 어떻게 다루는지 설명했다. 그는 SMT 시스템에서는 CPU 용량을 사용하지 않는다고 말했다. busy/idle 전환이 너무 빠르고 형제 상태를 추적하는 오버헤드가 지나치게 크기 때문이다. 대신 SMT 코어에서의 스케줄링은 우선순위로 이루어진다. CPU의 우선순위는 그 용량에 비례하지만, SMT 형제들은 가장 낮은 우선순위를 배정받아 마지막에 채워진다. SMT가 비활성화된 Meteor Lake 구성에서는 이 문제가 발생하지 않는다. SMT가 활성화된 경우 EAS는 우선순위에만 의존한다.[^lwn1078380-p19-1] Guo는 이것이 바로 이 발표에서 얻기를 기대했던 종류의 의견이라고 말했으며, 이 모델이 또 무엇을 포착해야 할지에 대해 Intel과 Arm 엔지니어들의 더 많은 제안을 환영한다고 덧붙였다.

토론은 Guo가 다음 단계인 선택적 마이그레이션을 예고하며 마무리되었다. 현재는 stealer가 stealee에서 작업을 가져올 때 항상 DSQ의 맨 앞 작업을 고르는데, 이것이 마이그레이션하기에 가장 좋은 후보가 아닐 수도 있다. 계획은 DSQ에서 다음 두 개에서 여덟 개까지의 작업을 미리 살펴보고, 작업 크기(도메인 용량에 맞춰), 지연시간 중요도, 캐시 지역성, 대기 시간(오래 기다린 작업을 구제해 꼬리 지연시간을 제한할 수 있도록)을 기준으로 선택하는 것이다. 동시에 완전 공정 스케줄러의 task\_hot()와 유사한 task-hot guard를 사용해, 대략 500µs 임계값으로 아직 캐시에 뜨거운 작업은 건너뛴다.

**Video**: [Evolving sched\_ext
- Changwoo Min and Gavin Guo](https://youtu.be/VrsRUlAttFo?si=JcVkhawmaDxP_kch)

#### 대형 서버에서의 Steam deck (계속) — David Dai와 Ryan Newton

David Dai가 맡은 발표 부분은 대형 서버에서 scx\_lavd 스케줄러의 성능을 살펴보며, 특히 프로덕션 환경에서 waker/wakee 휴리스틱을 분석했다. 복잡한 wakeup 체인이 포함된 사용자 대상 웹 서비스에서 scx\_lavd는 짧은 wakeup이 자주 발생하는 스레드를 매우 중요한 스레드로 성공적으로 식별한다. 이러한 작업에 우선순위를 부여하면 버스트 트래픽이나 CPU 경합 기간의 꼬리 지연시간이 줄어든다. 그러나 트레이드오프가 있다. scx\_lavd는 마지막 수준 캐시별 공유 디스패치 큐에 의존하기 때문에 작업 마이그레이션이 늘어나고, L1/L2 캐시 지역성이 나빠지며, 그 결과 작은 처리량 페널티가 발생한다.

두 번째 사례 연구인 캐싱 서비스에서는 이 휴리스틱이 의도치 않은 결과를 낳았다. 이 서비스는 읽기 작업을 한꺼번에 묶어 처리하기 위해 의도적으로 지연시키므로, writer 작업에 비해 wake-up 빈도가 낮아진다. 그 결과 scx\_lavd는 writer가 지연시간 측면에서 더 중요하다고 평가해, 휴리스틱의 역전이 발생했다. Q&A에서 Peter Zijlstra와 Guittot 같은 청중은 개발자들이 각 작업의 구체적인 작업 주기에 기반해 작업의 time slice를 수동으로 설정함으로써 EEVDF에서 지연시간 문제를 해결할 수 있다고 제안했고, Dai는 이를 시도하고 테스트해볼 수 있다고 인정했다.

캐싱 서비스에서 확인된 또 다른 문제는 소프트웨어 인터럽트의 영향이었다. 캐시 worker들은 주된 작업 대신 이러한 인터럽트를 처리하는 데 실행 시간의 최대 4분의 1까지 쓸 수 있었다. 이를 완화하기 위해 Dai는 CPU를 "steady" CPU와 "turbulent" CPU로 분류하는 방안을 제안했다. 청중 한 명이 turbulent CPU를 어떻게 정의하느냐고 묻자, Dai는 현재 임계값이 인터럽트 처리에 시간의 15% 이상을 쓰는 모든 CPU를 turbulent로 분류한다고 설명했다. 그들의 테스트에서는 이것이 코어의 대략 3분의 1에 해당했다. 작업의 지연시간 중요도와 사용률을 결합한 "preemption vulnerability" 점수를 계산하면, 시스템은 취약성과 중요도가 높은 작업을 turbulent CPU에서 멀리 배치할 수 있다. 이러한 지연시간 인식 배치는 전체 꼬리 지연시간을 개선하고 코어 전반의 부하 균형도 더 낫게 만들었다.

Ryan Newton의 발표 부분은 스케줄러 개발을 프로덕션 시스템에서 떼어낸 테스트 환경을 만드는 데 초점을 옮겼다. 그의 목표는 프로덕션 trace를 이식 가능한 재현 workload로 단순화하는 "abstract, fix, test" 루프다. 이 파이프라인은 프로덕션 trace를 가져와 단순화된 Rust 프로그램을 만들고, 더 작은 가상 머신 토폴로지에서 이를 실행한 다음, RT-app을 사용해 JSON 기반 workload 명세로 변환하는 과정을 포함한다. 최종적으로 이러한 명세는 사용자 공간 시뮬레이터인 SCX-SIM에서 실행된다.

SCX-SIM은 실제 커널을 사용하지 않는다. 대신 C stub을 통해 커널 함수를 에뮬레이션한다. 이를 통해 SCX-SIM은 비트 단위로 결정적이고 이식 가능하며, 단일 코어에서 여러 코어를 시뮬레이션하면서 실제 시간보다 세 배에서 열 배 빠르게 동작한다. 또한 SCX-SIM은 제어된 동시성 테스트를 사용한다. 시뮬레이터는 순차적으로 실행되지만, 인위적으로 제어되고 무작위화된 preemption 지점에서 작업 실행 조각들을 서로 끼워 넣어 race condition을 드러내고 동시성 버그를 테스트한다. Q&A에서 시뮬레이터 정확성에 대해 답하며 Ryan은, 예를 들어 context-switching 오버헤드를 모델링하기 위해 SCX-SIM이 무작위 지연을 도입하기는 하지만, 메모리와 캐시 모델링은 없다고 말했다. 한 청중은 작업 마이그레이션 중 실제 instructions-per-cycle 페널티를 하드웨어 performance monitoring unit 카운터로 기록해 시뮬레이터에 되먹임하는 방안을 제안했고, Newton은 그것이 매우 가치 있는 추가 기능이 될 것이라고 동의했다.

시뮬레이션 workflow는 시뮬레이터와 프로덕션 사이의 간극을 줄이는 데 AI coding agent를 포함한다. AI agent들은 wake frequency와 time-slice distribution 같은 시뮬레이터의 보정 파라미터를 반복적으로 조정해, 그 출력 trace가 프로덕션의 실제 Perfetto trace와 가깝게 맞도록 한다. 또한 agent들은 scx\_lavd 스케줄러의 특정 branch에 대한 unit test를 작성하도록 지시받으며, 이로 인해 test code coverage가 최대 77%까지 증가했다. 청중은 이 AI 기반 접근법에 관심을 보였고, 더 넓은 커뮤니티가 프로덕션 trace 단순화에 협력할 수 있도록 prompt와 configuration을 open-source하는 방안에 대한 논의가 이어졌다. 마지막으로 이 루프에서 인간의 역할을 묻는 질문에 Newton은, 인간은 주로 AI 환각을 막는 외부 guardrail을 세우고 AI가 오류를 범할 때 이를 바로잡는 데 필요하다고 결론지었다.

**Video**: [Steamdeck on large
servers (cont.) - David Dai and Ryan Newton (OSPM26)](https://youtu.be/73BT_UfHfqk?si=2N5RR8cW97Y_xR-S)

#### Hierarchical constant bandwidth server: 현재 상태와 향후 과제 — Yuri Andriaccio

이 발표는 [realtime group
scheduler](https://docs.kernel.org/scheduler/sched-rt-group.html)를 hierarchical constant bandwidth server(HCBS) 메커니즘으로 대체하는 것을 목표로 하는 [패치 세트](https://lwn.net/Articles/1024757/)의 최신 업데이트를 소개했다.[^lwn1078380-p19-2] 이 패치 세트는 원래 [OSPM
2025](https://lwn.net/Articles/1021332/#:~:text=Hierarchical%20CBS)에서 발표되었고, 이후 구현에 대한 의견을 모으기 위해 커널 메일링 리스트에 보내졌다. 이 발표 시점에 최신 제안 버전은 [RFC v4](https://lwn.net/ml/all/20251201124205.11169-1-yurand2000@gmail.com/)였다.

발표는 먼저 hierarchical constant bandwidth server가 무엇이고 왜 중요한지에 초점을 맞추었다. HCBS는 [deadline servers](https://lwn.net/Articles/934415/)를 사용해 realtime group scheduling을 재작업하고, 이를 control-group-v2 세계에 도입하며(v1 지원은 제거), 코드 규모를 크게 줄이고, 기존 하위 시스템을 재사용한다. 다른 실용적 개선 사항은 스케줄링 알고리즘의 realtime soundness, 대역폭 할당에 대한 더 나은 제어, 그리고 권한이 없는 FIFO 또는 round-robin realtime 작업 실행 가능성에 초점을 맞춘다.

구현 세부 사항은 OSPM 2025에서 이미 논의된 것과 다르지 않다. 전반적인 아이디어는 각 control group마다 물리 CPU별로 하나씩, 여러 deadline server와 run queue를 할당하는 것이다. 서버는 각 CPU에 대한 대역폭 예약을 제공하고, 실행 대상으로 선택될 때마다 새 control-group별 run queue에서 FIFO/RR 스케줄러를 재귀적으로 호출한다.

HCBS는 지속적으로 작업이 이루어지고 있으며, 최신 버전(이 발표 시점)은 kernel version 6.18을 기반으로 한다. 스케줄러 maintainer들과 다른 기여자들이 적극적으로 review해왔다. HCBS 전용 test 모음도 계속 업데이트되고 실행되어, 중요한 코드 구간이 테스트되고 시간적 보장과 격리 보장이 제공되는지 확인하고 있다.

발표는 CPU-hotplug 메커니즘 및 frequency scaling과의 통합처럼 패치 세트 개발 중 발생한 몇 가지 문제도 다루었다. 2025년에는 폭넓은 아이디어에 불과했지만, multi-CPU control group은 이번 발표에서 더 깊이 조사되고 논의되었다. 새로운 HCBS 메커니즘이 v2 control group에서만 사용 가능할 예정이므로, cpuset과 CPU controller를 통합해 partial reservation을 구현하자는 제안이 나왔다. 이는 CPU의 일부 집합에서 FIFO/RR 작업 실행을 허용하면서, 이 구성에 맞춰 admission test도 업데이트하기 위한 것이다. 원래의 multi-CPU 아이디어에는 CPU별로 서로 다른 budget과 period reservation도 포함되어 있지만, 기존 하위 시스템과의 통합은 여전히 열린 문제다.

또 다른 논의는 현재 sched\_rt\_{runtime/period}\_us sysfs knob의 의미를 둘러싸고 일어났다. 이들은 원래 realtime 작업에 허용되는 최대 대역폭을 지정하고 realtime throttling 메커니즘을 구현하는 데 사용되었다. 그 throttling은 kernel version 6.12에서 fair deadline server를 위해 제거되었다. 그 이후 sched\_rt 설정은 deadline scheduling class에서 할당 가능한 최대 대역폭만 제한하며, FIFO/RR 작업에는 영향을 주지 않는다. 받아들여진 해결책은 deadline entity의 기본 대역폭을 100%로 업데이트하는 것이었고, 이는 최근 kernel의 sched/tip branch에 [merge](https://git.kernel.org/pub/scm/linux/kernel/git/tip/tip.git/commit/?id=c2e390197ad1360db6686a8c89abaafaf83adf72)되었다.

마지막 논의는 현재 deadline-scheduler admission test의 의미와 가능한 대체 방안을 둘러싸고 일어났다. 사실 그 test는 모든 작업이 deadline을 지킬 것을 보장하지 않는다. 대신 deadline 작업의 response time이 무한정 커지지는 않는다는 것만 보장한다.

**Video**: [Hierarchical CBS:
current state and future challenges - Yuri Andriaccio (OSPM26)](https://youtu.be/HVwaVpXlMS4?si=Ma-vWJKNnsA1ZOBJ)

[Comments (1 posted)](https://lwn.net/Articles/1078696/#Comments)

**Page editor**: Joe Brockmeier

[^lwn1078380-p19-1]: EAS(Energy-Aware Scheduling)는 에너지와 성능 특성을 고려해 CPU를 고르는 Linux 스케줄링 기법이다.
[^lwn1078380-p19-2]: HCBS는 계층 구조를 가진 cgroup에서 실시간 작업에 일정 대역폭을 예약해 주기 위한 스케줄링 메커니즘이다.

# 단신

## 보안

### [Tor 0.4.8 지원 종료](https://lwn.net/Articles/1079119/)

#### 요약
- Tor Project는 Tor 0.4.8 및 그 이전 C Tor 버전에 대한 적극적인 지원을 곧 중단할 계획이다.
- 목표 지원 종료일은 2026년 9월 1일이며, 이후 Tor 0.4.9 이전 버전은 네트워크에서 동작하지 않게 된다.
- 0.4.9에서 오래된 디렉터리 데이터 필드를 제거해 클라이언트 디렉터리 대역폭을 줄이고 부트스트랩을 빠르게 하려는 것이 핵심 이유다.

Tor Project는 Tor 0.4.8 및 그 이전 C Tor 버전에 대한 지원을 곧 적극적으로 중단할 계획이라고 [발표했다](https://blog.torproject.org/sunsetting-tor-048/).

> 보통 우리는 지원되지 않는 릴리스라 해도, 꽤 타당한 이유가 없는 한 기존 릴리스를 깨뜨리지 않으려 한다. 이번 경우에는 몇 가지 이유가 있다. [...]
>
> 가장 중요한 이유는 이것이다. 0.4.9에서 우리는 디렉터리 데이터의 일부 기존 필드, 구체적으로 [TAP onion keys](https://spec.torproject.org/proposals/350-remove-tap.html)와 [family lines](https://spec.torproject.org/proposals/321-happy-families.html)를 더 이상 쓰지 않도록 만들었다. 이 필드들을 제거하면 모두에게 클라이언트 디렉터리 대역폭을 크게 절약해 줄 수 있다. 이는 다시 모든 Tor 클라이언트가 조금 더 빠르게 부트스트랩하도록 해 주며, 특히 느린 연결에서 그렇다. 하지만 이 필드들을 제거하면 이전 Tor 버전을 실행하는 클라이언트와 릴레이는 TAP onion keys가 존재할 것으로 기대하기 때문에 더 이상 동작하지 않는다. 따라서 향상된 성능을 더 빨리 제공하려면 0.4.8이 동작을 멈추는 날짜를 앞당길 필요가 있다.

현재 목표 지원 종료일은 2026년 9월 1일이며, 그 이후에는 Tor 0.4.9 이전의 모든 버전이 네트워크에서 동작을 멈추게 된다. 0.4.9.x 계열의 첫 안정 릴리스는 2026년 2월에 [발표되었고](https://forum.torproject.org/t/stable-release-0-4-9-5/21227), Tor 0.4.8.x 계열은 6월 1일에 수명 종료에 도달했다.

[댓글(게시 없음)](https://lwn.net/Articles/1079119/#Comments)

### [금주의 보안 인용문](https://lwn.net/Articles/1078683/)

> 우리가 AI를 국가 자산으로 생각하기 시작한다면, 각국은 자체 역량을 빠르게 개발하고 싶어 할 수 있다. 아니면 냉전과 매우 비슷한 연구 블록의 미래를 맞이할 수도 있다(그냥 재미 삼아 오세아니아와 유라시아를 제안해 본다).
>
> 위와 같은 상황은 상당한 불평등으로 이어질 것이다. 소수의 국가만 최고의 모델에 접근할 수 있고, 나머지는 국경을 넘도록 허용된 것에 만족해야 하며, 둘 사이의 격차는 모델이 개선되는 속도와 정확히 같은 속도로 누적될 것이다. 국가안보 프레임의 첫 번째 희생자는 개방성이다. 공개 가중치는 거의 정의상 모델을 전략 자산으로 보는 체제와 양립할 수 없다. 세상에 공개한 것을 수출 통제할 수는 없기 때문이다. 오픈 소스, Commons, 그리고 tinkering할 권리를 오랫동안 주장해 온 우리에게는 이 부분이 가장 걱정스러워야 한다. 유료 장벽 뒤의 독점 모델에 대한 접근을 잃는 것과, 공개 릴리스가 국가안보상 책임으로 재구성되고 개방 개발의 전체 정신이 닫아야 할 허점으로 취급되는 것은 전혀 다른 일이다. 칩 전쟁은 우리에게 파편화된 공급망을 남겼고, 새로운 모델 전쟁은 사용할 수 있는 모델이 여권에 따라 달라지는 파편화된 세계를 가져올 위험이 있다.

— [Andres
Guadamuz](https://www.technollama.co.uk/fable-and-the-impending-ai-cold-war)

[댓글(게시 없음)](https://lwn.net/Articles/1078683/#Comments)

## 커널 개발

### [커널 릴리스 현황](https://lwn.net/Articles/1079390/)

#### 요약
- 7.2 merge window는 아직 열려 있으며 2026년 6월 28일에 닫힐 것으로 예상된다.
- 6월 19일에 여러 안정 업데이트가 한꺼번에 릴리스되었다.

**7.2 merge window는 아직 열려 있다**. 2026년 6월 28일에 닫힐 것으로 예상된다.

**안정 업데이트**: [7.1.1](https://lwn.net/Articles/1078591/), [7.0.13](https://lwn.net/Articles/1078592/), [6.18.36](https://lwn.net/Articles/1078593/), [6.12.94](https://lwn.net/Articles/1078594/), [6.6.143](https://lwn.net/Articles/1078595/), [6.1.176](https://lwn.net/Articles/1078596/), [5.15.210](https://lwn.net/Articles/1078597/), [5.10.259](https://lwn.net/Articles/1078598/)가 모두 6월 19일에 릴리스되었다.

[댓글(게시 없음)](https://lwn.net/Articles/1079390/)

### [금주의 인용문](https://lwn.net/Articles/1079389/)

> 커널의 관점에서 SPDM [Security Protocols and Data Models]은 장치를 인증하고 증명하는 데 사용된다. 이 위협 모델에서 장치는 SPDM을 사용해 커널과 사용자 공간에서 검증될 때까지 신뢰할 수 없는 것으로 간주된다. 따라서 SPDM 데이터는 악의적일 수 있는 신뢰할 수 없는 데이터다.
>
> SPDM 명세도 복잡하다. 1.2.1 명세는 거의 200쪽이고 1.3.0 명세는 거의 250쪽에 달한다.
>
> 그러므로 우리는 커널이 복잡한 명세에서 온 신뢰할 수 없는 응답을 파싱하게 하고 있으며, 이는 가능한 exploit vector처럼 들린다. 이런 곳이야말로 Rust가 뛰어난 영역이다!
>
> 이 시리즈는 Rust로 SPDM requester를 구현한다.

— [Alistair Francis](https://lwn.net/ml/all/20260623045406.2589547-1-alistair.francis@wdc.com)

[댓글(게시 없음)](https://lwn.net/Articles/1079389/)

## 배포판

### [금주의 배포판 인용문](https://lwn.net/Articles/1078957/)

> 여러 해 동안 나는 cutting edge 시스템보다 안정적인 OS를 선택하는 사람들을 정말 많이 보았다.
>
> 나는 Debian을 종종 결국 도달하는 OS라고 부른다. 결국, 나이가 들거나 절박해지면 대부분의 여행자는 그 움직이지 않는 그림자 아래에서 쉬게 된다 :)

— [Tushar
Chauhan](https://mastodon.mit.edu/@tchauhan/116786738367588980)

[댓글(5개 게시)](https://lwn.net/Articles/1078957/)

## 개발

### [Flatpak으로 만든 GIMP 0.54.1](https://lwn.net/Articles/1078969/)

#### 요약
- GNOME 기여자 "balooii"가 1996년에 릴리스된 GIMP 0.54.1을 최신 64-bit Linux에서 빌드하고 실행되는 Flatpak으로 패키징했다.
- 이 버전은 Motif 기반이며 Larry Ewing이 Tux를 만들 때 사용한 것과 같은 버전이다.
- 오늘날 실무 그래픽 작업용으로 유용하지는 않겠지만, 30년 전 GIMP가 무엇을 할 수 있었는지 살펴보는 데 흥미로울 수 있다.

GIMP 프로젝트는 GNOME 기여자 "balooii"가 1996년에 릴리스된 GIMP 0.54.1을 최신 64-bit Linux 시스템에서 빌드하고 실행할 수 있는 Flatpak으로 패키징하는 작업을 했다고 [보고했다](https://floss.social/@GIMP/116782353256793213). 이는 [Motif](https://en.wikipedia.org/wiki/Motif_(software)) 기반 버전이며, Larry Ewing이 Tux를 만드는 데 [사용한](https://web.archive.org/web/19990208225150/http://www.isc.tamu.edu/%7Elewing/linux/notes.html) 바로 그 버전이기도 하다.

오늘날 본격적인 그래픽 작업에 유용할 가능성은 낮지만, 30년 된 GIMP 버전이 무엇을 할 수 있었는지 보고 싶은 사용자에게는 흥미로울 것이다.

[댓글(17개 게시)](https://lwn.net/Articles/1078969/)

### [Mastodon 4.6 릴리스](https://lwn.net/Articles/1078466/)

#### 요약
- Mastodon fediverse 플랫폼의 버전 4.6이 릴리스되었다.
- 핵심 기능은 프로필의 선별 컬렉션을 만들고 공유하는 Collections다.
- 이메일을 통한 게시물 구독, "year in review" 게시물 생성, 접근성 개선 등이 포함되었다.

Mastodon fediverse[^lwn1078380-p20-1] 플랫폼의 [버전
4.6](https://blog.joinmastodon.org/2026/06/mastodon-4.6/)이 릴리스되었다.

> 이번 릴리스의 대표 기능은 Collections로, 선별된 프로필 컬렉션을 만들고 공유하는 방법이다. Mastodon의 작업 정신 중 하나는 신뢰와 안전에 대한 우리의 약속이므로, 이 기능을 설계하면서 다른 플랫폼의 유사 기능에서 사람들이 겪었던 일부 함정과 악용을 피하기 위해 많은 생각과 주의를 기울였고, 동시에 주요 목표인 새 사용자가 Fediverse를 더 많이 발견하도록 돕는 데 집중했다.

그 밖의 새로운 기능으로는 이메일을 통한 게시물 구독 지원, "year in review" 게시물 생성 기능, 접근성 개선 등이 있다.

[댓글(게시 없음)](https://lwn.net/Articles/1078466/)

### [Software Freedom Conservancy의 LLM-backed generative AI 권고안](https://lwn.net/Articles/1078521/)

#### 요약
- Software Freedom Conservancy(SFC)는 FOSS 기여에서 LLM-backed generative AI 시스템을 사용할 때의 권고안을 공개했다.
- 권고안은 독점 시스템 사용으로 인한 피해를 줄이기 위한 실용적 도움을 제공하는 모범 관행으로 제시된다.
- SFC는 문서, 온라인 튜토리얼, 공개 Q&A, podcasts 등 후속 지원 자료를 제공하고 권고안을 계속 다듬을 예정이다.

[Software Freedom
Conservancy](https://sfconservancy.org/)(SFC)는 [FOSS
기여를 위한 LLM-backed generative AI 시스템 사용 권고안](https://sfconservancy.org/llm-gen-ai/llm-backed-generative-ai-recommendations.html)을 공개한다고 [발표했다](https://sfconservancy.org/news/2026/jun/18/llm-backed-generative-ai-recommendations/). 이 권고안은 SFC와 자유 소프트웨어 커뮤니티의 자원봉사자들이 만들었다.

> 이 권고안은 이러한 시스템이 FOSS 기여자에게 제기하는 극도로 어려운 딜레마를 반영한다. SFC와 자원봉사자들은 FOSS 개발자들이 다양한 관점에서 LLM-gen-AI에 접근하고 있음을 이해한다. 이 권고안은 FOSS 기여자가 LLM-gen-AI를 거부하든, 아니면 (자발적으로 또는 고용주의 지시에 따라) 사용하기로 하든 독점 시스템 사용으로 인한 피해를 최소화하기 위한 실용적 도움을 제공한다.
>
> 이 권고안은 SFC와 자원봉사자들이 FOSS 기여자 사이에서 증가하는 LLM-gen-AI 사용을 신중히 연구한 뒤 마련한 best practices(정의나 요구사항은 아님)다. SFC는 이 권고안에 이어 문서, 온라인 튜토리얼, 공개 Q&A, [podcasts](https://sfconservancy.org/casts/the-corresponding-source/), 기타 커뮤니티 참여를 포함한 일련의 [지원 자료](https://sfconservancy.org/llm-gen-ai)를 제공할 예정이다. 우리는 정기적으로 권고안을 개선하고 FOSS 기여자들이 이 어려운 지형을 헤쳐 나가도록 계속 지원할 것이다.

[댓글(50개 게시)](https://lwn.net/Articles/1078521/#Comments)

### [Systemd v261 릴리스](https://lwn.net/Articles/1078708/)

#### 요약
- Systemd v261이 긴 변경 목록과 함께 릴리스되었다.
- 새 cloud "Instance Metadata Service"(IMDS) 하위 시스템과 물리적 TPM이 없는 시스템을 위한 "boot secret" 기능이 포함되었다.
- 사용 가능하고 활성화된 경우 커널의 Live Update Orchestration(LUO) / Kexec Handover(KHO) 시스템도 지원한다.

Systemd v261은 새 cloud "Instance Metadata Service"(IMDS)[^lwn1078380-p20-2] 하위 시스템, 물리적 TPM이 없는 시스템에서 사용할 "boot secret" 기능, 그리고 존재하고 활성화된 경우 커널의 Live Update Orchestration(LUO) / Kexec Handover(KHO) 시스템 지원을 포함한 긴 변경 목록과 함께 릴리스되었다. 전체 변경 목록은 [release notes](https://github.com/systemd/systemd/releases/tag/v261)를 참조하라.

[댓글(28개 게시)](https://lwn.net/Articles/1078708/)

### [Xfce의 Wayland compositor 첫 preview 릴리스](https://lwn.net/Articles/1078942/)

#### 요약
- Brian Tarricone가 Xfce 데스크톱 환경을 위한 Wayland compositor인 xfwl4의 첫 preview 릴리스를 발표했다.
- 이 릴리스는 버그와 빠진 기능이 있는 alpha 릴리스로 보아야 한다.
- 목표는 X server에서 실행되는 Xfce 데스크톱과 최대한 비슷하게 동작하도록 만드는 것이다.

Brian Tarricone는 [Xfce](https://www.xfce.org/) 데스크톱 환경을 위한 Wayland compositor[^lwn1078380-p20-3]인 xfwl4의 첫 preview 릴리스를 [발표했다](https://www.spurint.org/journal/2026/06/xfwl4s-first-preview-release).

> 거의 6개월간 작업한 뒤, 물론 버그와 빠진 기능이 있겠지만 이제 더 넓은 사용을 받아들일 준비가 되었다고 느낀다. 이것을 alpha 릴리스로 생각해 달라. [...]
>
> xfwl4의 최종 목표는 X server에서 실행되는 Xfce 데스크톱과 가능한 한 비슷하게 동작하는 것이다. 이상적으로는 사용자가 둘 사이를 전환하면서 차이가 있다는 사실조차 모를 수 있어야 한다. 물론 현실에서는 그렇게까지 매끄럽지는 않을 것이고, 그 이상에 최대한 가까워지려면 아직 해야 할 일이 더 있다. 그래도 최소한 이것은 첫 번째로 탄탄하게 다듬은 결과물이다.

[댓글(31개 게시)](https://lwn.net/Articles/1078942/)

### [금주의 개발 인용문](https://lwn.net/Articles/1078685/)

> 경제학 학부생에게 오픈 소스 라이브러리가 어떻게 만들어지는지 설명해 주되 그것이 무엇인지는 말하지 않고 결과를 예측해 보라고 한다면, 그들은 앞뒤가 맞지 않는다고 말할 것이다. 가격도, 계약도, 책임도 없는 비배제적 재화, 생산자 수의 중앙값은 1명이고 소비자의 거의 전면적인 무임승차가 있는 상황이다. 교과서 어디에도 그런 배열이 안정적인 무언가를 만들어 낸다는 모델은 없다.
>
> 그런 다음 `npm install`을 실행하면 이 불가능한 재화 수백 개가 몇 초 만에 도착하고, 상용 소프트웨어 산업은 거의 전적으로 그 위에 올라서 있다. 오픈 소스는 시장 공리의 거의 전체 집합을 한꺼번에 깨뜨린다.

— [Andrew
Nesbitt](https://nesbitt.io/2026/06/18/open-source-vs-the-invisible-hand.html)

[댓글(게시 없음)](https://lwn.net/Articles/1078685/)

**페이지 편집자**: Daroc Alden

# 공지

[^lwn1078380-p20-1]: Fediverse는 ActivityPub 같은 프로토콜로 서로 연결되는 분산형 소셜 네트워크들의 연합을 가리킨다.
[^lwn1078380-p20-2]: IMDS는 클라우드 인스턴스가 자신의 메타데이터를 조회하도록 제공되는 서비스다.
[^lwn1078380-p20-3]: Wayland compositor는 Wayland 세션에서 창 합성, 입력, 화면 출력을 관리하는 구성요소다.

## 뉴스레터

### 배포판 및 시스템 관리

[DistroWatch Weekly](https://distrowatch.com/weekly.php?issue=20260622)
6월 22일

[This week in F-Droid](https://f-droid.org/en/2026/06/19/twif.html)
6월 19일

[Ubuntu Weekly News](https://discourse.ubuntu.com/t/ubuntu-weekly-newsletter-issue-949/84188)
6월 15일

### 개발

[Emacs News](https://sachachua.com/blog/2026/06/2026-06-22-emacs-news/)
6월 22일

[These Weeks in Firefox](https://blog.nightly.mozilla.org/2026/06/22/eyedropper-quick-action-geckodriver-0-37-and-tighter-file-permissions-these-weeks-in-firefox-issue-205/)
6월 22일

[GCC 14.3.1 Status Report](https://lwn.net/Articles/1078681/)
6월 19일

[What's cooking in git.git](https://lwn.net/Articles/1078762/)
6월 19일

[What's cooking in git.git](https://lwn.net/Articles/1079002/)
6월 23일

[What's cooking in git.git](https://lwn.net/Articles/1079133/)
6월 23일

[This Week in GNOME](https://thisweek.gnome.org/posts/2026/06/twig-254/)
6월 20일

[GNU Tools Weekly News](https://lwn.net/Articles/1078941/)
6월 21일

[Golang Weekly](https://golangweekly.com/issues/606)
6월 19일

[LLVM Weekly](https://llvmweekly.org/issue/651)
6월 22일

[This Week in Matrix](https://matrix.org/blog/2026/06/19/this-week-in-matrix-2026-06-19/)
6월 19일

[OCaml Weekly News](https://lwn.net/Articles/1079118/)
6월 23일

[Perl Weekly](http://perlweekly.com/archive/778.html)
6월 22일

[This Week in Plasma](https://blogs.kde.org/2026/06/20/this-week-in-plasma-6.7-is-here/)
6월 20일

[PyCoder's Weekly](https://pycoders.com/issues/740)
6월 23일

[Weekly Rakudo News](https://rakudoweekly.blog/2026/06/22/2026-25-dutch-art/)
6월 22일

[Ruby Weekly News](https://rubyweekly.com/issues/805)
6월 18일

[This Week in Rust](https://this-week-in-rust.org/blog/2026/06/17/this-week-in-rust-656/)
6월 17일

[Wikimedia Tech News](https://meta.wikimedia.org/wiki/Special:FeedItem/technews/20260622000000/en)
6월 22일

### 회의록

[Fedora FESCo meeting minutes](https://lwn.net/Articles/1079157/)
6월 23일

[openSUSE Release Engineering minutes](https://lwn.net/Articles/1078515/)
6월 17일

## 발표 제안 모집

### CFP 마감일: 2026년 6월 25일부터 2026년 8월 24일까지

다음 CFP 마감일 목록은
[LWN.net CFP Calendar](https://lwn.net/Calendar/Monthly/cfp/)에서 가져온 것입니다.[^lwn1078380-p21-1]

| 마감일 | 행사 날짜 | 행사 | 장소 |
| --- | --- | --- | --- |
| 6월 28일 | 10월 8일 | [Linux Security Summit Europe](https://events.linuxfoundation.org/linux-security-summit-europe/program/cfp/) | 프라하, 체코 |
| 6월 30일 | 11월 17일–11월 19일 | [Open Source Monitoring Conference](https://osmc.de/call-for-papers/) | 뉘른베르크, 독일 |
| 7월 1일 | 10월 3일–10월 4일 | [openSUSE.Asia Summit 2026](https://events.opensuse.org/conferences/oSAS26/program/proposals/new) | 욕야카르타, 인도네시아 |
| 7월 3일 | 9월 28일–9월 30일 | [X.Org Developers Conference](https://indico.freedesktop.org/event/12/abstracts/) | 토론토, 캐나다 |
| 7월 15일 | 7월 15일–7월 22일 | [BornHack 2026](https://bornhack.dk/bornhack-2026/program/call-for-participation/) | 퓐 섬, 덴마크 |
| 7월 31일 | 10월 14일–10월 17일 | [PyCon South Africa](https://za.pycon.org/pages/speaking/how_to_apply/) | 케이프타운, 남아프리카공화국 |
| 7월 31일 | 10월 1일–10월 2일 | [embedded Linux for Safe and Secure Applications](https://www.elsa-symposium.com/call-papers) | 괴팅겐, 독일 |
| 8월 1일 | 8월 25일–8월 30일 | [MiniDebConf and MiniDebCamp Winterthur 2026](https://ch2026.mini.debconf.org/contribute/cfp/) | 빈터투어, 스위스 |

여러분의 행사 CFP 마감일이 여기에 표시되지 않았다면,
[알려 주십시오](https://lwn.net/Calendar/new/).

## 예정된 행사

### 행사: 2026년 6월 25일부터 2026년 8월 24일까지

다음 행사 목록은
[LWN.net Calendar](https://lwn.net/Calendar/)에서 가져온 것입니다.

| 날짜 | 행사 | 장소 |
| --- | --- | --- |
| 7월 13일–7월 19일 | [DebCamp 26](https://debconf26.debconf.org/) | 산타페, 아르헨티나 |
| 7월 13일–7월 16일 | [Netdev](https://www.netdevconf.info/0x1A/) | 로마, 이탈리아 |
| 7월 13일–7월 19일 | [EuroPython](https://ep2026.europython.eu/) | 크라쿠프, 폴란드 |
| 7월 15일–7월 22일 | [BornHack 2026](https://bornhack.dk/bornhack-2026/) | 퓐 섬, 덴마크 |
| 7월 16일–7월 19일 | [Electromagnetic Field](https://www.emfcamp.org/) | 이스트너, 영국 |
| 7월 18일 | [AlmaLinux Day: Los Angeles](https://almalinux.org/almalinux-day-los-angeles-2026/) | 로스앤젤레스, CA, 미국 |
| 7월 20일–7월 25일 | [DebConf 26](https://debconf26.debconf.org/) | 산타페, 아르헨티나 |
| 8월 6일–8월 9일 | [FOSSY 2026](https://2026.fossy.ca/) | 밴쿠버, 캐나다 |
| 8월 8일–8월 9일 | [UbuCon Asia 2026 @ COSCUP](https://2026.ubucon.asia) | 타이베이, 대만 |
| 8월 11일–8월 12일 | [Open Source Summit Korea](https://events.linuxfoundation.org/open-source-summit-korea/) | 서울, 대한민국 |

여러분의 행사가 여기에 표시되지 않았다면,
[알려 주십시오](https://lwn.net/Calendar/new/).

[^lwn1078380-p21-1]: CFP는 보통 “Call for Presentations” 또는 “Call for Papers”를 뜻하며, 행사 발표나 논문 제안 모집을 가리킵니다.

## 보안 업데이트

이번 주 배포판 보안 공지 요약입니다. 표의 배포판, 공지 ID, 릴리스, 패키지명, 날짜는 추적 가능성을 위해 원문 그대로 보존했습니다.[^lwn1078380-p22-security]

### [2026년 6월 18일부터 2026년 6월 24일까지의 보안 공지 요약](https://lwn.net/Articles/1079387/)

| 배포판 | ID | 릴리스 | 패키지 | 날짜 |
| --- | --- | --- | --- | --- |
| AlmaLinux | [ALSA-2026:26459](https://lwn.net/Articles/1078849/) | 8 | 389-ds:1.4 | 2026-06-22 |
| AlmaLinux | [ALSA-2026:19200](https://lwn.net/Articles/1079218/) | 9 | corosync | 2026-06-23 |
| AlmaLinux | [ALSA-2026:26532](https://lwn.net/Articles/1078402/) | 10 | dracut | 2026-06-17 |
| AlmaLinux | [ALSA-2026:26534](https://lwn.net/Articles/1078606/) | 8 | dracut | 2026-06-18 |
| AlmaLinux | [ALSA-2026:26533](https://lwn.net/Articles/1078403/) | 9 | dracut | 2026-06-18 |
| AlmaLinux | [ALSA-2026:27733](https://lwn.net/Articles/1079219/) | 10 | firefox | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27717](https://lwn.net/Articles/1079220/) | 8 | firefox | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27734](https://lwn.net/Articles/1079221/) | 9 | firefox | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27353](https://lwn.net/Articles/1078850/) | 8 | kernel | 2026-06-22 |
| AlmaLinux | [ALSA-2026:27811](https://lwn.net/Articles/1079222/) | 8 | kernel | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27789](https://lwn.net/Articles/1079223/) | 9 | kernel | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27354](https://lwn.net/Articles/1078851/) | 8 | kernel-rt | 2026-06-22 |
| AlmaLinux | [ALSA-2026:27812](https://lwn.net/Articles/1079224/) | 8 | kernel-rt | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27738](https://lwn.net/Articles/1079225/) | 8 | libpq | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27842](https://lwn.net/Articles/1079226/) | 10 | memcached | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27862](https://lwn.net/Articles/1079227/) | 9 | memcached | 2026-06-23 |
| AlmaLinux | [ALSA-2026:26447](https://lwn.net/Articles/1078404/) | 9 | podman | 2026-06-18 |
| AlmaLinux | [ALSA-2026:26205](https://lwn.net/Articles/1078405/) | 9 | postfix | 2026-06-18 |
| AlmaLinux | [ALSA-2026:27741](https://lwn.net/Articles/1079228/) | 9 | postgresql | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27743](https://lwn.net/Articles/1079229/) | 10 | postgresql16 | 2026-06-23 |
| AlmaLinux | [ALSA-2026:28208](https://lwn.net/Articles/1079230/) | 8 | postgresql:13 | 2026-06-24 |
| AlmaLinux | [ALSA-2026:28143](https://lwn.net/Articles/1079231/) | 8 | postgresql:16 | 2026-06-24 |
| AlmaLinux | [ALSA-2026:28000](https://lwn.net/Articles/1079232/) | 10 | python-urllib3 | 2026-06-23 |
| AlmaLinux | [ALSA-2026:27929](https://lwn.net/Articles/1079233/) | 10 | python3.14-urllib3 | 2026-06-23 |
| AlmaLinux | [ALSA-2026:26008](https://lwn.net/Articles/1079234/) | 8 | redis:6 | 2026-06-23 |
| AlmaLinux | [ALSA-2026:26410](https://lwn.net/Articles/1078406/) | 9 | rsync | 2026-06-18 |
| AlmaLinux | [ALSA-2026:28074](https://lwn.net/Articles/1079235/) | 9 | skopeo | 2026-06-23 |
| AlmaLinux | [ALSA-2026:28553](https://lwn.net/Articles/1079236/) | 8 | vim | 2026-06-24 |
| AlmaLinux | [ALSA-2026:26709](https://lwn.net/Articles/1078407/) | 8 | xorg-x11-server | 2026-06-18 |
| AlmaLinux | [ALSA-2026:26562](https://lwn.net/Articles/1078408/) | 8 | xorg-x11-server-Xwayland | 2026-06-17 |
| Debian | [DSA-6349-1](https://lwn.net/Articles/1078409/) | stable | atril | 2026-06-17 |
| Debian | [DLA-4641-1](https://lwn.net/Articles/1079237/) | LTS | beets | 2026-06-23 |
| Debian | [DSA-6351-1](https://lwn.net/Articles/1078607/) | stable | chromium | 2026-06-18 |
| Debian | [DSA-6361-1](https://lwn.net/Articles/1079029/) | stable | ffmpeg | 2026-06-22 |
| Debian | [DLA-4635-1](https://lwn.net/Articles/1078608/) | LTS | firefox-esr | 2026-06-19 |
| Debian | [DSA-6350-1](https://lwn.net/Articles/1078410/) | stable | firefox-esr | 2026-06-17 |
| Debian | [DSA-6353-1](https://lwn.net/Articles/1078852/) | stable | gst-libav1.0 | 2026-06-19 |
| Debian | [DSA-6362-1](https://lwn.net/Articles/1079238/) | stable | gst-plugins-bad1.0 | 2026-06-23 |
| Debian | [DSA-6359-1](https://lwn.net/Articles/1078853/) | stable | gst-plugins-good1.0 | 2026-06-21 |
| Debian | [DLA-4643-1](https://lwn.net/Articles/1079239/) | LTS | imagemagick | 2026-06-23 |
| Debian | [DSA-6356-1](https://lwn.net/Articles/1078854/) | stable | imagemagick | 2026-06-21 |
| Debian | [DSA-6355-1](https://lwn.net/Articles/1078855/) | stable | kernel | 2026-06-21 |
| Debian | [DLA-4637-1](https://lwn.net/Articles/1078857/) | LTS | libconfig-inifiles-perl | 2026-06-19 |
| Debian | [DSA-6354-1](https://lwn.net/Articles/1078856/) | stable | libconfig-inifiles-perl | 2026-06-19 |
| Debian | [DLA-4638-1](https://lwn.net/Articles/1078858/) | LTS | libgd-perl | 2026-06-21 |
| Debian | [DLA-4639-1](https://lwn.net/Articles/1078860/) | LTS | libhttp-daemon-perl | 2026-06-21 |
| Debian | [DSA-6358-1](https://lwn.net/Articles/1078859/) | stable | libhttp-daemon-perl | 2026-06-21 |
| Debian | [DLA-4644-1](https://lwn.net/Articles/1079240/) | LTS | libmatio | 2026-06-24 |
| Debian | [DLA-4640-1](https://lwn.net/Articles/1078861/) | LTS | mediawiki | 2026-06-22 |
| Debian | [DLA-4634-1](https://lwn.net/Articles/1078411/) | LTS | nginx | 2026-06-18 |
| Debian | [DSA-6357-1](https://lwn.net/Articles/1078862/) | stable | pillow | 2026-06-21 |
| Debian | [DSA-6363-1](https://lwn.net/Articles/1079241/) | stable | python-urllib3 | 2026-06-23 |
| Debian | [DSA-6360-1](https://lwn.net/Articles/1078863/) | stable | squid | 2026-06-21 |
| Debian | [DLA-4636-1](https://lwn.net/Articles/1078609/) | LTS | thunderbird | 2026-06-19 |
| Debian | [DSA-6351-1](https://lwn.net/Articles/1078610/) | stable | thunderbird | 2026-06-18 |
| Debian | [DLA-4642-1](https://lwn.net/Articles/1079242/) | LTS | u-boot | 2026-06-23 |
| Fedora | [FEDORA-2026-6d00814a85](https://lwn.net/Articles/1078864/) | F44 | 389-ds-base | 2026-06-21 |
| Fedora | [FEDORA-2026-1ad4561f49](https://lwn.net/Articles/1078866/) | F43 | alertmanager | 2026-06-21 |
| Fedora | [FEDORA-2026-87b103f151](https://lwn.net/Articles/1078865/) | F44 | alertmanager | 2026-06-21 |
| Fedora | [FEDORA-2026-f027f57724](https://lwn.net/Articles/1078867/) | F43 | ansible-core | 2026-06-20 |
| Fedora | [FEDORA-2026-7f70f809f0](https://lwn.net/Articles/1078868/) | F44 | ansible-core | 2026-06-20 |
| Fedora | [FEDORA-2026-ceb2f5c5bb](https://lwn.net/Articles/1078869/) | F44 | buildah | 2026-06-22 |
| Fedora | [FEDORA-2026-40cf884ac9](https://lwn.net/Articles/1078611/) | F43 | chromium | 2026-06-19 |
| Fedora | [FEDORA-2026-f9a0af40b2](https://lwn.net/Articles/1079243/) | F43 | chromium | 2026-06-24 |
| Fedora | [FEDORA-2026-650bd96540](https://lwn.net/Articles/1078870/) | F44 | chromium | 2026-06-21 |
| Fedora | [FEDORA-2026-c42d951aad](https://lwn.net/Articles/1079245/) | F43 | coturn | 2026-06-24 |
| Fedora | [FEDORA-2026-dda1360c18](https://lwn.net/Articles/1079244/) | F44 | coturn | 2026-06-24 |
| Fedora | [FEDORA-2026-e692d95607](https://lwn.net/Articles/1079030/) | F43 | erlang | 2026-06-23 |
| Fedora | [FEDORA-2026-ef630b13b0](https://lwn.net/Articles/1079031/) | F44 | erlang | 2026-06-23 |
| Fedora | [FEDORA-2026-2aa86d411f](https://lwn.net/Articles/1078872/) | F43 | erlang-cowboy | 2026-06-21 |
| Fedora | [FEDORA-2026-c17ea7a74d](https://lwn.net/Articles/1078871/) | F44 | erlang-cowboy | 2026-06-21 |
| Fedora | [FEDORA-2026-2aa86d411f](https://lwn.net/Articles/1078874/) | F43 | erlang-cowlib | 2026-06-21 |
| Fedora | [FEDORA-2026-c17ea7a74d](https://lwn.net/Articles/1078873/) | F44 | erlang-cowlib | 2026-06-21 |
| Fedora | [FEDORA-2026-2aa86d411f](https://lwn.net/Articles/1078876/) | F43 | erlang-gun | 2026-06-21 |
| Fedora | [FEDORA-2026-c17ea7a74d](https://lwn.net/Articles/1078875/) | F44 | erlang-gun | 2026-06-21 |
| Fedora | [FEDORA-2026-bc8f441ba4](https://lwn.net/Articles/1079032/) | F44 | ffmpeg | 2026-06-23 |
| Fedora | [FEDORA-2026-1c873954fa](https://lwn.net/Articles/1078612/) | F43 | firefox | 2026-06-19 |
| Fedora | [FEDORA-2026-9c6082d92d](https://lwn.net/Articles/1078877/) | F44 | freerdp | 2026-06-22 |
| Fedora | [FEDORA-2026-28949d21e5](https://lwn.net/Articles/1079246/) | F44 | frr | 2026-06-24 |
| Fedora | [FEDORA-2026-28949d21e5](https://lwn.net/Articles/1079247/) | F44 | grout | 2026-06-24 |
| Fedora | [FEDORA-2026-c2a89ccca5](https://lwn.net/Articles/1078879/) | F43 | kubernetes1.33 | 2026-06-21 |
| Fedora | [FEDORA-2026-da02662d41](https://lwn.net/Articles/1078878/) | F44 | kubernetes1.33 | 2026-06-21 |
| Fedora | [FEDORA-2026-88ab77d111](https://lwn.net/Articles/1078881/) | F43 | kubernetes1.34 | 2026-06-21 |
| Fedora | [FEDORA-2026-eee09dc43b](https://lwn.net/Articles/1078880/) | F44 | kubernetes1.34 | 2026-06-21 |
| Fedora | [FEDORA-2026-0544eff1d8](https://lwn.net/Articles/1078883/) | F43 | kubernetes1.35 | 2026-06-21 |
| Fedora | [FEDORA-2026-b56d6f4b79](https://lwn.net/Articles/1078882/) | F44 | kubernetes1.35 | 2026-06-21 |
| Fedora | [FEDORA-2026-85d5d5f493](https://lwn.net/Articles/1079249/) | F43 | materialx | 2026-06-24 |
| Fedora | [FEDORA-2026-d2806ddffc](https://lwn.net/Articles/1079248/) | F44 | materialx | 2026-06-24 |
| Fedora | [FEDORA-2026-bc38ebdf4c](https://lwn.net/Articles/1078885/) | F43 | mingw-SDL2\_image | 2026-06-21 |
| Fedora | [FEDORA-2026-6f328b5020](https://lwn.net/Articles/1078884/) | F44 | mingw-SDL2\_image | 2026-06-21 |
| Fedora | [FEDORA-2026-1c873954fa](https://lwn.net/Articles/1078613/) | F43 | nss | 2026-06-19 |
| Fedora | [FEDORA-2026-28036f36d5](https://lwn.net/Articles/1078614/) | F44 | ocserv | 2026-06-19 |
| Fedora | [FEDORA-2026-3fd14ce272](https://lwn.net/Articles/1078615/) | F43 | ongres-scram | 2026-06-19 |
| Fedora | [FEDORA-2026-3f51edec7b](https://lwn.net/Articles/1078886/) | F44 | ongres-scram | 2026-06-20 |
| Fedora | [FEDORA-2026-3fd14ce272](https://lwn.net/Articles/1078616/) | F43 | ongres-stringprep | 2026-06-19 |
| Fedora | [FEDORA-2026-3f51edec7b](https://lwn.net/Articles/1078887/) | F44 | ongres-stringprep | 2026-06-20 |
| Fedora | [FEDORA-2026-840334a045](https://lwn.net/Articles/1078888/) | F43 | openssl | 2026-06-21 |
| Fedora | [FEDORA-2026-6988e8f652](https://lwn.net/Articles/1078617/) | F43 | perl-Archive-Tar | 2026-06-19 |
| Fedora | [FEDORA-2026-3cce371bdf](https://lwn.net/Articles/1078889/) | F43 | perl-Config-IniFiles | 2026-06-20 |
| Fedora | [FEDORA-2026-1c2676703e](https://lwn.net/Articles/1078890/) | F44 | perl-Config-IniFiles | 2026-06-20 |
| Fedora | [FEDORA-2026-5cf57e43e3](https://lwn.net/Articles/1079251/) | F43 | perl-Crypt-DSA | 2026-06-24 |
| Fedora | [FEDORA-2026-f4a6b0c635](https://lwn.net/Articles/1079250/) | F44 | perl-Crypt-DSA | 2026-06-24 |
| Fedora | [FEDORA-2026-e8231b773d](https://lwn.net/Articles/1078892/) | F43 | perl-Crypt-PBKDF2 | 2026-06-21 |
| Fedora | [FEDORA-2026-5b12cc327e](https://lwn.net/Articles/1078891/) | F44 | perl-Crypt-PBKDF2 | 2026-06-21 |
| Fedora | [FEDORA-2026-63831abaee](https://lwn.net/Articles/1078619/) | F43 | perl-GD | 2026-06-19 |
| Fedora | [FEDORA-2026-263adf0222](https://lwn.net/Articles/1078618/) | F44 | perl-GD | 2026-06-19 |
| Fedora | [FEDORA-2026-f276b2154e](https://lwn.net/Articles/1078621/) | F43 | perl-HTTP-Daemon | 2026-06-19 |
| Fedora | [FEDORA-2026-8982379b5c](https://lwn.net/Articles/1078620/) | F44 | perl-HTTP-Daemon | 2026-06-19 |
| Fedora | [FEDORA-2026-9a8f233b8f](https://lwn.net/Articles/1078623/) | F43 | perl-Net-Statsd | 2026-06-19 |
| Fedora | [FEDORA-2026-9c71664439](https://lwn.net/Articles/1078622/) | F44 | perl-Net-Statsd | 2026-06-19 |
| Fedora | [FEDORA-2026-ceb2f5c5bb](https://lwn.net/Articles/1078893/) | F44 | podman | 2026-06-22 |
| Fedora | [FEDORA-2026-3f51edec7b](https://lwn.net/Articles/1078894/) | F44 | postgresql-jdbc | 2026-06-20 |
| Fedora | [FEDORA-2026-dfc0e362e6](https://lwn.net/Articles/1079033/) | F43 | prometheus | 2026-06-23 |
| Fedora | [FEDORA-2026-ebaf2bfd71](https://lwn.net/Articles/1079034/) | F44 | prometheus | 2026-06-23 |
| Fedora | [FEDORA-2026-9a7f59fa7c](https://lwn.net/Articles/1079035/) | F43 | python-scrapy | 2026-06-23 |
| Fedora | [FEDORA-2026-bdf3581452](https://lwn.net/Articles/1079036/) | F44 | python-scrapy | 2026-06-23 |

| Fedora | [FEDORA-2026-a2c583a4ab](https://lwn.net/Articles/1079037/) | F44 | python3-docs | 2026-06-23 |
| Fedora | [FEDORA-2026-2deb979d80](https://lwn.net/Articles/1078896/) | F43 | python3.13 | 2026-06-21 |
| Fedora | [FEDORA-2026-dfc9182263](https://lwn.net/Articles/1078895/) | F44 | python3.13 | 2026-06-21 |
| Fedora | [FEDORA-2026-a2c583a4ab](https://lwn.net/Articles/1079038/) | F44 | python3.14 | 2026-06-23 |
| Fedora | [FEDORA-2026-e6094447f0](https://lwn.net/Articles/1078625/) | F43 | restic | 2026-06-19 |
| Fedora | [FEDORA-2026-2290b9a9ad](https://lwn.net/Articles/1078624/) | F44 | restic | 2026-06-19 |
| Fedora | [FEDORA-2026-5358fb95a0](https://lwn.net/Articles/1078627/) | F43 | singularity-ce | 2026-06-19 |
| Fedora | [FEDORA-2026-63ae478575](https://lwn.net/Articles/1078626/) | F44 | singularity-ce | 2026-06-19 |
| Fedora | [FEDORA-2026-284c049f7f](https://lwn.net/Articles/1078897/) | F44 | strongswan | 2026-06-22 |
| Fedora | [FEDORA-2026-2641c0a950](https://lwn.net/Articles/1079039/) | F43 | thorvg | 2026-06-23 |
| Fedora | [FEDORA-2026-3d1fcd4ffc](https://lwn.net/Articles/1079040/) | F44 | thorvg | 2026-06-23 |
| Fedora | [FEDORA-2026-e7c97d043e](https://lwn.net/Articles/1079041/) | F44 | tigervnc | 2026-06-23 |
| Fedora | [FEDORA-2026-c70cb96ff1](https://lwn.net/Articles/1078628/) | F44 | util-linux | 2026-06-19 |
| Fedora | [FEDORA-2026-3b2ddea116](https://lwn.net/Articles/1079042/) | F43 | vips | 2026-06-23 |
| Fedora | [FEDORA-2026-b9f00ad1b7](https://lwn.net/Articles/1079043/) | F44 | vips | 2026-06-23 |
| Fedora | [FEDORA-2026-cbf4cd18d1](https://lwn.net/Articles/1078629/) | F43 | vorbis-tools | 2026-06-19 |
| Fedora | [FEDORA-2026-1557aaef26](https://lwn.net/Articles/1078898/) | F43 | webkitgtk | 2026-06-20 |
| Fedora | [FEDORA-2026-d8f8abf763](https://lwn.net/Articles/1078899/) | F44 | xdg-desktop-portal | 2026-06-21 |
| Fedora | [FEDORA-2026-03f87de373](https://lwn.net/Articles/1079252/) | F43 | yt-dlp | 2026-06-24 |
| Fedora | [FEDORA-2026-bb702c613b](https://lwn.net/Articles/1078900/) | F44 | yt-dlp | 2026-06-21 |
| Mageia | [MGASA-2026-0222](https://lwn.net/Articles/1078630/) | 9 | gstreamer1.0-\* | 2026-06-18 |
| Mageia | [MGASA-2026-0221](https://lwn.net/Articles/1078412/) | 9 | libcap | 2026-06-18 |
| Mageia | [MGASA-2026-0223](https://lwn.net/Articles/1078631/) | 9 | libupnp | 2026-06-18 |
| Mageia | [MGASA-2026-0225](https://lwn.net/Articles/1078632/) | 9 | luajit | 2026-06-18 |
| Mageia | [MGASA-2026-0228](https://lwn.net/Articles/1079044/) | 9 | mumble | 2026-06-23 |
| Mageia | [MGASA-2026-0224](https://lwn.net/Articles/1078633/) | 9 | opensc | 2026-06-18 |
| Mageia | [MGASA-2026-0231](https://lwn.net/Articles/1079253/) | 9 | opensc | 2026-06-24 |
| Mageia | [MGASA-2026-0220](https://lwn.net/Articles/1078413/) | 9 | perl | 2026-06-18 |
| Mageia | [MGASA-2026-0230](https://lwn.net/Articles/1079254/) | 9 | perl-Archive-Tar | 2026-06-24 |
| Mageia | [MGASA-2026-0229](https://lwn.net/Articles/1079255/) | 9 | podofo | 2026-06-24 |
| Mageia | [MGASA-2026-0219](https://lwn.net/Articles/1078414/) | 9 | python-pillow | 2026-06-18 |
| Mageia | [MGASA-2026-0226](https://lwn.net/Articles/1078634/) | 9 | ruby-rack | 2026-06-18 |
| Mageia | [MGASA-2026-0227](https://lwn.net/Articles/1079045/) | 9 | sslh | 2026-06-23 |
| Oracle | [ELSA-2026-26459](https://lwn.net/Articles/1079046/) | OL8 | 389-ds:1.4 | 2026-06-22 |
| Oracle | [ELSA-2026-26534](https://lwn.net/Articles/1079047/) | OL8 | dracut | 2026-06-22 |
| Oracle | [ELSA-2026-13672](https://lwn.net/Articles/1079256/) | OL9 | fence-agents | 2026-06-23 |
| Oracle | [ELSA-2026-19704](https://lwn.net/Articles/1078415/) | OL7 | firefox | 2026-06-18 |
| Oracle | [ELSA-2026-22708](https://lwn.net/Articles/1078416/) | OL7 | firefox | 2026-06-18 |
| Oracle | [ELSA-2026-27717](https://lwn.net/Articles/1079048/) | OL8 | firefox | 2026-06-22 |
| Oracle | [ELSA-2026-7850](https://lwn.net/Articles/1078417/) | OL7 | gstreamer-plugins-base and gstreamer-plugins-good | 2026-06-18 |
| Oracle | [ELSA-2026-26335](https://lwn.net/Articles/1079049/) | OL8 | hplip | 2026-06-22 |
| Oracle | [ELSA-2026-25090](https://lwn.net/Articles/1078418/) | OL8 | httpd:2.4 | 2026-06-18 |
| Oracle | [ELSA-2026-25121](https://lwn.net/Articles/1078419/) | OL8 | kernel | 2026-06-18 |
| Oracle | [ELSA-2026-50318](https://lwn.net/Articles/1078421/) | OL8 | kernel | 2026-06-18 |
| Oracle | [ELSA-2026-27353](https://lwn.net/Articles/1079050/) | OL8 | kernel | 2026-06-22 |
| Oracle | [ELSA-2026-26427](https://lwn.net/Articles/1079051/) | OL8 | kernel | 2026-06-22 |
| Oracle | [ELSA-2026-50318](https://lwn.net/Articles/1078420/) | OL9 | kernel | 2026-06-18 |
| Oracle | [ELSA-2026-50318](https://lwn.net/Articles/1078422/) | OL9 | kernel | 2026-06-18 |
| Oracle | [ELSA-2026-50319](https://lwn.net/Articles/1079052/) | OL9 | kernel | 2026-06-22 |
| Oracle | [ELSA-2026-26348](https://lwn.net/Articles/1078423/) | OL8 | libpng12 | 2026-06-18 |
| Oracle | [ELSA-2026-26347](https://lwn.net/Articles/1078424/) | OL8 | libpng15 | 2026-06-18 |
| Oracle | [ELSA-2026-27738](https://lwn.net/Articles/1079257/) | OL8 | libpq | 2026-06-23 |
| Oracle | [ELSA-2026-26354](https://lwn.net/Articles/1078425/) | OL8 | libxml2 | 2026-06-18 |
| Oracle | [ELSA-2026-26355](https://lwn.net/Articles/1078426/) | OL8 | libxslt | 2026-06-18 |
| Oracle | [ELSA-2026-26180](https://lwn.net/Articles/1079258/) | OL8 | mysql:8.4 | 2026-06-23 |
| Oracle | [ELSA-2026-26352](https://lwn.net/Articles/1078427/) | OL8 | opencryptoki | 2026-06-18 |
| Oracle | [ELSA-2026-22468](https://lwn.net/Articles/1079053/) | OL7 | openssh | 2026-06-22 |
| Oracle | [ELSA-2026-26275](https://lwn.net/Articles/1078428/) | OL8 | openssl | 2026-06-18 |
| Oracle | [ELSA-2026-25932](https://lwn.net/Articles/1078429/) | OL8 | postfix | 2026-06-18 |
| Oracle | [ELSA-2026-26181](https://lwn.net/Articles/1079054/) | OL8 | postgresql:15 | 2026-06-22 |
| Oracle | [ELSA-2026-28143](https://lwn.net/Articles/1079259/) | OL8 | postgresql:16 | 2026-06-23 |
| Oracle | [ELSA-2026-26008](https://lwn.net/Articles/1079055/) | OL8 | redis:6 | 2026-06-22 |
| Oracle | [ELSA-2026-26408](https://lwn.net/Articles/1078430/) | OL8 | rsync | 2026-06-18 |
| Oracle | [ELSA-2026-50319](https://lwn.net/Articles/1079056/) |  | uek-kernel | 2026-06-22 |
| Oracle | [ELSA-2026-25918](https://lwn.net/Articles/1078431/) | OL8 | webkit2gtk3 | 2026-06-18 |
| Oracle | [ELSA-2026-26709](https://lwn.net/Articles/1078432/) | OL8 | xorg-x11-server | 2026-06-18 |
| Oracle | [ELSA-2026-26562](https://lwn.net/Articles/1078433/) | OL8 | xorg-x11-server-Xwayland | 2026-06-18 |
| Red Hat | [RHSA-2026:23102-01](https://lwn.net/Articles/1079025/) | EL10 | delve | 2026-06-23 |
| Red Hat | [RHSA-2026:23103-01](https://lwn.net/Articles/1079024/) | EL10.0 | delve | 2026-06-23 |
| Red Hat | [RHSA-2026:13665-01](https://lwn.net/Articles/1079197/) | EL10.0 | firefox | 2026-06-24 |
| Red Hat | [RHSA-2026:13977-01](https://lwn.net/Articles/1079200/) | EL7 | firefox | 2026-06-24 |
| Red Hat | [RHSA-2026:13600-01](https://lwn.net/Articles/1079202/) | EL8.4 | firefox | 2026-06-24 |
| Red Hat | [RHSA-2026:13683-01](https://lwn.net/Articles/1079198/) | EL8.6 | firefox | 2026-06-24 |
| Red Hat | [RHSA-2026:13682-01](https://lwn.net/Articles/1079201/) | EL8.8 | firefox | 2026-06-24 |
| Red Hat | [RHSA-2026:13596-01](https://lwn.net/Articles/1079203/) | EL9.0 | firefox | 2026-06-24 |
| Red Hat | [RHSA-2026:13922-01](https://lwn.net/Articles/1079190/) | EL9.2 | firefox | 2026-06-24 |
| Red Hat | [RHSA-2026:13582-01](https://lwn.net/Articles/1079204/) | EL9.4 | firefox | 2026-06-24 |
| Red Hat | [RHSA-2026:13583-01](https://lwn.net/Articles/1079205/) | EL9.6 | firefox | 2026-06-24 |
| Red Hat | [RHSA-2026:28038-01](https://lwn.net/Articles/1079018/) | EL9.6 | gvisor-tap-vsock | 2026-06-23 |
| Red Hat | [RHSA-2026:28233-01](https://lwn.net/Articles/1079185/) | EL10 | libpng | 2026-06-24 |
| Red Hat | [RHSA-2026:18064-01](https://lwn.net/Articles/1079191/) | EL10 | libpng | 2026-06-24 |
| Red Hat | [RHSA-2026:20551-01](https://lwn.net/Articles/1079186/) | EL10.0 | libpng | 2026-06-24 |
| Red Hat | [RHSA-2026:28255-01](https://lwn.net/Articles/1079184/) | EL9 | libpng | 2026-06-24 |
| Red Hat | [RHSA-2026:18028-01](https://lwn.net/Articles/1079196/) | EL9 | libpng | 2026-06-24 |
| Red Hat | [RHSA-2026:20550-01](https://lwn.net/Articles/1079189/) | EL9.2 | libpng | 2026-06-24 |
| Red Hat | [RHSA-2026:20549-01](https://lwn.net/Articles/1079194/) | EL9.4 | libpng | 2026-06-24 |
| Red Hat | [RHSA-2026:20548-01](https://lwn.net/Articles/1079193/) | EL9.6 | libpng | 2026-06-24 |
| Red Hat | [RHSA-2026:26348-01](https://lwn.net/Articles/1079187/) | EL8 | libpng12 | 2026-06-24 |
| Red Hat | [RHSA-2026:29020-01](https://lwn.net/Articles/1079180/) | EL8.6 | libpng12 | 2026-06-24 |
| Red Hat | [RHSA-2026:26347-01](https://lwn.net/Articles/1079188/) | EL8 | libpng15 | 2026-06-24 |
| Red Hat | [RHSA-2026:28244-01](https://lwn.net/Articles/1079182/) | EL9 | libpng15 | 2026-06-24 |
| Red Hat | [RHSA-2026:28458-01](https://lwn.net/Articles/1079181/) | EL9.2 | libpng15 | 2026-06-24 |
| Red Hat | [RHSA-2026:28457-01](https://lwn.net/Articles/1079183/) | EL9.4 | libpng15 | 2026-06-24 |
| Red Hat | [RHSA-2026:28922-01](https://lwn.net/Articles/1079207/) | EL8 | libreoffice | 2026-06-24 |
| Red Hat | [RHSA-2026:28290-01](https://lwn.net/Articles/1079208/) | EL9 | libreoffice | 2026-06-24 |
| Red Hat | [RHSA-2026:19159-01](https://lwn.net/Articles/1079005/) | EL10 | nginx | 2026-06-23 |
| Red Hat | [RHSA-2026:18063-01](https://lwn.net/Articles/1079007/) | EL10 | nginx | 2026-06-23 |
| Red Hat | [RHSA-2026:17790-01](https://lwn.net/Articles/1079012/) | EL10.0 | nginx | 2026-06-23 |
| Red Hat | [RHSA-2026:18029-01](https://lwn.net/Articles/1079009/) | EL9 | nginx | 2026-06-23 |
| Red Hat | [RHSA-2026:19374-01](https://lwn.net/Articles/1079003/) | EL9 | nginx | 2026-06-23 |
| Red Hat | [RHSA-2026:17791-01](https://lwn.net/Articles/1079011/) | EL9.0 | nginx | 2026-06-23 |
| Red Hat | [RHSA-2026:17751-01](https://lwn.net/Articles/1079014/) | EL9.2 | nginx | 2026-06-23 |
| Red Hat | [RHSA-2026:17792-01](https://lwn.net/Articles/1079016/) | EL9.4 | nginx | 2026-06-23 |
| Red Hat | [RHSA-2026:17794-01](https://lwn.net/Articles/1079010/) | EL9.6 | nginx | 2026-06-23 |
| Red Hat | [RHSA-2026:18041-01](https://lwn.net/Articles/1079008/) | EL8 | nginx:1.24 | 2026-06-23 |
| Red Hat | [RHSA-2026:28921-01](https://lwn.net/Articles/1079215/) | EL8 | nginx:1.24 | 2026-06-24 |
| Red Hat | [RHSA-2026:19371-01](https://lwn.net/Articles/1079006/) | EL9 | nginx:1.24 | 2026-06-23 |
| Red Hat | [RHSA-2026:28212-01](https://lwn.net/Articles/1079216/) | EL9 | nginx:1.24 | 2026-06-24 |
| Red Hat | [RHSA-2026:17793-01](https://lwn.net/Articles/1079013/) | EL9.4 | nginx:1.24 | 2026-06-23 |
| Red Hat | [RHSA-2026:17752-01](https://lwn.net/Articles/1079017/) | EL9.6 | nginx:1.24 | 2026-06-23 |
| Red Hat | [RHSA-2026:19372-01](https://lwn.net/Articles/1079004/) | EL9 | nginx:1.26 | 2026-06-23 |
| Red Hat | [RHSA-2026:17753-01](https://lwn.net/Articles/1079015/) | EL9.6 | nginx:1.26 | 2026-06-23 |
| Red Hat | [RHSA-2026:27856-01](https://lwn.net/Articles/1078847/) | EL10.0 | osbuild-composer | 2026-06-22 |
| Red Hat | [RHSA-2026:27712-01](https://lwn.net/Articles/1078848/) | EL9.6 | osbuild-composer | 2026-06-22 |
| Red Hat | [RHSA-2026:22709-01](https://lwn.net/Articles/1079027/) | EL9.6 | osbuild-composer | 2026-06-23 |
| Red Hat | [RHSA-2026:24470-01](https://lwn.net/Articles/1079023/) | EL10 | podman | 2026-06-23 |
| Red Hat | [RHSA-2026:26447-01](https://lwn.net/Articles/1079020/) | EL9 | podman | 2026-06-23 |
| Red Hat | [RHSA-2026:22713-01](https://lwn.net/Articles/1079026/) | EL10.0 | rhc | 2026-06-23 |
| Red Hat | [RHSA-2026:24337-01](https://lwn.net/Articles/1079022/) | EL9.6 | rhc | 2026-06-23 |
| Red Hat | [RHSA-2026:28074-01](https://lwn.net/Articles/1079019/) | EL9 | skopeo | 2026-06-23 |

| Red Hat | [RHSA-2026:14303-01](https://lwn.net/Articles/1079195/) | EL8.4 | thunderbird | 2026-06-24 |
| Red Hat | [RHSA-2026:15889-01](https://lwn.net/Articles/1079192/) | EL8.6 | thunderbird | 2026-06-24 |
| Red Hat | [RHSA-2026:14223-01](https://lwn.net/Articles/1079199/) | EL8.8 | thunderbird | 2026-06-24 |
| Red Hat | [RHSA-2026:13533-01](https://lwn.net/Articles/1079206/) | EL9.4 | thunderbird | 2026-06-24 |
| Red Hat | [RHSA-2026:28923-01](https://lwn.net/Articles/1079209/) | EL8 | tigervnc | 2026-06-24 |
| Red Hat | [RHSA-2026:26709-01](https://lwn.net/Articles/1079210/) | EL8 | xorg-x11-server | 2026-06-24 |
| Red Hat | [RHSA-2026:26610-01](https://lwn.net/Articles/1079211/) | EL9 | xorg-x11-server | 2026-06-24 |
| Red Hat | [RHSA-2026:26566-01](https://lwn.net/Articles/1079214/) | EL10 | xorg-x11-server-Xwayland | 2026-06-24 |
| Red Hat | [RHSA-2026:26562-01](https://lwn.net/Articles/1079213/) | EL8 | xorg-x11-server-Xwayland | 2026-06-24 |
| Red Hat | [RHSA-2026:26590-01](https://lwn.net/Articles/1079212/) | EL9 | xorg-x11-server-Xwayland | 2026-06-24 |
| Red Hat | [RHSA-2026:24716-01](https://lwn.net/Articles/1079021/) | EL10 | yggdrasil | 2026-06-23 |
| Slackware | [SSA:2026-168-01](https://lwn.net/Articles/1078434/) |  | bind | 2026-06-17 |
| Slackware | [SSA:2026-174-01](https://lwn.net/Articles/1079260/) |  | libarchive | 2026-06-23 |
| Slackware | [SSA:2026-168-02](https://lwn.net/Articles/1078435/) |  | libidn | 2026-06-17 |
| Slackware | [SSA:2026-168-03](https://lwn.net/Articles/1078436/) |  | mozilla | 2026-06-17 |
| Slackware | [SSA:2026-168-04](https://lwn.net/Articles/1078437/) |  | mozilla | 2026-06-17 |
| Slackware | [SSA:2026-168-05](https://lwn.net/Articles/1078438/) |  | openssl | 2026-06-17 |
| SUSE | [SUSE-SU-2026:2580-1](https://lwn.net/Articles/1079298/) | SLE15 oS15.4 | ImageMagick | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2428-1](https://lwn.net/Articles/1078446/) | SLE12 | LibVNCServer | 2026-06-17 |
| SUSE | [SUSE-SU-2026:2427-1](https://lwn.net/Articles/1078445/) | SLE15 oS15.6 | LibVNCServer | 2026-06-17 |
| SUSE | [SUSE-SU-2026:22190-1](https://lwn.net/Articles/1079314/) | SLE16.0 | LibVNCServer | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2438-1](https://lwn.net/Articles/1078439/) | SLE15 | alloy | 2026-06-17 |
| SUSE | [openSUSE-SU-2026:11053-1](https://lwn.net/Articles/1078901/) | TW | alloy | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2467-1](https://lwn.net/Articles/1078903/) | MP4.3 SLE15 | amazon-ssm-agent | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2468-1](https://lwn.net/Articles/1078902/) | SLE12 | amazon-ssm-agent | 2026-06-19 |
| SUSE | [SUSE-SU-2026:22157-1](https://lwn.net/Articles/1079261/) | SLE16.0 | amazon-ssm-agent | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22171-1](https://lwn.net/Articles/1079262/) | SLE16.0 | ansible-core | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11064-1](https://lwn.net/Articles/1078904/) | TW | ansible-core | 2026-06-20 |
| SUSE | [SUSE-SU-2026:2472-1](https://lwn.net/Articles/1078905/) | SLE15 | apache-sshd, jpgpj | 2026-06-19 |
| SUSE | [SUSE-SU-2026:22209-1](https://lwn.net/Articles/1079263/) | SLE16.0 | apache2 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22199-1](https://lwn.net/Articles/1079264/) | SLE16.0 | apache2 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2466-1](https://lwn.net/Articles/1078906/) | MP4.3 SLE15 oS15.4 | azure-storage-azcopy | 2026-06-19 |
| SUSE | [SUSE-SU-2026:22198-1](https://lwn.net/Articles/1079265/) | SLE16.0 | bind | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11073-1](https://lwn.net/Articles/1079266/) | TW | bitcoin-qt6 | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11071-1](https://lwn.net/Articles/1078907/) | TW | chromedriver | 2026-06-21 |
| SUSE | [SUSE-SU-2026:2493-1](https://lwn.net/Articles/1079057/) | SLE15 | containerized-data-importer | 2026-06-22 |
| SUSE | [openSUSE-SU-2026:11054-1](https://lwn.net/Articles/1078908/) | TW | containerized-data-importer | 2026-06-19 |
| SUSE | [openSUSE-SU-2026:11074-1](https://lwn.net/Articles/1079267/) | TW | containerized-data-importer | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22146-1](https://lwn.net/Articles/1078635/) | SLE-m6.2 | curl | 2026-06-18 |
| SUSE | [SUSE-SU-2026:22156-1](https://lwn.net/Articles/1079268/) | SLE16.0 | curl | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22159-1](https://lwn.net/Articles/1079269/) | SLE16.0 | distribution | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2458-1](https://lwn.net/Articles/1078636/) | SLE12 | dnsmasq | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2429-1](https://lwn.net/Articles/1078440/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 | docker | 2026-06-17 |
| SUSE | [SUSE-SU-2026:2578-1](https://lwn.net/Articles/1079271/) | SLE12 | docker-stable | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2579-1](https://lwn.net/Articles/1079270/) | SLE15 | docker-stable | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11075-1](https://lwn.net/Articles/1079272/) | TW | docker-stable | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22185-1](https://lwn.net/Articles/1079273/) | SLE16.0 | dovecot24 | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11076-1](https://lwn.net/Articles/1079274/) | TW | dracut | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:20966-1](https://lwn.net/Articles/1079275/) | oS16.0 | editorconfig-core-c | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22141-1](https://lwn.net/Articles/1078441/) | SLE-m6.1 | elemental-system-agent | 2026-06-17 |
| SUSE | [SUSE-SU-2026:2584-1](https://lwn.net/Articles/1079276/) | SLE15 oS15.4 | exiv2 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2444-1](https://lwn.net/Articles/1078637/) | SLE15 oS15.4 | ffmpeg-4 | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2445-1](https://lwn.net/Articles/1078638/) | SLE15 oS15.6 | ffmpeg-4 | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2583-1](https://lwn.net/Articles/1079277/) | SLE12 | firefox | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2582-1](https://lwn.net/Articles/1079278/) | SLE15 | firefox | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11052-1](https://lwn.net/Articles/1078909/) | TW | firefox | 2026-06-19 |
| SUSE | [SUSE-SU-2026:22216-1](https://lwn.net/Articles/1079280/) | SLE-m6.2 | freeipmi | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22163-1](https://lwn.net/Articles/1079279/) | SLE16.0 | freeipmi | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22194-1](https://lwn.net/Articles/1079281/) | SLE16.0 | freerdp | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2455-1](https://lwn.net/Articles/1078641/) | SLE12 | frr | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2457-1](https://lwn.net/Articles/1078640/) | SLE15 | frr | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2454-1](https://lwn.net/Articles/1078639/) | SLE15 oS15.5 | frr | 2026-06-18 |
| SUSE | [openSUSE-SU-2026:11077-1](https://lwn.net/Articles/1079282/) | TW | ghc-aws | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11078-1](https://lwn.net/Articles/1079283/) | TW | ghc-crypton-asn1-encoding | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11079-1](https://lwn.net/Articles/1079284/) | TW | ghc-crypton-asn1-parse | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11080-1](https://lwn.net/Articles/1079285/) | TW | ghc-crypton-asn1-types | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11081-1](https://lwn.net/Articles/1079286/) | TW | ghc-crypton-pem | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22230-1](https://lwn.net/Articles/1079287/) | SLE-m6.2 | glib-networking | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2465-1](https://lwn.net/Articles/1078910/) | SLE11 | glibc | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2440-1](https://lwn.net/Articles/1078442/) | SLE12 | glibc | 2026-06-18 |
| SUSE | [SUSE-SU-2026:22155-1](https://lwn.net/Articles/1079288/) | SLE16.0 | go1.25 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22154-1](https://lwn.net/Articles/1079289/) | SLE16.0 | go1.26 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2581-1](https://lwn.net/Articles/1079290/) | SLE12 | google-guest-agent | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11046-1](https://lwn.net/Articles/1078642/) | TW | google-osconfig-agent | 2026-06-18 |
| SUSE | [openSUSE-SU-2026:11040-1](https://lwn.net/Articles/1078443/) | TW | grafana | 2026-06-17 |
| SUSE | [SUSE-SU-2026:22225-1](https://lwn.net/Articles/1079292/) | SLE-m6.2 | graphite2 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2474-1](https://lwn.net/Articles/1078911/) | SLE12 | graphite2 | 2026-06-22 |
| SUSE | [SUSE-SU-2026:2477-1](https://lwn.net/Articles/1079059/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 | graphite2 | 2026-06-22 |
| SUSE | [SUSE-SU-2026:2478-1](https://lwn.net/Articles/1079058/) | SLE15 oS15.6 | graphite2 | 2026-06-22 |
| SUSE | [SUSE-SU-2026:22191-1](https://lwn.net/Articles/1079291/) | SLE16.0 | graphite2 | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:0212-1](https://lwn.net/Articles/1079293/) | osB15 | hamlib | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22233-1](https://lwn.net/Articles/1079294/) | SLE-m6.2 | helm | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2439-1](https://lwn.net/Articles/1078444/) | SLE15 SLE5.5 SLE-m5.5 | helm | 2026-06-17 |
| SUSE | [SUSE-SU-2026:22186-1](https://lwn.net/Articles/1079295/) | SLE16.0 | himmelblau | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22224-1](https://lwn.net/Articles/1079297/) | SLE-m6.2 | ignition | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22181-1](https://lwn.net/Articles/1079296/) | SLE16.0 | ignition | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11056-1](https://lwn.net/Articles/1078912/) | TW | inspektor-gadget | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2453-1](https://lwn.net/Articles/1078643/) | SLE12 | java-1\_8\_0-ibm | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2450-1](https://lwn.net/Articles/1078644/) | SLE12 | kernel | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2482-1](https://lwn.net/Articles/1079060/) | SLE15 | kernel | 2026-06-22 |
| SUSE | [SUSE-SU-2026:2591-1](https://lwn.net/Articles/1079299/) | SLE15 | kernel | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:20965-1](https://lwn.net/Articles/1079300/) | SLE16.0 oS16.0 | kernel | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2449-1](https://lwn.net/Articles/1078645/) | SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | krb5 | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2460-1](https://lwn.net/Articles/1078646/) | SLE15 oS15.6 | kubernetes-old | 2026-06-19 |
| SUSE | [openSUSE-SU-2026:11057-1](https://lwn.net/Articles/1078913/) | TW | kubevirt | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2461-1](https://lwn.net/Articles/1078647/) | SLE15 | ldns | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2462-1](https://lwn.net/Articles/1078648/) | SLE15 oS15.6 | ldns | 2026-06-19 |
| SUSE | [SUSE-SU-2026:22167-1](https://lwn.net/Articles/1079301/) | SLE16.0 | ldns | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11059-1](https://lwn.net/Articles/1078914/) | TW | lemon | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2599-1](https://lwn.net/Articles/1079302/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 oS15.4 | libarchive | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2490-1](https://lwn.net/Articles/1079061/) | SLE15 oS15.6 | libarchive | 2026-06-22 |
| SUSE | [SUSE-SU-2026:22175-1](https://lwn.net/Articles/1079303/) | SLE16.0 | libcaca | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22153-1](https://lwn.net/Articles/1079304/) | SLE16.0 | libheif | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2524-1](https://lwn.net/Articles/1079307/) | SLE15 | libinput | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2530-1](https://lwn.net/Articles/1079308/) | SLE15 oS15.4 | libinput | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2523-1](https://lwn.net/Articles/1079309/) | SLE15 oS15.5 | libinput | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2529-1](https://lwn.net/Articles/1079306/) | SLE15 oS15.6 | libinput | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22165-1](https://lwn.net/Articles/1079305/) | SLE16.0 | libinput | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22174-1](https://lwn.net/Articles/1079310/) | SLE16.0 | libjxl | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2531-1](https://lwn.net/Articles/1079313/) | SLE15 | libsolv, libzypp, zypper | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2575-1](https://lwn.net/Articles/1079312/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | libsolv, libzypp, zypper | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2590-1](https://lwn.net/Articles/1079311/) | SLE15 oS15.6 | libsolv, libzypp, zypper | 2026-06-23 |

| SUSE | [openSUSE-SU-2026:11049-1](https://lwn.net/Articles/1078649/) | TW | liburiparser1 | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2585-1](https://lwn.net/Articles/1079315/) | SLE12 | libxslt | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22208-1](https://lwn.net/Articles/1079316/) | SLE16.0 | libyang | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22200-1](https://lwn.net/Articles/1079317/) | SLE16.0 | libyang | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22226-1](https://lwn.net/Articles/1079319/) | SLE-m6.2 | mcphost | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22193-1](https://lwn.net/Articles/1079318/) | SLE16.0 | mcphost | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22210-1](https://lwn.net/Articles/1079320/) | SLE16.0 | mozjs128 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22201-1](https://lwn.net/Articles/1079321/) | SLE16.0 | mozjs128 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22228-1](https://lwn.net/Articles/1079322/) | SLE-m6.2 | ncurses | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22178-1](https://lwn.net/Articles/1079323/) | SLE16.0 | nginx | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:20967-1](https://lwn.net/Articles/1079324/) | oS16.0 | opensc | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2515-1](https://lwn.net/Articles/1079062/) | SLE11 | openssh, openssh-askpass-gnome | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2430-1](https://lwn.net/Articles/1078447/) | SLE12 | openssh8.4 | 2026-06-17 |
| SUSE | [SUSE-SU-2026:2598-1](https://lwn.net/Articles/1079325/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | openssl-3 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22145-1](https://lwn.net/Articles/1078650/) | SLE-m6.2 | openvswitch | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2463-1](https://lwn.net/Articles/1078915/) | SLE15 | openvswitch | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2481-1](https://lwn.net/Articles/1079063/) | SLE15 oS15.4 | openvswitch | 2026-06-22 |
| SUSE | [SUSE-SU-2026:2475-1](https://lwn.net/Articles/1079064/) | SLE15 oS15.6 | openvswitch | 2026-06-22 |
| SUSE | [SUSE-SU-2026:22152-1](https://lwn.net/Articles/1079326/) | SLE16.0 | openvswitch | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2476-1](https://lwn.net/Articles/1079065/) | SLE15 SLE5.5 SLE-m5.5 oS15.5 | openvswitch3 | 2026-06-22 |
| SUSE | [SUSE-SU-2026:22182-1](https://lwn.net/Articles/1079327/) | SLE16.0 | papers | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:0209-1](https://lwn.net/Articles/1078448/) | osB15 | perl-GD | 2026-06-18 |
| SUSE | [SUSE-SU-2026:22189-1](https://lwn.net/Articles/1079328/) | SLE16.0 | perl-HTML-Parser | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2442-1](https://lwn.net/Articles/1078449/) | SLE15 | perl-HTTP-Daemon | 2026-06-18 |
| SUSE | [SUSE-SU-2026:22187-1](https://lwn.net/Articles/1079329/) | SLE16.0 | perl-HTTP-Daemon | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22188-1](https://lwn.net/Articles/1079330/) | SLE16.0 | perl-Protocol-HTTP2 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2596-1](https://lwn.net/Articles/1079331/) | SLE15 SES7.1 oS15.3 | podman | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2597-1](https://lwn.net/Articles/1079332/) | SLE15 SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 oS15.4 | podman | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2489-1](https://lwn.net/Articles/1079066/) | oS15.3 | postfix | 2026-06-22 |
| SUSE | [SUSE-SU-2026:22177-1](https://lwn.net/Articles/1079333/) | SLE16.0 | postgresql14 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22183-1](https://lwn.net/Articles/1079334/) | SLE16.0 | postgresql15 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22184-1](https://lwn.net/Articles/1079335/) | SLE16.0 | postgresql16 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22149-1](https://lwn.net/Articles/1079336/) | SLE16.0 | postgresql17 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22220-1](https://lwn.net/Articles/1079341/) | SLE-m6.2 | python-PyJWT | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22170-1](https://lwn.net/Articles/1079340/) | SLE16.0 | python-PyJWT | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11041-1](https://lwn.net/Articles/1078450/) | TW | python-WebOb-doc | 2026-06-17 |
| SUSE | [SUSE-SU-2026:22173-1](https://lwn.net/Articles/1079337/) | SLE16.0 | python-aiohttp | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22158-1](https://lwn.net/Articles/1079338/) | SLE16.0 | python-ecdsa | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2488-1](https://lwn.net/Articles/1079067/) | SLE5.3 SLE5.4 SLE-m5.3 SLE-m5.4 | python-lxml | 2026-06-22 |
| SUSE | [openSUSE-SU-2026:0211-1](https://lwn.net/Articles/1079068/) | osB15 | python-nltk | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22192-1](https://lwn.net/Articles/1079339/) | SLE16.0 | python-paramiko | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2483-1](https://lwn.net/Articles/1079069/) | oS15.6 | python-python-multipart | 2026-06-22 |
| SUSE | [SUSE-SU-2026:22151-1](https://lwn.net/Articles/1079342/) | SLE16.0 | python-starlette | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2470-1](https://lwn.net/Articles/1078916/) | oS15.6 | python-starlette | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2486-1](https://lwn.net/Articles/1079070/) | MP4.3 SLE15 oS15.4 | python-urllib3 | 2026-06-22 |
| SUSE | [openSUSE-SU-2026:11068-1](https://lwn.net/Articles/1078917/) | TW | python311 | 2026-06-20 |
| SUSE | [openSUSE-SU-2026:11044-1](https://lwn.net/Articles/1078451/) | TW | python311-google-adk | 2026-06-17 |
| SUSE | [openSUSE-SU-2026:11067-1](https://lwn.net/Articles/1078918/) | TW | python311-joserfc | 2026-06-20 |
| SUSE | [SUSE-SU-2026:2464-1](https://lwn.net/Articles/1078919/) | SLE15 | python313 | 2026-06-19 |
| SUSE | [SUSE-SU-2026:2595-1](https://lwn.net/Articles/1079343/) | SLE15 oS15.4 | rekor | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2487-1](https://lwn.net/Articles/1079071/) | SLE15 oS15.5 | rmt-server | 2026-06-22 |
| SUSE | [SUSE-SU-2026:2452-1](https://lwn.net/Articles/1078652/) | SLE15 | rootlesskit | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2451-1](https://lwn.net/Articles/1078651/) | SLE15 oS15.6 | rootlesskit | 2026-06-18 |
| SUSE | [SUSE-SU-2026:2441-1](https://lwn.net/Articles/1078452/) | SLE15 oS15.6 | rustup | 2026-06-18 |
| SUSE | [SUSE-SU-2026:22218-1](https://lwn.net/Articles/1079347/) | SLE-m6.2 | sqlite3 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2527-1](https://lwn.net/Articles/1079346/) | SLE12 | sqlite3 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2528-1](https://lwn.net/Articles/1079345/) | SLE15 SLE5.3 SLE5.4 SLE5.5 SLE-m5.3 SLE-m5.4 SLE-m5.5 | sqlite3 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22166-1](https://lwn.net/Articles/1079344/) | SLE16.0 | sqlite3 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2459-1](https://lwn.net/Articles/1078653/) | SLE15 oS15.5 | strongswan | 2026-06-19 |
| SUSE | [SUSE-SU-2026:22168-1](https://lwn.net/Articles/1079348/) | SLE16.0 | strongswan | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2484-1](https://lwn.net/Articles/1079072/) | MP4.3 SLE15 | terraform-provider-local, terraform-provider-null | 2026-06-22 |
| SUSE | [SUSE-SU-2026:22234-1](https://lwn.net/Articles/1079349/) | SLE-m6.2 | tiff | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11060-1](https://lwn.net/Articles/1078920/) | TW | tinyproxy | 2026-06-19 |
| SUSE | [SUSE-SU-2026:22195-1](https://lwn.net/Articles/1079350/) | SLE16.0 | tomcat | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22197-1](https://lwn.net/Articles/1079351/) | SLE16.0 | tomcat10 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22196-1](https://lwn.net/Articles/1079352/) | SLE16.0 | tomcat11 | 2026-06-23 |
| SUSE | [openSUSE-SU-2026:11047-1](https://lwn.net/Articles/1078654/) | TW | traefik | 2026-06-18 |
| SUSE | [openSUSE-SU-2026:11045-1](https://lwn.net/Articles/1078453/) | TW | traefik2 | 2026-06-17 |
| SUSE | [openSUSE-SU-2026:11048-1](https://lwn.net/Articles/1078655/) | TW | trivy | 2026-06-18 |
| SUSE | [SUSE-SU-2026:22213-1](https://lwn.net/Articles/1079354/) | SLE-m6.2 | unbound | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22160-1](https://lwn.net/Articles/1079353/) | SLE16.0 | unbound | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2492-1](https://lwn.net/Articles/1079073/) | SLE12 | util-linux | 2026-06-22 |
| SUSE | [SUSE-SU-2026:2485-1](https://lwn.net/Articles/1079074/) | SLE15 | util-linux | 2026-06-22 |
| SUSE | [SUSE-SU-2026:22212-1](https://lwn.net/Articles/1079355/) | SLE16.0 | webkit2gtk3 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22203-1](https://lwn.net/Articles/1079356/) | SLE16.0 | webkit2gtk3 | 2026-06-23 |
| SUSE | [SUSE-SU-2026:2437-1](https://lwn.net/Articles/1078454/) | SLE15 oS15.6 | wireshark | 2026-06-17 |
| SUSE | [SUSE-SU-2026:2426-1](https://lwn.net/Articles/1078455/) | SLE15 | xwayland | 2026-06-17 |
| SUSE | [SUSE-SU-2026:22180-1](https://lwn.net/Articles/1079357/) | SLE16.0 | xwayland | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22221-1](https://lwn.net/Articles/1079359/) | SLE-m6.2 | zypper, libzypp, libsolv | 2026-06-23 |
| SUSE | [SUSE-SU-2026:22172-1](https://lwn.net/Articles/1079358/) | SLE16.0 | zypper, libzypp, libsolv | 2026-06-23 |
| Ubuntu | [USN-8448-1](https://lwn.net/Articles/1078456/) | 16.04 | dolibarr | 2026-06-17 |
| Ubuntu | [USN-8447-1](https://lwn.net/Articles/1078457/) | 16.04 18.04 20.04 22.04 24.04 26.04 | golang-go.crypto | 2026-06-17 |
| Ubuntu | [USN-8447-3](https://lwn.net/Articles/1079075/) | 16.04 18.04 20.04 22.04 24.04 25.10 26.04 | google-guest-agent | 2026-06-22 |
| Ubuntu | [USN-8444-1](https://lwn.net/Articles/1078458/) | 22.04 24.04 25.10 26.04 | graphite2 | 2026-06-17 |
| Ubuntu | [USN-8446-1](https://lwn.net/Articles/1078459/) | 26.04 | gst-plugins-bad1.0 | 2026-06-17 |
| Ubuntu | [USN-8459-1](https://lwn.net/Articles/1079076/) | 22.04 24.04 25.10 26.04 | haproxy | 2026-06-22 |
| Ubuntu | [USN-8442-1](https://lwn.net/Articles/1078460/) | 20.04 22.04 24.04 25.10 26.04 | kitty | 2026-06-17 |
| Ubuntu | [USN-8449-1](https://lwn.net/Articles/1078656/) | 16.04 18.04 20.04 22.04 24.04 26.04 | ldns | 2026-06-18 |
| Ubuntu | [USN-8193-2](https://lwn.net/Articles/1079360/) | 14.04 16.04 18.04 20.04 | libcap2 | 2026-06-23 |
| Ubuntu | [USN-8445-1](https://lwn.net/Articles/1078461/) | 22.04 24.04 25.10 26.04 | libconfig-inifiles-perl | 2026-06-17 |
| Ubuntu | [USN-8454-1](https://lwn.net/Articles/1078657/) | 18.04 20.04 22.04 24.04 25.10 26.04 | libheif | 2026-06-18 |
| Ubuntu | [USN-8453-1](https://lwn.net/Articles/1078658/) | 16.04 18.04 20.04 22.04 24.04 25.10 26.04 | libnet-cidr-lite-perl | 2026-06-18 |
| Ubuntu | [USN-8464-1](https://lwn.net/Articles/1079361/) | 22.04 24.04 25.10 26.04 | libnfs | 2026-06-23 |
| Ubuntu | [USN-8425-1](https://lwn.net/Articles/1078462/) | 26.04 | libnginx-mod-js | 2026-06-17 |
| Ubuntu | [USN-8463-1](https://lwn.net/Articles/1079362/) | 22.04 24.04 25.10 26.04 | libvncserver | 2026-06-23 |
| Ubuntu | [USN-8456-1](https://lwn.net/Articles/1079363/) | 22.04 24.04 | libxml2 | 2026-06-24 |
| Ubuntu | [USN-8460-1](https://lwn.net/Articles/1079077/) | 25.10 26.04 | libxml2 | 2026-06-22 |
| Ubuntu | [USN-8461-1](https://lwn.net/Articles/1079078/) | 26.04 | linux-azure | 2026-06-22 |
| Ubuntu | [USN-8388-2](https://lwn.net/Articles/1079079/) | 20.04 22.04 | linux-intel-iotg-5.15, linux-lowlatency, linux-lowlatency-hwe-5.15 | 2026-06-22 |
| Ubuntu | [USN-8462-1](https://lwn.net/Articles/1079080/) | 20.04 | linux-oracle-5.15 | 2026-06-22 |
| Ubuntu | [USN-8447-2](https://lwn.net/Articles/1078659/) | 16.04 18.04 | lxd | 2026-06-18 |
| Ubuntu | [USN-8457-1](https://lwn.net/Articles/1079081/) | 22.04 24.04 25.10 26.04 | mysql-8.0, mysql-8.4 | 2026-06-22 |
| Ubuntu | [USN-8457-2](https://lwn.net/Articles/1079364/) | 20.04 | mysql-8.0 | 2026-06-24 |
| Ubuntu | [USN-8455-1](https://lwn.net/Articles/1078921/) | 14.04 16.04 18.04 20.04 22.04 24.04 26.04 | netatalk | 2026-06-22 |
| Ubuntu | [USN-8458-1](https://lwn.net/Articles/1079082/) | 22.04 24.04 25.10 26.04 | nginx | 2026-06-22 |
| Ubuntu | [USN-8450-1](https://lwn.net/Articles/1078660/) | 26.04 | tomcat11 | 2026-06-18 |
| Ubuntu | [USN-8451-1](https://lwn.net/Articles/1078661/) | 14.04 16.04 18.04 20.04 22.04 24.04 25.10 26.04 | vim | 2026-06-18 |
| Ubuntu | [USN-8443-1](https://lwn.net/Articles/1078463/) | 16.04 18.04 20.04 22.04 24.04 | webpy | 2026-06-17 |

[Full Story](https://lwn.net/Articles/1079387/) ([comments: none](https://lwn.net/Articles/1079387/#Comments))

## Kernel patches of interest

[^lwn1078380-p22-security]: 보안 업데이트 표는 운영자가 취약점 패치 범위를 빠르게 대조하기 위한 색인입니다. 패키지명과 공지 번호의 정확성이 중요하므로 번역 과정에서도 행 데이터는 변경하지 않았습니다.

### 커널 릴리스

아래 항목은 이번 호에 수록된 안정 커널 릴리스와 커널 패치 게시 목록입니다. 작성자 이름, 링크 제목, 버전, 날짜는 추적을 위해 원문 형식을 대부분 유지했습니다.[^lwn1078380-p23-stable]

Greg Kroah-Hartman
[Linux 7.1.1](https://lwn.net/Articles/1078591/) 
6월 19

Greg Kroah-Hartman
[Linux 7.0.13](https://lwn.net/Articles/1078592/) 
6월 19

Greg Kroah-Hartman
[Linux 6.18.36](https://lwn.net/Articles/1078593/) 
6월 19

Greg Kroah-Hartman
[Linux 6.12.94](https://lwn.net/Articles/1078594/) 
6월 19

Greg Kroah-Hartman
[Linux 6.6.143](https://lwn.net/Articles/1078595/) 
6월 19

Greg Kroah-Hartman
[Linux 6.1.176](https://lwn.net/Articles/1078596/) 
6월 19

Greg Kroah-Hartman
[Linux 5.15.210](https://lwn.net/Articles/1078597/) 
6월 19

Greg Kroah-Hartman
[Linux 5.10.259](https://lwn.net/Articles/1078598/) 
6월 19

Luis Claudio R. Goncalves
[5.10.259-rt155](https://lwn.net/Articles/1079089/) 
6월 22

### 아키텍처별

Kiryl Shutsemau
[arm64: cross-CPU NMI via SDEI](https://lwn.net/Articles/1078482/) 
6월 17

Ruidong Tian
[arm64: add ARCH\_HAS\_COPY\_MC support](https://lwn.net/Articles/1078496/) 
6월 18

Jinjie Ruan
[arm64: Add HOTPLUG\_PARALLEL support for secondary CPUs](https://lwn.net/Articles/1078497/) 
6월 18

George Guo
[LoongArch: BPF: arena instruction gating, private stack and exceptions](https://lwn.net/Articles/1078487/) 
6월 18

Chenguang Zhao
[LoongArch bpf kptr xchg inline support](https://lwn.net/Articles/1078935/) 
6월 22

Yunhui Cui
[riscv: support effective hardware PTE A/D updates](https://lwn.net/Articles/1078491/) 
6월 18

Drew Fustini
[riscv: Add Ssqosid and initial CBQRI resctrl support](https://lwn.net/Articles/1078770/) 
6월 19

Varun R Mallya
[Add BPF Exceptions support for RISC-V](https://lwn.net/Articles/1078815/) 
6월 21

Charlie Jenkins via B4 Relay
[riscv: Generate riscv instruction functions](https://lwn.net/Articles/1078924/) 
6월 21

Atish Patra
[Add Counter delegation ISA extension support](https://lwn.net/Articles/1078932/) 
6월 22

wang.yechao255@zte.com.cn
[Implement Eager Page Splitting for RISC-V](https://lwn.net/Articles/1079374/) 
6월 24

Mete Durlu
[s390/idle: CPU idle driver](https://lwn.net/Articles/1078502/) 
6월 18

Alexander Gordeev
[s390/mm: Batch PTE updates in lazy MMU mode](https://lwn.net/Articles/1078529/) 
6월 18

Xu Yilun
[Enable DICE-based TDX Quoting Extension](https://lwn.net/Articles/1078493/) 
6월 18

Zhenzhong Duan
[Support memory hotplug/unplug for TDX CoCo guests](https://lwn.net/Articles/1079109/) 
6월 23

Pawan Gupta
[VMSCAPE optimization for BHI variant](https://lwn.net/Articles/1079151/) 
6월 23

### 빌드 시스템

Breno Leitao
[bootconfig: embed kernel.\* cmdline at build time](https://lwn.net/Articles/1079149/) 
6월 23

### 코어 커널

Shrikanth Hegde
[sched: Introduce cpu\_preferred\_mask and steal-driven vCPU backoff](https://lwn.net/Articles/1078478/) 
6월 17

Jing Wu
[Dynamic Housekeeping Management (DHM) via CPUSets](https://lwn.net/Articles/1078486/) 
6월 18

Masami Hiramatsu (Google)
[tracing/probes: Add more typecast features](https://lwn.net/Articles/1078775/) 
6월 21

Kumar Kartikeya Dwivedi
[Redesign Verification Errors](https://lwn.net/Articles/1078781/) 
6월 19

Waiman Long
[cgroup/cpuset: Support multiple source/destination cpusets for cpuset\_\*attach()](https://lwn.net/Articles/1078814/) 
6월 20

Leon Hwang
[bpf: Introduce global percpu data](https://lwn.net/Articles/1078950/) 
6월 22

Tarun Sahu
[liveupdate: kvm: guest\_memfd preservation](https://lwn.net/Articles/1078961/) 
6월 22

Amery Hung
[bpf: A common way to attach struct\_ops to a cgroup](https://lwn.net/Articles/1079155/) 
6월 23

Puranjay Mohan
[RCU: Enable callbacks to benefit from expedited grace periods](https://lwn.net/Articles/1079380/) 
6월 24

Hongfu Li
[cgroup/dmem: add per-region event counters](https://lwn.net/Articles/1079368/) 
6월 24

Breno Leitao
[workqueue: Shrink the lock time](https://lwn.net/Articles/1079379/) 
6월 24

Vincent Guittot
[sched/eevdf: Improve scheduling latency of short slice task](https://lwn.net/Articles/1079399/) 
6월 24

### 개발 도구

Abhishek Bapat
[alloc\_tag: introduce IOCTL-based filtering for MAP](https://lwn.net/Articles/1078533/) 
6월 18

### 장치 드라이버

Jun Yan
[Input: cap11xx - Add support for CAP1114](https://lwn.net/Articles/1078473/) 
6월 17

Mike Lothian
[drm/vino: DisplayLink DL3 dock driver (RFC, help wanted)](https://lwn.net/Articles/1078474/) 
6월 17

Kathiravan Thirumoorthy
[Add support for the REFGEN in the IPQ9650 SoC](https://lwn.net/Articles/1078477/) 
6월 17

Salih Erim
[iio: adc: add Versal SysMon driver](https://lwn.net/Articles/1078479/) 
6월 17

Jean-Michel Hautbois
[Coldfire m5441x: add RCM power-on reason driver](https://lwn.net/Articles/1078481/) 
6월 17

Frank.Li@oss.nxp.com
[media: add new API simple 1to1 subdev register and add imx parallel camera support](https://lwn.net/Articles/1078483/) 
6월 17

Satish Kharat
[enic: SR-IOV V2 admin channel and MBOX protocol](https://lwn.net/Articles/1078485/) 
6월 17

Santhosh Kumar K
[spi: cadence-quadspi: add PHY tuning support](https://lwn.net/Articles/1078492/) 
6월 18

Praveen Talari
[Enable SPI on SA8255p Qualcomm platforms](https://lwn.net/Articles/1078495/) 
6월 18

guoniu.zhou@oss.nxp.com
[media: nxp: Add CSI Pixel Formatter support](https://lwn.net/Articles/1078498/) 
6월 18

Wenmeng Liu
[media: i2c: Add OmniVision OG0VA1B camera sensor driver](https://lwn.net/Articles/1078501/) 
6월 18

Petar Stepanovic
[pwm: add Axiado AX3000 PWM support](https://lwn.net/Articles/1078503/) 
6월 18

Christian Marangi
[net: pcs: Introduce support for fwnode PCS](https://lwn.net/Articles/1078504/) 
6월 18

Rodrigo Alencar via B4 Relay
[AD9910 Direct Digital Synthesizer](https://lwn.net/Articles/1078506/) 
6월 18

Waqar Hameed
[Add driver for TI BQ25630 charger](https://lwn.net/Articles/1078507/) 
6월 18

Linus Walleij
[pmdomain: st: ux500: Implement ux500 power domains](https://lwn.net/Articles/1078510/) 
6월 18

Boshi Yu
[RDMA/erdma: Add DMA-BUF memory registration](https://lwn.net/Articles/1078512/) 
6월 18

Dongdong Hao
[scsi: Add LeapRAID driver support](https://lwn.net/Articles/1078513/) 
6월 18

Geetha sowjanya
[perf: marvell: LLC-TAD PMU MPAM filtering support](https://lwn.net/Articles/1078530/) 
6월 18

Nikhil Gautam
[iio: magnetometer: add support for Melexis MLX90393](https://lwn.net/Articles/1078531/) 
6월 18

Prabhakar
[Add PLL3 and LCDC\_CLKD support for RZ/T2H and RZ/N2H](https://lwn.net/Articles/1078534/) 
6월 18

alejandro.lucero-palau@amd.com
[Type2 device basic support](https://lwn.net/Articles/1078538/) 
6월 18

David Yang
[net: dsa: motorcomm: Add LED support](https://lwn.net/Articles/1078665/) 
6월 19

Matthew Leung
[phy: qcom: qmp-pcie: Add PCIe PHY support for Hawi](https://lwn.net/Articles/1078667/) 
6월 18

Marek Vasut
[PCI: rcar-gen4: irqchip/gic-v3: Handle GIC ITS](https://lwn.net/Articles/1078668/) 
6월 19

Yuanshen Cao
[dmaengine: sun6i-dma: Add support for Allwinner A733 DMA controller](https://lwn.net/Articles/1078671/) 
6월 19

Biju
[Add support for Renesas RZ/G3L LVDS encoder](https://lwn.net/Articles/1078675/) 
6월 19

Matthias Fend
[media: add Himax HM1246 image sensor](https://lwn.net/Articles/1078676/) 
6월 19

Himanshu Bhavani
[media: i2c: Add imx576 camera sensor driver](https://lwn.net/Articles/1078677/) 
6월 19

Pavitrakumar Managutte
[crypto: spacc - Add SPAcc Crypto Driver](https://lwn.net/Articles/1078690/) 
6월 19

Rishi Chhibber
[misc: vmw\_zerocopy: Add VMware zero-copy buffer sharing driver](https://lwn.net/Articles/1078769/) 
6월 19

Manaf Meethalavalappu Pallikunhi
[Add Qualcomm SPEL powercap driver](https://lwn.net/Articles/1078771/) 
6월 20

Maxwell Doose
[Add Sensirion STS30 temperature sensor driver](https://lwn.net/Articles/1078773/) 
6월 19

Otto Pflüger
[regulator: Add support for Unisoc SC2730 PMIC regulators](https://lwn.net/Articles/1078774/) 
6월 20

Koichiro Den
[dmaengine: dw-edma: Prepare for PCI EP DMA (part 1/3)](https://lwn.net/Articles/1078776/) 
6월 21

Koichiro Den
[PCI: endpoint: Expose endpoint DMA resources (part 2/3)](https://lwn.net/Articles/1078777/) 
6월 21

Koichiro Den
[PCI: endpoint: Add PCI DMA endpoint function (part 3/3)](https://lwn.net/Articles/1078778/) 
6월 21

Luca Leonardo Scorcia
[Add support for MT6392 PMIC](https://lwn.net/Articles/1078812/) 
6월 20

Maxwell Doose
[iio: temperature: Add support for the STS30 temperature sensor](https://lwn.net/Articles/1078813/) 
6월 20

joakim.zhang@cixtech.com
[Add Cix Sky1 AUDSS clock and reset support](https://lwn.net/Articles/1078923/) 
6월 22

Sumit Kumar
[bus: mhi: Add loopback driver](https://lwn.net/Articles/1078926/) 
6월 22

Qiang Yu
[clk: qcom: Add common clkref support and migrate Glymur and Mahua](https://lwn.net/Articles/1078927/) 
6월 21

Raviteja Laggyshetty
[interconnect: qcom: Add support for upcoming Maili SoC](https://lwn.net/Articles/1078928/) 
6월 22

Chinna Mopurigari Naveen Kumar Reddy
[USB: serial: ftdi\_sio: configurable read-URB defer, per-port low\_latency, latency\_timer reliability](https://lwn.net/Articles/1078929/) 
6월 22

Petar Stepanovic
[iio: adc: Add Axiado SARADC driver](https://lwn.net/Articles/1078931/) 
6월 22

Yu-Chun Lin
[gpio: realtek: Add support for Realtek DHC RTD1625](https://lwn.net/Articles/1078934/) 
6월 22

Mallesh Koujalagi
[Introduce cold reset recovery method](https://lwn.net/Articles/1078939/) 
6월 22

Dave Carey
[Lenovo Yoga Book 9 keyboard dock detection](https://lwn.net/Articles/1078940/) 
6월 21

Adrian Ng Ho Yin
[Add FPGA configuration and partial reconfiguration support for Agilex5](https://lwn.net/Articles/1078949/) 
6월 22

Amit Barzilai
[drm/ssd130x: Add support for the Solomon SSD1351 OLED controller](https://lwn.net/Articles/1078958/) 
6월 22

Biju
[Add Renesas RZ/G3L SD/eMMC support](https://lwn.net/Articles/1078959/) 
6월 22

Armin Wolf
[platform/x86: lg-laptop: Improve support for modern devices](https://lwn.net/Articles/1079084/) 
6월 22

Zhi Wang
[gpu: nova-core: boot GSP with vGPU enabled](https://lwn.net/Articles/1079085/) 
6월 22

Brian Daniels
[media: add virtio-media driver](https://lwn.net/Articles/1079086/) 
6월 22

Jakub Szczudlo
[iio: adc: Add support for TI ADS1110 to ti-ads1100 driver](https://lwn.net/Articles/1079087/) 
6월 23

Bjorn Andersson
[phy: qcom: edp: Update v8 programming sequence](https://lwn.net/Articles/1079088/) 
6월 22

Ryan Chen
[Add ASPEED AST2600 I2C controller driver](https://lwn.net/Articles/1079090/) 
6월 23

Tyrel Datwyler
[ibmvfc: Add NVMe-FC support](https://lwn.net/Articles/1079092/) 
6월 22

Esteban Urrutia via B4 Relay
[SM8450 IPA support](https://lwn.net/Articles/1079093/) 
6월 22

Jian Hu via B4 Relay
[clk: amlogic: Add A9 AO clock controller](https://lwn.net/Articles/1079094/) 
6월 23

Srirangan Madhavan
[PCI/CXL: Add CXL reset support for Type 2 devices](https://lwn.net/Articles/1079095/) 
6월 23

Chris Lu
[Bluetooth: btmtk: Add MT7928 support](https://lwn.net/Articles/1079096/) 
6월 23

Selvamani Rajagopal via B4 Relay
[Support onsemi's FD5121 multiphase digital controller](https://lwn.net/Articles/1079099/) 
6월 22

Jan Carlo Roleda
[Add support for LTC3208 multi-display driver](https://lwn.net/Articles/1079100/) 
6월 23

dongxuyang@eswincomputing.com
[Update designware pwm driver](https://lwn.net/Articles/1079101/) 
6월 23

Crescent Hsieh
[USB: serial: mxuport: add MUX50U support and updates](https://lwn.net/Articles/1079103/) 
6월 23

Roman Vivchar via B4 Relay
[AUXADC driver for the MediaTek mt6323 PMIC](https://lwn.net/Articles/1079104/) 
6월 23

Richard Cheng
[Support zero-sized HDM decoders](https://lwn.net/Articles/1079106/) 
6월 23

Aksh Garg
[PCI: Add DOE support for endpoint](https://lwn.net/Articles/1079107/) 
6월 23

Jingyi Wang
[Add binding and driver for Kaanapali SoCCP](https://lwn.net/Articles/1079108/) 
6월 23

Taniya Das
[clk: qcom: Add Nord multimedia clock controller support](https://lwn.net/Articles/1079110/) 
6월 23

Rodrigo Alencar via B4 Relay
[New features for the AD5686 IIO driver](https://lwn.net/Articles/1079111/) 
6월 23

Varshini Rajendran
[Add thermal management support for sama7d65](https://lwn.net/Articles/1079112/) 
6월 23

Shubham Patil
[Add AMD I3C master controller driver and bindings](https://lwn.net/Articles/1079113/) 
6월 23

Diogo Silva
[drm/exynos: DRM encoder improvements for Exynos devices](https://lwn.net/Articles/1079115/) 
6월 23

Boris Brezillon
[drm/panthor: Reduce dma\_fence signalling latency](https://lwn.net/Articles/1079116/) 
6월 23

Raag Jadav
[Introduce error threshold to drm\_ras](https://lwn.net/Articles/1079120/) 
6월 23

Maarten Lankhorst
[drm/i915/display: All patches to make PREEMPT\_RT work on i915 + xe.](https://lwn.net/Articles/1079121/) 
6월 22

Zhiping Zhang
[vfio/dma-buf: add TPH support for peer-to-peer access](https://lwn.net/Articles/1079122/) 
6월 22

Lukas Metz
[Add driver for DAC8163:](https://lwn.net/Articles/1079148/) 
6월 23

Sriman Achanta
[HID: steelseries: Refactor Arctis driver and add Arctis Nova 7 Gen2 support](https://lwn.net/Articles/1079150/) 
6월 23

Md Shofiqul Islam
[iio: health: add MAX86150 ECG and PPG biosensor driver](https://lwn.net/Articles/1079152/) 
6월 23

Christopher Höner
[ALSA: hda/realtek: Enable internal speakers on Razer Blade 16 (2025)](https://lwn.net/Articles/1079154/) 
6월 23

Kate Hsuan
[Add Sony IMX471 camera sensor driver](https://lwn.net/Articles/1079369/) 
6월 24

Karan Tilak Kumar
[Introduce functionality for NVMe initiator](https://lwn.net/Articles/1079370/) 
6월 23

Nas Chung
[Add support for Wave6 video codec driver](https://lwn.net/Articles/1079373/) 
6월 24

Arpit Saini
[drm/panel: add support for Ilitek ILI7807S DSI panels](https://lwn.net/Articles/1079375/) 
6월 24

Jack Wu via B4 Relay
[net: wwan: t9xx: Add MediaTek T9XX WWAN driver](https://lwn.net/Articles/1079376/) 
6월 24

Yu-Chun Lin
[clk / reset: realtek: Add RTD1625 clock and reset support](https://lwn.net/Articles/1079378/) 
6월 24

Ping-Ke Shih
[wifi: rtw89: coex: update BT coexistence to support dual BT for RTL8922D](https://lwn.net/Articles/1079382/) 
6월 24

Jagadeesh Kona
[Add camera clock controller support on Glymur platform](https://lwn.net/Articles/1079397/) 
6월 24

Gregory Price
[dax/kmem: atomic whole-device hotplug via sysfs](https://lwn.net/Articles/1079398/) 
6월 24

### Device-driver infrastructure

Philipp Stanner
[rust / dma\_buf: Add abstractions for dma\_fence](https://lwn.net/Articles/1078505/) 
6월 18

Mike Lothian
[rust: usb: synchronous bulk/control transfers + helpers](https://lwn.net/Articles/1078470/) 
6월 17

Mike Lothian
[rust: drm: minimal KMS bindings, EDID read, rotation, HDCP defs](https://lwn.net/Articles/1078472/) 
6월 17

Rong Zhang
[leds: Add support for hardware-initiated hardware control trigger transition](https://lwn.net/Articles/1078475/) 
6월 18

Detlev Casanova
[media: Add fdinfo support for v4l2 drivers](https://lwn.net/Articles/1078480/) 
6월 17

Paul Elder
[Add Shared Media Graph API](https://lwn.net/Articles/1078672/) 
6월 19

Danilo Krummrich
[rust: drm: Higher-Ranked Lifetime private data](https://lwn.net/Articles/1078772/) 
6월 20

alistair23@gmail.com
[lib: Rust implementation of SPDM](https://lwn.net/Articles/1079098/) 
6월 23

Hans de Goede
[RFC: Devicetree-ACPI hybrid mode](https://lwn.net/Articles/1079156/) 
6월 23

Akhil R
[Support ACPI and SETAASA device discovery](https://lwn.net/Articles/1079377/) 
6월 24

Matthew Brost
[drm/ttm, drm/xe: Page defragmentation for sub-optimally backed BOs](https://lwn.net/Articles/1079383/) 
6월 23

### Filesystems and block layer

Alex Markuze
[ceph: add binary logging (BLOG) for CephFS](https://lwn.net/Articles/1078469/) 
6월 17

Baokun Li
[ext4: allow more DIO writes under shared i\_rwsem](https://lwn.net/Articles/1078508/) 
6월 18

Alberto Ruiz via B4 Relay
[RFC: erofs: memory-backed mount for non-page-aligned ranges](https://lwn.net/Articles/1078532/) 
6월 18

hare@kernel.org
[namespace-aware configfs](https://lwn.net/Articles/1078674/) 
6월 19

Johannes Thumshirn
[btrfs: RAID5 with RAID stripe-tree (zoned + non-zoned)](https://lwn.net/Articles/1078678/) 
6월 19

Artem Blagodarenko
[Data in direntry (dirdata) feature](https://lwn.net/Articles/1078780/) 
6월 19

Jimmy Zuber
[fuse: allow FUSE\_SYNCFS for privileged userspace servers](https://lwn.net/Articles/1078768/) 
6월 19

Nanzhe Zhao
[[RFC PATCH v2 00/10] f2fs: support & optimize large folios for writable files](https://lwn.net/Articles/1078960/) 
6월 23

Keith Busch
[direct-io: validate user space vectors during extraction](https://lwn.net/Articles/1078962/) 
6월 22

Abd-Alrhman Masalkhi
[md/raid10: fixes, atomic write handling, and error-path cleanup](https://lwn.net/Articles/1079102/) 
6월 23

Yun Zhou
[ext4: deferred iput framework for EA inodes](https://lwn.net/Articles/1079105/) 
6월 23

Yu Kuai
[md/md-llbitmap: support reshape for RAID10 and RAID5](https://lwn.net/Articles/1079371/) 
6월 24

Yu Kuai
[md/linear: add fault-tolerant mode for unraid-like setups](https://lwn.net/Articles/1079372/) 
6월 24

Eric Biggers
[fscrypt: Standardize on blk-crypto](https://lwn.net/Articles/1079381/) 
6월 23

Hiroshi Nishida
[md/raid5: scalability and rebuild-path improvements](https://lwn.net/Articles/1079400/) 
6월 24

### 메모리 관리

Zhen Ni
[mm/page\_owner: add per-fd filter infrastructure for print\_mode and NUMA filtering](https://lwn.net/Articles/1078488/) 
6월 18

Hao Jia
[mm/zswap: Implement per-cgroup proactive writeback](https://lwn.net/Articles/1078489/) 
6월 18

Wen Jiang
[mm/vmalloc: Speed up ioremap, vmalloc and vmap with contiguous memory](https://lwn.net/Articles/1078494/) 
6월 18

Jane Chu
[hugetlb: Use PAGE granularity index in exported i/f and adopt the common read\_iter](https://lwn.net/Articles/1078476/) 
6월 17

Wang Lian
[mm/damon: Add mTHP-aware collapse/split with ARM SPE feedback](https://lwn.net/Articles/1078499/) 
6월 18

Ackerley Tng via B4 Relay
[guest\_memfd: In-place conversion support](https://lwn.net/Articles/1078670/) 
6월 18

gutierrez.asier@huawei-partners.com
[mm/damon: Introduce a huge page collapsing mechanism using auto tuning](https://lwn.net/Articles/1078691/) 
6월 19

Youngjun Park
[mm/swap, memcg: Introduce swap tiers for cgroup based swap control](https://lwn.net/Articles/1078779/) 
6월 21

Joshua Hahn
[mm/memcontrol, page\_counter: move stock from mem\_cgroup to page\_counter](https://lwn.net/Articles/1079153/) 
6월 23

### 네트워킹

Avinash Duduskar
[bpf: bidirectional VLAN support for bpf\_fib\_lookup()](https://lwn.net/Articles/1078484/) 
6월 18

Sechang Lim
[bpf, sockmap: reject a packet-modifying SK\_SKB stream parser](https://lwn.net/Articles/1078500/) 
6월 18

Mahe Tardy
[bpf: add icmp\_send kfunc](https://lwn.net/Articles/1078936/) 
6월 22

Xiaoliang Yang
[tc: introduce FRER action (IEEE 802.1CB)](https://lwn.net/Articles/1078933/) 
6월 22

Geliang Tang
[MPTCP KTLS support](https://lwn.net/Articles/1078937/) 
6월 22

### 보안 관련

Mike Lothian
[rust: crypto: library AES-128 / SHA-256 / HMAC + RSA](https://lwn.net/Articles/1078471/) 
6월 17

York Jasper Niebuhr
[Bootpatch-SLR: Randomizing Linux Kernel Structure Layouts at Boot](https://lwn.net/Articles/1078782/) 
6월 20

Justin Suess
[Implement LANDLOCK\_ADD\_RULE\_NO\_INHERIT](https://lwn.net/Articles/1078938/) 
6월 20

### Virtualization and containers

Fuad Tabba
[KVM: arm64: Rework pKVM vCPU state synchronisation](https://lwn.net/Articles/1078673/) 
6월 19

Zide Chen
[KVM: x86/pmu: Add hardware Topdown metrics support](https://lwn.net/Articles/1079097/) 
6월 22

Sebastian Ene
[KVM: arm64: Forward FFA\_NOTIFICATION\* calls to TrustZone](https://lwn.net/Articles/1079114/) 
6월 23

### 기타

Jakub Kicinski
[netdev development stats for 7.2](https://lwn.net/Articles/1078509/) 
6월 17

Stanislav Fomichev
[bpf development stats for 7.2](https://lwn.net/Articles/1078537/) 
6월 18

Clark Williams
[stalld v1.28.1](https://lwn.net/Articles/1078511/) 
6월 17

Kaitao Cheng
[Prepare mutable list iterators to cache cursor state](https://lwn.net/Articles/1078925/) 
6월 22

Gyutae Bae
[bpf: compare-and-delete (BPF\_F\_COMPARE) for hash maps](https://lwn.net/Articles/1078930/) 
6월 22

Ian Rogers
[perf tests: Robustness and performance improvements](https://lwn.net/Articles/1079091/) 
6월 22

Shuai Xue
[perf annotate: Add ARM64 data type profiling support](https://lwn.net/Articles/1079117/) 
6월 23

Alice Ryhl
[Rate limited printing for Rust](https://lwn.net/Articles/1079147/) 
6월 23

**Page editor**: Joe Brockmeier

[^lwn1078380-p23-stable]: LWN의 안정 커널 및 패치 목록은 각 하위 시스템별 검토 흐름을 보여 주는 운영 색인에 가깝습니다. 제목을 과도하게 의역하면 검색성이 떨어질 수 있어, 기술 식별자와 패치 제목은 원문 중심으로 보존했습니다.
