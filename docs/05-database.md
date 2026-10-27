# 공개 데이터 모델과 저장 계층

ZUKU의 실제 데이터베이스 스키마, 백업 구성, 복제 방식은 이 공개 저장소에
포함되지 않습니다.

## 공개된 모델

[`zuku-api` OpenAPI 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)의
`components/schemas`는 API가 주고받는 모델을 정의합니다.

| 모델 묶음       | 명세의 예                                                 |
| --------------- | --------------------------------------------------------- |
| 사용자와 인증   | `User`, `RegisterRequest`, `TokenResponse`                |
| 콘텐츠와 피드   | `Content`, `Comment`, `FeedResponse`                      |
| Jump            | `Game`, `GameReview`, `LeaderboardEntry`                  |
| 창작자와 신고   | `Creator`, `CreatorAnalytics`, `Report`                   |
| 목록 메타데이터 | `PaginationMeta`의 `total`, `limit`, `offset`, `has_more` |

이 모델은 API 모델입니다. 내부 테이블, 외래 키, 보관 기간, 캐시 키, 물리적
저장 위치와의 대응 관계는 이 저장소에서 정의하지 않습니다. 데이터 변경을 제안할 때는 명세에서
공개 응답의 호환성을 먼저 확인합니다.

이 문서는 데이터베이스 접근 권한을 제공하지 않습니다. 공개 API의 이용 범위는
[API 안내](06-api.md)를 따릅니다.
