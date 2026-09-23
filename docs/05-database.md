# 공개 데이터 모델과 저장 계층

ZUKU의 실제 데이터베이스 스키마, 백업 구성, 복제 방식은 이 공개 저장소에
포함되지 않습니다. 이전 문서의 PostgreSQL·Redis·R2 배치와 복구 수준은 여기에서
확인할 수 없는 운영 정보였으므로 현재 구성으로 제시하지 않습니다.

## 공개된 모델

[`zuku-api` OpenAPI 명세](https://github.com/zukuapp/zuku-api/blob/main/spec/zuku-api-v1.yaml)의
`components/schemas`에서 API가 주고받는 모델을 확인할 수 있습니다.

| 모델 묶음       | 명세의 예                                                 |
| --------------- | --------------------------------------------------------- |
| 사용자와 인증   | `User`, `RegisterRequest`, `TokenResponse`                |
| 콘텐츠와 피드   | `Content`, `Comment`, `FeedResponse`                      |
| Jump            | `Game`, `GameReview`, `LeaderboardEntry`                  |
| 창작자와 신고   | `Creator`, `CreatorAnalytics`, `Report`                   |
| 목록 메타데이터 | `PaginationMeta`의 `total`, `limit`, `offset`, `has_more` |

이는 **API 모델**입니다. 내부 테이블, 외래 키, 보관 기간, 캐시 키, 물리적 저장
위치와 1:1로 대응한다고 가정하지 마세요. 데이터 변경을 제안할 때는 공개 응답의
호환성부터 명세에서 확인하세요.

이 문서는 데이터베이스 접근 권한을 제공하지 않습니다. 공개 API의 이용 가능 여부
역시 [API 안내](06-api.md)의 범위를 따릅니다.
