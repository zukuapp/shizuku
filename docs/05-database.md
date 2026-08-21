# Database Design

## Primary Databases

### PostgreSQL — Relational Data
- User accounts and profiles
- Content metadata
- Social graph (follows, likes, comments)
- Monetization records

### Redis — Cache & Session
- Session storage (with TTL)
- Content cache
- Rate limiting
- Real-time features (WebSocket pub/sub)

### Cloudflare R2 — Object Storage
- Media files (MP4, images)
- WASM binary packages
- Static assets

## Key Principles

- All queries use prepared parameterization (SQL injection prevention)
- Sensitive data encrypted at rest
- Regular backup with point-in-time recovery
- Connection pooling via application layer
- Database migrations are versioned and reversible

---

*Detailed schema documentation will be added as the platform develops.*
