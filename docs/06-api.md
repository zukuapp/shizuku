# 공개 API 계약 읽기

[`zuku-api/spec/zuku-api-v1.yaml`](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)이
OpenAPI 3.1 형식의 경로·모델 기준입니다. 이 문서는 명세를 찾는 방법을 설명하며,
외부 API 접근 가능성을 약속하지 않습니다.

## 경로와 응답

명세의 `servers`에는 `/v1` 주소가 적혀 있습니다. `paths`에는 `/auth/me`,
`/feeds`, `/contents`, `/jump/games` 등의 상대 경로가 정의돼 있습니다. 이전
문서의 `/v1/content`와 `/v1/users` 예시는 이 명세와 맞지 않으므로 사용하지
마세요.

대부분의 목록 작업은 `limit`과 `offset`을 사용하며, `PaginationMeta`는 `total`,
`limit`, `offset`, `has_more`를 정의합니다. `/swipe/feed`는 `cursor` 요청과
`next_cursor` 응답을 쓰는 예외입니다. 페이지 이동 방식과 응답 형태는 작업별
정의를 확인하세요.

## 인증과 이용 상태

명세에는 Bearer 토큰과 `X-API-Key` 보안 방식이 선언돼 있습니다. 어떤 요청에 어떤
권한이 필요한지는 해당 작업의 `security` 정의와 서비스의 실제 접근 정책을 함께
확인해야 합니다. 명세의 서버 주소나 SDK 소스만으로 개발자 계정, 토큰 발급, 운영
API 사용 권한을 추정하지 마세요.

[`zuku-api/packages/sdk/`](https://github.com/zukuapp/zuku-api/tree/main/packages/sdk)는
TypeScript SDK 소스입니다. npm에 `@zuku/sdk`가 게시돼 있다는 뜻은 아닙니다.
로컬에서 형식만 검토할 때는 OpenAPI 문서와 소스를 우선 읽으세요.

보안 문제는
[조직 보안 정책](https://github.com/zukuapp/.github/blob/main/SECURITY.md)을
이용하세요.
