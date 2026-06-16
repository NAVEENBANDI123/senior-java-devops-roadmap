# Part 6 — The Mega Project: "ShopSphere" E-Commerce Platform

> **One project, twelve phases.** Instead of disconnected tutorials, you grow a single production-grade e-commerce platform alongside the roadmap. Every phase adds a feature, a technology, a DevOps practice, and a cloud service. By month 12, you have a portfolio centerpiece that *is* your senior-engineer evidence.

[← Projects](05-projects.md) · [Back to README](../README.md) · [Execution Plan →](07-execution-plan.md)

---

## Why E-Commerce?

It naturally demands **everything** a senior backend + DevOps engineer must know: auth, catalog, search, inventory, payments, orders, notifications, high read traffic, consistency under concurrency, and 24/7 operations. It maps cleanly to microservices and tells a compelling interview story.

---

## Target End-State Architecture (Month 12)

```
 [CloudFront CDN] → [WAF] → [Route53] → [ALB / Ingress]
                                   │
                        [API Gateway (Spring Cloud Gateway)]
                                   │  (JWT/OIDC auth, rate limiting)
   ┌──────────┬──────────┬─────────┼─────────┬───────────┬─────────────┐
 [Auth]   [Catalog]  [Inventory] [Cart]   [Order]    [Payment]   [Notification]
   │          │          │         │         │           │             │
[Postgres] [PG+ES]   [Postgres] [Redis]  [Postgres]  [Postgres]    [Postgres]
   └──────────┴────── KAFKA event bus (Outbox + SAGA + CQRS) ────────┘
        [Config Server][Eureka][Resilience4j][Redis cache][S3 media]
        OBSERVABILITY: Prometheus + Grafana + ELK + OpenTelemetry/Jaeger
        PLATFORM: EKS · RDS · MSK · ElastiCache · Terraform · Argo CD
```

---

## Phase-by-Phase Build Log

For each phase: **🛠 Feature · ⚙️ Technology · 🔧 DevOps · ☁️ Cloud.**

### Phase 1 — Core Java → Domain Model
- 🛠 **Feature:** Model the domain (Product, Cart, Order, User, Money value object) as a clean console/library prototype.
- ⚙️ **Tech:** Pure Java — records, sealed types, streams, generics, `Optional`; a concurrent in-memory inventory using `ConcurrentHashMap` + atomic operations.
- 🔧 **DevOps:** Git repo, Maven/Gradle, branch strategy, `.gitignore`, commit hygiene.
- ☁️ **Cloud:** — (local only)

### Phase 2 — Database → Schema & Queries
- 🛠 **Feature:** Persist catalog, users, orders. Product search by category/price with proper indexes.
- ⚙️ **Tech:** PostgreSQL schema, normalization, indexes, `EXPLAIN ANALYZE` tuning, transactions for checkout.
- 🔧 **DevOps:** Flyway migrations versioned in Git; local Postgres via Docker.
- ☁️ **Cloud:** —

### Phase 3 — Spring → REST Monolith
- 🛠 **Feature:** Full CRUD APIs: catalog, cart, orders, auth (register/login). Caching of product reads.
- ⚙️ **Tech:** Spring Boot, Data JPA, Security + JWT, Validation, `@ControllerAdvice`, Redis cache, `@Scheduled` cleanup jobs, Testcontainers tests.
- 🔧 **DevOps:** Docker Compose (app + Postgres + Redis); unit + integration tests in CI.
- ☁️ **Cloud:** —

### Phase 4 — API Engineering → Hardening
- 🛠 **Feature:** Pagination (keyset) on catalog, filtering/sorting, idempotent checkout, API versioning, rate limiting.
- ⚙️ **Tech:** springdoc-openapi, Bucket4j + Redis rate limiter, idempotency keys, RFC 7807 errors.
- 🔧 **DevOps:** Contract docs published as a CI artifact; API linting.
- ☁️ **Cloud:** —

### Phase 5 — Microservices → Decompose
- 🛠 **Feature:** Split monolith → Auth, Catalog, Inventory, Cart, Order, Payment, Notification services. Checkout becomes a SAGA (order → reserve inventory → payment → confirm), with the Outbox pattern publishing events to Kafka. CQRS read model for order history.
- ⚙️ **Tech:** Spring Cloud Gateway, Eureka, Config Server, Kafka, Resilience4j (circuit breaker/retry), transactional Outbox, SAGA orchestrator, distributed tracing.
- 🔧 **DevOps:** One pipeline per service; Compose runs full stack incl. Kafka.
- ☁️ **Cloud:** — (still local/Compose)

### Phase 6 — DevOps Foundations → Operability
- 🛠 **Feature:** TLS, reverse proxy, health endpoints, graceful shutdown.
- ⚙️ **Tech:** Actuator health/readiness, structured JSON logging with correlation IDs.
- 🔧 **DevOps:** Nginx reverse proxy + TLS; deployment shell scripts; Linux server hardening basics; Git trunk-based flow with PR reviews.
- ☁️ **Cloud:** First deploy to a single cloud VM (EC2) manually.

