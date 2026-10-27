# ZUKU 공개 플랫폼 개요

ZUKU는 Trecillo가 만드는 창작·미디어 플랫폼입니다. 공개 웹사이트의
[ZUKU 제품 지도](https://zukuapp.github.io/platform/)는 Thread, Hype, Swipe,
Jump 등의 화면을 소개합니다.

## 공개 개발 자료

| 영역             | 공개 자료                                                                                                                                                                 | 범위                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| HTML5 게임       | [`zwf`](https://github.com/zukuapp/zwf)                                                                                                                                   | ZIP → ZWF2 컴파일러, 검사기, 플레이어 경계 명세 |
| Jump 패키지      | [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d)                                                                                                     | 매니페스트 스키마와 공개 런타임 어댑터          |
| API 모델         | [`zuku-api`](https://github.com/zukuapp/zuku-api)                                                                                                                         | OpenAPI 3.1 문서와 SDK 소스                     |
| ZUKBOX 저작·재생 | [`zukbox`](https://github.com/zukuapp/zukbox), [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime), [`zukbox-player`](https://github.com/zukuapp/zukbox-player) | 에디터, ZWF1 바이너리 파서, 렌더러              |

ZWF2와 ZUKBOX ZWF1은 확장자 `.zwf`를 공유하지만 파일 구조가 다릅니다. 각
경로는 [공개 아키텍처](01-architecture.md)에 있습니다.

## 사용 경로와 명세의 차이

[`zwf` 입문](https://github.com/zukuapp/.github/blob/main/docs/getting-started.md)은
로컬에서 재현하는 패키징 절차입니다. OpenAPI 문서의 서버 주소와 데이터 모델은
외부 계정·토큰 발급이나 운영 API 접근을 보장하지 않습니다.

[`zukujs-cli`](https://github.com/zukuapp/zukujs-cli)는 두 명령 별칭과 단일
Agent Core를 제공합니다. `zukujs-cli`는 생성·검증·패키징·업로드 소스를
포함합니다.
실제 서비스 호출·공개 게시·GUI 지원 상태는 해당 저장소의 검증 결과와 릴리스가
기준입니다.

## 문서의 기준

공개 형식과 인터페이스는
[조직 개발 문서](https://github.com/zukuapp/.github/blob/main/docs/README.md)에
있습니다. 필드별 세부 사항은 연결된 저장소의 명세를 따릅니다. 이 저장소의
[문서 목차](README.md)는 개요와 경계 설명을 모읍니다. 사용·수정 조건은
[이 저장소의 라이선스](../LICENSE.md)에 있습니다.
