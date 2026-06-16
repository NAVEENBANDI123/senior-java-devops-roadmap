# Part 5 — Project Roadmap (3 Portfolio Projects)

> Three progressively harder projects that prove your skills to interviewers. Each includes architecture, tech stack, features, DevOps, AWS deployment, and monitoring. Build these *if* you want variety; otherwise the single [Mega Project](06-mega-project.md) covers everything.

[← Platforms](04-platforms.md) · [Back to README](../README.md) · [Mega Project →](06-mega-project.md)

---

## 🟡 Project 1 — Intermediate: "TaskFlow" (Task Management API)

**Goal:** Prove solid backend fundamentals. Buildable in ~3–4 weeks.

### Architecture (description)
```
[Client / Postman] → [Nginx reverse proxy] → [Spring Boot Monolith]
                                                   │
                                    ┌──────────────┼──────────────┐
                                 [PostgreSQL]   [Redis cache]  [Flyway migrations]
```
A single deployable Spring Boot app, fronted by Nginx, backed by Postgres with Redis caching. Clean layered architecture (controller → service → repository).

### Tech Stack
Java 21, Spring Boot, Spring Data JPA, Spring Security (JWT), PostgreSQL, Redis, Flyway, MapStruct, springdoc-openapi, JUnit 5, Mockito, Testcontainers.

### Features
- User registration/login with JWT + refresh tokens
- Projects, tasks, labels; assign tasks to users
- Pagination, filtering, sorting on task lists
- Role-based access (USER/ADMIN)
- Caching of hot reads; optimistic locking on updates
- Global exception handling (RFC 7807 Problem Details)
- OpenAPI docs

### DevOps Setup
- Dockerfile (multi-stage), Docker Compose (app + Postgres + Redis)
- GitHub Actions: test → SonarCloud → build image → push to registry
- Flyway migrations in pipeline

### AWS Deployment
- Single EC2 (or ECS Fargate) + RDS Postgres + ElastiCache Redis
- ALB in front; Route53 domain; ACM TLS cert
- Secrets in AWS Secrets Manager

### Monitoring Setup
- Spring Actuator + Micrometer → Prometheus → Grafana dashboard
- Structured JSON logs → CloudWatch Logs
- Basic alarm on 5xx rate & latency

> ✅ **Proves:** Spring depth, security, testing, caching, basic DevOps + cloud.

---

## 🔴 Project 2 — Advanced: "StreamHub" (Event-Driven Content Platform)

**Goal:** Prove distributed systems & async messaging. ~6–8 weeks.

### Architecture (description)
```
                         [API Gateway (Spring Cloud Gateway)]
                                       │
        ┌──────────────┬───────────────┼───────────────┬──────────────┐
   [User Svc]     [Content Svc]    [Feed Svc]     [Notification Svc]  [Media Svc]
        │               │               │                │               │
   [Postgres]      [Postgres]    [Redis + Postgres]  [Postgres]      [S3]
        └───────────────┴──────── KAFKA event bus ─────┴───────────────┘
                         [Config Server] [Eureka] [Resilience4j]
```
Event-driven microservices communicating via Kafka. Feed service builds timelines from content events (fan-out on write).

### Tech Stack
Spring Cloud (Gateway, Config, Eureka), Kafka, Resilience4j, PostgreSQL per service, Redis, S3 (media), OpenTelemetry, Keycloak (OAuth2/OIDC).

### Features
- OAuth2/OIDC auth via Keycloak
- Publish content → Kafka event → feed fan-out + notifications
- Resilient inter-service calls (circuit breaker, retry, fallback)
- Distributed tracing across all services
- Media upload to S3 with presigned URLs

### DevOps Setup
- One Dockerfile per service; Docker Compose for full local stack (incl. Kafka, Keycloak)
- GitHub Actions monorepo pipeline with path filters + matrix builds
- Helm charts per service

### AWS Deployment
- EKS cluster; services as Deployments behind Ingress
- MSK (managed Kafka) or self-managed; RDS per service; ElastiCache
- HPA on CPU/custom metrics

### Monitoring Setup
- Prometheus + Grafana (per-service dashboards, RED metrics)
- Loki/ELK for centralized logs with correlation IDs
- Jaeger/Tempo for distributed traces via OpenTelemetry
- SLOs + alerting on error budget burn

> ✅ **Proves:** Microservices, Kafka, resilience, observability, Kubernetes.

---

## 🚀 Project 3 — Enterprise: "PayFlow" (Distributed Payments/Banking Platform)

**Goal:** Prove senior-level rigor: consistency, correctness, security, scale. ~8–12 weeks.

### Architecture (description)
```
        [CDN] → [WAF] → [API Gateway] → [Auth/OIDC]
                                │
   ┌────────────┬──────────────┼───────────────┬─────────────┐
[Account Svc] [Payment Svc] [Ledger Svc]  [Fraud Svc]   [Notification Svc]
     │             │             │              │              │
[Postgres]   [Postgres]    [Postgres]      [ML/rules]    [Postgres]
     └──── Transactional Outbox → Kafka → SAGA orchestrator ───┘
                  [Read models / CQRS] ← projections
```
SAGA-orchestrated distributed transactions, transactional outbox for reliable events, CQRS read models, double-entry ledger for correctness.

### Tech Stack
Everything from StreamHub + SAGA orchestration, Outbox + Debezium (CDC), CQRS, idempotency keys, Vault/Secrets Manager, rate limiting, audit logging.

### Features
- Money transfer via SAGA (account → payment → ledger → notification) with compensations
- Idempotent payment API (safe retries)
- Double-entry ledger; eventual consistency with read models (CQRS)
- Fraud checks; rate limiting; full audit trail
- Strong security: OAuth2, mTLS between services, secrets rotation, OWASP hardening

### DevOps Setup
- GitOps (Argo CD) deploying Helm charts
- Progressive delivery: canary/blue-green
- Full IaC with Terraform; policy-as-code (OPA) optional
- Secrets via Vault/Secrets Manager with rotation

### AWS Deployment
- Multi-AZ EKS; RDS Multi-AZ + read replicas; MSK
- VPC with private subnets, NAT, security groups; WAF + CloudFront
- Least-privilege IAM roles (IRSA)

### Monitoring Setup
- Full three pillars: Prometheus/Grafana, ELK, OpenTelemetry + Jaeger
- SLOs, error budgets, paging alerts (Alertmanager)
- Distributed tracing across SAGA steps; ledger reconciliation dashboards

> ✅ **Proves:** Senior-level distributed systems, data consistency, security, production operations — interview-ready for senior roles.

---

## Project Progression Summary

| | TaskFlow 🟡 | StreamHub 🔴 | PayFlow 🚀 |
|---|---|---|---|
| Architecture | Monolith | Microservices | SAGA/CQRS/Outbox |
| Messaging | — | Kafka | Kafka + Outbox + CDC |
| Deployment | EC2/ECS | EKS | Multi-AZ EKS + GitOps |
| Consistency | Single DB tx | Eventual | SAGA + compensations |
| Observability | Basic | Full RED + tracing | SLOs + error budgets |
| Interview signal | Mid-level solid | Distributed-capable | Senior-ready |

[← Platforms](04-platforms.md) · [Back to README](../README.md) · [Mega Project →](06-mega-project.md)
