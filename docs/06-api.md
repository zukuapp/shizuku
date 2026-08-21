# API Design

## API Principles

- **REST-first**: Resource-oriented design with predictable URLs
- **Versioning**: URL-based (`/v1/`)
- **Authentication**: OAuth 2.0 + Session tokens
- **Pagination**: Cursor-based for list endpoints
- **Content-Type**: `application/json`

## Base URL

```
https://api.zuzunza.com/v1/
```

## Authentication

All API requests require authentication via:
1. `Authorization: Bearer <token>` header (OAuth 2.0)
2. Session cookie (for browser-based clients)

## Common Response Format

```json
{
  "status": "ok",
  "data": {},
  "meta": {
    "cursor": "next_page_token",
    "has_more": true
  }
}
```

## Error Format

```json
{
  "status": "error",
  "code": "VALIDATION_ERROR",
  "message": "Human-readable error message",
  "details": []
}
```

## Core Endpoints

| Method | Path              | Description         |
|--------|-------------------|---------------------|
| GET    | /v1/content       | List content        |
| POST   | /v1/content       | Create content      |
| GET    | /v1/content/{id}  | Get content detail  |
| GET    | /v1/users/me      | Current user        |
| GET    | /v1/users/{id}    | User profile        |

## Rate Limiting

- 100 requests per minute per authenticated user
- 20 requests per minute per IP (unauthenticated)
- Rate limit headers included in responses

---

*Full OpenAPI 3.1 specification: [zuku-api repository](https://github.com/zukuapp/zuku-api)*
