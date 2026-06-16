# Part 2 — Complete Learning Roadmap (12 Phases)

> The spine of the entire journey. Each topic carries: **Why it matters · Real-world usage · 🟢→🟡→🔴 path · Practical exercises · 🔥 Interview weight.** Build the [Mega Project](06-mega-project.md) alongside every phase.

[← Skill Assessment](01-skill-assessment.md) · [Back to README](../README.md) · [Resources →](03-resources.md)

**Jump to:** [P1 Core Java](#phase-1-core-java-mastery) · [P2 Databases](#phase-2-database-engineering) · [P3 Spring](#phase-3-spring-ecosystem) · [P4 APIs](#phase-4-api-engineering) · [P5 Microservices](#phase-5-microservices) · [P6 DevOps](#phase-6-devops-foundations) · [P7 Docker](#phase-7-docker) · [P8 Kubernetes](#phase-8-kubernetes) · [P9 CI/CD](#phase-9-cicd) · [P10 AWS](#phase-10-cloud-aws) · [P11 Observability](#phase-11-monitoring--observability) · [P12 System Design](#phase-12-system-design)

---

## Phase 1: Core Java Mastery

🟡→🔴 · **Timeline:** Weeks 1–6 · **Goal:** Stop being a "framework user" and become someone who understands what runs underneath.

### Topic-by-topic

#### OOP & SOLID ⭐🔥
- **Why it matters:** Every design decision traces back to these. Bad OOP = unmaintainable code.
- **Real-world usage:** Modeling domains (Order, Payment), choosing composition over inheritance, dependency inversion enabling testability.
- **Path:** 🟢 Encapsulation/inheritance/polymorphism → 🟡 Composition vs inheritance, interfaces vs abstract → 🔴 SOLID applied to real modules, designing for change.
- **Exercises:** Refactor a "God class" into SOLID-compliant classes; model a parking lot using composition.
- **Interview:** 🔥🔥🔥 Asked at every level.

#### Collections Framework ⭐🔥
- **Why:** Wrong data structure = O(n) where O(1) was possible.
- **Usage:** `HashMap` for lookups, `ArrayList` vs `LinkedList`, `ConcurrentHashMap` in multithreaded code, `TreeMap` for ordering.
- **Path:** 🟢 List/Set/Map basics → 🟡 Big-O of each, `equals`/`hashCode` contract → 🔴 Internal mechanics (hashing, resizing, fail-fast iterators).
- **Exercises:** Implement an LRU cache with `LinkedHashMap`; explain why a bad `hashCode` degrades `HashMap` to O(n).
- **Interview:** 🔥🔥🔥 `HashMap` internals are a perennial favorite.

#### Generics 🟡
- **Why:** Type safety + reusable APIs.
- **Path:** 🟢 `List<T>` → 🟡 Bounded types, wildcards (`? extends`, `? super`), PECS → 🔴 Type erasure implications.
- **Exercises:** Write a generic `Repository<T, ID>`; explain PECS with a copy method.
- **Interview:** 🔥🔥 Type erasure & wildcards.

#### Exception Handling 🟡🔥
- **Why:** Robust software; clean failure semantics.
- **Path:** 🟢 try/catch/finally, checked vs unchecked → 🟡 Custom exceptions, try-with-resources → 🔴 Exception design strategy, when to wrap vs propagate.
- **⚠️ Common Mistake:** Swallowing exceptions (`catch(Exception e){}`) or logging + rethrowing (double logging).
- **Interview:** 🔥🔥 checked vs unchecked, finally semantics.

#### Streams API & Functional Programming & Lambdas ⭐🔥
- **Why:** Modern, declarative, concise data processing.
- **Usage:** Transforming collections, grouping/aggregating, pipelines over DB results.
- **Path:** 🟢 `filter/map/collect` → 🟡 `groupingBy`, `flatMap`, `Optional`, method refs → 🔴 Custom collectors, parallel streams (and their traps), lazy evaluation.
- **⚠️ Common Mistake:** Side effects inside streams; overusing parallel streams.
- **Exercises:** Group orders by status & sum totals; flatten nested lists; build a word-frequency counter.
- **Interview:** 🔥🔥🔥 Live coding staple.

#### Multithreading & Concurrency ⭐🔥🚀
- **Why:** THE senior differentiator. Performance + correctness under load.
- **Usage:** Parallelizing I/O, thread-safe caches, background jobs.
- **Path:** 🟢 Thread/Runnable, `synchronized` → 🟡 Java Memory Model, `volatile`, `Atomic*`, locks, deadlock/livelock → 🔴 `ReentrantLock`, `ReadWriteLock`, lock-free structures, false sharing.
- **⚠️ Common Mistake:** Assuming `synchronized` solves visibility automatically without understanding happens-before.
- **Exercises:** Reproduce + fix a race condition; build a thread-safe bounded buffer; cause & resolve a deadlock.
- **Interview:** 🔥🔥🔥 Heavily tested for senior.

#### Executors & Thread Pools ⭐💼
- **Why:** Never `new Thread()` in production.
- **Path:** 🟢 `ExecutorService`, `submit` → 🟡 `ThreadPoolExecutor` tuning (core/max/queue), `ScheduledExecutorService` → 🔴 Sizing pools (CPU vs I/O bound), rejection policies, custom thread factories.
- **Exercises:** Build a worker pool that processes a queue; tune pool size for an I/O-bound task.
- **Interview:** 🔥🔥

#### CompletableFuture & Async 🔴🚀
- **Why:** Non-blocking composition of async work.
- **Path:** 🟡 `supplyAsync`, `thenApply/thenCompose` → 🔴 Combining futures, exception handling, custom executors, `allOf/anyOf`.
- **Exercises:** Call 3 services in parallel and aggregate; add timeout + fallback.
- **Interview:** 🔥🔥 Increasingly common.

#### JVM Internals, GC & Memory Management 🔴🚀🔥
- **Why:** Debug OutOfMemoryErrors, latency spikes, and tune for throughput.
- **Usage:** Diagnosing prod incidents, choosing GC, sizing heap.
- **Path:** 🟡 Heap vs stack, generations (young/old), class loading → 🔴 GC algorithms (G1, ZGC, Parallel), GC logs, profiling (JFR, VisualVM), escape analysis, metaspace.
- **Exercises:** Trigger & analyze an OOM with a heap dump; read GC logs; compare G1 vs ZGC pause times.
- **Interview:** 🔥🔥🔥 for senior; ⚠️ many candidates fail here.

#### Design Patterns 🟡🔥
- **Why:** Shared vocabulary; proven solutions.
- **Path:** 🟢 Singleton, Factory, Builder, Strategy → 🟡 Observer, Decorator, Adapter, Template → 🔴 When NOT to use a pattern; patterns in Spring (proxy, template, factory).
- **Exercises:** Spot 5 patterns inside the Spring codebase; refactor an `if/else` chain to Strategy.
- **Interview:** 🔥🔥

> ✅ **Phase 1 Mastery Checkpoint:** You can explain `HashMap` internals, write a thread-safe cache, read a GC log, and refactor code to SOLID — without notes.

---

## Phase 2: Database Engineering

🟡→🔴 · **Timeline:** Weeks 5–8 · **Goal:** Treat the database as an engineered system, not a black box.

| Topic | Why it matters | 🟢→🟡→🔴 Path | 🔥 |
|-------|----------------|---------------|:--:|
| **SQL** ⭐ | Daily language of data | SELECT/JOIN → subqueries/CTEs/window functions → set theory, recursive queries | 🔥🔥🔥 |
| **PostgreSQL** ⭐💼 | The modern default | Setup, types → JSONB, extensions → MVCC, VACUUM, partitioning | 🔥🔥 |
| **MySQL** | Ubiquitous in industry | Basics → InnoDB engine → replication, tuning | 🔥 |
| **Indexing** ⭐🔥 | #1 performance lever | B-tree basics → composite/covering indexes → index-only scans, selectivity | 🔥🔥🔥 |
| **Query Optimization** 🚀 | Fix slow systems | Read queries → rewrite for indexes → join algorithms, statistics | 🔥🔥 |
| **Transactions** ⭐🔥 | Data correctness | ACID → commit/rollback → distributed tx, 2PC | 🔥🔥🔥 |
| **Locking** 🔴 | Concurrency correctness | Row vs table → optimistic vs pessimistic → deadlock detection | 🔥🔥 |
| **Isolation Levels** ⭐🔥 | Subtle bugs source | Read Committed → Repeatable Read → Serializable; anomalies (dirty/phantom/non-repeatable reads) | 🔥🔥🔥 |
| **Execution Plans** 🚀💼 | Diagnose slowness | `EXPLAIN` → `EXPLAIN ANALYZE` → cost model, seq vs index scan | 🔥🔥 |
| **Database Design** ⭐ | Foundation of everything | Normalization (1NF–3NF) → denormalization trade-offs → schema for scale | 🔥🔥 |

**Exercises:** Take a 2-second query and make it <50ms using indexes (prove with `EXPLAIN ANALYZE`); design a schema for the mega-project; reproduce a phantom read at different isolation levels; create a deadlock and resolve it.

> ⚠️ **Common Mistake:** Adding indexes blindly. Indexes speed reads but slow writes and consume memory — measure first.

> ✅ **Phase 2 Checkpoint:** You can read an execution plan, justify every index, and explain isolation-level anomalies with examples.

---

## Phase 3: Spring Ecosystem

🟡→🔴 · **Timeline:** Weeks 7–14 · **Goal:** Deep Spring fluency — the daily-job multiplier.

| Topic | Why / Real-world usage | Path highlights | 🔥 |
|-------|------------------------|-----------------|:--:|
| **Spring Core (IoC/DI)** ⭐🔥 | Foundation of all Spring | Beans, scopes, `@Configuration`, bean lifecycle, `ApplicationContext` | 🔥🔥🔥 |
| **Spring Boot** ⭐ | Autoconfig, fast startup | Starters, autoconfiguration, `application.yml`, profiles, Actuator | 🔥🔥 |
| **Spring MVC** ⭐ | The web layer | `@RestController`, request lifecycle, `DispatcherServlet`, content negotiation | 🔥🔥 |
| **Spring Data JPA** ⭐💼 | Data access | Repositories, derived queries, `@Query`, projections, specifications | 🔥🔥 |
| **Hibernate** ⭐🔥 | The ORM underneath | Entity lifecycle, fetch types, **N+1 problem**, caching, `@Transactional` interplay | 🔥🔥🔥 |
| **Spring Security** ⭐🔥🚀 | Auth/authz | Filter chain, `UserDetailsService`, method security, CORS/CSRF | 🔥🔥🔥 |
| **JWT** ⭐💼 | Stateless auth | Structure, signing, validation, refresh tokens | 🔥🔥 |
| **OAuth2 / OIDC** 🔴🚀 | Delegated auth | Auth code flow, resource server, Keycloak/Cognito | 🔥🔥 |
| **Validation** 🟡 | Clean input handling | Bean Validation (`@Valid`), custom validators, group validation | 🔥 |
| **Exception Handling** ⭐ | Consistent API errors | `@ControllerAdvice`, `@ExceptionHandler`, Problem Details (RFC 7807) | 🔥🔥 |
| **Testing** ⭐🔥🚀 | Confidence to ship | `@WebMvcTest`, `@DataJpaTest`, Mockito, **Testcontainers**, `@SpringBootTest` | 🔥🔥 |
| **Caching** 🟡💼 | Latency & cost | `@Cacheable`, cache abstraction, eviction strategies | 🔥 |
| **Redis** ⭐💼 | Cache + more | As cache, session store, rate limiter, pub/sub, distributed lock | 🔥🔥 |
| **Scheduling** 🟡 | Background work | `@Scheduled`, cron, `ShedLock` for clustered jobs | 🔥 |

**Exercises:** Diagnose & fix an N+1 query (enable SQL logging, prove the fix); secure an API with JWT + refresh tokens; write a `@DataJpaTest` against a real Postgres via Testcontainers; add Redis caching with measured latency improvement.

> ⚠️ **Common Mistake:** `@Transactional` on a private/self-invoked method (Spring proxies don't intercept it) — a classic trap.

> ✅ **Phase 3 Checkpoint:** You can secure, test, cache, and transactionally manage a Spring service and explain the bean lifecycle and Hibernate session.

---

## Phase 4: API Engineering

🟡→🔴 · **Timeline:** Weeks 13–16 · **Goal:** Design APIs that survive scale, versioning, and abuse.

| Topic | Why / Usage | Path | 🔥 |
|-------|-------------|------|:--:|
| **REST APIs** ⭐🔥 | Standard interface | Resources, verbs, status codes → HATEOAS, Richardson Maturity Model | 🔥🔥🔥 |
| **OpenAPI / Swagger** ⭐💼 | Contract & docs | springdoc-openapi, schema-first vs code-first | 🔥 |
| **API Versioning** 🟡🚀 | Evolve without breaking clients | URI vs header vs media-type versioning, deprecation strategy | 🔥🔥 |
| **Pagination** ⭐💼 | Performance on large sets | Offset vs **keyset/cursor** pagination | 🔥🔥 |
| **Filtering & Sorting** 🟡 | Flexible queries | Query params, specification pattern, avoiding injection | 🔥 |
| **Security** ⭐ | Protect endpoints | AuthN/AuthZ, scopes, input validation, OWASP API Top 10 | 🔥🔥 |
| **Rate Limiting** 🔴🚀 | Protect & fair-use | Token bucket, Redis-backed, Bucket4j, per-client quotas | 🔥🔥 |
| **Idempotency** 🔴🚀💼 | Safe retries | Idempotency keys for POST, at-least-once semantics | 🔥🔥 |

**Exercises:** Convert offset pagination to keyset; add an idempotency key to a payment endpoint; implement Redis-backed rate limiting; generate OpenAPI docs and a typed client.

> ✅ **Phase 4 Checkpoint:** Your API is versioned, documented, paginated (keyset), rate-limited, and idempotent on writes.

---

## Phase 5: Microservices

🔴🚀 · **Timeline:** Weeks 17–28 · **Goal:** The senior leap — design, build, and operate distributed systems.

| Topic | Why / Usage | Key concepts | 🔥 |
|-------|-------------|--------------|:--:|
| **Microservices Architecture** ⭐🔥 | When/why to split | Service boundaries (DDD), data ownership, monolith-first wisdom | 🔥🔥🔥 |
| **API Gateway** ⭐💼 | Single entry point | Spring Cloud Gateway: routing, auth, rate limit, aggregation | 🔥🔥 |
| **Service Discovery / Eureka** 🟡 | Dynamic locations | Client vs server-side discovery, registry | 🔥 |
| **Config Server** 🟡💼 | Centralized config | Spring Cloud Config, refresh, secrets | 🔥 |
| **Resilience4j / Circuit Breaker** ⭐🔥🚀 | Fault tolerance | Circuit breaker, retry, bulkhead, rate limiter, timeout | 🔥🔥🔥 |
| **Distributed Tracing** 🔴💼 | Debug across services | Trace/span, correlation IDs, OpenTelemetry | 🔥🔥 |
| **Kafka** ⭐🔥🚀 | Event backbone | Topics, partitions, consumer groups, offsets, ordering, exactly-once | 🔥🔥🔥 |
| **RabbitMQ** 🟡 | Task queues | Exchanges, queues, routing keys, ack/nack | 🔥 |
| **SAGA Pattern** 🔴🚀🔥 | Distributed transactions | Choreography vs orchestration, compensating txns | 🔥🔥🔥 |
| **CQRS** 🔴🚀 | Read/write separation | Command vs query models, eventual consistency | 🔥🔥 |
| **Outbox Pattern** 🔴🚀💼 | Reliable event publishing | Transactional outbox, CDC (Debezium) | 🔥🔥 |

**Exercises:** Split the mega-project monolith into 3 services; add a circuit breaker with fallback; implement a SAGA for order→payment→inventory; build the transactional outbox to publish events to Kafka reliably.

> ⚠️ **Common Mistake:** Distributed monolith — services that can't deploy independently and share a database. Splitting too early is worse than too late.

> ✅ **Phase 5 Checkpoint:** You can justify a service boundary, handle partial failure with Resilience4j, and explain SAGA + Outbox with diagrams.

---

## Phase 6: DevOps Foundations

🟢→🔴 · **Timeline:** Weeks 5–28 (parallel) · **Goal:** Operate your own software.

| Topic | Why / Usage | Path | 🔥 |
|-------|-------------|------|:--:|
| **Linux** ⭐🔥💼 | Everything runs on it | Filesystem, permissions, processes, systemd, `top/htop`, `journalctl` | 🔥🔥🔥 |
| **Shell Scripting** ⭐💼 | Automation | bash basics → pipes/redirection → robust scripts (`set -euo pipefail`) | 🔥🔥 |
| **Git & GitHub** ⭐🔥 | Collaboration | branching, rebase, merge, PRs, conflict resolution, trunk-based dev | 🔥🔥🔥 |
| **Networking** ⭐🔥🚀 | Distributed systems basis | OSI/TCP-IP, ports, sockets, latency, NAT, firewalls | 🔥🔥 |
| **DNS** 🟡 | How names resolve | A/AAAA/CNAME/MX, TTL, resolution flow | 🔥🔥 |
| **HTTP / HTTPS** ⭐🔥 | The web protocol | methods, status, headers, keep-alive, HTTP/2, TLS handshake | 🔥🔥🔥 |
| **Reverse Proxy / Nginx** ⭐💼 | Routing, TLS, LB | reverse proxy, TLS termination, load balancing, caching | 🔥🔥 |

**Exercises:** Write a deployment shell script with error handling; configure Nginx as reverse proxy + TLS for the app; resolve a real Git rebase conflict; trace a request through DNS → TLS → HTTP.

> ✅ **Phase 6 Checkpoint:** You're comfortable on a Linux server, can script deployments, and explain a request's full network journey.

---

## Phase 7: Docker

🟡→🔴 · **Timeline:** Weeks 17–20 · **Goal:** Containerize anything, efficiently and securely.

| Topic | Why / Usage | Path | 🔥 |
|-------|-------------|------|:--:|
| **Containers** ⭐🔥 | Consistent runtime | namespaces/cgroups, container vs VM | 🔥🔥🔥 |
| **Images** ⭐ | Immutable artifacts | layers, registries, tagging | 🔥🔥 |
| **Dockerfiles** ⭐💼 | Build recipes | instructions, layer caching, `.dockerignore` | 🔥🔥 |
| **Volumes** 🟡 | Persistent data | bind mounts vs named volumes | 🔥 |
| **Networking** 🟡 | Container comms | bridge/host networks, port mapping, DNS | 🔥 |
| **Docker Compose** ⭐💼 | Local multi-service | service definitions, dependencies, env, healthchecks | 🔥🔥 |
| **Multi-stage Builds** ⭐🚀💼 | Small, secure images | build vs runtime stage, distroless/JRE-slim | 🔥🔥 |

**Exercises:** Write a multi-stage Dockerfile for the Spring app (final image <200MB); compose app + Postgres + Redis + Kafka locally; add healthchecks; shrink an image by 70%.

> ⚠️ **Common Mistake:** Running as root, copying the whole context, fat single-stage images with the full JDK.

> ✅ **Phase 7 Checkpoint:** Optimized multi-stage image, full local stack via Compose, runs as non-root.

---

## Phase 8: Kubernetes

🔴🚀 · **Timeline:** Weeks 21–28 · **Goal:** Run and troubleshoot containers at scale.

| Topic | Why / Usage | Path | 🔥 |
|-------|-------------|------|:--:|
| **Pods** ⭐🔥 | Smallest unit | lifecycle, multi-container, probes (liveness/readiness/startup) | 🔥🔥🔥 |
| **Deployments** ⭐ | Declarative rollout | replicas, rolling updates, rollbacks | 🔥🔥 |
| **Services** ⭐ | Stable networking | ClusterIP/NodePort/LoadBalancer | 🔥🔥 |
| **Ingress** ⭐💼 | HTTP routing | ingress controller, TLS, path/host routing | 🔥🔥 |
| **ConfigMaps** 🟡 | Config injection | env vs volume mounts | 🔥 |
| **Secrets** ⭐ | Sensitive data | base64 reality, external secret stores | 🔥🔥 |
| **HPA** 🔴🚀 | Auto scaling | metrics-based scaling, resource requests/limits | 🔥🔥 |
| **Helm** ⭐💼 | Package manager | charts, templating, values, releases | 🔥🔥 |

**Exercises:** Deploy the app to a local cluster (kind/minikube); add probes; expose via Ingress + TLS; configure HPA and load-test scaling; package as a Helm chart.

> ⚠️ **Common Mistake:** No resource requests/limits (breaks the scheduler & HPA); missing readiness probe (traffic to unready pods).

> ✅ **Phase 8 Checkpoint:** App runs on K8s with probes, Ingress, autoscaling, and a Helm chart; you can debug a `CrashLoopBackOff`.

---

## Phase 9: CI/CD

🟡→🔴 · **Timeline:** Weeks 21–32 · **Goal:** Automated, quality-gated, repeatable delivery.

| Topic | Why / Usage | Path | 🔥 |
|-------|-------------|------|:--:|
| **GitHub Actions** ⭐💼 | Modern CI/CD | workflows, jobs, caching, matrix, secrets, OIDC to cloud | 🔥🔥 |
| **Jenkins** 🟡 | Enterprise standard | pipelines (Jenkinsfile), agents, plugins | 🔥 |
| **SonarQube** ⭐💼 | Code quality gate | coverage, smells, security hotspots, quality gates | 🔥🔥 |
| **Nexus / Artifact Mgmt** 🟡 | Store artifacts | repositories, versioning, proxying | 🔥 |
| **Deployment Pipelines** ⭐🚀 | Safe releases | build→test→scan→image→deploy; blue-green, canary | 🔥🔥 |

**Exercises:** Build a GitHub Actions pipeline: test → SonarQube gate → build image → push to registry → deploy to K8s; add a canary stage; fail the build on coverage < 80%.

> ✅ **Phase 9 Checkpoint:** A push to main ships to staging automatically through quality gates with zero manual steps.

---

## Phase 10: Cloud (AWS)

🔴🚀 · **Timeline:** Weeks 29–40 · **Goal:** Design and run production workloads on AWS.

| Service | Why / Usage | 🔥 |
|---------|-------------|:--:|
| **IAM** ⭐🔥 | Identity & least privilege | 🔥🔥🔥 |
| **EC2** ⭐ | Compute VMs | 🔥🔥 |
| **S3** ⭐🔥 | Object storage, static hosting, backups | 🔥🔥🔥 |
| **VPC** ⭐🚀 | Networking isolation, subnets, routing | 🔥🔥 |
| **RDS** ⭐💼 | Managed databases, backups, read replicas | 🔥🔥 |
| **Load Balancers (ALB/NLB)** ⭐ | Distribute traffic, health checks | 🔥🔥 |
| **Auto Scaling** 🔴 | Elastic capacity | 🔥🔥 |
| **ECS** 🟡💼 | Container orchestration (simpler) | 🔥 |
| **EKS** 🔴🚀 | Managed Kubernetes | 🔥🔥 |
| **CloudWatch** ⭐💼 | Metrics, logs, alarms | 🔥🔥 |
| **Route53** 🟡 | DNS + routing policies | 🔥 |
| **Secrets Manager** ⭐ | Secret rotation & storage | 🔥🔥 |

**Exercises:** Deploy the app to ECS/EKS behind an ALB; RDS Postgres with read replica; least-privilege IAM roles; store secrets in Secrets Manager; CloudWatch dashboard + alarm; everything via Terraform (IaC bonus).

> ⚠️ **Common Mistake:** Over-permissive IAM (`*:*`), public S3 buckets, no cost alarms.

> ✅ **Phase 10 Checkpoint:** Production-style deployment on AWS with IaC, least-privilege IAM, managed DB, and alarms.

---

## Phase 11: Monitoring & Observability

🔴🚀 · **Timeline:** Weeks 37–44 · **Goal:** Know what your system is doing before users tell you.

| Topic | Why / Usage | 🔥 |
|-------|-------------|:--:|
| **Prometheus** ⭐💼 | Metrics collection (pull), PromQL, alert rules | 🔥🔥 |
| **Grafana** ⭐💼 | Dashboards & visualization | 🔥🔥 |
| **ELK / Loki Stack** ⭐ | Centralized logging & search | 🔥🔥 |
| **OpenTelemetry** 🔴🚀 | Vendor-neutral instrumentation (metrics/logs/traces) | 🔥🔥 |
| **Distributed Tracing** 🔴🚀💼 | Follow a request across services (Jaeger/Tempo) | 🔥🔥 |
| **The 3 Pillars + SLOs** 🚀 | Metrics, Logs, Traces; SLI/SLO/error budgets | 🔥🔥 |

**Exercises:** Expose Micrometer metrics → Prometheus → Grafana dashboard; structured JSON logs to Loki/ELK; end-to-end trace across services; define an SLO + alert on burn rate.

> ✅ **Phase 11 Checkpoint:** You can answer "is the system healthy?" and "where is the latency?" from dashboards & traces alone.

---

## Phase 12: System Design

🔴🚀🔥 · **Timeline:** Weeks 41–52 (and forever) · **Goal:** Reason about large systems and ace design interviews.

| Topic | Why / Usage | 🔥 |
|-------|-------------|:--:|
| **Scalability** ⭐🔥 | Vertical vs horizontal, stateless design | 🔥🔥🔥 |
| **CAP Theorem** ⭐🔥 | Consistency/availability trade-offs under partition | 🔥🔥🔥 |
| **Caching** ⭐🔥 | Cache-aside, write-through, eviction, invalidation, CDN | 🔥🔥🔥 |
| **Load Balancing** ⭐ | L4 vs L7, algorithms, health checks | 🔥🔥 |
| **Messaging** ⭐🚀 | Async decoupling, queues vs logs, backpressure | 🔥🔥 |
| **Distributed Systems** 🔴🚀 | Consensus, replication, partitioning, idempotency | 🔥🔥 |
| **Database Scaling** ⭐🔥 | Read replicas, sharding, partitioning, CQRS | 🔥🔥🔥 |

**Method (use in every interview):**
1. Clarify requirements (functional + non-functional) & scope.
2. Estimate scale (QPS, storage, bandwidth).
3. Define API + data model.
4. High-level architecture diagram.
5. Deep-dive on bottlenecks (DB, cache, queue).
6. Address scaling, failure, consistency, observability.
7. State trade-offs explicitly.

**Exercises:** Design URL shortener, rate limiter, news feed, payment system, the mega-project at 10M users. Write one design doc per week.

> ✅ **Phase 12 Checkpoint:** You can design a system end-to-end in 45 minutes, justify trade-offs, and estimate capacity.

---

[← Skill Assessment](01-skill-assessment.md) · [Back to README](../README.md) · [Resources →](03-resources.md)
