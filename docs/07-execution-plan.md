# Part 7 — Execution Plans (6 / 9 / 12 Month)

> Three pacing options. Each week has **📘 Learning · 🛠 Project · 🎤 Interview** goals. Pick based on your weekly hours, then protect the time ruthlessly.

[← Mega Project](06-mega-project.md) · [Back to README](../README.md) · [Interview Prep →](08-interview-prep.md)

| Plan | Weekly hours | Intensity | Best for |
|------|:---:|-----------|----------|
| [12-Month](#-12-month-plan-sustainable--recommended) | 8–12 | 🟢 Sustainable | Full-time job + life balance — **recommended default** |
| [9-Month](#-9-month-plan-focused) | 12–18 | 🟡 Focused | Motivated, some evenings + weekends |
| [6-Month](#-6-month-plan-intense) | 20–30 | 🔴 Intense | Between jobs / bootcamp-style / sabbatical |

> ⚠️ **Common Mistake:** Choosing the 6-month plan with a demanding full-time job, burning out by week 6, and quitting. **Consistency beats intensity.** A finished 12-month plan crushes an abandoned 6-month one.

---

## 🟢 12-Month Plan (Sustainable — Recommended)

**Rhythm:** ~10 hrs/week = ~6 learning + ~3 project + ~1 interview prep. Drill interview Qs 30 min/day from month 3 onward.

### Month 1–2 — Core Java + Database Foundations
| Week | 📘 Learning | 🛠 Project (ShopSphere) | 🎤 Interview |
|:--:|------------|------------------------|-------------|
| 1 | OOP, SOLID, collections internals | Repo setup, domain model (records, value objects) | Java basics Qs |
| 2 | Generics, exceptions, Optional | Inventory with `ConcurrentHashMap` | Collections Qs |
| 3 | Streams + functional + lambdas | Refactor domain logic to streams | Streams live-coding |
| 4 | Multithreading, JMM, `volatile`, locks | Concurrent inventory reservation | Concurrency Qs |
| 5 | Executors, `CompletableFuture` | Parallel price/stock fetch prototype | Threading Qs |
| 6 | JVM, GC, memory; design patterns | Apply Strategy/Factory in pricing | JVM/GC Qs |
| 7 | SQL deep (joins, CTEs, windows) | Postgres schema + Flyway migrations | SQL Qs |
| 8 | Indexing, EXPLAIN, transactions, isolation | Tune catalog search query <50ms | DB internals Qs |

### Month 3–4 — Spring + API Engineering
| Week | 📘 Learning | 🛠 Project | 🎤 Interview |
|:--:|------------|-----------|-------------|
| 9 | Spring Core (IoC/DI), Boot autoconfig | Bootstrap Spring Boot, catalog CRUD | Spring core Qs |
| 10 | Spring MVC, Data JPA, Hibernate (N+1) | Cart + order APIs; fix an N+1 | JPA/Hibernate Qs |
| 11 | Spring Security + JWT + refresh tokens | Auth module | Security Qs |
| 12 | Validation, exception handling, testing | `@ControllerAdvice`, Testcontainers tests | Testing Qs |
| 13 | Caching, Redis, scheduling | Redis product cache + cleanup job | Caching Qs |
| 14 | REST maturity, OpenAPI, versioning | springdoc docs + v1 API | REST design Qs |
| 15 | Pagination (keyset), filtering, idempotency | Keyset catalog + idempotent checkout | API design Qs |
| 16 | Rate limiting (Bucket4j+Redis) | Add rate limiting; **deploy monolith to EC2** | Mid-level mock interview |

### Month 5–6 — Microservices + Messaging
| Week | 📘 Learning | 🛠 Project | 🎤 Interview |
|:--:|------------|-----------|-------------|
| 17 | Microservices principles, DDD boundaries | Plan service split | MS architecture Qs |
| 18 | Spring Cloud Gateway, Eureka, Config | Extract Auth + Catalog services | Service discovery Qs |
| 19 | Kafka fundamentals (topics/partitions/groups) | Catalog → Kafka events | Kafka Qs |
| 20 | Resilience4j (CB, retry, bulkhead) | Resilient inter-service calls | Resilience Qs |
| 21 | SAGA pattern | Checkout SAGA (order→inventory→payment) | SAGA Qs |
| 22 | Outbox pattern + CDC | Transactional outbox → Kafka | Consistency Qs |
| 23 | CQRS, eventual consistency | Order-history read model | CQRS Qs |
| 24 | Distributed tracing concepts | Correlation IDs across services | Distributed systems Qs |

### Month 7–8 — Docker + Kubernetes
| Week | 📘 Learning | 🛠 Project | 🎤 Interview |
|:--:|------------|-----------|-------------|
| 25 | Docker: images, layers, Dockerfiles | Multi-stage Dockerfiles all services | Docker Qs |
| 26 | Compose, volumes, networking, multi-stage | `docker compose up` full stack + Trivy scan | Container Qs |
| 27 | K8s: pods, deployments, services, probes | Deploy to kind/minikube | K8s core Qs |
| 28 | Ingress, ConfigMaps, Secrets | Ingress + TLS + config | K8s networking Qs |
| 29 | HPA, resources, Helm | HPA + Helm charts | K8s scaling Qs |
| 30 | Linux + shell + networking + Nginx | Deploy scripts, Nginx reverse proxy | Linux/networking Qs |
| 31 | DNS, HTTP/HTTPS, TLS | Harden + observe request path | Networking Qs |
| 32 | Review + buffer | Stabilize K8s deploy | Mock: backend + DevOps |

### Month 9–10 — CI/CD + AWS
| Week | 📘 Learning | 🛠 Project | 🎤 Interview |
|:--:|------------|-----------|-------------|
| 33 | GitHub Actions deeply | Test→build→push pipeline | CI/CD Qs |
| 34 | SonarQube, Nexus, quality gates | Add Sonar gate + coverage threshold | Quality Qs |
| 35 | Deployment strategies (canary/blue-green) | Canary stage to staging | Delivery Qs |
| 36 | AWS IAM, EC2, S3, VPC | IAM roles, S3 media, VPC layout | AWS core Qs |
| 37 | RDS, ALB, Auto Scaling, Route53 | RDS + ALB + DNS | AWS Qs |
| 38 | ECS vs EKS, Secrets Manager | Deploy to EKS via ECR | EKS Qs |
| 39 | Terraform (IaC) | Provision platform with Terraform | IaC Qs |
| 40 | Argo CD / GitOps | GitOps deploy | GitOps Qs |

### Month 11–12 — Observability + System Design + Polish
| Week | 📘 Learning | 🛠 Project | 🎤 Interview |
|:--:|------------|-----------|-------------|
| 41 | Prometheus + Grafana + Micrometer | RED dashboards per service | Observability Qs |
| 42 | ELK/Loki + structured logs | Centralized logs + correlation | Logging Qs |
| 43 | OpenTelemetry + Jaeger; SLOs | End-to-end traces + SLO alerts | Tracing Qs |
| 44 | System design fundamentals (scalability, CAP) | Design doc: ShopSphere @10M users | SD: URL shortener |
| 45 | Caching, load balancing, DB scaling | Add CDN, read replicas, cache strategy | SD: rate limiter |
| 46 | Messaging, distributed systems patterns | Load test (k6); tune Auto Scaling | SD: news feed |
| 47 | Mock system design interviews | Chaos test + runbooks | SD: payment system |
| 48 | Resume, GitHub polish, demo video | Final README + architecture diagram | Full senior mock loop |

> Weeks 49–52: buffer, deepen weak areas, apply & interview.

---

## 🟡 9-Month Plan (Focused)

Same 12-phase sequence, compressed by ~25%. ~15 hrs/week.

| Months | Focus | Key milestones |
|:--:|-------|----------------|
| 1 | Core Java + Concurrency + JVM | Domain model + concurrent inventory (wks 1–4) |
| 2 | Database + Spring Core/Boot/MVC | Tuned schema + catalog/cart APIs (wks 5–8) |
| 3 | Spring Security/JPA/Testing + API hardening | Secured, tested, documented API; deploy monolith (wks 9–12) |
| 4 | Microservices + Kafka | Service split + Kafka events + Resilience4j (wks 13–16) |
| 5 | SAGA/Outbox/CQRS + Docker | Distributed checkout + containerized stack (wks 17–20) |
| 6 | Kubernetes + Linux/Networking | EKS-ready Helm deploy (wks 21–24) |
| 7 | CI/CD + AWS core | Full pipeline + AWS deploy + Terraform (wks 25–28) |
| 8 | AWS advanced + Observability | EKS + monitoring + tracing + SLOs (wks 29–32) |
| 9 | System Design + Polish | Design docs, load test, mocks, portfolio (wks 33–36) |

**Weekly cadence:** 8 hrs learning + 5 hrs project + 2 hrs interview drilling. Interview prep starts week 6.

---

## 🔴 6-Month Plan (Intense)

Bootcamp pace. ~25 hrs/week. Two phases per month, parallelizing DevOps with backend.

| Month | Backend track | DevOps/Cloud track | Project milestone |
|:--:|---------------|--------------------|-------------------|
| 1 | Core Java + Concurrency + JVM + DB | Linux + Git + Docker basics | Domain model + Dockerized Postgres |
| 2 | Spring (all) + API engineering | Docker mastery + Compose | Secured, tested, containerized monolith |
| 3 | Microservices + Kafka + Resilience4j | Kubernetes core | Service split running on K8s |
| 4 | SAGA + Outbox + CQRS | CI/CD (Actions + Sonar) + Helm | Distributed checkout + automated pipeline |
| 5 | — (stabilize) | AWS (IAM/VPC/RDS/EKS) + Terraform | Production AWS deploy via IaC |
| 6 | System Design intensive | Observability (Prom/Grafana/OTel) | Monitored platform + design docs + mocks |

**Weekly cadence:** 12 hrs learning + 9 hrs project + 4 hrs interview. Daily interview drilling from week 1.

> ⚠️ Only viable with 20+ free hours/week. Schedule rest days to avoid burnout. Skip nothing — instead, go slightly shallower and revisit post-plan.

---

## Universal Weekly Template (any plan)

```
Mon–Fri (1.5–2 hrs/day):
  • 45–60 min: learn the week's topic (video/book/docs)
  • 30–45 min: apply it to ShopSphere
  • 20–30 min: drill interview questions for that topic
Sat (3–4 hrs):
  • Bigger project work block; integrate the week's feature
  • Write/commit, open a PR, review your own diff
Sun (1 hr):
  • Review notes, update skill matrix, plan next week
  • One mock question (system design or behavioral)
```

> ✅ **Execution Checkpoint:** End each week with a green CI build, a merged PR on ShopSphere, and 1 new topic you can teach aloud.

[← Mega Project](06-mega-project.md) · [Back to README](../README.md) · [Interview Prep →](08-interview-prep.md)