### Phase 7 — Docker → Containerize
- 🛠 **Feature:** Every service runs as an optimized container.
- ⚙️ **Tech:** Multi-stage Dockerfiles (JRE-slim/distroless, non-root), `.dockerignore`, healthchecks.
- 🔧 **DevOps:** Full local environment via a single `docker compose up` (all services + infra). Image scanning (Trivy).
- ☁️ **Cloud:** Push images to ECR.

### Phase 8 — Kubernetes → Orchestrate
- 🛠 **Feature:** Platform runs on K8s with autoscaling and zero-downtime deploys.
- ⚙️ **Tech:** Deployments, Services, Ingress + TLS, ConfigMaps/Secrets, liveness/readiness/startup probes, HPA, resource requests/limits.
- 🔧 **DevOps:** Helm charts per service; rolling updates + rollback; local kind/minikube first.
- ☁️ **Cloud:** Deploy to **EKS**.

### Phase 9 — CI/CD → Automate Delivery
- 🛠 **Feature:** Push to main → automatically tested, scanned, built, deployed to staging.
- ⚙️ **Tech:** GitHub Actions (matrix + path filters), SonarQube quality gates, Nexus/ECR artifacts.
- 🔧 **DevOps:** Pipeline: build → test → Sonar gate → image → scan → deploy (Helm/Argo CD); canary stage.
- ☁️ **Cloud:** OIDC from GitHub Actions to AWS (no long-lived keys).

### Phase 10 — AWS → Production Platform
- 🛠 **Feature:** Production-grade, multi-AZ, secure deployment.
- ⚙️ **Tech:** Managed services replace self-hosted infra.
- 🔧 **DevOps:** **Terraform** provisions everything (IaC); Argo CD GitOps.
- ☁️ **Cloud:** EKS (multi-AZ), RDS Postgres (Multi-AZ + read replica), MSK (Kafka), ElastiCache (Redis), S3 (media), ALB, Route53, ACM, IAM least-privilege (IRSA), Secrets Manager, CloudWatch, Auto Scaling.

### Phase 11 — Observability → See Everything
- 🛠 **Feature:** Dashboards, centralized logs, end-to-end traces, alerting, SLOs.
- ⚙️ **Tech:** Micrometer → Prometheus → Grafana (RED metrics per service), ELK/Loki logs, OpenTelemetry → Jaeger/Tempo traces.
- 🔧 **DevOps:** Alertmanager paging on SLO error-budget burn; runbooks.
- ☁️ **Cloud:** CloudWatch alarms + dashboards complement Prometheus.

### Phase 12 — System Design → Scale & Document
- 🛠 **Feature:** Handle Black-Friday-scale traffic: CDN for static, read replicas, cache layers, async order processing, sharding plan.
- ⚙️ **Tech:** CloudFront CDN, cache-aside + write-through strategy, DB read replicas + partitioning, Kafka backpressure, idempotency everywhere.
- 🔧 **DevOps:** Load testing (k6/Gatling); chaos experiments; capacity planning.
- ☁️ **Cloud:** Auto Scaling tuned from load tests; cost optimization review.
- 📄 **Deliverable:** A full **design doc** (requirements → capacity estimates → architecture → trade-offs) — your interview centerpiece.

---

## Progress Tracker

| Phase | Milestone | Done |
|:--:|-----------|:--:|
| 1 | Domain model + concurrency prototype | ☐ |
| 2 | Tuned Postgres schema + migrations | ☐ |
| 3 | Secured, tested Spring monolith | ☐ |
| 4 | Hardened, documented API | ☐ |
| 5 | Microservices + Kafka + SAGA + Outbox | ☐ |
| 6 | Operable: TLS, logs, health, first VM deploy | ☐ |
| 7 | All services containerized + scanned | ☐ |
| 8 | Running on EKS with HPA + Helm | ☐ |
| 9 | Full CI/CD with quality gates + canary | ☐ |
| 10 | Terraform-provisioned AWS platform | ☐ |
| 11 | Metrics + logs + traces + SLO alerts | ☐ |
| 12 | Load-tested, CDN, read replicas + design doc | ☐ |

> 💼 **Portfolio impact:** When complete, this single repo demonstrates ~90% of what senior Java + DevOps interviews probe. Pin it on GitHub with a great README, architecture diagram, and a short demo video/loom.

> ✅ **Mega Project Checkpoint:** You can walk an interviewer through ShopSphere end-to-end — code, deployment, failure handling, and scaling — for 30+ minutes confidently.

[← Projects](05-projects.md) · [Back to README](../README.md) · [Execution Plan →](07-execution-plan.md)
