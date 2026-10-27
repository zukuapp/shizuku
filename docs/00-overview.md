# ZUKU 공개 플랫폼 개요

ZUKU는 Trecillo가 만드는 창작·미디어 플랫폼입니다. 공개 웹사이트의
[ZUKU 제품 지도](https://zukuapp.github.io/platform/)는 Thread, Hype, Swipe,
Jump 등의 화면을 소개합니다.

## 공개 개발 자료

| 영역             | 저장소                                                                                                                                                                    | 내용                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| HTML5 게임       | [`zwf`](https://github.com/zukuapp/zwf)                                                                                                                                   | ZIP → ZWF2 컴파일러, 검사기, 플레이어 경계 명세 |
| Jump 패키지      | [`zuku-engine-next2d`](https://github.com/zukuapp/zuku-engine-next2d)                                                                                                     | 매니페스트 스키마와 공개 런타임 어댑터          |
| API 모델         | [`zuku-api`](https://github.com/zukuapp/zuku-api)                                                                                                                         | OpenAPI 3.1 문서와 SDK 소스                     |
| ZUKBOX 저작·재생 | [`zukbox`](https://github.com/zukuapp/zukbox), [`zukbox-runtime`](https://github.com/zukuapp/zukbox-runtime), [`zukbox-player`](https://github.com/zukuapp/zukbox-player) | 에디터, ZWF1 바이너리 파서, 렌더러              |

ZWF2와 ZUKBOX ZWF1은 확장자 `.zwf`를 공유하지만 파일 구조가 다릅니다. 각
경로는 [공개 아키텍처](01-architecture.md)에 있습니다.

## 시작하기

[`zwf` 입문](https://github.com/zukuapp/.github/blob/main/docs/getting-started.md)은
로컬에서 HTML5 게임을 패키징하는 절차입니다.

[`zukujs-cli`](https://github.com/zukuapp/zukujs-cli)는 두 명령 별칭과 단일
Agent Core를 제공하며 생성·검증·패키징·업로드 소스를 포함합니다.

형식과 인터페이스의 전체 설명은
[조직 개발 문서](https://github.com/zukuapp/.github/blob/main/docs/README.md)에
있습니다.
