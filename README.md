<!-- markdownlint-disable MD033 MD041 -->
<a href="https://zukuapp.github.io/docs/">
  <img
    src="https://raw.githubusercontent.com/zukuapp/.github/main/profile/assets/developer-hero.png"
    alt="Trecillo 로고와 ZUKU 개발자 허브 안내"
    width="760"
  >
</a>
<!-- markdownlint-enable MD033 MD041 -->

# ZUKU 공개 개발 개요

**ZUKU(즈쿠)**는 Trecillo(트레실로)가 만드는 창작·미디어 플랫폼입니다. 이
저장소는 공개 개발 문서의 길잡이입니다. 실제 파일 형식과 API 필드는 각 저장소의
명세에서 확인하세요.

| 찾는 내용            | 시작할 곳                                                                                                                                              |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 개발 문서 전체       | [ZUKU 개발자 문서](https://github.com/zukuapp/.github/blob/main/docs/README.md)                                                                        |
| HTML5 게임 패키징    | [`zwf` 5분 입문](https://github.com/zukuapp/.github/blob/main/docs/getting-started.md) · [ZWF2 명세](https://github.com/zukuapp/zwf/blob/main/SPEC.md) |
| Jump 게임 메타데이터 | [`zuku-engine-next2d` 매니페스트 스키마](https://github.com/zukuapp/zuku-engine-next2d/blob/main/schemas/jump-manifest.schema.json)                    |
| 공개 API 모델        | [`zuku-api` OpenAPI 3.1 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)                                                     |
| ZUKBOX 바이너리      | [`zukbox-runtime` 형식 명세 초안](https://github.com/zukuapp/zukbox-runtime/blob/main/docs/zwf-format-v0.md)                                           |

## 이 저장소의 문서

| 문서                                            | 내용                                     |
| ----------------------------------------------- | ---------------------------------------- |
| [문서 목차](docs/README.md)                     | 이 저장소 문서의 범위와 읽는 순서        |
| [플랫폼 개요](docs/00-overview.md)              | 공개 제품과 개발 경로                    |
| [공개 아키텍처](docs/01-architecture.md)        | ZWF2, ZUKBOX ZWF1, API 계약의 경계       |
| [공개 작업 방식](docs/02-project-management.md) | 변경 제안과 명세 갱신                    |
| [데이터 모델](docs/05-database.md)              | 공개 API 모델과 비공개 저장 계층의 구분  |
| [API 안내](docs/06-api.md)                      | OpenAPI 명세를 읽는 방법                 |
| [브랜드 안내](docs/07-frontend-design.md)       | 현행 Trecillo 로고와 ZUKU 색상           |
| [배포·운영 문서의 범위](docs/08-deployment.md)  | 공개 저장소에서 확인할 수 있는 검증 경로 |

## 형식과 도구의 상태

`zwf`는 HTML5 ZIP을 **ZWF2**로 컴파일하고 검사하는 공개 도구입니다. ZUKBOX의
**ZWF1**은 같은 `.zwf` 확장자를 쓰지만 별도 바이너리 형식입니다. 두 형식을
교차해서 읽을 수 있다고 가정하지 마세요.

`zuku-cli`의 `create`, `validate`, `package`, `upload` 명령은 현재 구현에서 안내
메시지만 출력하는 초기 형태입니다. 패키지 제작을 시작할 때는 위 `zwf` 입문을
사용하세요. 공개 API 명세는 경로와 모델의 계약이며 서비스 계정, 운영 상태, API
접근 권한을 보증하지 않습니다.

## 이름과 기여

사용자에게 표시하는 이름은 **ZUKU(즈쿠)**, 회사명은
**Trecillo(트레실로)**입니다. `Shizuku`는 이 저장소에 남아 있는 이전
프로젝트명입니다. 현행 로고와 표기법은
[브랜드 문서](docs/07-frontend-design.md)를 따릅니다.

문서 수정은 [기여 안내](CONTRIBUTING.md)를 참고하세요. 취약점은 공개 Issue 대신
[보안 정책](https://github.com/zukuapp/.github/blob/main/SECURITY.md)에 따라
비공개로 제보해 주세요.
