# 공개 API 계약 읽기

[`zuku-api/spec/zuku-api-v1.yaml`](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)이
OpenAPI 3.1 형식의 경로·모델 기준입니다.

## 경로와 응답

명세의 `servers`에는 `/v1` 주소가 있습니다. `paths`는 `/auth/me`, `/feeds`,
`/contents`, `/jump/games` 등의 상대 경로를 정의합니다.

| 페이지네이션 방식   | 요청              | 응답                                                      |
| ------------------- | ----------------- | --------------------------------------------------------- |
| 오프셋(대부분)      | `limit`, `offset` | `PaginationMeta`의 `total`, `limit`, `offset`, `has_more` |
| 커서(`/swipe/feed`) | `cursor`          | `next_cursor`                                             |

## 인증과 SDK

명세는 Bearer 토큰과 `X-API-Key` 보안 방식을 선언합니다. 요청별 인증 방식은
해당 작업의 `security` 정의를 따릅니다.

[`zuku-api/packages/sdk/`](https://github.com/zukuapp/zuku-api/tree/main/packages/sdk)는
TypeScript SDK 소스입니다.

보안 문제는
[조직 보안 정책](https://github.com/zukuapp/.github/blob/main/SECURITY.md)에 따라
제보합니다.
