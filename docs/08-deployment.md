# Deployment Architecture

## Infrastructure

```
Internet
  |
Cloudflare (WAF + DDoS + SSL + CDN)
  |
nginx (TLS Termination + Static Files + Reverse Proxy)
  |
+---------+---------+---------+
|         |         |         |
Next.js   Backend   WASM
(SSR)     (Rust)    Runtime
```

## Deployment Strategy

- **Rolling updates**: Zero-downtime deployments
- **Blue-Green**: Staging before production cutover
- **Canary**: Gradual traffic shifting

## Database

- **PostgreSQL**: Streaming replication with failover
- **Redis**: Sentinel mode + AOF persistence
- **R2**: Multi-region replication, automatic backup

## Monitoring

- Application metrics via structured logging
- Infrastructure monitoring (CPU, memory, disk, network)
- Alerting on error rates and latency thresholds

## CI/CD Pipeline

1. Push to branch triggers CI (test, lint, build)
2. Merge to main triggers staging deployment
3. Release tag triggers production deployment
4. Rollback available via previous deployment artifacts
