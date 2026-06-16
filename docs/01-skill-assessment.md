# Part 1 — Skill Assessment

> *"You can't plot a route without knowing your starting coordinates."* This part maps where a typical 1.5-year Java developer stands, the gaps that quietly block promotion, what the market actually rewards, and what each future level demands.

[← Back to README](../README.md) · [Next: Roadmap →](02-roadmap.md)

---

## 1.1 Typical Skills of a Java Developer with 1.5 Years Experience

What you *probably* can do today (and that's a great foundation):

| Area | Typical Capability | Level |
|------|--------------------|-------|
| Java syntax | Comfortable with classes, interfaces, collections, loops | 🟡 |
| OOP | Uses inheritance/polymorphism; fuzzy on composition vs inheritance trade-offs | 🟢 |
| Spring Boot | Builds CRUD REST controllers, `@Service`, `@Repository` | 🟡 |
| JPA/Hibernate | Basic entities & repositories; unaware of N+1, lazy/eager pitfalls | 🟢 |
| SQL | SELECT/JOIN/WHERE; rarely writes indexes or reads execution plans | 🟢 |
| Git | commit/push/pull/branch; shaky on rebase, conflict resolution | 🟡 |
| Testing | Writes a few unit tests; no real integration/contract testing | 🟢 |
| Debugging | Reads stack traces, uses IDE debugger | 🟡 |
| Tools | Maven/Gradle basics, Postman | 🟡 |

---

## 1.2 Common Knowledge Gaps (the silent promotion-blockers)

> ⚠️ These are the gaps that keep developers stuck at "mid-level" for years.

1. **Concurrency** — Can write threads but doesn't understand the memory model, `volatile`, deadlocks, or `CompletableFuture`. 🔥
2. **JVM internals & GC** — No mental model of heap, generations, or how a memory leak happens. 🔥
3. **Database engineering** — No indexing strategy, never read an `EXPLAIN ANALYZE`, doesn't understand isolation levels. 🔥
4. **Transactions** — Uses `@Transactional` cargo-cult style; unaware of propagation, rollback rules, proxy self-invocation traps. ⚠️
5. **System design** — Can't reason about scaling, caching layers, or consistency trade-offs. 🔥
6. **Production operations** — Never set up CI/CD, containers, monitoring, or alerting. Can't answer "what happens when it's 3am and the service is down?"
7. **Testing discipline** — No test pyramid, no Testcontainers, fragile or absent tests.
8. **API maturity** — No versioning, pagination, idempotency, or rate-limiting strategy.
9. **Security** — Vague on JWT vs session, OAuth2 flows, OWASP Top 10.
10. **Communication** — Can't yet write a design doc or explain trade-offs to non-experts. 🚀

---

## 1.3 Current Market Expectations (2026)

What hiring teams expect by seniority for Java backend roles:

| Expectation | Mid (2–3 yr) | Senior (5+ yr) |
|-------------|--------------|----------------|
| Ships features independently | ✅ | ✅ |
| Owns a service end-to-end (build → deploy → operate) | partial | ✅ |
| Designs systems & writes design docs | ❌ | ✅ |
| Strong on concurrency, JVM, DB internals | growing | ✅ |
| Microservices + messaging (Kafka) | exposure | ✅ |
| Containers + Kubernetes in production | exposure | ✅ |
| CI/CD ownership | helps | ✅ |
| Cloud (AWS) hands-on | exposure | ✅ |
| Observability (metrics/logs/traces) | basic | ✅ |
| Mentors others, leads code reviews | ❌ | ✅ |
| Drives technical decisions & trade-offs | ❌ | ✅ |

> 💼 **Reality check:** The market increasingly rewards **"backend engineers who can operate their own software."** Pure-Java specialists without any DevOps/Cloud are seen as incomplete for senior roles in most product companies.

---

## 1.4 Skills Required by Level — Comparison Matrix

| Skill Area | 🟢 1.5 yr (You) | 🟡 3 yr | 🔴 5 yr | 🚀 Senior Engineer | 🧭 Tech Lead |
|------------|-----------------|---------|---------|--------------------|--------------|
| **Core Java** | Syntax, collections | Streams, generics, exceptions mastery | Concurrency, internals | JVM tuning, GC analysis | Sets Java standards for team |
| **Concurrency** | Threads basics | Executors, synchronization | CompletableFuture, locks | Lock-free, reactive | Reviews concurrency designs |
| **JVM/GC** | Aware it exists | Heap/stack model | GC types, profiling | Tuning, leak hunting | Capacity & perf strategy |
| **Design Patterns/SOLID** | Heard of them | Applies common ones | Refactors to patterns | Designs clean modules | Enforces architecture |
| **Databases** | CRUD SQL | Joins, indexing | Query tuning, isolation | Sharding, replication | Data architecture |
| **Spring** | CRUD APIs | Data JPA, Security | Custom config, caching | Reactive, advanced security | Framework standards |
| **APIs** | REST basics | Versioning, validation | Rate limiting, idempotency | API governance | API strategy |
| **Microservices** | — | Reads about them | Builds them | Designs boundaries, resilience | Owns platform architecture |
| **Messaging (Kafka)** | — | Produce/consume | Partitions, consumer groups | Exactly-once, schema mgmt | Event-driven strategy |
| **Testing** | Few unit tests | Mockito, integration | Testcontainers, contract | Test strategy | Quality culture |
| **Docker** | Run containers | Write Dockerfiles | Multi-stage, optimization | Image security | Container standards |
| **Kubernetes** | — | Pods/Deployments | Ingress, HPA, Helm | Operators, troubleshooting | Cluster strategy |
| **CI/CD** | Manual deploys | Basic pipeline | Full pipeline + quality gates | Deployment strategies | Delivery platform |
| **AWS** | — | EC2/S3/RDS | VPC, ECS/EKS, IAM | Well-Architected design | Cloud strategy & cost |
| **Observability** | Logs to console | Structured logging | Metrics + dashboards | Tracing, SLOs/alerts | Observability platform |
| **System Design** | — | Component diagrams | Scaling, caching, CAP | End-to-end designs | Org-wide architecture |
| **Leadership** | — | Helps peers | Leads features | Mentors, drives decisions | Leads teams & roadmap |

---

## 1.5 Your Personalized Gap Plan

Based on the typical profile, prioritize in this order (highest ROI first):

| Priority | Focus | Why now | Maps to Phase |
|:---:|-------|---------|---------------|
| 1 | Concurrency + JVM/GC | Biggest interview & seniority differentiator | [Phase 1](02-roadmap.md#phase-1-core-java-mastery) |
| 2 | Database engineering | Quietly causes most production incidents | [Phase 2](02-roadmap.md#phase-2-database-engineering) |
| 3 | Spring depth (Security, Tx, Testing) | Daily-job multiplier | [Phase 3](02-roadmap.md#phase-3-spring-ecosystem) |
| 4 | Microservices + Kafka | The senior leap | [Phase 5](02-roadmap.md#phase-5-microservices) |
| 5 | Docker → K8s → AWS → CI/CD | "Operate your own software" | Phases 6–10 |
| 6 | System Design | Ties everything together for interviews | [Phase 12](02-roadmap.md#phase-12-system-design) |

> ✅ **Mastery Checkpoint for Part 1:** You can honestly fill in the [Master Skill Matrix](../README.md#-master-skill-matrix-part-10-summary) and name your top 3 gaps without hesitation.

[← Back to README](../README.md) · [Next: Roadmap →](02-roadmap.md)
